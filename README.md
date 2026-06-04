# 마리아병원 디자인 시스템 v2.1

마리아의료재단의 공식 색상·타이포 디자인 시스템. 각 분원 원무과 실무자와 브랜드전략부가 인쇄물·PPT·SNS 콘텐츠 제작 시 일관된 브랜드 인상을 유지할 수 있도록 설계되었습니다.

## 핵심 변화 (v1.0 → v2.1)
- 마스코트 캐릭터 **POPO**에서 추출한 **포포 틸 `#1D9581`**을 공식 강조색으로 도입.
- 4 코어 컬러 + 밝기 스케일 구조 정립 (마리아 그린 / 포포 틸 / 마리아 핑크 / 마리아 아이보리).
- 상태 색상(성공/경고/오류/안내/활성) 추가.
- 원무과 실무자 눈높이의 안내 문서(정본) 제공.

## 파일 구조

```
claude-design-upload/
├── README.md                      ← 본 문서
├── tokens/
│   ├── design-tokens.json         ← 구조화된 토큰 (AI/개발/디자인용)
│   └── design-tokens.css          ← 웹 구현용 CSS 변수
├── docs/
│   ├── v2.1-실무자용.html         ← 정본 가이드 (브라우저에서 열기)
│   ├── v2.1-실무자용.pdf          ← 인쇄·배포용
│   ├── blurb.txt                  ← Claude Design의 Company blurb 필드용
│   └── notes.md                   ← Claude Design의 Any other notes 필드용
└── assets/
    ├── MARIA_BI Color.png         ← 브랜드 컬러 레퍼런스
    ├── logos/                     ← 공식 로고 (5가지 색상 조합)
    └── characters/
        ├── POPO_01.png            ← 포포 (포포 틸 색상의 유래)
        └── POPO_02.png
```

## 4 코어 컬러

| 이름 | HEX | 용도 |
|---|---|---|
| 마리아 그린 | `#1E3131` | 제목·공식 버튼·표지 배경 |
| 포포 틸 | `#1D9581` | 강조 버튼·링크·CTA |
| 마리아 핑크 | `#E0A793` | 따뜻한 강조·부드러운 버튼 |
| 마리아 아이보리 | `#F4EEED` | 배경 구분·카드 배경 |

## 사용법

### 실무자 (원무과)
1. `docs/v2.1-실무자용.pdf`를 열거나 인쇄해서 참고.
2. PPT·한글 프로그램의 "사용자 지정 색상" → "Hex" 칸에 `#` 없이 6자리 입력 (예: `1E3131`).

### 디자이너
1. `tokens/design-tokens.json`을 피그마 Tokens 플러그인에 import.
2. `assets/logos/`, `assets/characters/` 활용.

### 개발자
1. `tokens/design-tokens.css`를 앱의 전역 스타일에 import.
2. CSS 변수로 참조: `color: var(--text-primary); background: var(--bg-ivory);`.
3. **사내 웹 서비스는 [`docs/web-ui-guidelines-v1.md`](docs/web-ui-guidelines-v1.md)** 를 단일 기준으로 따른다 — 파비콘·헤더·본문 너비·로그인·제목·폰트·색 + 신규앱 체크리스트. 헤더 상세·카피코드는 [`docs/internal-service-header-v1.md`](docs/internal-service-header-v1.md). 레퍼런스: claim·console·popo-studio·mou-admin.

## 유지보수
- 정본은 `docs/v2.1-실무자용.html`입니다. 토큰은 이 문서에서 추출한 값입니다.
- 색상·타이포 변경이 필요할 경우: (1) HTML 정본 업데이트 → (2) `design-tokens.json` 동기화 → (3) `design-tokens.css` 동기화 → (4) Claude Design 재학습.

## 문의
마리아의료재단 브랜드전략부
