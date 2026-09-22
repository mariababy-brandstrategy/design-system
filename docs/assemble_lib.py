"""공용 문서 조립기 — docs/ 의 HTML→PDF 문서 4종이 함께 쓰는 라이브러리(2026-09-22, 종전 조립기 3벌을 한 벌로).

조립 = 템플릿 + (tokens/design-tokens.css → styles/document-base.css → 문서 override) + 워드마크 SVG + 서브셋 폰트 + 이미지 → 단일 HTML.
사용 = 각 `docs/<slug>-src/assemble.py` 가 `assemble(...)` 을 부른다. `--pdf` 를 주면 크롬 헤드리스로 PDF 까지 만들고 쪽수를 찍는다.

쓰기 전 검사(실패 시 낡은 생성물을 남기지 않는다):
  ① 서브셋 글꼴 커버리지 — chars.txt 가 아니라 **woff2 의 실제 cmap** 을 본다(2026-09-08 Codex 4b: 원본 Pretendard 에 없는 글자는
     목록에 넣어도 서브셋에 못 들어가 조용히 시스템 글꼴로 떨어진다. ✕ U+2715 · ⬇ U+2B07 실제 사례).
  ② 절 번호 — 절 머리(`.sec-head`)의 번호는 비어 있거나 "자연수." 하나뿐이고, 문서 순서대로 1.·2.·… 로 빠짐·중복 없이 이어진다
     (AGENTS.md 「문서 레이어」 절 번호 정의, 2026-09-22). 빈 번호(서문·부록성 절)는 번호 붙은 절 사이에 오지 않는다. 차례(toc)와의 정합은 미검사.
  ③ 옛 부서명 '브랜드전략부' 0건(조직개편 → CX부. 2026-09-10 색상 가이드 표지·꼬리에서 실측 발견).
  ④ 절차용 표식(`tag prop`·`tag check`) 잔존 0.
  ⑤ 미치환 `{{ }}` 0.
"""
import base64, html as _html, json, os, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent          # docs/
REPO = HERE.parent if (HERE.parent/'tokens/design-tokens.css').exists() else pathlib.Path(os.path.expanduser('~/design-system'))
FONT = REPO/'assets/fonts/pretendard/maria-doc-sans-subset.woff2'   # Pretendard v1.3.9 variable 서브셋, OFL RFN 때문에 개명(README 참조)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
OLD_DEPT = '브랜드전략부'
SEC_RE = re.compile(r'<div\s+class=["\']sec-head(?:\s[^"\']*)?["\'][^>]*>\s*<span\s+class=["\']no["\'][^>]*>([^<]*)</span>', re.S)


def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def wordmark_paths():
    svg = (REPO/'assets/logos/svg/maria-wordmark.svg').read_text(encoding='utf-8')
    paths = ''.join(re.findall(r'<path[^>]*/>', svg))
    paths = re.sub(r'\s*fill="currentColor"\s*fill-opacity="1"', '', paths)   # 부모 fill 상속
    return re.sub(r'\s+fill-rule="nonzero"', '', paths)


def font_cmap(path=FONT):
    """서브셋 woff2 가 실제로 담은 코드포인트. fontTools 가 없으면 None(=미검증)."""
    code = ("import sys,json;from fontTools.ttLib import TTFont;"
            "print(json.dumps(sorted(TTFont(sys.argv[1]).getBestCmap())))")
    for py in (sys.executable, str(FONT.parent/'build/.venv/bin/python')):
        try:
            r = subprocess.run([py, '-c', code, str(path)], capture_output=True, text=True, timeout=120)
            if r.returncode == 0: return set(json.loads(r.stdout))
        except Exception: pass
    return None


def visible_text(t):
    text = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    text = re.sub(r'<script.*?</script>', '', text, flags=re.S)
    return _html.unescape(re.sub(r'<[^>]+>', '', text))   # 엔티티(&nbsp; 등)를 실제 글자로 펴서 본다


