# §5 미시 사례 렌더 — 출처·재현 (2026-09-03)

세 장 모두 AI 생성이 아니라 HTML→PNG 렌더(1080×1920, 크롬 헤드리스 CDP). 재현 = `~/maria-ops-archive/handoffs/space-brand-guide/mock/`(`python3 build.py && node render.mjs`, SVG·명령·README 동봉). 색은 안내판·픽토그램 판이 §3 일곱 색만(보조 글자도 마리아 그린)이고, 도어사인은 운영 화면 UI 팔레트(웹 토큰)를 그대로 보존한다(캡션이 물리 사인 기준 아님을 밝힌다).

| 파일 | 내용 | 출처 |
|---|---|---|
| `sign-doorsign.png` | 진료실 디지털 도어사인 예시 화면 | `~/maria-doorsign-v2/build/tool-src.html`(부천마리아 운영 도구, 2026-08) `#screen` 모드에 예시 상태(진료실 3 · OOO 원장 · 공지 2건 · 진료중) 주입 후 캡처. 화면 UI 이며 물리 사인 색·배치 기준 아님 |
| `sign-directory.png` | 층별 안내판 목업(아이보리 판면 · 그린 글자 · 현재 층 막대 하나만 포포 틸 · 로고 없음) | `mock/build.py` 생성. 실 이름 예시 |
| `sign-pictograms.png` | 공공안내 픽토그램 12종, 마리아 그린 단색 | 아래 AIGA/DOT 도안 |

## 픽토그램 도안 — AIGA/DOT Symbol Signs

- 원 도안: 미국 교통부(DOT)가 AIGA 와 함께 1974년과 1979년에 만든 공공안내 심볼 50종. AIGA 는 이를 저작권 없이 누구나 쓸 수 있게 공개한다고 안내한다(https://www.aiga.org/resources/symbol-signs, 2026-09-03 검색 결과로 확인. 페이지 직접 fetch 는 403).
- 사용 파일: `apancik/public-domain-icons` 저장소 `dist/`(commit `df284bf4bbd52becf5d3cf73791660e3f538a1e3`, 2022-07-29). README: "free of known restrictions under copyright law … even for commercial purposes, all without asking permission, or attribution". 교차 확인 = Wikimedia Commons `Category:AIGA symbol signs` 의 `PD-AIGA` 파일들이 API extmetadata `LicenseShortName=Public domain`(2026-09-03).
- ⚠ 위 셋은 권리자의 법적 보증이 아니다. 문서 캡션에는 법률 판정을 적지 않고 출처만 적는다.
- ⚠ AIGA/DOT 는 ISO 7001 과 별개 체계다. "계열·원류"로 부르지 않는다. 응급·금연·비상구 같은 안전·법정 표지는 이 세트로 대체하지 않는다(화재안전기준 유도등·안전보건표지·금연 표지 별도).
- 라벨은 원 도안 이름과 1:1 — Nursery 는 유아실(수유실 아님), Drinking Fountain 은 음수대(정수기 아님).

| 파일(apancik dist) | 라벨 | sha256 앞 12 |
|---|---|---|
| `symbol information question help.svg` | 안내 / Information | `a8c619e2bbf4` |
| `human waiting room.svg` | 대기실 / Waiting Room | `9c3235ff1097` |
| `symbol elevator.svg` | 엘리베이터 / Elevator | `4f9bc217a4a2` |
| `symbol stairs.svg` | 계단 / Stairs | `6765ca37a01d` |
| `human unisex restroom toilets.svg` | 화장실 / Toilets | `9cefa0771b9d` |
| `human baby nursery.svg` | 유아실 / Nursery | `9f0d62008d02` |
| `human drinking fountain water fountain.svg` | 음수대 / Drinking Fountain | `6072fa3738ea` |
| `object cup coffee tea drink coffeeshop.svg` | 카페 / Coffee Shop | `0e319d2331d2` |
| `symbol cashier.svg` | 수납 / Cashier | `d61bbcc2300c` |
| `symbol parking.svg` | 주차 / Parking | `894c222def42` |
| `object coat check clothes hanger.svg` | 물품 보관 / Coat Check | `c0ae30021802` |
| `object telephone.svg` | 전화 / Telephone | `2d549eee26f3` |

## 검토했으나 쓰지 않은 세트
- KS S ISO 7001(한국 표준): 심볼 파일은 한국표준정보망(KSSN)에서 AI/EPS 로 제공하며 견적 요청 절차 = 유상. 이번 렌더에는 쓰지 않았다. 협력사가 실제 제작에 쓰는 것은 별개.
- JIS Z 8210 / 에코모재단 표준안내용도기호: 2017 가이드라인 원문에 "누구나 자유롭게 사용" 문구. 다만 현행 페이지는 비JIS 도안만 EPS/PNG 배포로 구분해 재확인이 필요해 채택하지 않았다.
- Health icons(healthicons.org, CC0): 의료 도상(초음파·채혈 등)이 필요할 때의 대안. 이번 판은 공공안내만 다뤄 미사용.
- SEGD/Hablamos Juntos 의료 심볼 56종: 라이선스 문구를 사이트에서 확인하지 못해 미사용.
