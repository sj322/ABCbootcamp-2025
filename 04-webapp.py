import streamlit as st
from ai import get_personality_analysis
from dotenv import load_dotenv

load_dotenv()


st.title("🔮 AI 관상 보기 프로그램")
st.write("---")

st.write("안녕하세요! AI 관상가입니다.")


face_desc = st.text_area("얼굴 특징을 입력해주세요")
face_desc = face_desc.strip()           #필요 없는 공백 제거



if st.button("관상 보기", type="primary"):
    if face_desc:
        with st.spinner("관상을 분석 중입니다..."):
            result = get_personality_analysis(face_desc)
            st.write("입력 값\n"+face_desc)
            st.info(result)
    else:
        # st.warning("얼굴 특징을 입력하고, 관상보기 버튼을 클릭해주세요.")
        st.error("얼굴 특징을 입력하고, 관상보기 버튼을 클릭해주세요.")         # 경고문 출력






