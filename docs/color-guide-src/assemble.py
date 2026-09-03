"""색상 가이드 조립: 템플릿 + (tokens → document-base → override) + 워드마크 SVG + 서브셋 폰트 → 단일 HTML.
편집 = 템플릿 → python3 assemble.py → 크롬 헤드리스 PDF:
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/v2.1-실무자용.pdf" "file://$PWD/v2.1-실무자용.html"
편집 정본은 이 폴더의 template 이다 — docs/v2.1-실무자용.{html,pdf} 는 생성물이므로 직접 고치지 말 것.
repo 안(docs/color-guide-src/)에서는 상대경로, 작업본 폴더에서는 ~/design-system 을 정본으로 읽는다."""
import base64,re,pathlib,os
S=pathlib.Path(__file__).resolve().parent
REPO=S.parents[1] if (S.parents[1]/'tokens/design-tokens.css').exists() else pathlib.Path(os.path.expanduser('~/design-system'))
t=(S/'color-guide-v2.1.template.html').read_text(encoding='utf-8')
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
svg=(REPO/'assets/logos/svg/maria-wordmark.svg').read_text(encoding='utf-8')
paths=''.join(re.findall(r'<path[^>]*/>',svg))
paths=re.sub(r'\s*fill="currentColor"\s*fill-opacity="1"','',paths)  # 부모 fill 상속
paths=re.sub(r'\s+fill-rule="nonzero"','',paths)
FONT=REPO/'assets/fonts/pretendard/maria-doc-sans-subset.woff2'  # Pretendard v1.3.9 variable 서브셋, OFL RFN 때문에 개명(README 참조)
rep={'{{TOKENS_CSS}}':(REPO/'tokens/design-tokens.css').read_text(encoding='utf-8'),
     '{{BASE_CSS}}':(REPO/'styles/document-base.css').read_text(encoding='utf-8'),
     '{{FONT_B64}}':b64(FONT),
     '{{WM_PATHS}}':paths}
out=t
for k,v in rep.items(): out=out.replace(k,v)
assert '{{' not in out, re.findall(r'\{\{[A-Z_]+\}\}',out)
OUT=(S.parent/'v2.1-실무자용.html') if S.name=='color-guide-src' else (S/'v2.1-실무자용.html')  # repo 안이면 정식 소비자(docs/)에 바로 쓴다
OUT.write_text(out,encoding='utf-8')
# 서브셋 글자 커버리지(비ASCII 전수 — 밖이면 토큰 사슬의 다음 폰트로 떨어진다)
sub=set((FONT.parent/'chars.txt').read_text(encoding='utf-8'))
text=re.sub(r'<style.*?</style>','',t,flags=re.S); text=re.sub(r'<[^>]+>','',text)
missing=sorted({c for c in text if ord(c)>0x7F and c not in sub and not c.isspace()})
print('out',OUT,'bytes',len(out.encode()),'repo',REPO,'missing glyphs',len(missing),''.join(missing)[:200])
assert not missing, '서브셋 밖 글자 — chars.txt 에 추가하고 폰트를 다시 빌드할 것: '+''.join(missing)
