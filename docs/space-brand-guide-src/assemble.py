import base64,re,sys,pathlib
S=pathlib.Path(__file__).resolve().parent  # 핸드오프 폴더 기준
t=(S/'space-brand-guide-v1.0.template.html').read_text(encoding='utf-8')
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
svg=pathlib.Path('/Users/dyshin/design-system/assets/logos/svg/maria-wordmark.svg').read_text(encoding='utf-8')
paths=''.join(re.findall(r'<path[^>]*/>',svg))
paths=re.sub(r'\s*fill="currentColor"\s*fill-opacity="1"','',paths)  # 부모 fill 상속
paths=re.sub(r'\s+fill-rule="nonzero"','',paths)
rep={'{{FONT_B64}}':b64('/Users/dyshin/maria-doorsign-v2/build/pretendard-subset.woff2'),
     '{{WM_PATHS}}':paths,
     '{{IMG_SIGNAGE}}':b64(S/'img/signage.png'),'{{IMG_BADGE}}':b64(S/'img/badge.png')}
n_prop=t.count('tag prop')-1  # 표식 설명의 예시 태그 1개 제외
assert 'tag check' not in t, '확인 필요 태그 잔존'
t=t.replace('{{N_PROP}}',str(n_prop)); print('초안 제안',n_prop,'건')
out=t
for k,v in rep.items(): out=out.replace(k,v)
assert '{{' not in out, re.findall(r'\{\{[A-Z_]+\}\}',out)
(S/'space-brand-guide-v1.0.html').write_text(out,encoding='utf-8')
# 서브셋 글자 커버리지
sub=set(open('/Users/dyshin/maria-doorsign-v2/build/subset-chars.txt',encoding='utf-8').read())
text=re.sub(r'<style.*?</style>','',t,flags=re.S); text=re.sub(r'<[^>]+>','',text)
missing=sorted({c for c in text if ord(c)>0x2000 and c not in sub and not c.isspace()})
print('bytes',len(out.encode()),'missing glyphs',len(missing),''.join(missing)[:200])
