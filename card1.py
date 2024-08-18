
import streamlit as st
import pandas as pd

# 각종 상태 변수를 초기화
if 'cards' not in st.session_state:
    st.session_state.cards = []

# 카드 추가 함수
def add_card(card_name, allocated_amount):
    if card_name and allocated_amount > 0:
        st.session_state.cards.append({
            "카드": card_name,
            "월별 사용지정금액": allocated_amount,
            "지출금액": 0,
            "사용가능금액": allocated_amount,
        })

# 카드 삭제 함수
def remove_card(card_name):
    st.session_state.cards = [card for card in st.session_state.cards if card['카드'] != card_name]

# 카드 수정 함수
def update_card(card_name, updated_spending):
    for card in st.session_state.cards:
        if card["카드"] == card_name:
            card["지출금액"] = updated_spending
            card["사용가능금액"] = card["월별 사용지정금액"] - updated_spending
            break

# 앱 제목
st.title("카드 관리 앱")

# 카드 추가 입력란
card_name = st.text_input("카드 이름을 입력하세요:")
allocated_amount = st.number_input("월별 사용지정금액을 입력하세요:", min_value=0)

# 카드 추가 버튼
if st.button("카드 추가"):
    add_card(card_name, allocated_amount)

# 카드 목록을 데이터프레임 형식으로 준비
cards_df = pd.DataFrame(st.session_state.cards)

# 카드 목록 표시
st.subheader("내 카드 목록:")
if not cards_df.empty:
    # 표 형태로 카드 상태 출력
    st.dataframe(cards_df, use_container_width=True)

    # 카드 업데이트 섹션
    selected_card = st.selectbox("수정할 카드를 선택하세요", cards_df['카드'].tolist())

    updated_spending = st.number_input("지출금액을 입력하세요:", min_value=0)

    if st.button("카드 수정"):
        update_card(selected_card, updated_spending)

    # 카드 삭제 버튼
    if st.button("선택한 카드 삭제"):
        remove_card(selected_card)

else:
    st.write("카드가 없습니다.")