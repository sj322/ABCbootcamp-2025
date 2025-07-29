# AI 실습 예제 모음

이 프로젝트는 다양한 AI 기술(OpenAI API, 음성 합성, 데이터 시각화 등)을 실습하기 위한 Python 예제 코드 모음입니다.  
모든 코드는 **공부 및 연습용**으로 작성되었습니다.

---

## 폴더/파일 구조 및 역할

- **01-openai-test.py**  
  OpenAI API를 이용한 텍스트 생성 예제

- **02-openai-chat.py**  
  OpenAI ChatGPT API를 활용한 대화형 챗봇 예제

- **03-openai-image.py**  
  OpenAI DALL·E API를 이용한 이미지 생성 예제

- **04-webapp.py**  
  Streamlit 기반 관상 분석 웹앱

- **05-tts-gtts.py**  
  gTTS(Google Text-to-Speech)로 텍스트 음성 합성 및 재생

- **06-tts-pygame.py**  
  gTTS와 pygame을 활용한 음성 합성 및 오디오 재생

- **07-melon-top100.py**  
  멜론 차트 Top100 데이터 크롤링 및 시각화

- **08-web-melon-top100.py**  
  멜론 차트 Top100 데이터를 웹에서 시각화하는 Streamlit 앱

---

## 환경 및 설치 방법

1. **Python 3.8 이상**이 필요합니다.
2. 필수 패키지 설치:
   ```
   pip install -r requirements.txt
   ```

---

## 환경 변수 설정

OpenAI API를 사용하는 예제는 환경 변수 설정이 필요합니다.  
프로젝트 루트에 `.env` 파일을 생성하고 아래와 같이 입력하세요:

```
OPENAI_API_KEY=sk-xxxx***your_key***xxx
```

---

## 실행 방법

각 예제는 아래와 같이 실행할 수 있습니다.

- CLI 예제:
  ```
  python 01-openai-test.py
  ```
- Streamlit 웹앱 예제:
  ```
  streamlit run 04-webapp.py
  ```

---

## 주요 라이브러리

- openai
- streamlit
- gtts
- pygame
- requests
- beautifulsoup4 등

---

## 참고 및 주의사항

- 본 프로젝트는 **공부 및 연습용**입니다.
- 데이터 및 API 사용 시 각 서비스의 정책을 준수하세요.
- 멜론 차트 데이터는 크롤링을 통해 수집되며, 해당 사이트의 이용약관을 따릅니다.


