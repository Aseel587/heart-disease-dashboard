import streamlit as st
import numpy as np
import joblib

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model.pkl")

# =========================
# TITLE
# =========================
st.markdown("""
<div style="background:linear-gradient(135deg,#2563EB,#0F172A);
padding:25px;border-radius:18px;color:white;margin-bottom:20px">

<h1>🫀 Heart Disease Prediction</h1>
<p>Enter patient data to predict risk level</p>

</div>
""", unsafe_allow_html=True)

# =========================
# MAPPINGS
# =========================
cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}

fbs_map = {
    "Normal": 0,
    "High": 1
}

restecg_map = {
    "Normal": 0,
    "ST-T Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

slope_map = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}

ca_map = {
    "0 vessels": 0,
    "1 vessel": 1,
    "2 vessels": 2,
    "3 vessels": 3
}

thal_map = {
    "Normal": 0,
    "Fixed defect": 1,
    "Reversible defect": 2
}

# =========================
# INPUT FORM
# =========================
with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120, 40)
        sex = st.selectbox("Gender", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", list(cp_map.keys()))
        trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
        chol = st.number_input("Cholesterol", 100, 600, 200)
        fbs = st.selectbox("Fasting Blood Sugar", list(fbs_map.keys()))
        thal = st.selectbox("Thalassemia", list(thal_map.keys()))

    with col2:
        restecg = st.selectbox("Rest ECG", list(restecg_map.keys()))
        thalach = st.number_input("Max Heart Rate", 60, 220, 150)
        exang = st.selectbox("Exercise Angina", ["No", "Yes"])
        oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)
        slope = st.selectbox("Slope", list(slope_map.keys()))
        ca = st.selectbox("Major Vessels", list(ca_map.keys()))

    submit = st.form_submit_button("🔍 Predict")

# =========================
# PREDICTION
# =========================
if submit:

    sex = 1 if sex == "Male" else 0
    cp = cp_map[cp]
    fbs = fbs_map[fbs]
    restecg = restecg_map[restecg]
    slope = slope_map[slope]
    ca = ca_map[ca]
    thal = thal_map[thal]
    exang = 1 if exang == "Yes" else 0

    input_data = np.array([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]])

    prob = model.predict_proba(input_data)[0]

    healthy_prob = prob[0]
    disease_prob = prob[1]

    st.divider()

    # =========================
    # RESULTS
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="background:#1E293B;padding:20px;border-radius:15px;text-align:center">
            <h3 style="color:#22c55e">💚 Healthy</h3>
            <h2>{healthy_prob*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background:#1E293B;padding:20px;border-radius:15px;text-align:center">
            <h3 style="color:#ef4444">❤️ Heart Disease</h3>
            <h2>{disease_prob*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # DECISION
    # =========================
    if disease_prob > 0.5:
        st.error("⚠️ High risk of heart disease")
    else:
        st.success("✅ Low risk of heart disease")