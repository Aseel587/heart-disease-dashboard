import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE SETUP
# =========================
st.set_page_config(layout="wide", page_title="Data Explorer")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("heart.csv")

df = load_data()

# =========================
# MAPS
# =========================
sex_map = {0: "Female", 1: "Male"}
target_map = {0: "Healthy", 1: "Heart Disease"}

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🔎 Filters")

age = st.sidebar.slider(
    "Age",
    int(df.age.min()),
    int(df.age.max()),
    (int(df.age.min()), int(df.age.max()))
)

gender = st.sidebar.multiselect(
    "Gender",
    options=[0, 1],
    default=[0, 1],
    format_func=lambda x: sex_map[x]
)

# =========================
# FILTER DATA
# =========================
filtered = df[
    (df.age.between(age[0], age[1])) &
    (df.sex.isin(gender))
].copy()

# =========================
# VIEW DATA
# =========================
df_view = filtered.copy()
df_view["sex"] = df_view["sex"].map(sex_map)
df_view["target"] = df_view["target"].map(target_map)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.block-container{padding-top:2rem;padding-bottom:2rem;}

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
    text-align:center;
}

.card:hover{
    transform:translateY(-6px);
    border:1px solid #38BDF8;
}

.title{color:white;font-size:18px;margin-bottom:8px;}
.number{font-size:36px;font-weight:bold;color:#38BDF8;}
.subtitle{color:#94A3B8;font-size:14px;}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("""
<div class="banner">
<h1 style="color:white;">📂 Data Explorer</h1>
<p style="font-size:18px;color:#CBD5E1;">
Quick view and filtering of the dataset
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
        <div class="number">{len(filtered)}</div>
        <div class="subtitle">Filtered</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="title">👨‍⚕️ Male</div>
        <div class="number">{(filtered.sex==1).sum()}</div>
        <div class="subtitle">Count</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="title">👩‍⚕️ Female</div>
        <div class="number">{(filtered.sex==0).sum()}</div>
        <div class="subtitle">Count</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="title">❤️ Heart Cases</div>
        <div class="number">{filtered.target.sum()}</div>
        <div class="subtitle">Positive</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SIMPLE VISUAL 
# =========================

plot_df = filtered.copy()
plot_df["sex"] = plot_df["sex"].map(sex_map)

gender_counts = plot_df["sex"].value_counts().reset_index()
gender_counts.columns = ["Gender", "Count"]

fig = px.bar(
    gender_counts,
    x="Gender",
    y="Count",
    title="Gender Distribution",
    text="Count",
    color="Gender",
    color_discrete_sequence=["#38BDF8", "#f472b6"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# TABLE
# =========================
st.subheader("📋 Dataset Preview")

st.dataframe(df_view, use_container_width=True)