def check(t):
    """쓰기 전 검사 ①~④. 실패 = AssertionError."""
    text = visible_text(t)
    assert FONT.exists(), f'서브셋 글꼴 없음: {FONT}'
    covered = font_cmap()
    assert covered is not None, ('서브셋 cmap 을 읽지 못함 — fontTools 가 없거나 woff2 가 깨짐. chars.txt 로 대신하지 않는다'
                                 '(목록에만 있고 폰트엔 없는 글자를 못 잡는다 — 2026-09-08 실측). `pip install fonttools brotli` 후 재실행')
    missing = sorted({c for c in text if ord(c) > 0x7F and ord(c) not in covered and not c.isspace()})
    assert not missing, ('서브셋 밖 글자 — 원본 Pretendard 에 있으면 chars.txt·unicodes.txt 에 추가하고 build/build.sh 로 재빌드, '
                         '없으면 본문에서 지원 문자로 바꿀 것: ' + ''.join(missing))
    nos = [m.group(1).strip() for m in SEC_RE.finditer(t)]
    assert nos, '절 머리(.sec-head + .no)를 하나도 못 찾음 — 마크업 형식 확인'
    bad = [n for n in nos if n and not re.fullmatch(r'[1-9]\d*\.', n)]
    assert not bad, f'절 번호 표기 위반(허용 = 빈 값 또는 "자연수."): {bad}'
    seq = [int(n[:-1]) for n in nos if n]
    assert seq == list(range(1, len(seq)+1)), f'절 번호가 1.부터 빠짐·중복 없이 이어지지 않음: {seq}'
    first = next((i for i, n in enumerate(nos) if n), len(nos)); last = max((i for i, n in enumerate(nos) if n), default=-1)
    assert all(n for n in nos[first:last+1]), f'빈 번호가 번호 붙은 절 사이에 있음: {nos}'
    assert OLD_DEPT not in text, f'옛 부서명 {OLD_DEPT!r} 잔존 — CX부로 고칠 것'
    assert 'tag prop' not in t and 'tag check' not in t, '절차용 표식 잔존'
    return len(covered)


def assemble(src_dir, template, out_name, images=None, post=None, argv=None):
    """src_dir/template 를 조립해 docs/<out_name>.html 에 쓴다. images = {'{{IMG_X}}': 경로}. post = HTML 후처리 함수.
    argv 에 --pdf 가 있으면 docs/<out_name>.pdf 도 만든다."""
    argv = sys.argv[1:] if argv is None else argv
    src_dir = pathlib.Path(src_dir).resolve()
    t = (src_dir/template).read_text(encoding='utf-8')
    cov = check(t)
    rep = {'{{TOKENS_CSS}}': (REPO/'tokens/design-tokens.css').read_text(encoding='utf-8'),
           '{{BASE_CSS}}': (REPO/'styles/document-base.css').read_text(encoding='utf-8'),
           '{{FONT_B64}}': b64(FONT),
           '{{WM_PATHS}}': wordmark_paths(),
           **{k: b64(v) for k, v in (images or {}).items()}}
    out = t
    for k, v in rep.items(): out = out.replace(k, v)
    if post: out = post(out)
    assert '{{' not in out, re.findall(r'\{\{[A-Z_]+\}\}', out)
    OUT = HERE/f'{out_name}.html'
    OUT.write_text(out, encoding='utf-8')
    print('out', OUT.relative_to(REPO), 'bytes', len(out.encode()), 'cmap', cov)
    if '--pdf' in argv:
        pdf = to_pdf(OUT)
        print('pdf', pdf.relative_to(REPO), 'pages', page_count(pdf))
    else:
        old = OUT.with_suffix('.pdf')
        if old.exists() and old.stat().st_mtime < OUT.stat().st_mtime:
            print(f'⚠ {old.name} 는 방금 쓴 HTML 보다 오래됐다 — `--pdf` 로 다시 만들 것')
    return OUT


def to_pdf(html_path):
    """임시 파일에 찍고 종료코드·PDF 유효성(열림·쪽수>0)을 확인한 뒤 원자적으로 교체 — 실패 시 낡은 PDF 를 남기지 않고 새 PDF 로 덮지도 않는다(Codex 4b 2026-09-22)."""
    pdf = html_path.with_suffix('.pdf'); tmp = html_path.with_name(html_path.stem + '.tmp.pdf')
    if tmp.exists(): tmp.unlink()
    r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                        f'--print-to-pdf={tmp}', f'file://{html_path}'], capture_output=True, text=True, timeout=300)
    ok = r.returncode == 0 and tmp.exists() and tmp.stat().st_size > 0
    n = page_count(tmp) if ok else 0
    if n == '?': n = 1 if tmp.read_bytes()[:5] == b'%PDF-' else 0   # fitz 없으면 헤더만 확인(쪽수는 미검증)
    if not ok or not isinstance(n, int) or n < 1:
        if tmp.exists(): tmp.unlink()
        raise AssertionError(f'PDF 생성 실패(exit {r.returncode}, pages {n}) — 기존 {pdf.name} 은 건드리지 않음: {r.stderr[-400:]}')
    os.replace(tmp, pdf)
    return pdf


def page_count(pdf):
    try:
        import fitz
        return fitz.open(pdf).page_count
    except Exception:
        return '?'
