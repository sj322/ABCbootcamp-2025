from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env 파일이 있다면, 환경변수로서 로딩
client = OpenAI()  # OPENAI_API_KEY 환경변수 지정이 필요


stream = client.responses.create(
    model="gpt-4o",
    input="자취생을 위한 가성비 저녁메뉴 추천해줘, 추천해줄 때 본론만 말해",
    stream=True, # 값(청크)을 생산할 준비
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end='', flush=True)




