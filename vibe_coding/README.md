# ✨ 채피 (Chappy): 일상 대화형 실시간 뉴스 분석 비서

*"단순한 챗봇을 넘어, 세상의 소식을 분석하여 전달합니다."*

> 채피(Chappy)는 GMS(GPT-5-Nano) 기반의 인공지능 챗봇으로, 사용자와의 친근한 대화뿐만 아니라 Google News RSS를 활용한 실시간 뉴스 분석 기능을 제공합니다.

### 🚀 핵심 기능 (Core Features)

1. **지능형 일반 대화:** 사용자의 일상적인 질문에 반응하는 친근한 AI 페르소나 적용.

2. **실시간 뉴스 검색 (RAG 기반):** 뉴스, 기사 등의 키워드 감지 시 실시간 RSS 데이터를 수집.

3. **심층 뉴스 분석:** 단순한 제목 나열이 아닌, 5개의 최신 기사를 종합하여 통찰력 있는 분석 결과 제공.

4. **투명한 정보 출처:** 분석에 참고한 기사의 원문 링크를 함께 제공하여 정보 신뢰도 확보.

### 🛠 기술 스택 (Tech Stack)

- 언어: Python 3.11+

- 프레임워크: Streamlit (웹 UI 인터페이스)

- AI 엔진: OpenAI API (GMS 전용 서버 및 gpt-5-nano 모델)

- 데이터 수집: Feedparser (Google News RSS 파싱)

- 환경 관리: Python-dotenv (API Key 보안 관리)

### 📦 설치 및 실행 방법 (Setup & Run)

1. 가상환경 설정 (권장)

    프로젝트의 독립성을 위해 가상환경 사용을 강력히 권장합니다.

    ```pythhon
    # 가상환경 생성
    python -m venv venv

    # 가상환경 활성화 (Windows)
    .\venv\Scripts\activate

    # 가상환경 활성화 (Mac/Linux)
    source venv/bin/activate
    ```


2. 필수 라이브러리 설치

    ```python
    pip install streamlit openai feedparser python-dotenv
    ```


3. 환경 변수 설정

    프로젝트 루트 디렉토리에 .env 파일을 생성하고 발급받은 API 키를 입력합니다. (보안 주의: 이 파일은 절대 외부(GitHub 등)에 공유하지 마세요.)

    ```python
    OPENAI_API_KEY=your_api_key_here
    ```


4. 서비스 실행

    ```python
    streamlit run app.py
    ```


### 📂 프로젝트 구조 (Project Structure)


- app.py              # 메인 애플리케이션 코드 (UI 및 로직 통합)

- .env                # API Key 및 환경 변수 설정 (생성 필요)

- README.md           # 프로젝트 가이드 문서



### ⚠️ 비판적 점검 및 주의사항

- API 호출 제한: GMS 서버 상태나 API 할당량에 따라 응답 속도가 달라질 수 있습니다.

- 키워드 탐지: 현재는 단순 키워드 매칭 방식으로 뉴스 검색을 호출합니다. 질문의 의도를 분석하는 더 정교한 트리거(예: LLM 기반 판단)를 원할 경우 로직 고도화가 필요합니다.

- 데이터 최신성: Google News RSS 업데이트 주기에 따라 실제 기사 발행 시점과 수 분의 차이가 발생할 수 있습니다.

### 👨‍💻 개발자 정보

이름: 오규연

소속: SSAFY_15기_서울_1반

문의: 59raphyy@gmail.com