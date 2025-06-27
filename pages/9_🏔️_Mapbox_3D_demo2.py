import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

# 載入 .env
load_dotenv()
mapbox_token = os.getenv("MAPBOX_TOKEN")

if not mapbox_token:
    st.error("❌ MAPBOX_TOKEN 未正確讀取")
    st.stop()

# ✅ 使用你的自訂 Mapbox 樣式
custom_map_style = "mapbox://styles/river543/cl7rhvnlh000e14mfl6xrx31b"

# 生成了一個包含 1000 個隨機經緯度座標
chart_data = pd.DataFrame(
    # np.random.randn(1000, 2) / [50, 50] + [23.8, 121],
    np.random.randn(1000, 2) / [40, 40] + [23.8, 121],
    columns=["lat", "lon"],
)

deck = pdk.Deck(
    map_style=custom_map_style,
    initial_view_state=pdk.ViewState(
        latitude=23.8,
        longitude=121.0,
        zoom=10,
        pitch=45,
        bearing=0
    ),
    # layers=[],  # 無資料圖層
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=chart_data,
            get_position="[lon, lat]",
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=chart_data,
            get_position="[lon, lat]",
            get_color="[200, 30, 0, 160]",
            get_radius=200,
        ),
    ],
    api_keys={"mapbox": mapbox_token},
)

st.title("🗺️ 使用客製 Mapbox 樣式")
st.pydeck_chart(deck, use_container_width=True)
