# 마리아병원 디자인 시스템 v2.1

마리아의료재단의 공식 색상·타이포 디자인 시스템. 각 분원 원무과 실무자와 CX부가 인쇄물·PPT·SNS 콘텐츠 제작 시 일관된 브랜드 인상을 유지할 수 있도록 설계되었습니다.

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
│   ├── README.md                  ← **현행 문서 고정 안내**(최신판 링크는 항상 여기)
│   ├── assemble_lib.py            ← 문서 조립 공용 로직·검사(4 소비자 공통)
│   ├── color-guide-src/           ← 브랜드 가이드 · 색상 **편집 정본**(template + assemble.py)
│   ├── screen-brand-guide-src/    ← 브랜드 가이드 · 화면 **편집 정본**
│   ├── space-brand-guide-src/     ← 브랜드 가이드 · 공간 **편집 정본**
│   ├── brief-spec-src/            ← 브랜드 디자인 규격 약식판 **편집 정본**
│   ├── 브랜드-가이드-색상-v*.{html,pdf}   ← 생성물 (A4 10쪽) — 인쇄물·슬라이드 색 기준
│   ├── 브랜드-가이드-화면-v*.{html,pdf}   ← 생성물 (A4 17쪽) — 화면 제작 협력사·사내 개발 배포용
│   ├── 브랜드-가이드-공간-v*.{html,pdf}   ← 생성물 (A4 12쪽) — 인테리어·건축설계·사인 협력사 배포용
│   ├── 브랜드-디자인-규격-약식판-v*.{html,pdf} ← 생성물 (A4 8쪽) — 세 가이드 요약
│   │                              (현행 판 번호는 docs/README.md 가 정본 — 여기엔 적지 않는다, 2026-09-22)
│   ├── archive/                   ← 구판 생성물(배포 당시 그대로)
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
| 포포 틸 | `#1D9581` | 비텍스트 강조(아이콘·게이지·장식) — 글자·글자 배경은 짙은 틸 `#167565`(§1-4) |
| 마리아 핑크 | `#E0A793` | 따뜻한 강조·부드러운 버튼 |
| 마리아 아이보리 | `#F4EEED` | 배경 구분·카드 배경 |

## 사용법

### 실무자 (원무과)
1. 브랜드 가이드 · 색상 PDF 를 열거나 인쇄해서 참고 — 현행판 링크는 [`docs/README.md`](docs/README.md)(판이 오르면 파일명이 바뀌므로 여기서 직접 링크하지 않는다).
2. PPT·한글 프로그램의 "사용자 지정 색상" → "Hex" 칸에 `#` 없이 6자리 입력 (예: `1E3131`).

### 디자이너
1. `tokens/design-tokens.json`을 피그마 Tokens 플러그인에 import.
2. `assets/logos/`, `assets/characters/` 활용.

### 개발자
1. `tokens/design-tokens.css`를 앱의 전역 스타일에 import.
2. CSS 변수로 참조: `color: var(--text-primary); background: var(--bg-ivory);`.
3. **외부 협력사에 전달할 화면 기준은 브랜드 가이드 · 화면 PDF**(현행판 링크 = [`docs/README.md`](docs/README.md), A4 17쪽, HTML 동봉) — 색·로고·글자·형태·아이콘·문구·상태·다이얼로그·화면 폭·폼·탭 제목 + 조건부 셸. 항목마다 반드시/맞춰 주십시오/참고 3등급. 편집 정본은 `docs/screen-brand-guide-src/*.template.html`(생성물 직접 수정 금지).
4. **사내 웹 서비스는 [`docs/web-ui-guidelines-v1.md`](docs/web-ui-guidelines-v1.md)** 를 단일 기준으로 따른다 — 파비콘·헤더·본문 너비·로그인·제목·폰트·색 + 신규앱 체크리스트. 헤더 상세·카피코드는 [`docs/internal-service-header-v1.md`](docs/internal-service-header-v1.md). 레퍼런스: claim·console·popo-studio·mou-admin.
5. **환자·보호자가 읽는 게시 문안의 표기는 [`docs/copy-style-notice-v1.md`](docs/copy-style-notice-v1.md)** 를 따른다 — 날짜·시간·장소 표기, 문장 종결, 불변 원칙(사실·의무 강도 무변경). 공지문·뉴스레터·안내문 공통. 소비처는 문서 끝 JSON 블록을 자기 상수로 복제하고 하니스가 일치를 검사한다(첫 소비처 = hub 자유 공지문 "AI 다듬기").

## 유지보수
- **색·타이포 값의 원본은 `tokens/`(design-tokens.css·json)** 이고, 브랜드 가이드 · 색상(PDF)은 그 값을 인쇄물 독자에게 설명하는 문서입니다. 둘이 어긋나면 PDF 쪽을 다시 찍습니다(2026-09-22 사용자 결정 — 2026-04 제정 때는 PDF 가 먼저였으나 지금은 앱 6개와 문서 4종이 토큰을 직접 씁니다. `AGENTS.md` 「문서 레이어」와 같은 문장).
- **편집 정본은 `docs/color-guide-src/color-guide.template.html`** 입니다(2026-09-03 조판 이전 · 2026-09-22 판 없는 이름으로).
  `docs/브랜드-가이드-색상-v*.{html,pdf}` 는 `python3 docs/color-guide-src/assemble.py --pdf` 가 만드는 **생성물**이므로 직접 고치지 마세요 — 다음 조립에서 지워집니다.
- 색상·타이포 변경이 필요할 경우: (1) `design-tokens.css`·`design-tokens.json` 갱신 → (2) 가이드 템플릿 반영 후 4 문서 재조립(판 올림, 규칙 = `AGENTS.md` 「문서 레이어」) → (3) Claude Design 재학습.

## 문의
마리아의료재단 CX부
