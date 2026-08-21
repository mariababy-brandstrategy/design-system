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
| **폰트** | Pretendard `@v1.3.9` **variable**: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable[.min].css`. `@latest`·static 금지(버전 드리프트). **`.min` 여부는 자유** — 이 CSS 는 `@font-face` 한 줄짜리(526B)라 압축 이득이 없고, jsDelivr 이 붙이는 안내 주석 탓에 `.min` 쪽이 오히려 588B 로 더 크다(2026-07-31 실측). 고정 대상은 **버전과 variant** 뿐이다. |
| **헤더** | `docs/internal-service-header-v1.md` 참조. `bg-maria-green` → `max-w-7xl mx-auto px-6 py-4`. 스크롤 시 상단 고정(`sticky top-0 z-40`). 로고 = **브랜드 워드마크**(§로고: `@maria/brand-logo`, 헤더는 `h-[18px] text-white` + `trim`) + 짧은 영문 서비스명 병기. 글자 타이핑 금지. 활성 탭 = 알약 `bg-text-on-dark text-maria-green` + `aria-current="page"`(비활성은 속성 없음), 비활성 `text-maria-green-300 hover:text-text-on-dark`. |
| **로고** | 전용 워드마크. §로고 참조. `assets/logos/svg/` 정본. 어두운 배경=흰색, 밝은 배경=그린. |
| **아이콘** | **Lucide 계열 단일 세트**(두 번째 아이콘 세트 병용 금지). 24×24 격자 · 획 `stroke-width` 2 · 색은 `currentColor`. 크기는 숫자가 아니라 **역할**로 고른다(`size-3.5`/**`size-4`**/`size-5` + 전체화면 상태 `size-8`·`size-12`). 표기는 `size-*` 하나로. §1-2 참조. |
| **본문 너비** | 페이지 외곽 셸(컨테이너)은 전 앱 `max-w-7xl`(1280px) — 셸을 별도로 더 좁히지 말 것. 가독성 목적의 **내부 콘텐츠 컬럼** 축소(예: hub 자료실 `max-w-4xl`)는 허용 — `internal-service-header-v1.md` v1.4 §8과 정합(2026-07-30). |
| **페이지 제목** | `text-2xl font-semibold tracking-tight text-text-primary sm:text-3xl`(=text-foreground). 제목 블록 하단 `mb-6`. 상단 여백은 레이아웃 `<main>`의 `py-6` 단일소스(페이지가 추가 py 주지 말 것). **앱별 예외는 §8 표를 따른다**(hub·popo). |
| **on-dark 색** | 헤더 글자·활성 탭 배경 = **아이보리 `#F4EEED`**(`--text-on-dark`). 순백 아님. (버튼 글자 `btn-*-fg`는 별개로 `#FFFFFF`.) |
| **로그인 페이지** | 아래 §3. |
| **브랜드 색** | maria-green `#1E3131` / popo-teal `#1D9581` / ivory `#F4EEED` — `tokens/design-tokens.css` 그대로. |

> **페이지 안 컨트롤의 활성 배경 — `popo-teal-700` 선례**(2026-08-12, popo-studio `/history`).
> `popo-teal`(500, `#1D9581`) 위에 on-dark(`#F4EEED`) 작은 글자를 얹으면 대비 **3.23:1** 로
> WCAG AA(작은 글자 4.5:1)에 못 미친다. 같은 팔레트의 `popo-teal-700`(`#167565`)이면 **4.86:1**
> 로 통과한다. 그래서 popo-studio 히스토리의 인페이지 세그먼트(종류·범위·기간) 활성 배경은
> `popo-teal-700` 을 쓴다. **브랜드 색 3종의 값은 그대로**이며(ui-audit `brand-color` 대상 불변,
> 스케일 변형은 검사 대상 아님), 헤더 활성 탭(알약 = `bg-text-on-dark`)과도 무관하다.
> 다른 앱이 같은 형태(작은 글자 + 틸 채움)를 만들 때 이 선례를 따를 것 — 토큰 주석의
> "마우스 오버" 는 500의 hover 용도를 적은 것이지 700의 유일한 용도가 아니다.

