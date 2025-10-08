import streamlit as st
import random

# --- 1. 교사용 응원 문구 리스트 (여기서 자유롭게 편집하세요!) ---
TEACHER_QUOTES = [
    "선생님의 열정은 학생들의 미래를 밝히는 빛입니다. 오늘도 수고 많으셨습니다!",
    "작은 씨앗이 큰 나무가 되듯, 선생님의 가르침은 아이들의 꿈을 키웁니다. 늘 감사합니다.",
    "때로는 지치고 힘들겠지만, 선생님의 미소는 아이들에게 가장 큰 응원입니다. 힘내세요!",
    "교육은 마음에서 마음으로 전달되는 사랑입니다. 선생님의 따뜻한 마음에 박수를 보냅니다.",
    "수많은 길 중 가장 고귀한 길을 걷는 선생님, 언제나 존경하고 응원합니다.",
    "어제의 노력은 오늘의 결실로, 오늘의 노력은 내일의 희망으로! 선생님의 헌신에 감사드립니다.",
    "선생님은 아이들의 세상을 넓혀주는 마법사입니다. 오늘도 멋진 마법을 보여주셨네요!",
    "가장 큰 선물은 지식과 사랑을 주는 것입니다. 선생님은 매일 귀한 선물을 주시는군요.",
    "포기하지 않는 용기, 그것이 바로 선생님의 가장 큰 힘입니다. 항상 선생님 편입니다!",
    "선생님의 한 마디가 아이들의 인생을 바꿀 수 있습니다. 그 소중한 영향력에 감사드립니다."
]

# --- 2. 앱 기본 설정 ---
st.set_page_config(
    page_title="교사용 응원 카드",
    page_icon="💖"
)

st.title("💖 교사용 응원 카드 💖")
st.write("선생님, 오늘도 수고 많으셨습니다! 잠시 쉬어가며 따뜻한 응원을 받아보세요.")

# --- 3. 세션 상태 초기화 (이전 응원 문구를 저장하기 위해 사용) ---
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "아직 응원 문구를 받지 않으셨어요!"

# --- 4. '오늘의 응원 받기' 버튼 ---
if st.button("✨ 오늘의 응원 받기 ✨"):
    # 새로운 응원 문구 무작위 선택
    new_quote = random.choice(TEACHER_QUOTES)
    
    # 이전에 동일한 문구가 나왔다면 다른 문구를 선택 시도 (선택 사항)
    # 무한 루프 방지를 위해 리스트가 1개 초과일 때만 시도
    if len(TEACHER_QUOTES) > 1:
        while new_quote == st.session_state.last_quote:
            new_quote = random.choice(TEACHER_QUOTES)
            
    st.session_state.last_quote = new_quote # 현재 문구를 이전 문구로 저장
    st.success(f"**🌟 오늘의 응원 🌟**\n\n_{st.session_state.last_quote}_") # 즉시 표시

# --- 5. '최근 응원 문구 다시 보기' 버튼 ---
st.markdown("---") # 구분선 추가
if st.button("📖 최근 응원 문구 다시 보기"):
    st.info(f"**➡️ 이전에 받은 응원 ⬅️**\n\n_{st.session_state.last_quote}_")

# --- 6. 하단 안내 문구 ---
st.markdown("""
<br>
<small>Made with ❤️ for Teachers</small>
""", unsafe_allow_html=True)