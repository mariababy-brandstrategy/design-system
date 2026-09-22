"""브랜드 디자인 규격 약식판 조립 — 템플릿 + 공간 가이드 이미지 재사용 + 표지 썸네일 → docs/브랜드-디자인-규격-약식판-v1.1.{html,pdf}.
공용 로직·검사 = docs/assemble_lib.py. 2026-09-22 편입(경영진 보고 2026-09-10 작업본의 약식 규격 템플릿 이전).
문서 고유 후처리: 본문 텍스트의 #RRGGBB 앞에 색 네모(.hex) — 직전 태그에 nochip 이 있으면 건너뛴다. 태그 속성·CSS 는 건드리지 않는다.
  python3 assemble.py --pdf"""
import pathlib, re, sys
S = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(S.parents[0]))
from assemble_lib import assemble, REPO
SP = REPO/'docs/space-brand-guide-src/img'
IMG = {**{f'{{{{IMG_{k}}}}}': SP/v for k, v in {'SPACE_RECEPTION': 'space-reception.jpg', 'SPACE_CORRIDOR': 'space-corridor.jpg', 'SPACE_LOUNGE': 'space-lounge.jpg',
                                             'SIGN_DOORSIGN': 'sign-doorsign.png', 'SIGN_DIRECTORY': 'sign-directory.png', 'SIGN_PICTOGRAMS': 'sign-pictograms.png'}.items()},
       **{f'{{{{IMG_{k}}}}}': S/'img'/v for k, v in {'COVER_COLOR': 'cover-color.png', 'COVER_SPACE': 'cover-space.png', 'COVER_SCREEN': 'cover-screen.png'}.items()}}

def hex_chips(out):
    head, sep, body = out.partition('</head>')
    parts = re.split(r'(<[^>]+>)', body); last = ''
    for n, seg in enumerate(parts):
        if seg.startswith('<'): last = seg; continue
        if 'nochip' in last or not seg.strip(): continue
        parts[n] = re.sub(r'#([0-9A-Fa-f]{6})\b', lambda m: f'<span class="hex"><i style="background:#{m.group(1)}"></i>#{m.group(1)}</span>', seg)
    return head + sep + ''.join(parts)

assemble(S, 'brief-spec.template.html', '브랜드-디자인-규격-약식판-v1.1', images=IMG, post=hex_chips)
