import streamlit as st

st.set_page_config(
    page_title="Heart Disease Dashboard",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

home = st.Page("pages/Home.py", title="Home", icon="🏠", default=True)
explorer = st.Page("pages/Data_Explorer.py", title="Data Explorer", icon="📂")
analysis = st.Page("pages/Data_Analysis.py", title="Data Analysis", icon="📊")
prediction = st.Page("pages/Prediction.py", title="AI Prediction", icon="🧠")

pg = st.navigation({
    "Heart Disease Dashboard": [home, explorer, analysis, prediction]
})

st.logo("https://img.icons8.com/fluency/96/heart-with-pulse.png")

pg.run()