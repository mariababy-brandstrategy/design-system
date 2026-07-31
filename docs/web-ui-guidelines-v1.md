# 사내 웹 UI 일관성 가이드 v1 (2026-06-04)

마리아의료재단 **사내 웹 서비스**(로그인 뒤 직원이 쓰는 도구)를 만들 때 따라야 하는 단일 기준.
신규 앱은 **이 문서에서 시작**한다.

레퍼런스 구현: **claim**(claims.maria-baby.com) · **console**(console.maria-baby.com) · **popo-studio**(popo-studio.maria-baby.com) · **mou-admin**(mou-admin.maria-baby.com) — 4앱 모두 이 기준에 맞춰져 있음.

> **이 repo(design-system)가 단일 출처(SoT)다.** 토큰값은 `tokens/design-tokens.css`, 헤더는 `docs/internal-service-header-v1.md`, 전체 규칙은 본 문서.
> 코드 부품(토큰·컴포넌트)을 앱에 **설치**하는 건 shadcn 레지스트리 **`@maria`**(github `dyshin-maria/maria-ui`, https://maria-ui.vercel.app)가 담당 — 레지스트리는 이 repo의 토큰을 *복제*할 뿐, 값이 갈리면 **이 repo가 우선**이다.

---

## 1. 표준 v1 요약

| 영역 | 기준 |
|---|---|
| **파비콘** | iR 마크. `app/icon.png`(1000×1000) + `app/apple-icon.png`(512×512). 원본 = `assets/web-icons/`. Next 기본 ▲(`favicon.ico`)는 **삭제**. |
| **폰트** | Pretendard `@v1.3.9` **variable**: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css`. `@latest`·static 금지(버전 드리프트). |
| **헤더** | `docs/internal-service-header-v1.md` 참조. `bg-maria-green` → `max-w-7xl mx-auto px-6 py-4`. 스크롤 시 상단 고정(`sticky top-0 z-40`). 로고 = **브랜드 워드마크**(§로고: `@maria/brand-logo`, 헤더는 `h-[18px] text-white` + `trim`) + 짧은 영문 서비스명 병기. 글자 타이핑 금지. 활성 탭 = 알약 `bg-text-on-dark text-maria-green` + `aria-current="page"`(비활성은 속성 없음), 비활성 `text-maria-green-300 hover:text-text-on-dark`. |
| **로고** | 전용 워드마크. §로고 참조. `assets/logos/svg/` 정본. 어두운 배경=흰색, 밝은 배경=그린. |
| **본문 너비** | 페이지 외곽 셸(컨테이너)은 전 앱 `max-w-7xl`(1280px) — 셸을 별도로 더 좁히지 말 것. 가독성 목적의 **내부 콘텐츠 컬럼** 축소(예: hub 자료실 `max-w-4xl`)는 허용 — `internal-service-header-v1.md` v1.4 §8과 정합(2026-07-30). |
| **페이지 제목** | `text-2xl font-semibold tracking-tight text-text-primary sm:text-3xl`(=text-foreground). 제목 블록 하단 `mb-6`. 상단 여백은 레이아웃 `<main>`의 `py-6` 단일소스(페이지가 추가 py 주지 말 것). |
| **on-dark 색** | 헤더 글자·활성 탭 배경 = **아이보리 `#F4EEED`**(`--text-on-dark`). 순백 아님. (버튼 글자 `btn-*-fg`는 별개로 `#FFFFFF`.) |
| **로그인 페이지** | 아래 §3. |
| **브랜드 색** | maria-green `#1E3131` / popo-teal `#1D9581` / ivory `#F4EEED` — `tokens/design-tokens.css` 그대로. |

기술 스택(현 4앱): Next.js 16 + Tailwind v4 + Clerk + Pretendard.

## 1-1. 로고 (브랜드 워드마크)

마리아 로고는 **전용 워드마크**(커스텀 BI — `R`자에 사람 모티프가 든 디자인)다. **어떤 폰트로도 글자를 타이핑해 흉내 내지 말 것.** 반드시 아래 벡터 자산을 쓴다.

- **정본 자산**: `assets/logos/svg/`
  - `maria-wordmark.svg` — `fill="currentColor"`. 인라인 SVG·React에서 색을 CSS로 제어(**권장**).
  - `maria-wordmark-green.svg` — 고정 마리아 그린 `#1E3131`. 밝은 배경·`<img>`용.
  - `maria-wordmark-white.svg` — 고정 흰색. 어두운 배경·`<img>`용.
  - 래스터가 필요하면 `assets/logos/*.png`(white·색상별 01~05).
- **색 규칙**: 어두운 배경 = **흰색**, 밝은 배경 = **마리아 그린 `#1E3131`**(디자이너 3원칙 "어두운 배경엔 100% white"와 일치). **아이보리 워드마크 금지.**
- **비율·여백**: 601:229 (≈2.63:1) 고정, 가로세로비 유지. 클리어 스페이스 = 워드마크 높이의 1/2 이상.
- **코드 소비**: `@maria/brand-logo`(registry:component, currentColor 인라인) → 어두운 배경 `<BrandLogo className="h-5 text-white" />`, 밝은 배경 `text-maria-green`. 비-React/정적 HTML은 위 SVG를 인라인하거나 `<img src="…maria-wordmark-{green|white}.svg">`.
- **텍스트와 나란히 둘 때**: 원본 viewBox 는 `.ai` 페이지 박스라 마크 **아래에 52.4/228.8 만큼 여백**이 남는다. 그대로 가운데 정렬하면 옆 글자와 **밑선이 어긋난다**(2026-07-31 헤더에서 발견). `trim` 속성(마크 실제 경계 viewBox `52.586 27.125 496.027 149.266`) + `items-baseline` 을 쓴다 — 상자 밑변이 곧 글자 밑선이라 폰트 지표와 무관하게 맞는다.
- **출처/재생성**: `01.로고/로고모음/로고 색상별.ai` → `pdftocairo -svg -f1 -l1`(벡터, 래스터 내장 0). .ai 원본 그린(#163231)은 공식 토큰 #1E3131로 정규화.
- **현재 적용 현황(2026-07-31)**: 정적 산출물·신규 작업 + **사내 웹앱 헤더 4/5** 워드마크 사용(console·popo·mou·claim 완료, **hub 잔여** — `internal-service-header-v1.md` §8 참조). 텍스트 로고 legacy 허용은 **종료** — ui-audit static 이 `header-wordmark` 로 강제한다(BrandLogo 부재 또는 아이보리 착색이면 FAIL). 단 hub 는 ui-audit APPS 에 미등록이라 이 강제가 닿지 않는다. 헤더 적용 규격은 `internal-service-header-v1.md` §2·§4(v1.5).

## 2. 신규 앱 적용 절차

1. `tokens/design-tokens.css`를 앱 `globals.css`(또는 `styles/design-tokens.css`)에 그대로 가져온다. **값을 옮겨 적지 말고 파일째 복사**.
2. `@maria` 레지스트리에서 토큰·부품 설치(§4). (설치 불가 시 §7 비상 경로.)
3. 헤더를 `internal-service-header-v1.md`의 `PageShell`로 구성.
4. 로그인 페이지를 §3 템플릿으로.
5. 파비콘 `assets/web-icons/icon.png`·`apple-icon.png`를 앱 `app/`에 복사, `favicon.ico` 삭제.
6. 폰트 CDN 링크(§1)를 `layout`에 추가.
7. §5 필수 확인 체크 → §6 검증 → `internal-service-header-v1.md` §8 적용현황 표에 한 줄 추가.

## 3. 로그인 페이지 템플릿

4앱 동일(claim·console·popo·mou). 공개 화면이라 미리보기로도 검증 가능.

- 바깥: `<main className="flex min-h-screen flex-col items-center justify-center bg-bg-ivory p-6">`
- 제목 블록: `<div className="mb-6 text-center">` 안에 `<h1 className="text-2xl font-bold tracking-tight text-text-primary">{앱이름}</h1>` + `<p className="mt-1 text-sm text-text-body">{한 줄 설명}</p>`
- 폼 카드: `<… className="w-full max-w-sm space-y-4 rounded-lg border border-border-default bg-bg-default p-6">` (2026-07-08: 장식용 `shadow-sm` 제거 — 경계는 1px border로. 그림자는 드롭다운·모달 등 떠 있는 층에만.)
  - 입력: `w-full rounded-md bg-bg-default border border-border-default px-3 py-2.5 text-sm focus:border-popo-teal-500 focus:ring-1 focus:ring-popo-teal-500`
  - 버튼: `w-full rounded-md bg-maria-green text-text-on-dark font-semibold py-2.5 hover:bg-maria-green-700 disabled:opacity-50`
  - 에러: `rounded-md bg-state-error-bg px-3 py-2 text-sm text-state-error-fg` (#FCEEED / #8B4540)
- 푸터: `<p className="mt-6 text-center text-xs text-text-muted">마리아의료재단 CX부</p>`

## 4. `@maria` 레지스트리 설치

```bash
# components.json 의 registries 에 추가:
#   "@maria": { "url": "https://maria-ui.vercel.app/r/{name}.json",
#               "headers": { "Authorization": "Bearer ${MARIA_UI_TOKEN}" } }
MARIA_UI_TOKEN=<토큰> pnpm dlx shadcn@latest add @maria/theme        # 토큰
MARIA_UI_TOKEN=<토큰> pnpm dlx shadcn@latest add @maria/brand-logo   # 워드마크 로고
```
토큰 발급/원문 보관·접근 검증은 `dyshin-maria/maria-ui`의 `RUNBOOK.md`. (헤더/로그인 컴포넌트는 레지스트리에 추가 예정 — 그 전엔 design-system 문서의 코드를 카피.)

## 5. 필수 수동 확인 (배포 후)

- [ ] 탭 파비콘이 iR 마크 (`/icon.png` HTTP 200 응답, 56,774 bytes 기준)
- [ ] 헤더 `max-w-7xl`·`bg-maria-green`·활성 탭 알약 강조
- [ ] 본문 `max-w-7xl`
- [ ] 페이지 제목 `text-2xl semibold`(데스크톱 3xl)
- [ ] 로그인 페이지 §3 일치
- [ ] **라이브 CSS의 `--text-on-dark` 정의값 = `#f4eeed`** (파일이 아니라 배포 CSS로 확인)
- [ ] 폰트 CDN = `@v1.3.9/variable`

## 6. 금지·주의

- ❌ `globals.css`에서 `@import` **뒤**에 `:root { --text-on-dark: … }` 등으로 토큰 **재정의(override)** — 토큰을 가려 라이브가 갈린다(2026-06-04 console·popo 실제 사고).
- ❌ 앱별로 hex 값을 손으로 옮겨 적기 — `tokens/design-tokens.css`를 파일째 가져올 것.
- ❌ 본문 페이지를 임의로 더 좁히기(7xl 통일 위반).
- ⚠️ 검증은 토큰 파일이 아니라 **배포된 CSS**로(override가 파일엔 안 보이고 라이브에만 나타남).

## 7. 비상 fallback (레지스트리 접근 불가 시)

`@maria` 레지스트리는 인증 게이트(private)다. 토큰 만료·장애·긴급 hotfix로 접근이 막히면:
1. 이 repo `tokens/design-tokens.css`를 직접 복사(레지스트리 없이도 토큰 확보).
2. 헤더/로그인은 `internal-service-header-v1.md`·본 문서 §3 코드를 카피.
3. 레지스트리 토큰 복구는 maria-ui `RUNBOOK.md`.

→ **레지스트리가 막혀도 이 repo만 있으면 수동으로 일관성 적용 가능.**

## 8. 예외

기준에서 벗어나야 하는 합당한 이유가 있으면 **먼저 명시 확인** 후 진행하고, 이 문서에 사유와 함께 기록한다.

## 9. 변경 이력

- **v1.3 (2026-07-31)**: 헤더 행에 활성 탭 `aria-current="page"` 추가(알약 배경은 시각 사용자에게만 현재 위치를 알린다). 상세 규격 = `internal-service-header-v1.md` v1.6.
- **v1.2 (2026-07-31)**: 헤더 행에 **스크롤 상단 고정**(`sticky top-0 z-40`) 추가. §1-1 로고: 소비 예시의 색을 `text-text-on-dark`(아이보리) → `text-white` 로 정정(같은 절의 "아이보리 워드마크 금지"와 모순이던 오기) + 텍스트와 나란히 둘 때의 `trim`·`items-baseline` 밑선 규칙 신설 + 4앱 텍스트 로고 legacy 허용 종료(ui-audit `header-wordmark` 강제). 상세 규격 = `internal-service-header-v1.md` v1.5.
- **v1.1 (2026-06-17)**: §1-1 로고(브랜드 워드마크) 신설. 정본 SVG(`assets/logos/svg/`, currentColor·green·white) + 색/비율/소비 규칙 + "글자 타이핑 금지" 명문화. 헤더 로고를 텍스트→워드마크로 변경(앱 적용은 `@maria/brand-logo`로 단계 이행, 별도 롤아웃). 기존 PNG 로고는 벡터 부재로 코드 산출물에 미사용되던 갭 해소.
- **v1 (2026-06-04)**: claim·console·popo·mou 4앱 전수 UI 통일 작업에서 추출. 파비콘·헤더·너비·로그인·제목·폰트·on-dark(아이보리) 확정 + 토큰 override 드리프트 함정 명문화.