기술 스택(현 7앱 — console·popo-studio·mou·claim·hub·labs·sns): Next.js 16 + Tailwind v4 + Clerk + Pretendard.
> 앱 목록의 **기계 정본은 maria-ui `scripts/ui-audit.config.mjs` 의 `APPS`** 다 — 이 문장과 갈리면 그쪽이 맞다.
> (2026-08-21 정정: 오래 "4앱"으로 적혀 있어 labs·sns·hub 를 빠뜨릴 위험이 있었다.)

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
- **현재 적용 현황(2026-08-04)**: 정적 산출물·신규 작업 + **사내 웹앱 헤더 6/6** 워드마크 사용(console·popo·mou·claim·hub·labs 전수 — `internal-service-header-v1.md` §8 참조. labs 는 운영자 영역 한정 헤더). 텍스트 로고 legacy 허용은 **종료** — ui-audit static 이 `header-wordmark` 로 강제한다(BrandLogo 부재 또는 아이보리 착색이면 FAIL). hub 도 ui-audit APPS 에 등록돼 같은 강제를 받는다. 헤더 적용 규격은 `internal-service-header-v1.md` §2·§4(v1.9).

## 1-2. 아이콘 (v1.12, 2026-08-21 신설)

아이콘 정본은 **Lucide 계열 한 세트**다. 2026-08-21 실측 전까지 정본이 정해진 적이 없었다 —
claim(웹·desktop)만 lucide 를 쓰고 console·hub·popo-studio·mou·labs 는 필요할 때마다
인라인 `<svg>` 를 손으로 그려 넣고 있었다. 이 절은 그 상태를 끝내기 위한 것이다.
**이미 사실상의 기본값이던 것을 문서로 굳히는 것**이라 이동 비용은 거의 없다.

> 이 절이 정하는 것은 **눈에 보이는 약속**(어느 계열·크기·획·색·접근성)뿐이다.
> 구현 매핑(npm 패키지명 `lucide-react`·지원 버전 범위·설치법)은 배포층인
> **maria-ui `registry.json` 의 `@maria/icon` 항목이 단일 출처**다. 같은 값을 두 곳에 적지 않는다.

### 규칙

- **세트 — Lucide 계열만.** **두 번째 아이콘 세트를 들이지 않는다.** 세트마다 획 굵기·광학 크기·
  모서리 처리가 달라 한 화면에 섞이면 바로 보인다. 필요한 글리프가 Lucide 에 없으면
  인라인 `<svg>` 를 그리기 전에 **§8 예외 절차**(사전 확인 후 이 문서에 기록)를 밟는다.
  → 자동 검사 `icon-set(static)` 이 **알려진** 대체 세트를 잡는다(아래 "검사의 한계" 참조).
- **격자·획 — 24×24, `stroke-width` 2**(Lucide 기본값). `strokeWidth` 를 재정의하지 않는다.
  (7앱 실측 재정의 **0건** — 이미 지켜지던 것을 명문화한 것이다.)
- **색 — `currentColor` 를 그대로 두고 글자 색 유틸(`text-*`)로 제어**한다. 아이콘에 색을 직접
  박지 않는다. 부모의 글자 색을 따라가는 것이 기본 동작이고, 그래야 다크·반전 표면에서 같이 움직인다.
- **크기 — 숫자가 아니라 역할로 고른다.**

  | 역할 | 크기 | 클래스 | 쓰는 곳 |
  |---|---|---|---|
  | 인라인 | 14px | `size-3.5` | 본문 글자 옆, 배지·칩 안 |
  | **기본** | 16px | **`size-4`** | 버튼·입력·셀렉트·메뉴 항목 — **애매하면 이것** |
  | 강조 | 20px | `size-5` | 카드 머리말, 목록 항목의 선행 아이콘 |
  | 전체 화면 상태 | 32·48px | `size-8`·`size-12` | 페이지 전체 로딩 스피너, 빈 화면 |

  **크기 목록만 적으면 난립이 그대로 재발하므로 역할을 함께 못박는다** — 실측 당시 claim 웹이
  18회 사용에 7가지 크기, desktop 이 18회에 7가지를 쓰고 있었다.
  표 밖의 크기는 **§8 예외**(사전 확인 후 기록)다.
