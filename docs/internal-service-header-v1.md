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
| 좌우 패딩 | 24px | `px-6` |
| 상하 패딩 | 16px | `py-4` |
| 좌측 영역 gap | 24px | `gap-6` |
| 우측 영역 gap | 16px | `gap-4` |
| 인쇄 시 | 숨김 | `print:hidden` |
| 탭 넘침 처리 | 가로 스크롤 + 가장자리 스크롤 그림자 | `overflow-x-auto` + local/scroll 그라데이션 (§4 nav 참조) |

> **탭 넘침 규칙(2026-07-30, hub 사고 유래)**: 화면이 좁아 탭이 잘리면 `overflow-x-auto`만으로는
> 사용자가 스크롤 가능한 줄 모른다(hub 모바일에서 끝 메뉴가 통째로 숨었던 실사고). 잘렸을 때만
> 끝이 어두워지는 스크롤 그림자를 nav 배경 4겹 그라데이션(덮개 `local`·그림자 `scroll`)으로 넣는다.
> 정본 구현 코드가 이미 포함하므로 신규 앱은 별도 작업 불요.

## 3. 구조

```
┌────────────────────────────────────────────────────────────────┐
│ [앱 이름]  [탭] [탭] [탭]      [검색?] [secondary] [UserMenu] │
└────────────────────────────────────────────────────────────────┘
       └ 좌: 브랜드 + 1차 탭 ──┘    └ 우: 2차 액션 ──────────┘
```

- **좌측**: 앱 이름 (text-lg font-bold) → 1차 네비게이션 탭(pill 형태)
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
import { cn } from "@/lib/utils";
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
  return (
    <div className="flex flex-1 flex-col">
      <header className="bg-maria-green print:hidden">
        <div className={cn("mx-auto flex items-center justify-between gap-4 px-6 py-4", maxWidth)}>
          <div className="flex min-w-0 items-baseline gap-6">
            <Link
              href="/"
              className="text-lg font-bold whitespace-nowrap tracking-tight text-text-on-dark transition-opacity hover:opacity-80"
            >
              {appName}
            </Link>
            {/* 탭 넘침 규칙(§2): 잘렸을 때만 끝이 어두워지는 스크롤 그림자.
                덮개(bg색)는 내용과 함께 스크롤(local), 그림자는 상자에 고정(scroll) —
                끝까지 밀면 덮개가 그림자를 가려 사라진다. */}
            <nav
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
          <div className="flex items-center gap-4">
            {rightSlot}
            {secondaryLinks?.map((l) => (
              <Link
                key={l.key}
                href={l.href}
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

### 6.4 Clerk 게이트 앱 (hub)

인증 게이트(env)가 꺼지면 ClerkProvider 자체를 렌더하지 않는 앱은 정본 AppHeader를
그대로 쓸 수 없다(정본은 `useUser()`를 무조건 호출 → Provider 없으면 크래시). 이 경우
**시각 사양(§2)을 그대로 복제한 이식본**을 만들고 UserMenu만 `next/dynamic`으로 렌더될
때만 로드한다. 적용형: hub `components/site-header.tsx` (2026-07-30).

### 6.3 UserMenu

별도 패턴 — 정본 구현은 maria-ui 비공개 레지스트리 `@maria/user-menu`(`registry/components/UserMenu.tsx`, console·popo 정본의 byte-identical 복제층). 신규 앱은 `shadcn add @maria/user-menu`로 설치한다(@maria/tokens 동반 설치됨). 이니셜 아바타 + 이름·이메일·로그아웃만. Clerk의 `UserButton` 그대로 쓰지 말 것 (사내 도구에 불필요한 "계정 관리" 노출 방지).

## 7. 인쇄 처리

헤더는 `print:hidden`으로 인쇄 시 자동 제거된다 (잉크·종이 절약, 청구서·보고서 캡처에 헤더가 끼어드는 것 방지).

## 8. 적용 현황

| 앱 | 도메인 | 본문 폭 | 비고 |
|---|---|---|---|
| claim | claims.maria-baby.com | `max-w-7xl` | 의료 청구 |
| console | console.maria-baby.com | `max-w-7xl` | 통합 어드민 |
| popo-studio | popo-studio.maria-baby.com | `max-w-7xl` | 미디어 생성 |
| mou-admin | mou-admin.maria-baby.com | `max-w-7xl` | 진료 접수 (토큰 클래스명만 `on-dark` 등으로 다름, 값 동일) |
| hub | hub.maria-baby.com | 헤더 `max-w-7xl` · 본문 `max-w-6xl` | 분원 허브. Clerk 게이트 이식본(§6.4). 본문 폭 통일(§3)은 미실시 |

신규 앱 합류 시 이 표에 한 줄 추가하고 PR을 보낸다.

## 9. 변경 이력

- **v1 (2026-05-07)**: 초안. popo-studio + claim 헤더를 통일하면서 추출.
- **v1.1 (2026-06-04)**: 4앱(claim·console·popo·mou) 전수 통일 반영. 본문 폭 `max-w-7xl` 통일, `text-on-dark` = 아이보리 `#F4EEED` 로 정정(§5 필수토큰의 `#FFFFFF` 오기 수정 — 이 오기를 console·popo 가 globals override 로 따라가 drift 원인이 됐음). 활성 탭 알약·로그인·파비콘·제목 등 전체 규칙은 같은 폴더 `web-ui-guidelines-v1.md` 참조.
- **v1.2 (2026-06-11)**: §5에 `--color-*` = Tailwind v4 `@theme` 계층 명시(`:root` 오배치 방지) + var() 매핑 표준 적용형 추가. §6.3 UserMenu 정본을 maria-ui 레지스트리 `@maria/user-menu`로 지정(TODO 해소).
- **v1.3 (2026-07-30)**: 탭 넘침 가장자리 스크롤 그림자 규칙 추가(§2·§4 — hub 모바일 실사고 유래, 5앱 정본 일괄 반영). 정본 구현을 maria-ui 레지스트리 `@maria/app-header`로 명시(§4). hub 합류(§6.4 Clerk 게이트 이식본 변형·§8). 미해결: 헤더 `print:hidden`이 §2·§7 계약과 달리 4앱 설치본에 없음(결정 대기) · hub 본문 폭 `max-w-6xl`(§3 통일 미실시).
