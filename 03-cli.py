from ai import get_personality_analysis
from dotenv import load_dotenv
load_dotenv() 


print("안녕  AI 관상가양반이요 \n얼굴 특징을 입력하시면 성격과 미래를 알려주겠소")
line = input("\n얼굴 특징 입력 >>> ").strip()
print()
print(repr(line))

if not line:
    print("Error : 얼굴 특징을 입력하지 않으셨습니다")
else:
    print('입력하신 얼굴 특징 : ', line)
    re = get_personality_analysis(line)
    print('분석 완료!\n',re)
    
