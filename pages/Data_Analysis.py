import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE SETUP
# =========================

st.set_page_config(layout="wide", page_title="Data Analysis")

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("heart.csv")

df = load_data()

df["target_label"] = df["target"].map({
    0: "Healthy",
    1: "Heart Disease"
})

# =========================
# STYLE 
# =========================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.banner{
    background:linear-gradient(135deg,#2563EB,#0F172A);
    padding:28px;
    border-radius:20px;
    margin-bottom:25px;
}

.card{
    background:#1E293B;
    padding:22px;
    border-radius:18px;
    box-shadow:0px 0px 18px rgba(0,0,0,.35);
    border:1px solid rgba(255,255,255,.05);
    transition:.3s;
    text-align:center;
}

.card:hover{
    transform:translateY(-6px);
    border:1px solid #38BDF8;
}

.title{
    color:white;
    font-size:18px;
    margin-bottom:8px;
}

.number{
    font-size:36px;
    font-weight:bold;
    color:#38BDF8;
}

.subtitle{
    color:#94A3B8;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE 
# =========================

st.markdown("""
<div class="banner">

<h1 style="color:white;">📊 Data Analysis</h1>

<p style="font-size:18px;color:#CBD5E1;">
Understand patterns and relationships in the dataset
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# KPI CARDS 
# =========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="title">👥 Patients</div>
        <div class="number">{len(df)}</div>
        <div class="subtitle">Total Records</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="title">❤️ Heart Cases</div>
        <div class="number">{df["target"].sum()}</div>
        <div class="subtitle">Positive Cases</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="title">📊 Features</div>
        <div class="number">{df.shape[1]}</div>
        <div class="subtitle">Columns</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="title">📈 Disease Rate</div>
        <div class="number">{round(df["target"].mean()*100,1)}%</div>
        <div class="subtitle">Percentage</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# ANALYSIS CHARTS
# =========================

st.divider()
st.subheader("📊 Deep Analysis")

col1, col2 = st.columns(2)

# Age distribution
with col1:
    fig1 = px.histogram(df, x="age", nbins=20, title="Age Distribution")
    st.plotly_chart(fig1, use_container_width=True)

# Disease ratio
with col2:
    fig2 = px.pie(df, names="target_label", title="Disease Ratio",
                  color_discrete_sequence=["#22c55e", "#ef4444"])
    st.plotly_chart(fig2, use_container_width=True)

# Correlation (important analysis)
st.subheader("🔥 Correlation Heatmap")

fig3 = px.imshow(
    df.corr(numeric_only=True),
    text_auto=True,
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(fig3, use_container_width=True)

# Box plot
st.subheader("📌 Age vs Disease")

fig4 = px.box(
    df,
    x="target_label",
    y="age",
    color="target_label"
)

st.plotly_chart(fig4, use_container_width=True)

# =========================
# INSIGHTS
# =========================

st.subheader("🧠 Insights")

st.markdown("""
- Heart disease increases with age  
- Chest pain is a strong indicator  
- Some medical features are highly correlated  
- Older patients show higher risk distribution  
""")    