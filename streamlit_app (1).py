
import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

# 1. 제목
st.title("🚇 서울 지하철 혼잡도 예측 대시보드")
st.markdown("날짜, 시간대, 역명을 선택하면 예측된 혼잡도와 대안 교통수단, 정책 제안을 확인할 수 있습니다.")

# 2. 사용자 입력
st.sidebar.header("🔧 예측 조건 선택")
selected_date = st.sidebar.date_input("날짜 선택")
selected_hour = st.sidebar.selectbox("시간대 선택", range(5, 24))
selected_line = st.sidebar.selectbox("호선 선택", ["1호선", "2호선", "3호선", "4호선"])
selected_station = st.sidebar.text_input("역명 입력", "강남")

# 3. 예측 결과 출력 (샘플)
st.subheader("📈 예측 혼잡도 결과")
predicted_level = np.random.choice(["낮음", "보통", "높음"], p=[0.3, 0.4, 0.3])
st.metric(label="예측 혼잡도", value=predicted_level)

# 4. 변수 영향도 바 차트
st.subheader("📊 혼잡도 영향 변수")
influences = pd.DataFrame({
    '변수': ['강수량', '기온', '요일', '출근시간 여부'],
    '영향도': [0.32, 0.25, 0.18, 0.25]
})
st.bar_chart(influences.set_index('변수'))

# 5. 대안 제안
st.subheader("🚦 대안 제안")
if predicted_level == "높음":
    st.markdown("- ⚠️ **탄력 배차 필요**: 2분 간격 단축 권장")
    st.markdown("- 🚌 **주변 버스 노선**: 342, 740번 등 대체 가능")
else:
    st.markdown("- ✅ 현재 상황은 양호합니다.")

# 6. 지도 시각화
st.subheader("🗺️ 혼잡도 클러스터 지도 (예시)")
m = folium.Map(location=[37.4979, 127.0276], zoom_start=13)
folium.CircleMarker([37.4979, 127.0276], radius=10, popup="강남역", color="red").add_to(m)
st_data = st_folium(m, width=700)
