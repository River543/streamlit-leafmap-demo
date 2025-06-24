import streamlit as st
import pydeck as pdk
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

deck = pdk.Deck(
    map_style=custom_map_style,
    initial_view_state=pdk.ViewState(
        latitude=23.8,
        longitude=121.0,
        zoom=6.4,
        pitch=45,
    ),
    layers=[],  # 無資料圖層
    api_keys={"mapbox": mapbox_token},
)

st.title("🗺️ 使用客製 Mapbox 樣式")
st.pydeck_chart(deck, use_container_width=True)
