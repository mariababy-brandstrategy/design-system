# Pretendard 서브셋 → Maria Doc Sans (문서 레이어 임베드용)

- 원본: Pretendard **v1.3.9** variable(`build/PretendardVariable.woff2`, name "Version 1.309", SHA-256 `9599f12f…d900b4`) — 정본 `docs/web-ui-guidelines-v1.md` §1 표가 고정한 버전. 출처 = jsDelivr `orioncactus/pretendard@v1.3.9`.
- 산출물: `maria-doc-sans-subset.woff2` — 가변 축(wght 45–930) 보존. 문자 = `chars.txt`(KS X 1001 완성형 2350자 + ASCII + Latin-1 보충 + 일반 구두점 + 화살표 + 공간 브랜드 가이드 실사용 문자, 2,771자), `unicodes.txt` 는 같은 목록의 코드포인트.
- **이름이 'Maria Doc Sans' 인 이유**: SIL OFL 1.1 은 글리프를 덜어낸 서브셋을 Modified Version 으로 보고, 예약 글꼴명(Reserved Font Name "Pretendard")을 저작자 서면 허락 없이 쓸 수 없게 한다(`build/LICENSE.txt` 조항 3). 그래서 name 테이블의 패밀리·풀네임·PostScript 이름을 개명하고 저작권·라이선스 레코드는 원문 그대로 둔다(`build/rename.py`). 글자 모양·지표는 Pretendard 그대로다.
- 재생성: `build/build.sh`(fonttools 4.64.0 · brotli 1.2.0, venv 권장). 문자를 늘리려면 `chars.txt`·`unicodes.txt` 를 같이 갱신하고 다시 빌드한다. woff2 는 timestamp 를 담지 않아 같은 입력·도구면 byte 가 재현된다(산출물 SHA-256 은 build.sh 가 출력).
- 소비: HTML→PDF 문서 조립 스크립트가 base64 로 임베드한다 — `@font-face{font-family:"Maria Doc Sans";font-weight:100 900}` 를 선언하고 문서 override 가 `.doc{font-family:"Maria Doc Sans",var(--font-family-primary)}` 로 토큰 사슬 앞에 둔다. 웹 앱은 이 파일이 아니라 §1 표의 CDN(원본 무변형, 이름 그대로)을 쓴다.
- 라이선스: SIL OFL 1.1 (`build/LICENSE.txt`).
