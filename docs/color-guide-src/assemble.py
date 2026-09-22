"""브랜드 가이드 · 색상 조립 — 템플릿 → docs/브랜드-가이드-색상-v2.3.{html,pdf}. 공용 로직·검사 = docs/assemble_lib.py.
편집 정본은 이 폴더의 template 이다 — docs/ 의 생성물은 직접 고치지 말 것(다음 조립에서 지워진다).
  python3 assemble.py --pdf   (HTML + 크롬 헤드리스 PDF + 쪽수)"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from assemble_lib import assemble
assemble(pathlib.Path(__file__).parent, 'color-guide.template.html', '브랜드-가이드-색상-v2.3')
