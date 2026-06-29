import streamlit as st
import pandas as pd

st.logo("https://img.icons8.com/fluency/96/heart-with-pulse.png")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("heart.csv")

df = load_data()

# ===============================
# MAPS 
# ===============================
target_map = {0: "Healthy", 1: "Heart Disease"}

# ===============================
# STATS
# ===============================
patients = len(df)

heart = df["target"].sum()          # المصابين
healthy = patients - heart          # السليمين

risk_rate = round((heart / patients) * 100, 1)

# =====================
# CSS
# =====================
st.markdown("""
<style>

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

.card{
background:#1E293B;
padding:22px;
border-radius:18px;
box-shadow:0px 0px 18px rgba(0,0,0,.35);
text-align:center;
transition:.3s;
}

.card:hover{
transform:translateY(-6px);
}

.number{
font-size:40px;
font-weight:bold;
color:#38BDF8;
}

.title{
font-size:18px;
color:white;
}

.banner{
background:linear-gradient(135deg,#2563EB,#0F172A);
padding:35px;
border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================
# HERO
# =====================
left, right = st.columns([3,1])

with left:
    st.markdown("""
<div class='banner'>

<h1 style='color:white'>
❤️ Heart Disease Prediction Dashboard
</h1>

<p style='font-size:20px;color:#CBD5E1'>
Predict Heart Disease Using Machine Learning &
Explore Medical Data Interactively
</p>

</div>
""", unsafe_allow_html=True)

with right:
    st.image(
        "https://img.icons8.com/color/480/heart-with-pulse.png",
        width=220
    )

st.write("")

# =====================
# CARDS
# =====================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card'>
    <div class='title'>👥 Patients</div>
    <div class='number'>{patients}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card'>
    <div class='title'>❤️ Heart Disease</div>
    <div class='number'>{heart}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card'>
    <div class='title'>💚 Healthy</div>
    <div class='number'>{healthy}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    rate = round((heart / patients) * 100, 1)
    st.markdown(f"""
    <div class='card'>
    <div class='title'>📊 Risk Rate</div>
    <div class='number'>{rate}%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
# =====================
# ABOUT
# =====================

st.subheader("About The Project")

st.write("""
This dashboard predicts the likelihood of heart disease using Machine Learning models.

It also provides interactive visualizations that help understand patient data and identify important health indicators.
""")

st.subheader("Objectives")

st.markdown("""
✅ Predict heart disease  
✅ Analyze medical data  
✅ Interactive dashboard  
✅ Support healthcare decisions  
""")

st.divider()

st.subheader("Dataset Preview")
# =====================
#  VIEW
# =====================
df_view = df.copy()

df_view["target"] = df_view["target"].map({
    0: "Healthy",
    1: "Heart Disease"
})

df_view["sex"] = df_view["sex"].map({
    0: "Female",
    1: "Male"
})

df_view["cp"] = df_view["cp"].map({
    0: "Typical Angina",
    1: "Atypical",
    2: "Non-anginal",
    3: "Asymptomatic"
})

df_view["fbs"] = df_view["fbs"].map({
    0: "Normal",
    1: "High"
})

df_view["exang"] = df_view["exang"].map({
    0: "No",
    1: "Yes"
})
st.dataframe(df_view, use_container_width=True)

st.divider()

st.markdown(
    "<h3 style='text-align:center;'>👥 Team Members</h3>",
    unsafe_allow_html=True
)

row1 = st.columns(4)

with row1[0]:
    st.markdown("**Aseel Alsaedi**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/aseel-sultan-2a4b562b3)")

with row1[1]:
    st.markdown("**Yasser Alsehli**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/yasseralsehli)")

with row1[2]:
    st.markdown("**Razan Alzahrani**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/razan-alzahrani-89513620b)")

with row1[3]:
    st.markdown("**Rand Aljamily**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/randhamoud)")

st.write("")

row2 = st.columns(3)

with row2[0]:
    st.markdown("**Amal Almutairi**")

with row2[1]:
    st.markdown("**Salma Alboqami**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/salmaalboqami)")

with row2[2]:
    st.markdown("**Wafaa Masoud**")