- **표기는 `size-*` 하나로.** `h-4 w-4` 는 결과가 같지만 표기가 갈리면 검색·감사가 성립하지 않는다.
  ⚠ 이 규칙은 **아이콘 컴포넌트에만** 적용된다 — §3 `AuthOtpHelp` 의 `h-4 w-4` 는 아이콘이 아니라
  `?` 글자를 담은 **버튼**의 크기라 대상이 아니다.
- **import 이름은 짧은 쪽.** `Check`·`Search` 를 쓰고 `CheckIcon`·`SearchIcon` 별칭은 쓰지 않는다
  (같은 글리프에 이름이 둘이면 검색·감사가 반쪽이 된다).
- **위 두 항목의 공통 예외 = `components/ui/` 의 shadcn 생성 파일.** CLI 가 다시 만들어내는 파일이라
  손으로 고치지 않는다(고쳐도 다음 `shadcn add` 에 덮인다). 실측상 `*Icon` 별칭은 정확히 이 디렉터리
  6개 파일에만 있고, 손으로 쓴 19개 파일은 전부 짧은 이름을 쓰고 있었다.
- **접근성** — 크기·획·색만 정하면 정본이 반쪽이다.
  - **장식용**(옆에 같은 뜻의 글자가 이미 있음) → `aria-hidden`.
  - **아이콘이 혼자 뜻을 전달**하면 → 접근 가능한 이름을 준다(옆에 텍스트를 두거나 `aria-label`).
  - **아이콘만 있는 버튼은 `aria-label` 필수.** 없으면 스크린리더에서 "버튼"으로만 읽힌다.

### 검사의 한계 (정직 표기)

`icon-set(static)` 은 **알려진** 대체 아이콘 패키지(tabler·hugeicons·heroicons·react-icons 등)를
FAIL 로 잡고, 이름이 수상한 미지 패키지는 **WARN + 사람 판정**으로 돌린다.
**"아이콘 패키지인가"의 판정은 결국 사람의 의미 판단이라 완전한 자동 차단은 불가능하다.**
검사 이름에 `known-` 을 붙여 이 불완전성을 드러냈고, 못 잡는 구간은 §8 사전 확인 게이트가 막는다.

### 미수렴 (2026-08-21 현재)

