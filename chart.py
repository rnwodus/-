import streamlit as st
import pandas as pd
import numpy as np

st.header('계산기와 라인 차트')

# 초기 데이터 생성
if 'chart_data' not in st.session_state:
    st.session_state.chart_data = pd.DataFrame(
        [[0], [0], [0]],
        columns=['result']
    )

# Streamlit 위젯으로 사용자 입력 받기
number = st.number_input(
    "Insert a number", value=0.0, placeholder="Type a number...", key="number1"
)

number2 = st.number_input(
    "Insert a number", value=0.0, placeholder="Type a number...", key="number2"
)

# 선택된 연산 방법
option = st.selectbox(
    "Select operation:",
    ("+", "*", "-"),
    index=0,
    placeholder="Select an operation..."
)

button = st.button("Calculate")

# 결과를 저장할 변수
result = None

if button:
    if option == "+":
        result = number + number2
    elif option == "-":
        result = number - number2
    elif option == "*":
        result = number * number2

    # 결과를 DataFrame으로 변환하여 session_state의 chart_data에 추가
    result_df = pd.DataFrame([[result]], columns=['result'])
    st.session_state.chart_data = pd.concat([st.session_state.chart_data, result_df], ignore_index=True)

    # 결과 출력 및 업데이트된 데이터프레임과 차트 표시
    st.write(f"Calculation result: {result}")

# 업데이트된 DataFrame과 차트 표시
st.dataframe(st.session_state.chart_data)
st.line_chart(st.session_state.chart_data)

st.write("Selected operation:", option)
