# 여기는 마리아 사내 웹 UI 의 규칙 정본(SoT)이다

`docs/web-ui-guidelines-v1.md`(진입점) + `docs/internal-service-header-v1.md`(헤더 상세)
+ `tokens/design-tokens.css`(토큰 값). 다른 어디와 값이 갈리면 **여기가 우선한다.**

소비 구조: 이 문서의 규칙을 `dyshin-maria/maria-ui` 의 비공개 레지스트리 `@maria/*` 가
코드로 구현하고, 사내 5앱(console·popo-studio·mou-admin·claim·hub)이 그걸 설치해 쓴다.
hub 만 `components.json` 이 없어 손복사본이다.

## 문서를 고칠 때

문서만 고치면 **아무것도 바뀌지 않는다.** 규칙을 바꿨으면 구현과 앱까지 따라가야 한다:

1. `maria-ui` 의 `registry/` 구현 갱신
2. `maria-ui/scripts/ui-audit.mjs` 에 그 규칙을 강제하는 검사 추가·갱신
3. 5앱 재동기(4앱은 `shadcn add --overwrite`, hub 는 손복사)
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
