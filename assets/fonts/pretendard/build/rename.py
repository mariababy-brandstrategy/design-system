"""OFL Reserved Font Name 준수: 서브셋(Modified Version)은 'Pretendard' 이름을 쓸 수 없다 → 'Maria Doc Sans' 로 개명.
저작권(0)·상표(7)·라이선스(13·14) 레코드는 원문 유지(OFL 이 요구). 사용: python rename.py IN.woff2 OUT.woff2"""
import sys
from fontTools.ttLib import TTFont
src,dst=sys.argv[1],sys.argv[2]
f=TTFont(src); KEEP={0,7,13,14}; n=0
for r in f['name'].names:
    if r.nameID in KEEP: continue
    s=r.toUnicode()
    if 'Pretendard' in s:
        s=s.replace('Pretendard Variable','Maria Doc Sans').replace('PretendardVariable','MariaDocSans').replace('Pretendard','Maria Doc Sans')
        if r.nameID in (6,25): s=s.replace(' ','')
        r.string=s; n+=1
f.flavor='woff2'; f.save(dst); print('renamed records',n)
