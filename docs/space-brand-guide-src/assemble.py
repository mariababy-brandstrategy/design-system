"""브랜드 가이드 · 공간 조립 — 템플릿 + img/ → docs/브랜드-가이드-공간-v1.2.{html,pdf}. 공용 로직·검사 = docs/assemble_lib.py.
  python3 assemble.py --pdf"""
import pathlib, sys
S = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(S.parents[0]))
from assemble_lib import assemble
IMG = {'{{IMG_SIGNAGE}}': S/'img/signage.png', '{{IMG_BADGE}}': S/'img/badge.png',
       # §1 공간 인상 = AI 생성 이미지(분위기 참고용) · 5절 미시 사례 = 실제 렌더(img/sign-sources.md)
       '{{IMG_SPACE_LOUNGE}}': S/'img/space-lounge.jpg', '{{IMG_SPACE_CORRIDOR}}': S/'img/space-corridor.jpg', '{{IMG_SPACE_RECEPTION}}': S/'img/space-reception.jpg',
       '{{IMG_SIGN_DOORSIGN}}': S/'img/sign-doorsign.png', '{{IMG_SIGN_DIRECTORY}}': S/'img/sign-directory.png', '{{IMG_SIGN_PICTOGRAMS}}': S/'img/sign-pictograms.png'}
assemble(S, 'space-brand-guide.template.html', '브랜드-가이드-공간-v1.2', images=IMG)
