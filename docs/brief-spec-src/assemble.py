"""브랜드 디자인 규격 약식판 조립 — 템플릿 + 공간 가이드 이미지 재사용 + 표지 썸네일 → docs/브랜드-디자인-규격-약식판-v1.2.{html,pdf}.
공용 로직·검사 = docs/assemble_lib.py. 2026-09-22 편입(경영진 보고 2026-09-10 작업본의 약식 규격 템플릿 이전).
문서 고유 후처리: 본문 텍스트의 #RRGGBB 앞에 색 네모(.hex) — 직전 태그에 nochip 이 있으면 건너뛴다. 태그 속성·CSS 는 건드리지 않는다.
  python3 assemble.py --pdf            # 조립 + PDF
  python3 assemble.py --covers --pdf   # 마지막 쪽 「실무 가이드 3종」 표지 썸네일 3장을 먼저 다시 뜨고 조립
표지 썸네일(img/cover-{color,space,screen}.png) = docs/ 직하 **현행판** 가이드 PDF 1쪽을 72dpi 로 렌더(A4 = 595×842 px).
  2026-09-22 v1.2 에서 방법을 코드로 고정 — 편입 때 손으로 만든 3장이 구판(색상 v2.2·공간 v1.1·화면 v1.1) PDF 의 같은 렌더와 픽셀 단위로 동일했다(역추적 diff 0).
  가이드의 판이 오르면 `--covers` 로 다시 뜨고, 그 밑 figcaption 의 판·쪽수 문구는 템플릿에서 손으로 맞춘다(썸네일은 그림, 문구는 글 — 조립기가 문구를 만들지 않는다).
  archive/ 는 보지 않는다(이름 규칙 ④ — docs/ 직하 = 현행판만이라 시리즈마다 정확히 1개여야 하고, 아니면 멈춘다)."""
import pathlib, re, sys
S = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(S.parents[0]))
from assemble_lib import assemble, REPO
SP = REPO/'docs/space-brand-guide-src/img'
IMG = {**{f'{{{{IMG_{k}}}}}': SP/v for k, v in {'SPACE_RECEPTION': 'space-reception.jpg', 'SPACE_CORRIDOR': 'space-corridor.jpg', 'SPACE_LOUNGE': 'space-lounge.jpg',
                                             'SIGN_DOORSIGN': 'sign-doorsign.png', 'SIGN_DIRECTORY': 'sign-directory.png', 'SIGN_PICTOGRAMS': 'sign-pictograms.png'}.items()},
       **{f'{{{{IMG_{k}}}}}': S/'img'/v for k, v in {'COVER_COLOR': 'cover-color.png', 'COVER_SPACE': 'cover-space.png', 'COVER_SCREEN': 'cover-screen.png'}.items()}}
COVERS = {'cover-color.png': '브랜드-가이드-색상-v*.pdf', 'cover-space.png': '브랜드-가이드-공간-v*.pdf', 'cover-screen.png': '브랜드-가이드-화면-v*.pdf'}

def make_covers():
    """현행판 가이드 PDF 1쪽 → img/cover-*.png (72dpi). 세 시리즈를 먼저 전부 확인·렌더한 뒤에 저장한다 — 하나라도 어긋나면 한 장도 바꾸지 않는다
    (판이 섞인 썸네일 방지, Codex 4b 2026-09-22). 개수 검사는 assert 가 아니라 예외(`python -O` 에서도 산다). PyMuPDF(fitz) 필수."""
    import fitz   # PyMuPDF — assemble_lib.page_count 와 같은 의존이지만 여기선 필수(없으면 ImportError 로 멈춘다)
    todo = []
    for png, pat in COVERS.items():
        hits = sorted((REPO/'docs').glob(pat))
        if len(hits) != 1:
            raise SystemExit(f'{pat}: docs/ 직하 현행판 PDF 가 정확히 1개여야 한다(이름 규칙 ④) — {[h.name for h in hits]}')
        with fitz.open(hits[0]) as d:
            todo.append((png, hits[0].name, d[0].get_pixmap()))   # dpi 기본 72 → A4 595×842
    for png, src, pix in todo:
        pix.save(str(S/'img'/png))
        print('cover', png, '<-', src, f'{pix.width}x{pix.height}')

def hex_chips(out):
    head, sep, body = out.partition('</head>')
    parts = re.split(r'(<[^>]+>)', body); last = ''
    for n, seg in enumerate(parts):
        if seg.startswith('<'): last = seg; continue
        if 'nochip' in last or not seg.strip(): continue
        parts[n] = re.sub(r'#([0-9A-Fa-f]{6})\b', lambda m: f'<span class="hex"><i style="background:#{m.group(1)}"></i>#{m.group(1)}</span>', seg)
    return head + sep + ''.join(parts)

if '--covers' in sys.argv: make_covers()
assemble(S, 'brief-spec.template.html', '브랜드-디자인-규격-약식판-v1.2', images=IMG, post=hex_chips)
