"""화면 브랜드 가이드 조립: 템플릿 + (tokens → document-base → override) + 워드마크 SVG + 서브셋 폰트 → 단일 HTML.
편집 = 템플릿 → python3 assemble.py → 크롬 헤드리스 PDF:
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/화면-브랜드-가이드-v1.0.pdf" "file://$PWD/화면-브랜드-가이드-v1.0.html"
repo 안(docs/screen-brand-guide-src/)에서는 상대경로, 작업본 폴더에서는 ~/design-system 을 정본으로 읽는다.
공간 브랜드 가이드와 달리 이미지가 없다(전 예시가 텍스트·색·표) — 조립 대상은 CSS 3종 + 폰트 + 워드마크뿐이다.

⚠ 커버리지 검사는 `chars.txt` 가 아니라 **실제 woff2 의 cmap** 을 본다(2026-09-08 Codex 4b 실측).
   chars.txt 만 대조하면 원본 Pretendard 에 **없는** 글자를 목록에 넣은 것만으로 통과한다 —
   서브셋에는 들어갈 수 없으므로 그 글자는 조용히 시스템 폰트로 떨어진다(✕ U+2715 · ⬇ U+2B07 이 실제 사례).
   검사는 파일을 쓰기 **전에** 돌아 실패 시 낡은 생성물을 남기지 않는다."""
import base64,html,json,os,pathlib,re,subprocess,sys
S=pathlib.Path(__file__).resolve().parent
REPO=S.parents[1] if (S.parents[1]/'tokens/design-tokens.css').exists() else pathlib.Path(os.path.expanduser('~/design-system'))
FONT=REPO/'assets/fonts/pretendard/maria-doc-sans-subset.woff2'  # Pretendard v1.3.9 variable 서브셋, OFL RFN 때문에 개명(README 참조)

def font_cmap(path):
    """서브셋 woff2 가 실제로 담은 코드포인트. fontTools 가 없으면 None(=미검증)."""
    code=("import sys,json;from fontTools.ttLib import TTFont;"
          "print(json.dumps(sorted(TTFont(sys.argv[1]).getBestCmap())))")
    for py in (sys.executable, str(FONT.parent/'build/.venv/bin/python')):
        try:
            r=subprocess.run([py,'-c',code,str(path)],capture_output=True,text=True,timeout=120)
            if r.returncode==0: return set(json.loads(r.stdout))
        except Exception: pass
    return None

t=(S/'screen-brand-guide-v1.0.template.html').read_text(encoding='utf-8')

# ── 커버리지 검사 (쓰기 전) ──
text=re.sub(r'<style.*?</style>','',t,flags=re.S)
text=html.unescape(re.sub(r'<[^>]+>','',text))          # 엔티티(&nbsp; 등)를 실제 글자로 펴서 본다
cmap=font_cmap(FONT)
if cmap is None:
    covered=set(ord(c) for c in (FONT.parent/'chars.txt').read_text(encoding='utf-8'))
    print('⚠ fontTools 없음 — cmap 대신 chars.txt 로 대조했다(목록에만 있고 폰트엔 없는 글자를 못 잡는다)')
else:
    covered=cmap
missing=sorted({c for c in text if ord(c)>0x7F and ord(c) not in covered and not c.isspace()})
assert not missing, ('서브셋 밖 글자 — 원본 Pretendard 에 있으면 chars.txt·unicodes.txt 에 추가하고 build/build.sh 로 재빌드, '
                     '없으면 본문에서 지원 문자로 바꿀 것: '+''.join(missing))

# ── 조립 ──
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
svg=(REPO/'assets/logos/svg/maria-wordmark.svg').read_text(encoding='utf-8')
paths=''.join(re.findall(r'<path[^>]*/>',svg))
paths=re.sub(r'\s*fill="currentColor"\s*fill-opacity="1"','',paths)  # 부모 fill 상속
paths=re.sub(r'\s+fill-rule="nonzero"','',paths)
rep={'{{TOKENS_CSS}}':(REPO/'tokens/design-tokens.css').read_text(encoding='utf-8'),
     '{{BASE_CSS}}':(REPO/'styles/document-base.css').read_text(encoding='utf-8'),
     '{{FONT_B64}}':b64(FONT),
     '{{WM_PATHS}}':paths}
out=t
for k,v in rep.items(): out=out.replace(k,v)
assert '{{' not in out, re.findall(r'\{\{[A-Z_]+\}\}',out)
OUT=(S.parent/'화면-브랜드-가이드-v1.0.html') if S.name=='screen-brand-guide-src' else (S/'screen-brand-guide-v1.0.html')  # repo 안이면 정식 소비자(docs/)에 바로 쓴다
OUT.write_text(out,encoding='utf-8')
print('out',OUT,'bytes',len(out.encode()),'repo',REPO,'cmap',len(covered) if cmap else 'chars.txt fallback','missing 0')
