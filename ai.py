from openai import OpenAI




def get_personality_analysis(face_desc: str) -> str:
    # 원하는 어떠한 형태로든 지시문 문자열을 생성하실 수 있습니다.
    '''
    인자로 얼굴 설명을 받아, OpenAI LLM API를 활용하여 성격과 미래를 분석합니다.
    
    '''
    prompt = "당신은 전문 관상가입니다. "
    prompt += "사람들의 얼굴 특징을 보고 성격과 미래를 친근하게 분석해주세요."
    prompt += "\n 얼굴 특징 : " + face_desc

    client = OpenAI()  # OPENAI_API_KEY 환경변수 지정이 필요
    #여기서 key를 지정하지 않아도 이미 설정 해놓은 게 있다면 자동으로 찾아서 적용된다

    response = client.responses.create(
        model="gpt-4o",  # 사용할 두뇌 지정
        input=prompt,
    )
    print("usage :", response.usage)

    return response.output_text


