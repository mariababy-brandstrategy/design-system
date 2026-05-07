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
| 헤더 텍스트 (강조) | 흰색 | `text-text-on-dark` |
| 헤더 텍스트 (보조) | `#A8BABA` | `text-maria-green-300` |
| 활성 탭 배경 | 흰색 | `bg-text-on-dark` |
| 활성 탭 글자 | `#1E3131` | `text-maria-green` |
| 좌우 패딩 | 24px | `px-6` |
| 상하 패딩 | 16px | `py-4` |
| 좌측 영역 gap | 24px | `gap-6` |
| 우측 영역 gap | 16px | `gap-4` |
| 인쇄 시 | 숨김 | `print:hidden` |

## 3. 구조

```
┌────────────────────────────────────────────────────────────────┐
│ [앱 이름]  [탭] [탭] [탭]      [검색?] [secondary] [UserMenu] │
└────────────────────────────────────────────────────────────────┘
       └ 좌: 브랜드 + 1차 탭 ──┘    └ 우: 2차 액션 ──────────┘
```

- **좌측**: 앱 이름 (text-lg font-bold) → 1차 네비게이션 탭(pill 형태)
- **우측**: 검색·secondary 링크·UserMenu (이니셜 아바타)
- **본문 폭**: 앱마다 달라도 됨. 데이터 위주는 `max-w-7xl`, 폼 위주는 `max-w-6xl`. 헤더 inner div의 max-width는 본문과 같게.

## 4. 카피 가능 코드 (React + Tailwind 4)

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
            <nav className="flex items-center gap-1">
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
--color-text-on-dark: #FFFFFF;
```

색 hex 값은 **레포 루트 `tokens/design-tokens.css`와 일치해야 한다**. 임의로 옮겨 적지 말고 그대로 가져올 것.

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

### 6.3 UserMenu

별도 패턴 — `UserMenu v1` 참조 (TODO: 같은 폴더에 추가). 이니셜 아바타 + 이름·이메일·로그아웃만. Clerk의 `UserButton` 그대로 쓰지 말 것 (사내 도구에 불필요한 "계정 관리" 노출 방지).

## 7. 인쇄 처리

헤더는 `print:hidden`으로 인쇄 시 자동 제거된다 (잉크·종이 절약, 청구서·보고서 캡처에 헤더가 끼어드는 것 방지).

## 8. 적용 현황

| 앱 | 도메인 | 본문 폭 | 비고 |
|---|---|---|---|
| popo-studio | popo-studio.maria-baby.com | `max-w-6xl` | 폼 위주 |
| claim | claims.maria-baby.com | `max-w-7xl` | 데이터 테이블 |

신규 앱 합류 시 이 표에 한 줄 추가하고 PR을 보낸다.

## 9. 변경 이력

- **v1 (2026-05-07)**: 초안. popo-studio + claim 헤더를 통일하면서 추출.
