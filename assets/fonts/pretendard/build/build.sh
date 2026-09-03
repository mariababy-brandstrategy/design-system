#!/bin/sh
# Pretendard v1.3.9 variable → 서브셋 woff2 (마리아 문서 레이어 임베드용)
# 원본: https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/packages/pretendard/dist/web/variable/woff2/PretendardVariable.woff2
#   = build/PretendardVariable.woff2 (name "Version 1.309", SHA-256 9599f12fd42fc0bce1cd50b47a0c022e108d7aa64dd0d1bb0ed44f3282d900b4)
# 라이선스 OFL 1.1 = build/LICENSE.txt. 서브셋은 Modified Version 이라 예약 글꼴명 'Pretendard' 를 쓸 수 없다 → rename.py 로 'Maria Doc Sans'.
# 도구: fonttools 4.64.0 · brotli 1.2.0 (python3 -m venv .venv && .venv/bin/pip install 'fonttools==4.64.0' 'brotli==1.2.0')
# 실행: PYFT_PYTHON=.venv/bin/python sh build/build.sh   (woff2 는 timestamp 를 담지 않아 같은 입력·도구면 byte 재현)
set -e; cd "$(dirname "$0")/.."
PY="${PYFT_PYTHON:-python3}"
"$PY" -m fontTools.subset build/PretendardVariable.woff2 \
  --unicodes-file=unicodes.txt --flavor=woff2 --layout-features='*' \
  --name-IDs='*' --notdef-outline --output-file=build/_subset-tmp.woff2
"$PY" build/rename.py build/_subset-tmp.woff2 maria-doc-sans-subset.woff2 && rm -f build/_subset-tmp.woff2
shasum -a 256 maria-doc-sans-subset.woff2