- **claim 12px 6곳**(웹 3 + desktop 3, `audit-results-view.tsx` 의 `h-3 w-3`) — 역할 표 밖 크기.
- **console·hub·popo-studio·mou·labs 의 인라인 `<svg>`** — 아이콘 패키지 없이 손으로 그린 것.
- 둘 다 **각 앱을 다음에 손볼 때 수렴**한다(사용자 결정 2026-08-21 — 일괄 교체하지 않는다).
  정본 수립이 먼저이고 수렴은 자연히 따라온다는 판단이다.

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
  - 에러: `<div role="alert" className="rounded-md bg-state-error-bg px-3 py-2 text-sm text-state-error-fg">` (#FCEEED / #8B4540). **`role="alert"` 는 필수다** — 이 속성이 없으면 화면에는 사유가 떴는데 스크린리더에는 아무 일도 안 일어난 것과 같다(눈으로 볼 수 없는 직원은 "다음"을 눌러도 왜 안 넘어가는지 알 수 없다). `role="alert"` 가 `aria-live="assertive"`·`aria-atomic` 을 함의하므로 그 둘은 따로 적지 않는다. (v1.8)
  - **에러 영역은 항상 그려 둔다 — 조건부로 감싸지 않는다.** (v1.9) 호출부는 `{error && <AuthError …/>}` 가 아니라 `<AuthError message={error} seq={errorSeq} />` 다. 오류가 없을 때는 `sr-only` 로 남아 화면·레이아웃에 영향을 주지 않는다. 이유 둘:
    ① **live region 은 글이 들어오기 전부터 DOM 에 있어야 안내가 확실하다.** 영역과 글이 같은 순간에 삽입되면 읽지 않는 스크린리더가 있다.
    ② `seq`(오류 발생 횟수)를 넘겨 **DOM 변화를 보장한다** — 동기 검증 오류는 React batching 으로 `null → 같은 문자열` 이 커밋조차 되지 않기 때문이다. ⚠ **단 이것으로 "연속 동일 오류 재발표"는 해결되지 않는다(v1.10 에서 실측으로 정정).**
  - **브라우저 기본 유효성 검사를 끈다 — 폼에 `noValidate`.** (v1.10) `required` 는 **그대로 둔다**(스크린리더가 "필수 사항"으로 읽어주는 유용한 표시). 끄기 전에는 빈칸 제출 시 브라우저가 폼 제출 자체를 막아 앱의 빈칸 오류 문구가 **한 번도 표시된 적 없는 죽은 코드**였고, 대신 뜨는 브라우저 말풍선은 실측에서 **낭독되지 않았다**(필드 설명만 읽힘). 메시지는 우리 `role="alert"` 영역이 맡는다.
  - **입력 필드는 오류와 연결한다.** (v1.9) 오류가 있을 때 해당 입력에 `aria-invalid="true"` + `aria-describedby={AUTH_ERROR_ID}`. 연결이 없으면 필드로 이동했을 때 "무엇이 잘못됐는지"가 다시 안 읽힌다(오류 발표를 놓쳤거나 나중에 되짚는 경우).
  - **이메일 입력 필드에 "username" 신호를 쓰지 않는다 — `id`·`name`·`autoComplete` 전부 `email` 로.** (v1.11)
    비밀번호 관리자 확장(iCloud 암호 실측, 1Password 계열 동류)이 "username" 신호가 하나라도 있으면
    로그인 필드로 붙어 제안 오버레이를 띄우고 **Enter(암묵적 제출)를 가로챈다** — 버튼 클릭·Tab 이동은
    되는데 Enter 만 안 되는 증상. 이 SSO 는 비밀번호가 없어(OTP 단독) username 자동완성을 잃을 것도 없다.
    2026-08-18 사용자 실브라우저 A/B 실측: id·autoComplete 중 **하나만 "username" 이어도 차단**,
    둘 다 "email" 이면 통과(sns 가 그 산 증거였다).
  - 인증 코드 필드 라벨 옆 **OTP 도움말**: `@maria/auth-primitives`의 `AuthOtpHelp` — `?` 아이콘(`h-4 w-4 cursor-help rounded-full border-border-default`), hover·키보드 포커스·모바일 탭 시 실제 인증 메일을 축소 재현한 팝오버. 팝오버는 떠 있는 층이라 그림자 허용. 메일 재현부는 외부 메일 모사라 마리아 토큰이 아닌 원문 색·서체(Helvetica·`#111827`)를 쓴다(실물과 같아야 사용자가 알아봄). 예시 코드는 가짜 고정값 852937. (v1.6)
- 푸터: `<p className="mt-6 text-center text-xs text-text-muted">마리아의료재단 CX부</p>`

### 3-1. 로그인 문구 표준 (v1.6, 2026-08-04 사용자 결정)

사용자 노출 문구에서 **"가입"이라는 말을 쓰지 않는다** — 사내 SSO에 회원가입 개념이 없기 때문(계정은 이메일 인증만으로 생기고, 앱 권한은 신청·승인이다). 세 단어로 통일:

| 개념 | 표준 용어 | 예 |
|---|---|---|
| 계정이 SSO에 있음/없음 | **등록** | "등록된 이메일은 즉시 로그인됩니다" · "등록되지 않은 이메일입니다" |
| OTP 본인 확인 | **이메일 인증** | hub 신규 버튼 "인증하기" |
| 앱 권한 요청(전 앱 공통) | **접근 신청** | popo·claim 신규 버튼 "접근 신청" · console "접근 승인" |

운영자 화면·Slack 알림도 같은 용어를 쓴다(직원-운영자 용어 이원화 금지). 코드 식별자·계약 문서 내부 용어는 불변.

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
- ❌ **Lucide 외 아이콘 세트를 추가로 들이기**(§1-2). 획 굵기·광학 크기·모서리가 세트마다 달라 한 화면에 섞이면 바로 보인다. 필요한 글리프가 없으면 인라인 `<svg>` 를 그리기 전에 §8 사전 확인.
- ⚠️ 검증은 토큰 파일이 아니라 **배포된 CSS**로(override가 파일엔 안 보이고 라이브에만 나타남).

> **자동 검사 범위(2026-07-31~)**: 위 재정의 사고는 오랫동안 `--text-on-dark` 한 색에만 방어가 있었다.
> 나머지 브랜드 색은 ui-audit 이 클래스 **이름**(`bg-maria-green`)만 보고 그 이름이 가리키는 **값**은
> 아무도 보지 않았다. 이제 `brand-color(live)`·`brand-color(static)` 이 `--maria-green` `--popo-teal`
> `--bg-ivory` 의 구체값을 정본과 대조한다(스케일 변형 `--maria-green-700` 등은 대상 아님).
> 라이브 쪽이 확정 판정 — static 은 배포 전에 잡는 층이다.

## 7. 비상 fallback (레지스트리 접근 불가 시)

`@maria` 레지스트리는 인증 게이트(private)다. 토큰 만료·장애·긴급 hotfix로 접근이 막히면:
1. 이 repo `tokens/design-tokens.css`를 직접 복사(레지스트리 없이도 토큰 확보).
2. 헤더/로그인은 `internal-service-header-v1.md`·본 문서 §3 코드를 카피.
3. 레지스트리 토큰 복구는 maria-ui `RUNBOOK.md`.

→ **레지스트리가 막혀도 이 repo만 있으면 수동으로 일관성 적용 가능.**

## 8. 예외

기준에서 벗어나야 하는 합당한 이유가 있으면 **먼저 명시 확인** 후 진행하고, 이 문서에 사유와 함께 기록한다.

기록되지 않은 예외는 예외가 아니라 **드리프트**다. 다음 사람이 "승인된 이탈"과 "실수"를
구분할 방법이 없기 때문이다 — 아래 두 건은 실제로 그 상태로 2개월 가까이 방치되며
ui-audit 이 매 회차 WARN 을 냈다(2026-07-31 조사).

| 앱 | 항목 | 승인된 값 | 사유 |
|---|---|---|---|
| **hub** | 페이지 제목 | `text-[25px] font-bold tracking-tight text-foreground` (반응형 확대 없음) | 승인 시안 `hub/docs/mockups/2026-07-21-hub-preview-v11.html`(`h1 { font-size: 25px; font-weight: 700 }`)대로 구현. 허브는 카드 그리드 위주라 표준 제목(24→30px)이 카드 제목과 층위가 겹쳤다. hub 10개 페이지에 일관 적용. |
| **hub** | 폰트 | 자체 호스팅 `@font-face` → `/fonts/PretendardVariable.woff2` | 외부 CDN 요청 제거. 버전 대조가 성립하지 않으므로 ui-audit 이 **바이트+sha256** 으로 자산 자체를 고정한다(`ui-audit.config.mjs` `selfHostedFont`). |
| **popo-studio** | 페이지 제목 | **없음**(구조적) | 스튜디오형 앱이라 페이지 제목 블록을 두지 않는다. 현재 위치는 헤더 활성 탭이 알린다. `<h1>` 3개는 전부 로그인·승인대기·업로드 화면의 화면명이지 페이지 제목이 아니다. |
| **hub** | §3 로그인 — 바깥 컨테이너·푸터 | 바깥 = `flex flex-1 flex-col items-center justify-center bg-bg-ivory p-6`(`<div>`, `min-h-screen` 없음) · 푸터 = **없음**(`SiteFooter` 담당) | hub 로그인은 `(bare)` 레이아웃의 `<main>` 안에서 렌더되므로 자기가 `<main>`·`min-h-screen` 을 다시 만들지 않고 `flex-1` 로 채운다. CX부 크레딧도 레이아웃의 `SiteFooter` 가 이미 그린다. 제목·폼 카드는 §3 그대로 적용. |

> **예외의 이력화**: hub 제목 예외는 표준을 바꾸자는 뜻이 아니다. hub 가 표준으로 돌아오려면
> 시안부터 다시 그려야 하므로, 그때까지 **여기 적힌 값이 hub 의 기준**이고 ui-audit 은 그 값으로
> hub 를 검사한다(면제가 아니라 **다른 값으로 강제**). popo 만 검사 면제이며, 이는
> "제목을 새로 달 때 아무도 안 본다"는 공백을 동반한다 — 제목을 도입하면 이 표를 먼저 고칠 것.

## 9. 변경 이력

- **v1.12 (2026-08-21)**: **§1-2 아이콘 정본 신설 — 정본이 없던 자리를 채운 것**(규칙 변경이 아니라
  공백 메우기). 최상위 18개 프로젝트 `package.json` + 실제 import 를 전수 실측한 결과 **아이콘 정본이
  정해진 적이 없었다** — claim 만 `lucide-react` 를 쓰고(웹 `^1.11.0`/설치 1.11.0, **desktop 은 별도 패키지
  `maria-claim-desktop` 로 `^1.14.0`/설치 1.14.0**) 나머지 5앱은 인라인 `<svg>` 를 손으로 그려 넣고 있었으며
  maria-ui 레지스트리에는 **아이콘 항목 자체가 없었다.** 사실상의 기본값이던 **Lucide 를 정본으로 확정**하고
  ① 세트 단일화 ② 24×24·획 2 ③ `currentColor` ④ **역할별 크기 4단**(숫자 나열이 아니라 역할 — claim 이
  18회 사용에 7가지 크기를 쓰고 있었다) ⑤ 표기 `size-*` 통일 ⑥ import 짧은 이름 ⑦ 접근성 3항목을 못박았다.
  구현 매핑(패키지명·버전 범위)은 **배포층 maria-ui `@maria/icon`** 에 두고 여기엔 적지 않는다(값 이중화 금지).
  ui-audit `icon-set(static)` 신설 — **완전 차단이 불가능함을 검사 이름(`known-`)과 문서에 명시**하고
  미지 패키지는 WARN+사람 판정으로 돌렸다. 아울러 **§1 기술 스택의 "현 4앱" 을 7앱으로 정정**(오래 낡아 있어
  labs·sns·hub 를 빠뜨릴 위험이 있었다). 기각안: tabler 통일(claim 25파일을 갈아야 하고 얻는 게 스타일 1종),
  hugeicons Pro(CDN 페이지뷰·대역폭 과금), 정하지 않기(인라인 SVG 가 계속 느는 쪽으로 굳음).
  검토 = Codex(gpt-5.6-sol) 1회 — 초안의 실측 오류 2건(desktop 을 미러로 오인·아이콘 19종을 17종으로 셈)과
  문서 위치 분리안을 그쪽 지적으로 바로잡았다.
- **v1.11 (2026-08-18)**: §3 에 **이메일 입력 "username" 신호 금지**(id·autoComplete 전부 email) 신설.
  6앱이 id="username"+autoComplete="username" 이라 비밀번호 관리자 확장(iCloud 암호)이 로그인 필드로
  붙어 Enter 제출을 가로챘다(사용자 보고 — sns 만 email 시그니처라 정상). 헤드리스(확장 없는 환경)에선
  7앱 전부 Enter 정상이라 앱 코드 결함이 아니었고, 8/12 Enter 사각 수정의 실측(7/7)이 이 변수를 못 본
  이유이기도 하다. 아울러 v1.10 ⓑ 의 "sns 만 required 가 없어 정상"은 **오기**였다(8/7부터 있었다) —
  sns 폼에 `noValidate` 를 마저 붙여 7앱 정합. ui-audit `login(static)` 에 "username" 신호 검사 추가.
- **v1.10 (2026-08-12)**: **v1.9 의 주장 하나를 실측으로 정정하고, 빈칸 제출 경로를 닫았다.**
  ⓐ **정정**: v1.9 는 `seq` 로 "연속 동일 오류도 재발표된다"고 적었는데 **거짓이다.**
  VoiceOver 실측 결과 첫 오류는 낭독되지만 **같은 문구의 두 번째는 낭독되지 않는다** —
  VoiceOver 가 live region 의 새 내용이 직전과 글자까지 같으면 무시하기 때문이다.
  노드 교체 같은 마크업 기법으로는 못 넘고, **문장 자체를 바꿔야만**(예: "(2번째 시도)") 읽힌다.
  그건 문구 변경이라 **범위 밖으로 두기로 했다**(사용자 결정 — 첫 오류 낭독으로 충분).
  `seq` 는 유지한다(DOM 변화 보장은 유효, NVDA·JAWS 는 미실측).
  **교훈: 정적 검사 통과는 "코드에 계약이 박혔다"까지만 증명한다. v1.8·v1.9 는 청취 0회로 완료 보고됐다.**
  ⓑ **빈칸 제출**: 6앱(console·popo·claim·mou·hub·labs)이 `required` 때문에 브라우저에 막혀
  자기 빈칸 오류 문구를 **한 번도 못 띄우고 있었다**(sns 만 `required` 가 없어 정상 동작).
  폼에 `noValidate` 를 붙여 메시지를 우리 영역으로 돌렸다. `required` 는 낭독용으로 유지.
- **v1.9 (2026-08-12)**: §3 에러 박스 계약을 **속성에서 구조로** 넓혔다. v1.8 은 `role="alert"` 만 요구했는데,
  그것만으로는 두 구멍이 남아 있었다. ①**영역과 글이 동시에 삽입되면** 안 읽는 스크린리더가 있다 →
  오류가 없을 때도 `sr-only` 로 노드를 남기는 **상시 live region** 으로 전환. ②**같은 오류가 연속되면
  DOM 이 안 바뀌어 무음** — 특히 동기 검증 오류는 React batching 으로 `null → 같은 문자열` 이 커밋조차
  되지 않는다 → 앱이 넘기는 **`seq`**(오류 발생 횟수)로 안쪽 노드를 교체해 매번 재발표. 추가로 입력 필드에
  **`aria-invalid` + `aria-describedby`** 연결을 요구한다. ui-audit `login-a11y-call(static)` 신설 —
  정의가 아니라 **호출부**를 본다(조건부 마운트·`seq` 미전달을 FAIL).
  ⚠ **v1.8 의 검증은 전부 정적 검사였다** — 이번에 처음 VoiceOver 실측으로 확인한다.
- **v1.8 (2026-08-12)**: §3 **에러 박스에 `role="alert"` 필수** 명문화. 규칙 신설이 아니라 **7앱 전부가
  빠뜨리고 있던 접근성 공백을 닫은 것** — 로그인 실패 사유가 화면에만 뜨고 스크린리더에는 아무 일도
  안 일어나던 상태였다(`{error && <AuthError …/>}` 로 새로 삽입되는 노드라 이 속성이 유일한 통지 수단).
  ui-audit 에 `login-a11y(static)` 신설 — **속성 유무가 아니라 값까지** 본다(`role="status"`·
  `role="alertdialog"` 같은 그럴듯한 오답이 통과하지 않게. 변이 7종으로 판별력 확인).
  정본 `AuthPrimitives.tsx` 수정 + 7앱 재동기로 이행. 발견 경로 = 로그인 Enter 수정 작업의 잔여 표류 점검.
- **v1.7 (2026-08-04)**: §1-1 적용 현황 갱신 — labs 합류로 사내 웹앱 헤더 **6/6**(운영자 영역 한정). 헤더 규격 포인터 v1.9(`linkPrefetch` 옵션 신설·labs 행 추가)로 갱신. 규칙 변경 없음.
- **v1.6 (2026-07-31)**: **규칙 변경 없음 — 검사 범위만 규격을 따라잡았다.** 이 문서가 이미 적어둔 값 중
  ui-audit 이 안 보던 두 자리를 닫았다. ①**§1 페이지 제목**: 규격 5토큰 중 `tracking-tight` 와 색 토큰
  (`text-text-primary`=`text-foreground`)이 검사에서 빠져 있었다 — 두 토큰이 사라져도 통과했다.
  §8 hub 예외도 표에 적힌 승인값 전체(`text-[25px] font-bold tracking-tight text-foreground`)가 아니라
  앞 2토큰만 검사하고 있었다. ②**§1 브랜드 색**: `maria-green`·`popo-teal`·`bg-ivory` 의 **값**을
  아무도 안 봤다(§6 아래 주 참조). 5앱 실측 결과 **이탈 0**이라 앱 수정 없이 검사만 넓혔다 —
  로그인 카드의 `border` 처럼, 공백이 비어 있는지는 닫아 보기 전엔 알 수 없다.
- **v1.6 (2026-08-04)**: §3 에 **OTP 도움말 부품(`AuthOtpHelp`)** 추가(사용자 결정 — 시안 A: `?` 아이콘 hover 시 실제 인증 메일 축소 재현) + **§3-1 로그인 문구 표준** 신설("가입" 금지 — 등록/이메일 인증/접근 신청 3용어, 전 앱·운영자 화면·Slack 공통). ui-audit `login(static)`에 `otpHelp` 항목 추가. 배경: 사용자 지적 "OTP만 넣으면 바로 쓰는데 '가입 완료'라고 나온다"(hub 실측 스크린샷).
- **v1.5 (2026-07-31)**: §8 에 **hub §3 로그인 예외**(바깥 컨테이너·푸터) 추가 — `(bare)` 레이아웃 안에서 렌더되는 구조상 차이. 아울러 ui-audit 에 **§3 로그인 템플릿 검사(`login(static)`)** 를 신설했더니 **5앱 전부가 §3 의 `shadow-sm` 제거(v1 2026-07-08 결정)를 이행하지 않은 채** 돌고 있었다 — 원인은 레지스트리 정본 `AuthPrimitives.tsx` 에 `shadow-sm` 이 남아 있던 것. 문서만 고치고 구현을 안 고친 전형이라, 정본 수정 + 5앱 재동기로 이행했다. 규칙 자체는 변경 없음(§3 문구 그대로).
- **v1.4 (2026-07-31)**: **§8 예외 표 신설**(비어 있던 절) — hub 페이지 제목 `text-[25px] font-bold`(2026-07-21 승인 시안) · hub 자체 호스팅 폰트 · popo 페이지 제목 없음(구조적)을 승인된 예외로 명문화. 폰트 행의 **`.min` 강제 해제** — 이 CSS 는 `@font-face` 한 줄(526B)이라 압축 이득이 없고 `.min` 이 오히려 588B 로 크다(실측). 고정 대상은 버전·variant 뿐. 아울러 ui-audit 의 `x-ui-standard` 마커 검사를 **폐기**했다 — 이 문서에 없는 규칙을 점검표가 단독으로 요구하던 것으로, 5앱 전부 MISSING 이 정상이었다(규칙 미채택).
- **v1.3 (2026-07-31)**: 헤더 행에 활성 탭 `aria-current="page"` 추가(알약 배경은 시각 사용자에게만 현재 위치를 알린다). 상세 규격 = `internal-service-header-v1.md` v1.6.
- **v1.2 (2026-07-31)**: 헤더 행에 **스크롤 상단 고정**(`sticky top-0 z-40`) 추가. §1-1 로고: 소비 예시의 색을 `text-text-on-dark`(아이보리) → `text-white` 로 정정(같은 절의 "아이보리 워드마크 금지"와 모순이던 오기) + 텍스트와 나란히 둘 때의 `trim`·`items-baseline` 밑선 규칙 신설 + 4앱 텍스트 로고 legacy 허용 종료(ui-audit `header-wordmark` 강제). 상세 규격 = `internal-service-header-v1.md` v1.5.
- **v1.1 (2026-06-17)**: §1-1 로고(브랜드 워드마크) 신설. 정본 SVG(`assets/logos/svg/`, currentColor·green·white) + 색/비율/소비 규칙 + "글자 타이핑 금지" 명문화. 헤더 로고를 텍스트→워드마크로 변경(앱 적용은 `@maria/brand-logo`로 단계 이행, 별도 롤아웃). 기존 PNG 로고는 벡터 부재로 코드 산출물에 미사용되던 갭 해소.
- **v1 (2026-06-04)**: claim·console·popo·mou 4앱 전수 UI 통일 작업에서 추출. 파비콘·헤더·너비·로그인·제목·폰트·on-dark(아이보리) 확정 + 토큰 override 드리프트 함정 명문화.
