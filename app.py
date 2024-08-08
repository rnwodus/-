import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import time

# 설정
st.title('센서 수위 값 시각화')

# 센서 ID 입력 받기
sensor_id = st.text_input('센서 ID를 입력하세요:', '')

# 데이터 저장을 위한 변수 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['timestamp', 'value'])

if 'temp' not in st.session_state:
    st.session_state.temp = pd.DataFrame(columns=['timestamp', 'value'])

if 'hum' not in st.session_state:
    st.session_state.hum = pd.DataFrame(columns=['timestamp', 'value'])

# 슬라이더로 업데이트 주기 설정
update_interval = st.slider('데이터 업데이트 주기 (초):', min_value=2, max_value=60, value=10, step=5)

# 실시간 데이터 업데이트
if sensor_id:
    st.subheader('센서 수위 그래프')

    # 데이터 업데이트를 위한 컨테이너
    warning_container = st.empty()
    chart_container = st.empty()
    st.title("습도")
    chart_container1 = st.empty()
    st.title("온도")
    chart_container2 = st.empty()
    

    while True:
        url = f'https://cnu.soungmin.me/value?sensor_id={sensor_id}'
        response = requests.get(url)

        if response.status_code == 200:
            # 데이터 처리
            data = response.text
            try:
                # 숫자로 변환
                value = float(data)
                
                # 데이터프레임에 새 데이터 추가
                new_entry = pd.DataFrame({
                    'timestamp': [datetime.now()],
                    'value': [value]
                })
                st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

                # 데이터프레임 업데이트 및 시각화
                df = st.session_state.data
                chart_container.line_chart(df.set_index('timestamp')['value'])
                
                # 경고 메시지 표시
                if value > 600:
                    warning_container.warning('경고: 센서 수위 값이 600을 넘었습니다!')
                else:
                    warning_container.empty()

            except ValueError:
                st.error('받은 데이터가 유효하지 않습니다.')
        else:
            st.error('서버에 연결할 수 없습니다. 센서 ID를 확인하세요.')
        
        url = f'https://cnu.soungmin.me/value?sensor_id=1'
        response = requests.get(url)

        if response.status_code == 200:
            # 데이터 처리
            data = response.text
            try:
                # 숫자로 변환
                value = float(data)
                
                # 데이터프레임에 새 데이터 추가
                new_entry = pd.DataFrame({
                    'timestamp': [datetime.now()],
                    'value': [value]
                })
                st.session_state.temp = pd.concat([st.session_state.temp, new_entry], ignore_index=True)

                # 데이터프레임 업데이트 및 시각화
                df = st.session_state.temp
                chart_container1.line_chart(df.set_index('timestamp')['value'])
                
                

            except ValueError:
                st.error('받은 데이터가 유효하지 않습니다.')
        else:
            st.error('서버에 연결할 수 없습니다. 센서 ID를 확인하세요.')
        
        url = f'https://cnu.soungmin.me/value?sensor_id=2'
        response = requests.get(url)

        if response.status_code == 200:
            # 데이터 처리
            data = response.text
            try:
                # 숫자로 변환
                value = float(data)
                
                # 데이터프레임에 새 데이터 추가
                new_entry = pd.DataFrame({
                    'timestamp': [datetime.now()],
                    'value': [value]
                })
                st.session_state.hum = pd.concat([st.session_state.hum, new_entry], ignore_index=True)

                # 데이터프레임 업데이트 및 시각화
                df = st.session_state.hum
                chart_container2.line_chart(df.set_index('timestamp')['value'])
                
                

            except ValueError:
                st.error('받은 데이터가 유효하지 않습니다.')
        else:
            st.error('서버에 연결할 수 없습니다. 센서 ID를 확인하세요.')

        # 데이터 업데이트 주기 (사용자가 설정한 주기에 따라) 
        time.sleep(update_interval)