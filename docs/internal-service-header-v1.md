# 사내 서비스 공통 헤더 v1

마리아의료재단 사내 웹 서비스가 공유하는 헤더 패턴. 신규 앱 합류 시 이 문서를 보고 카피하면 즉시 통일된 인상이 만들어진다.

레퍼런스 구현체: **popo-studio** ([popo-studio.maria-baby.com](https://popo-studio.maria-baby.com)) · **claim** ([claims.maria-baby.com](https://claims.maria-baby.com))

---

## 1. 목적

- 모든 사내 서비스가 같은 시각 인상을 갖도록 한다.
- 사용자(직원)가 사내 도구를 옮겨다닐 때 인지 부담을 줄인다.
- 새 앱이 합류할 때 디자인 결정을 다시 하지 않도록 한다.

## 2. 시각 사양

| 항목 | 값 | 토큰 |
|---|---|---|
| 헤더 배경 | `#1E3131` | `bg-maria-green` |
| 헤더 텍스트 (강조) | 아이보리 `#F4EEED` | `text-text-on-dark` |
| 헤더 텍스트 (보조) | `#A8BABA` | `text-maria-green-300` |
| 활성 탭 배경 | 아이보리 `#F4EEED` | `bg-text-on-dark` |
| 활성 탭 글자 | `#1E3131` | `text-maria-green` |
| 활성 탭 표시(비시각) | 현재 위치 노출 | `aria-current="page"` (비활성은 속성 없음) — **1차 탭뿐 아니라 현재 페이지를 가리키는 모든 헤더 링크** |
| 좌우 패딩 | 24px | `px-6` |
| 상하 패딩 | 16px | `py-4` |
| 좌측 영역 gap | 16px | `gap-4` (구분선 양옆 균형 — 2026-07-31 이전엔 `gap-6`) |
| 브랜드 내부 gap | 10px | `gap-2.5` (워드마크↔서비스명) |
| 우측 영역 gap | 12px | `gap-3` (2026-06-05 claim 수렴에서 4→3, 이때 표 갱신을 빠뜨려 문서만 `gap-4`로 남아 있었다 — 2026-07-31 정정) |
| 인쇄 시 | 숨김 | `print:hidden` |
| 탭 넘침 처리 | 가로 스크롤 + 가장자리 스크롤 그림자 | `overflow-x-auto` + local/scroll 그라데이션 (§4 nav 참조) |
| 활성 탭 자동 노출 | 넘칠 때 현재 탭을 보이는 자리로 | nav 컨테이너 `scrollLeft` 조정 (경로 변경마다, §4 useEffect) |
| 스크롤 동작 | 상단 고정 | `sticky top-0 z-40` |
| 브랜드 | 워드마크 + 서비스명 **둘 다 흰색** | `<BrandLogo trim className="h-[18px] text-white" />` + `text-base font-semibold text-white` |
| 브랜드↔네비 구분선 | 1px 세로선, 네비 있을 때만 | `h-5 w-px bg-maria-green-300/40` |
| 헤더 높이 | 64px (py-4 32 + 콘텐츠 32) | — |

> **스크롤 고정 규칙(2026-07-31)**: 네비게이션 바가 있는 사내 서비스는 스크롤해도 헤더가
> 화면 상단에 붙어 따라온다. `z-40`은 앱 모달·다이얼로그(관례상 `z-50`)가 헤더를 덮게 하려는
> 값이다 — 헤더를 `z-50` 이상으로 올리면 모달 위에 헤더가 뜬다.
> ⚠️ **두 가지 필수 동반 조치**가 있다. 빠뜨리면 조용히 깨진다.
> 1. **헤더만 감싸는 래퍼 `<div>` 안에 두지 말 것.** `sticky`는 자기 부모 박스 안에서만 움직인다.
>    부모 높이가 헤더 높이와 같으면 이동할 공간이 없어 그냥 같이 스크롤돼 사라진다
>    (claim의 `print:hidden` 래퍼가 실제로 이 경우였다 — 제거로 해소). 헤더는 본문까지 포함하는
>    세로 컨테이너의 직접 자식이어야 한다.
> 2. **`<html>`에 `scroll-pt-20`**(=80px, 헤더 64 + 여유 16). 없으면 `#앵커` 이동·폼 오류 필드
>    포커스·`scrollIntoView()`의 대상이 고정 헤더 뒤로 숨는다. 내부 스크롤 컨테이너를 따로 두는
>    화면은 그 컨테이너에 준다.

> **브랜드 규칙(2026-07-31)**: 좌상단은 **앱 이름을 타이핑한 글자가 아니라 마리아 워드마크**다
> ([[web-ui-guidelines-v1]] §1-1 — 로고는 전용 BI라 어떤 폰트로도 흉내 내면 안 된다).
> 어두운 헤더 위에서는 **100% 흰색**(`text-white`)이고 **아이보리(`text-on-dark`)는 금지**다
> (디자이너 3원칙). 워드마크 옆에는 짧은 영문 서비스명을 병기해 5앱을 구분한다
> (Console·Studio·MOU·Claims·Hub). **서비스명도 워드마크와 같은 흰색**이라 브랜드가 한 덩어리로
> 읽히고, 아이보리인 네비 탭과 위계가 갈린다(2026-07-31 사용자 결정).
> ⚠️ 워드마크 원본 `viewBox`는 `.ai` 페이지 박스라 마크 아래에 52.4/228.8 만큼 여백이 남는다.
> 그대로 가운데 정렬하면 **서비스명과 밑선이 어긋난다.** `trim`(마크 실제 경계 viewBox)
> + `items-baseline` 으로 상자 밑변을 글자 밑선에 일치시킨다.

> **활성 탭 표시 규칙(2026-07-31)**: 알약 배경은 **눈으로 보는 사용자에게만** 현재 위치를
> 알린다. 스크린리더에도 알리려면 활성 탭 링크에 `aria-current="page"`를 준다.
> 비활성 탭은 **속성 자체를 빼야** 한다 — `aria-current="false"`로 렌더하면 일부 보조기술이
> 여전히 읽는다. 정본은 `aria-current={active ? "page" : undefined}` 형태다.
> `aria-current={active}`(boolean)는 `"true"`로 렌더돼 규격 밖이므로 쓰지 않는다.
>
> **적용 범위(2026-07-31 사용자 결정)**: 1차 알약 탭 전용이 아니다. **헤더 안에서 색으로 현재
> 위치를 표시하는 링크는 모두** 같은 속성을 갖는다 — popo 의 `관리자`, claim 의 `사용 안내`·
> `휴지통`·`관리자 메뉴` 같은 우측 보조 링크(§6.1·§6.2)가 여기 해당한다. 판단 기준은 "1차냐
> 2차냐"가 아니라 **"이 링크가 지금 보고 있는 페이지를 가리키는가"** 다. 색만으로 표시하면
> 눈으로 보는 사용자에게만 전달된다는 문제는 알약이든 텍스트 링크든 똑같다.
> 5앱 모두 보조 링크와 1차 탭이 동시에 활성이 되는 경로가 없어 `aria-current` 가 한 화면에
> 둘 이상 생기지 않는다(2026-07-31 확인). 새 링크를 추가할 때 이 조건을 깨지 않는지 볼 것.

> **탭 넘침 규칙(2026-07-30, hub 사고 유래)**: 화면이 좁아 탭이 잘리면 `overflow-x-auto`만으로는
> 사용자가 스크롤 가능한 줄 모른다(hub 모바일에서 끝 메뉴가 통째로 숨었던 실사고). 잘렸을 때만
> 끝이 어두워지는 스크롤 그림자를 nav 배경 4겹 그라데이션(덮개 `local`·그림자 `scroll`)으로 넣는다.
> 정본 구현 코드가 이미 포함하므로 신규 앱은 별도 작업 불요.

> **활성 탭 자동 노출 규칙(2026-07-31)**: 그림자만으로는 "더 있다"만 알리고 **현재 어느 메뉴에
> 있는지는 못 알린다.** 넘친 상태에서 주소로 바로 들어오면 활성 알약이 스크롤 밖에 남아,
> 화면에는 전혀 무관한 첫 탭만 보인다. 경로가 바뀔 때마다 활성 탭이 보이는 자리로 오도록
> **nav 컨테이너의 `scrollLeft`를 조정한다**(§4 `useEffect`).
> - **`scrollIntoView()`를 쓰지 않는다.** 그건 조상 스크롤 컨테이너를 타고 올라가 **페이지를
>   세로로도 움직여**, sticky 헤더가 있는 화면이 열자마자 튄다. 가로 스크롤은 nav 안에서
>   끝나야 하므로 컨테이너 `scrollLeft`를 직접 민다.
> - 탭이 보이는 칸보다 **넓을 때는 왼쪽(글자 시작)을 맞춘다.** 오른쪽 맞춤은 긴 라벨의 끝만
>   남겨 무슨 메뉴인지 못 읽게 된다.
> - 가장자리 그림자(12px)에 알약이 걸리지 않게 `edge = 16px` 여유를 둔다.
>
> 근거(2026-07-31 헤드리스 실측, 인증 상태 = 운영과 동일): hub 320px 에서 메뉴가 들어갈 칸은
> **92px 인데 메뉴 전체 길이는 439px** 이라, 6개 경로 중 5개에서 활성 탭이 **0% 노출**이었다.
> 375px 에서도 4개가 0% 였다. 도입 후 375px 는 전 경로 100%, 320px 는 74~100% 가 된다.
> 같은 계산으로 5앱 모두 모바일에서 넘친다(console 8탭 중 320px 에서 1개만 온전히 보임).
> 이 규칙이 hub 전용 땜질이 아니라 정본에 있는 이유다.

## 3. 구조

```
┌────────────────────────────────────────────────────────────────┐
│ [워드마크] 서비스명 │ [탭] [탭]    [검색?] [secondary] [UserMenu] │
└────────────────────────────────────────────────────────────────┘
       └ 좌: 브랜드 │ 1차 탭 ──┘    └ 우: 2차 액션 ──────────┘
```

- **좌측**: 마리아 워드마크 + 서비스명(text-base font-semibold) → 세로 구분선 → 1차 네비게이션 탭(pill 형태).
  워드마크와 서비스명은 한 링크(`/`)로 묶여 한 덩어리로 읽히고, 구분선 뒤부터가 이동 메뉴다.
- **우측**: 검색·secondary 링크·UserMenu (이니셜 아바타)
- **본문 폭**: 전 앱 `max-w-7xl` 통일 (2026-06-04 결정). 헤더 inner div의 max-width도 본문과 같게 (`max-w-7xl`).

## 4. 카피 가능 코드 (React + Tailwind 4)

> **정본 구현 = maria-ui 비공개 레지스트리 `@maria/app-header`**(`registry/components/AppHeader.tsx`,
> 4앱 byte-identical 소비, `registryDependencies`로 `@maria/user-menu` 동반). 신규 앱은
> `shadcn add @maria/app-header`로 설치하는 것이 원칙이고, 아래 코드는 레지스트리를 쓸 수 없는
> 예외 상황(예: Clerk 없는 앱 — §6.4)용 참조다. 탭 넘침 스크롤 그림자(§2)도 정본에 포함돼 있다.
> 의존성: `next/link`, `clsx` 또는 `cn`, 본문 max-width를 props로 노출 가능.

```tsx
import Link from "next/link";
import { useEffect, useRef } from "react";
import { cn } from "@/lib/utils";
import BrandLogo from "./brand-logo"; // 마리아 워드마크 — @maria/brand-logo
import UserMenu from "./user-menu"; // 별도 패턴 — UserMenu v1 문서 참조

type Tab = { href: string; label: string; key: string };

export function PageShell({
  appName,           // 좌상단 앱 이름
  tabs,              // 1차 네비게이션 탭
  active,            // 현재 활성 탭의 key
  rightSlot,         // 검색 등 우측 보조 슬롯 (선택)
  secondaryLinks,    // 우측 secondary 링크 (선택)
  maxWidth = "max-w-7xl", // 앱별로 결정
  children,
}: {
  appName: string;
  tabs: Tab[];
  active: string;
  rightSlot?: React.ReactNode;
  secondaryLinks?: { href: string; label: string; key: string }[];
  maxWidth?: string;
  children: React.ReactNode;
}) {
  const navRef = useRef<HTMLElement>(null);

  // 활성 탭 자동 노출(§2) — 좁은 화면에서 메뉴가 넘칠 때 현재 탭을 보이는 자리로 끌어온다.
  // scrollIntoView 가 아니라 컨테이너 scrollLeft 를 직접 민다: scrollIntoView 는 조상까지
  // 거슬러 올라가 페이지를 세로로도 움직여, sticky 헤더가 있는 화면이 열자마자 튄다.
  useEffect(() => {
    const nav = navRef.current;
    if (!nav) return;
    const tab = nav.querySelector<HTMLElement>('[aria-current="page"]');
    if (!tab) return;
    const navBox = nav.getBoundingClientRect();
    const tabBox = tab.getBoundingClientRect();
    const edge = 16; // 가장자리 그림자(12px)에 알약이 걸리지 않게 두는 여유
    if (tabBox.width > navBox.width - edge * 2 || tabBox.left < navBox.left + edge) {
      // 칸보다 넓은 탭을 오른쪽에 맞추면 라벨 끝만 남는다 — 왼쪽(글자 시작)을 맞춘다.
      nav.scrollLeft -= navBox.left + edge - tabBox.left;
    } else if (tabBox.right > navBox.right - edge) {
      nav.scrollLeft += tabBox.right - (navBox.right - edge);
    }
  }, [active]); // 정본은 usePathname() 을 쓴다 — 현재 위치가 바뀔 때마다 다시 맞춘다

  return (
    // ⚠️ 헤더는 이 세로 컨테이너의 직접 자식이어야 한다(§2 — 헤더만 감싸는 래퍼 div 금지).
    <div className="flex flex-1 flex-col">
      <header className="bg-maria-green print:hidden sticky top-0 z-40">
        <div className={cn("mx-auto flex items-center justify-between gap-4 px-6 py-4", maxWidth)}>
          <div className="flex min-w-0 items-center gap-4">
            {/* 브랜드 = 워드마크 + 서비스명. items-baseline + trim 이라야 밑선이 맞는다(§2). */}
            <Link
              href="/"
              aria-label={`마리아 ${appName}`}
              className="flex shrink-0 items-baseline gap-2.5 transition-opacity hover:opacity-80"
            >
              <BrandLogo className="h-[18px] text-white" title="" trim />
              <span className="text-base font-semibold whitespace-nowrap tracking-tight text-white">
                {appName}
              </span>
            </Link>
            {/* 브랜드와 이동 메뉴의 경계. 네비가 없으면 가를 것도 없다. */}
            {tabs.length > 0 && <span aria-hidden className="h-5 w-px shrink-0 bg-maria-green-300/40" />}
            {/* 탭 넘침 규칙(§2): 잘렸을 때만 끝이 어두워지는 스크롤 그림자.
                덮개(bg색)는 내용과 함께 스크롤(local), 그림자는 상자에 고정(scroll) —
                끝까지 밀면 덮개가 그림자를 가려 사라진다. */}
            <nav
              ref={navRef}
              className="flex items-center gap-1 overflow-x-auto"
              style={{
                background:
                  "linear-gradient(to right, var(--maria-green), var(--maria-green)) left/24px 100% no-repeat local, " +
                  "linear-gradient(to right, var(--maria-green), var(--maria-green)) right/24px 100% no-repeat local, " +
                  "radial-gradient(farthest-side at 0 50%, rgba(0,0,0,0.55), transparent) left/12px 100% no-repeat scroll, " +
                  "radial-gradient(farthest-side at 100% 50%, rgba(0,0,0,0.55), transparent) right/12px 100% no-repeat scroll",
              }}
            >
              {tabs.map((t) => (
                <Link
                  key={t.key}
                  href={t.href}
                  // 현재 위치를 스크린리더에 알린다(§2 활성 탭 표시 규칙).
                  // 비활성은 속성 자체를 빼야 한다 — "false" 는 일부 AT 가 여전히 읽는다.
                  aria-current={active === t.key ? "page" : undefined}
                  className={cn(
                    "rounded-md px-3 py-1.5 text-sm font-semibold transition-colors",
                    active === t.key
                      ? "bg-text-on-dark text-maria-green"
                      : "text-maria-green-300 hover:text-text-on-dark",
                  )}
                >
                  {t.label}
                </Link>
              ))}
            </nav>
          </div>
          <div className="flex shrink-0 items-center gap-3">
            {rightSlot}
            {secondaryLinks?.map((l) => (
              <Link
                key={l.key}
                href={l.href}
                // 보조 링크도 현재 페이지를 가리키면 같은 속성을 갖는다(§2 적용 범위).
                // 색으로만 표시하면 눈으로 보는 사용자에게만 전달되는 건 알약과 똑같다.
                aria-current={active === l.key ? "page" : undefined}
                className={cn(
                  "text-sm font-semibold transition-colors",
                  active === l.key
                    ? "text-text-on-dark"
                    : "text-maria-green-300 hover:text-text-on-dark",
                )}
              >
                {l.label}
              </Link>
            ))}
            <UserMenu />
          </div>
        </div>
      </header>
      <main className={cn("mx-auto w-full flex-1 px-6 py-6", maxWidth)}>{children}</main>
    </div>
  );
}
```

## 5. 필수 토큰

신규 앱 `globals.css`에 다음 토큰이 정의되어 있어야 한다 (마리아 v2.1):

```css
--color-maria-green: #1E3131;
--color-maria-green-300: #A8BABA;   /* 다크 헤더 위 보조 텍스트 */
--color-maria-green-400: #7E9897;
--color-maria-green-500: #6E827D;
--color-maria-green-600: #4A605C;
--color-maria-green-700: #2D4544;   /* 다크 헤더 위 인풋 배경 */
--color-text-on-dark: #F4EEED;      /* 아이보리. ⚠️ #FFFFFF 아님 — tokens/design-tokens.css 와 일치 */
```

색 hex 값은 **레포 루트 `tokens/design-tokens.css`와 일치해야 한다**. 임의로 옮겨 적지 말고 그대로 가져올 것.
> 참고: 위 `--color-*` 정의는 Tailwind v4 **`@theme` 계층**이다(`:root`에 두면 유틸리티 클래스가 생성되지 않음). 표준 적용형은 raw 토큰(`design-tokens.css`)을 `@import`한 뒤 `@theme inline`에서 `--color-maria-green: var(--maria-green);`처럼 var() 매핑하는 것 — popo·console 적용형 참조. 이렇게 하면 hex가 한 곳(design-tokens.css)에만 존재한다.
> ⚠️ **함정(2026-06-04 실제 사고)**: `globals.css`에서 `@import "design-tokens.css"` **뒤**에 `:root { --text-on-dark: #FFFFFF }` 같은 override 를 두면 토큰값(#F4EEED)을 가려 **라이브가 흰색**이 된다. 토큰을 재정의하지 말 것. 검증은 파일이 아니라 **배포된 CSS**(`/_next/static/chunks/*.css` 의 `--text-on-dark:` 정의)로 한다.

## 6. 변형

### 6.1 검색 슬롯이 있는 경우 (claim)

`rightSlot`에 검색 인풋을 넣는다. 다크 배경 위 인풋 스타일:

```tsx
<Input
  className="h-8 w-[220px] border-maria-green-700 bg-maria-green-700 pl-7 text-xs text-text-on-dark placeholder:text-maria-green-300 focus-visible:border-text-on-dark focus-visible:ring-text-on-dark/30"
/>
```

### 6.2 관리자 전용 링크 (popo, claim 둘 다)

`secondaryLinks`에 조건부로 추가하거나, 상위에서 권한 검사 후 props로 전달.

이 링크들도 **현재 페이지를 가리키면 `aria-current="page"`를 갖는다**(§2 적용 범위,
2026-07-31). 색만 바꾸고 속성을 빼면 알약 탭과 같은 문제가 그대로 남는다.
정본을 안 거치고 앱이 직접 그리는 링크(popo `관리자`, claim `사용 안내`·`휴지통`·
`관리자 메뉴`)라 **앱 쪽에서 손으로 넣어야** 하고, ui-audit `header-aria-current` 가
"색으로 활성을 표시하는데 속성이 없는 링크"를 잡는다.

### 6.4 Clerk 게이트 앱 (hub)

인증 게이트(env)가 꺼지면 ClerkProvider 자체를 렌더하지 않는 앱은 정본 AppHeader를
그대로 쓸 수 없다(정본은 `useUser()`를 무조건 호출 → Provider 없으면 크래시). 이 경우
**시각 사양(§2)을 그대로 복제한 이식본**을 만들고 UserMenu만 `next/dynamic`으로 렌더될
때만 로드한다. 적용형: hub `components/site-header.tsx` (2026-07-30).

워드마크도 같은 사정이다. hub 에는 `components.json` 이 없어 `shadcn add` 를 쓸 수 없으므로
`@maria/brand-logo` 정본을 `components/brand-logo.tsx` 로 **복사**한다(byte-identical).
BrandLogo 는 `registryDependencies` 없는 순수 SVG 라 Clerk 와 무관하다 — components.json 을
갖춘 앱이라면 그냥 설치하면 된다.

> ⚠️ 이식본은 정본이 바뀌어도 **자동으로 따라오지 않는다.** 정본을 고쳤으면 hub 도 같이
> 고치고, `node scripts/ui-audit.mjs --static-only --app hub` 로 확인한다(2026-07-31 부터
> hub 는 ui-audit 대상이다). 파일 사본은 `shasum` 으로 정본과 대조한다.

### 6.3 UserMenu

별도 패턴 — 정본 구현은 maria-ui 비공개 레지스트리 `@maria/user-menu`(`registry/components/UserMenu.tsx`, console·popo 정본의 byte-identical 복제층). 신규 앱은 `shadcn add @maria/user-menu`로 설치한다(@maria/tokens 동반 설치됨). 이니셜 아바타 + 이름·이메일·로그아웃만. Clerk의 `UserButton` 그대로 쓰지 말 것 (사내 도구에 불필요한 "계정 관리" 노출 방지).

## 7. 인쇄 처리

헤더는 `print:hidden`으로 인쇄 시 자동 제거된다 (잉크·종이 절약, 청구서·보고서 캡처에 헤더가 끼어드는 것 방지).

## 8. 적용 현황

| 앱 | 도메인 | 서비스명 | 본문 폭 | 비고 |
|---|---|---|---|---|
| claim | claims.maria-baby.com | Claims | `max-w-7xl` | 의료 청구 |
| console | console.maria-baby.com | Console | `max-w-7xl` | 통합 어드민 |
| popo-studio | popo-studio.maria-baby.com | Studio | `max-w-7xl` | 미디어 생성 |
| mou-admin | mou-admin.maria-baby.com | MOU | `max-w-7xl` | 진료 접수 (토큰 클래스명만 `on-dark` 등으로 다름, 값 동일) |
| hub | hub.maria-baby.com | Hub | `max-w-7xl` | 분원 허브. Clerk 게이트 이식본(§6.4) — 정본 파일을 직수입하지 않으므로 워드마크도 사본(`components/brand-logo.tsx`, 정본과 byte-identical)이다. 정본이 바뀌면 **손으로 따라와야** 하고, 그 드리프트는 ui-audit 이 잡는다. 좁은 콘텐츠 페이지(자료실·신청 등)의 `max-w-4xl` 본문 컬럼은 §3 위반 아님(페이지 내부 컬럼 폭) |

**5앱 전수 적용 완료(2026-07-31)** — 헤더 계약(워드마크 브랜드·`sticky top-0 z-40`·`scroll-pt-20`·
활성 탭 `aria-current`)이 5앱 모두에 들어갔고, 5앱 모두 ui-audit 대상이다.

서비스명은 **짧은 영문 한 단어**가 원칙이다(2026-07-31 결정) — 워드마크가 이미 "마리아"를 말하고
있으므로 옆 글자는 어느 서비스인지만 가르면 된다. 신규 앱 합류 시 이 표에 한 줄 추가하고 PR을 보낸다.

## 9. 변경 이력

- **v1 (2026-05-07)**: 초안. popo-studio + claim 헤더를 통일하면서 추출.
- **v1.1 (2026-06-04)**: 4앱(claim·console·popo·mou) 전수 통일 반영. 본문 폭 `max-w-7xl` 통일, `text-on-dark` = 아이보리 `#F4EEED` 로 정정(§5 필수토큰의 `#FFFFFF` 오기 수정 — 이 오기를 console·popo 가 globals override 로 따라가 drift 원인이 됐음). 활성 탭 알약·로그인·파비콘·제목 등 전체 규칙은 같은 폴더 `web-ui-guidelines-v1.md` 참조.
- **v1.2 (2026-06-11)**: §5에 `--color-*` = Tailwind v4 `@theme` 계층 명시(`:root` 오배치 방지) + var() 매핑 표준 적용형 추가. §6.3 UserMenu 정본을 maria-ui 레지스트리 `@maria/user-menu`로 지정(TODO 해소).
- **v1.3 (2026-07-30)**: 탭 넘침 가장자리 스크롤 그림자 규칙 추가(§2·§4 — hub 모바일 실사고 유래, 5앱 정본 일괄 반영). 정본 구현을 maria-ui 레지스트리 `@maria/app-header`로 명시(§4). hub 합류(§6.4 Clerk 게이트 이식본 변형·§8). 미해결: 헤더 `print:hidden`이 §2·§7 계약과 달리 4앱 설치본에 없음(결정 대기) · hub 본문 폭 `max-w-6xl`(§3 통일 미실시).
- **v1.4 (2026-07-30)**: v1.3 미해결 2건 종결. ① `print:hidden`을 레지스트리 정본+5앱 설치본에 실반영(§2·§7 계약 준수로 결정). ② hub 본문 폭 `max-w-6xl`→`max-w-7xl` 통일(§3 합류 — 홈·언론보도·비품·푸터·인쇄도구 셸 5곳, 페이지 내부의 좁은 콘텐츠 컬럼 `max-w-4xl`은 유지).
- **v1.5 (2026-07-31)**: ① **스크롤 고정** — 네비게이션 바가 있는 사내 서비스는 헤더가 상단에
  붙어 따라온다(`sticky top-0 z-40`). 동반 조치 2건을 §2에 못박음: 헤더만 감싸는 래퍼 div 금지
  (claim 실사고), `<html>`에 `scroll-pt-20`(앵커·포커스 대상이 헤더 뒤로 숨는 회귀 방지 — Codex 지적).
  ② **브랜드를 텍스트에서 워드마크로** — 좌상단 앱 이름 타이핑을 폐기하고 `@maria/brand-logo`
  워드마크(흰색) + 짧은 영문 서비스명으로 교체. 원본 viewBox 의 아래 여백 탓에 밑선이 어긋나는
  문제는 `trim` + `items-baseline` 으로 해소(사용자 시각 QA 지적). ③ 브랜드와 네비 사이 세로 구분선(좌측 gap-6→gap-4). 서비스명 색은 워드마크와 같은 흰색.
  ④ 서비스명 표기를 §8 표에 명시(Console·Studio·MOU·Claims·Hub).
- **v1.6 (2026-07-31)**: **활성 탭 `aria-current="page"`**(§2 표·활성 탭 표시 규칙·§4 코드).
  지금까지 현재 위치가 알약 배경으로만 표시돼 스크린리더 사용자에게는 전달되지 않았다.
  비활성 탭은 속성 자체를 뺀다(`"false"` 는 일부 AT 가 읽음). ui-audit `header-aria-current`
  가 계약을 강제한다 — 삼항을 분해해 **조건·참분기·거짓분기를 따로** 본다(토큰 존재만 보면
  `!active ? "page" : undefined` 같은 분기 반전이 통과한다. 실측으로 확인하고 강화했다).
  같은 날 §2 표의 **우측 영역 gap 오기 정정**(`gap-4`→`gap-3`, 2026-06-05 claim 수렴 때
  바뀐 값을 표에 반영하지 않아 문서만 옛 값으로 남아 있었다).
  ※ 이 절의 v1.4/v1.5 순서가 뒤바뀌어 있어 함께 바로잡았다(내용 변경 없음).
- **v1.7 (2026-07-31)**: ① **활성 탭 자동 노출**(§2 규칙·§4 `useEffect`). 좁은 화면에서 메뉴가
  넘치면 활성 알약이 스크롤 밖에 남아 무관한 첫 탭만 보였다 — 헤드리스 실측에서 hub 320px
  6개 경로 중 5개가 활성 탭 **0% 노출**이었고(메뉴 칸 92px vs 메뉴 길이 439px), 같은 계산으로
  **5앱 전부** 모바일에서 넘친다. 경로가 바뀔 때마다 nav 컨테이너 `scrollLeft` 를 조정한다.
  `scrollIntoView()` 는 금지 — 조상을 타고 올라가 페이지를 세로로도 움직여 sticky 헤더 화면이
  튄다. 칸보다 넓은 탭은 왼쪽(글자 시작) 맞춤. 도입 후 375px 전 경로 100%, 320px 74~100%.
  ② **`aria-current` 적용 범위 확정**(§2·§6.2, 사용자 결정) — 1차 알약 탭 전용이 아니라
  **헤더에서 색으로 현재 위치를 표시하는 모든 링크**. popo `관리자`, claim `사용 안내`·
  `휴지통`·`관리자 메뉴` 가 대상이다. ui-audit 이 "색으로 활성을 표시하는데 속성이 없는 링크"를
  FAIL 로 잡는다.
