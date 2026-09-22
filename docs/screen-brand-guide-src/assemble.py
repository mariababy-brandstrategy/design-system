"""브랜드 가이드 · 화면 조립 — 템플릿 → docs/브랜드-가이드-화면-v1.2.{html,pdf}. 이미지 없음(전 예시가 텍스트·색·표). 공용 로직·검사 = docs/assemble_lib.py.
  python3 assemble.py --pdf"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from assemble_lib import assemble
assemble(pathlib.Path(__file__).parent, 'screen-brand-guide.template.html', '브랜드-가이드-화면-v1.2')
