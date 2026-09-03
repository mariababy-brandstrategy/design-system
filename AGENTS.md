# 여기는 마리아 사내 웹 UI 의 규칙 정본(SoT)이다

`docs/web-ui-guidelines-v1.md`(진입점) + `docs/internal-service-header-v1.md`(헤더 상세)
+ `tokens/design-tokens.css`(토큰 값). 다른 어디와 값이 갈리면 **여기가 우선한다.**

소비 구조: 이 문서의 규칙을 `dyshin-maria/maria-ui` 의 비공개 레지스트리 `@maria/*` 가
코드로 구현하고, 사내 현역 6앱(console·popo-studio·mou-admin·hub·labs·sns)이 그걸 설치해 쓴다
(claim 은 2026-08-22 서비스 폐기 — 2026-08-25 검사 모집단에서도 제외됨. 되살리면 재등록).
hub 는 `components.json` 이 없어 레지스트리 부품은 손복사본이고, **토큰은 design-system
서브모듈**(`hub/design-system` → 이 repo)로 소비한다 — 토큰 개정 시 hub 는 서브모듈 포인터를
올린다(2026-08-25 실측 정정: 종전 "토큰도 손복사" 기술은 사실과 달랐다).
(2026-08-12 정정: 오래 "5앱"으로 적혀 있어 **labs·sns 를 빠뜨릴 위험**이 있었다.
앱 목록의 기계 정본은 `maria-ui/scripts/ui-audit.config.mjs` 의 `APPS` 다.)

## 문서를 고칠 때

문서만 고치면 **아무것도 바뀌지 않는다.** 규칙을 바꿨으면 구현과 앱까지 따라가야 한다:

1. `maria-ui` 의 `registry/` 구현 갱신
2. `maria-ui/scripts/ui-audit.mjs` 에 그 규칙을 강제하는 검사 추가·갱신
3. 6앱 재동기(5앱은 `shadcn add --overwrite`, hub 는 부품 손복사·토큰은 서브모듈 bump)
4. `node ~/maria-ui/scripts/ui-audit.mjs --static-only` 로 전수 확인
5. 문서 끝 **변경 이력에 버전 한 줄** 추가

## 정본에서 벗어나는 변경 요청을 받으면

바로 적용하지 말고 먼저 "이건 정본의 <어느 항목>과 다르다"를 알리고 확인을 받는다.
디자인 변경은 전부 에이전트를 거친다는 전제로 **자동 순찰을 두지 않기로 했다**
(사용자 결정 2026-07-31). 감시자가 없으므로 이 확인 절차가 유일한 게이트다.

## 브랜드 자산 주의

로고는 전용 워드마크다. **어떤 폰트로도 글자를 타이핑해 흉내 내지 않는다.**
정본 SVG = `assets/logos/svg/`, 코드 소비는 `@maria/brand-logo`.
어두운 배경에서는 100% 흰색(`text-white`)이고 아이보리(`text-on-dark`)는 금지다.

## 문서 레이어 — HTML→PDF 문서는 「문서를 고칠 때」 5단계 밖이다 (2026-09-03 신설)

토큰을 소비하는 **정적 문서**(브라우저로 읽고 A4 로 인쇄하는 HTML→PDF)는 사내 웹 UI 가 아니다.
registry 부품을 쓰지 않고 6앱과 재동기할 것도 없다.

- **면제 기준은 바뀐 파일이다.** `styles/document-base.css` 와 `docs/` 의 문서 소스만 바뀌면 5단계를 발동하지
  않는다. 같은 작업이 `tokens/design-tokens.css`·`docs/web-ui-guidelines-v1.md`·이 파일을 만지면 그 부분은 5단계로 판정한다.
- **우선순위**: 공유 축(색·대비·굵기·크기 스케일·간격 스텝·폰트)은 이 파일 첫 문단의 정본이 우선한다 →
  `styles/document-base.css`(문서 구현 — 절 리듬·판면·인쇄만 여기가 정한다) → 문서 자체 override(예외는 사유 주석과 함께).
- **포함 순서 고정**: `tokens/design-tokens.css` → `styles/document-base.css` → 문서 override. base 는 스코프 루트 `.doc`
  아래에서만 작동한다 — `.doc` 하위 요소 기본값(h1~h4·p·a·목록·표·figure·footer) + opt-in 기구(`.sheet`·`.sec-head`·`.cont` 등).
  전역 리셋은 없지만 `@page` 는 전역 인쇄 규칙이라 스코프할 수 없다 → base 는 문서 전용이며 앱 번들에 넣지 않는다.
- **적용되는 정본 축**: §1-1 로고 · §1-4 색·대비(값 기준) · §1-9 굵기·스케일 · §1-10 간격 스텝 · Pretendard 고정 버전
  (문서 임베드용 서브셋 = `assets/fonts/pretendard/`, 웹 앱은 §1 표의 CDN).
- **적용 대상 부재**(§1-12 셸과 같은 이유 — 오갈 화면이 없다): 헤더·본문 너비·`<main>` 여백·페이지 제목 블록 ·
  §1-2 아이콘 세트 · §1-3 탭 제목 서식 · §1-5 다이얼로그 · §1-7 배지 · §1-8 행동 라벨 · §1-13 폼 버튼(상호작용 축 전부).
- **소비자**(2): `docs/공간-브랜드-가이드-v1.0.{html,pdf}`(소스 `docs/space-brand-guide-src/`) · `docs/v2.1-실무자용.{html,pdf}`
  (색상 가이드, 소스 `docs/color-guide-src/`, 2026-09-03 이전). base 를 고치면 소비자 전부를
  재조립해 렌더 diff 로 확인하고 이 목록을 갱신한다. 기계 검사는 두지 않는다(소비자 1~2건 — 정직 표기).
- 최초 신설(2026-09-03)은 5단계 계약이 있던 상태에서 이 파일을 바꾼 것이므로, `ui-audit.mjs --static-only` 를 1회 돌려
  웹 UI 영향 없음을 확인하고 결과를 커밋 메시지에 남겼다.

## UI 작업의 완료 조건

**UI 를 건드린 작업은 `node ~/maria-ui/scripts/ui-audit.mjs --static-only` 가 통과해야
끝난 것이다**(권고가 아니라 완료 조건).
사람이 의도하지 않은 시각 변화는 주로 옆문으로 들어온다 — **오래된 브랜치 병합 ·
Tailwind/의존성 업그레이드 · codemod · GitHub 웹 편집**도 UI 변경으로 친다.
사전 확인 모델은 그 경로들을 스스로 막지 못하므로, 이 확인이 마지막 그물이다.
