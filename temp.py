import streamlit as st
import numpy as np
import pandas as pd
import time

# Streamlit 웹 애플리케이션 설정
st.title('실시간 온도 모니터링')

# 슬라이더를 사용하여 업데이트 주기 설정
update_interval = st.slider('업데이트 주기 (초)', min_value=1, max_value=60, value=5, step=1)

# 데이터 저장을 위한 리스트 초기화
temperature_data = []

# 온도 데이터를 생성하는 함수 (가상의 데이터 예시)
def get_temperature():
    # 실제 센서 데이터 읽기를 여기에 구현
    return np.random.uniform(20, 25)  # 20도에서 25도 사이의 랜덤 값  

# 그래프를 업데이트할 공간을 예약
chart_placeholder = st.empty()

# 주기적으로 데이터를 업데이트하는 부분
while True:
    # 새로운 온도 데이터 수집
    temp = get_temperature()
    temperature_data.append(temp)
    
    # 데이터가 너무 많아지면, 오래된 데이터 제거
    if len(temperature_data) > 100:
        temperature_data.pop(0)
    
    # 데이터 프레임 생성
    df = pd.DataFrame(temperature_data, columns=['온도'])
    df.index.name = '시간'
    
    # Streamlit에서 그래프 표시
    chart_placeholder.line_chart(df['온도'])
    
    # 업데이트 주기 슬라이더에 따라 대기
    time.sleep(update_interval)