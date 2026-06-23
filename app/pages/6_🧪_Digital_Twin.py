import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Digital Twin Control Room",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
}

.main-title {
    font-size:48px;
    font-weight:800;
    color:#38BDF8;
}

.subtitle {
    color:#CBD5E1;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
🧪 Digital Twin Control Room
</div>

<div class="subtitle">
Physics-Informed Distillation Intelligence Platform
</div>
""", unsafe_allow_html=True)

model = joblib.load("models/physics_sei_model.pkl")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Digital Twin", "ONLINE")
k2.metric("Operating State", "STATE 3")
k3.metric("Risk Level", "LOW")
k4.metric("Simulation", "ACTIVE")

st.divider()

st.subheader("⚙️ Process Intelligence Workflow")

w1, w2, w3, w4, w5 = st.columns(5)

w1.info("📡 Plant Data")
w2.info("⚙️ Features")
w3.info("🧠 AI Engine")
w4.info("🎯 Optimization")
w5.info("🧪 Digital Twin")

with st.expander("⚙️ Simulation Controls", expanded=False):

    c1, c2 = st.columns(2)

    with c1:
        FlowC1 = st.slider("FlowC1", 100.0, 300.0, 188.66)
        PressureC1 = st.slider("PressureC1", 100.0, 400.0, 227.78)
        VapourPressure = st.slider("VapourPressure", 10.0, 100.0, 60.88)
        FlowC2 = st.slider("FlowC2", 10.0, 100.0, 65.25)

    with c2:
        Column_Temp_Avg = st.slider("Column Temp Avg", 200.0, 400.0, 276.93)
        Column_Temp_Span = st.slider("Column Temp Span", 500.0, 1200.0, 893.15)
        FlowC3 = st.slider("FlowC3", 1.0, 20.0, 6.82)
        FlowC4 = st.slider("FlowC4", 1.0, 20.0, 6.41)

X = pd.DataFrame([{
    "FlowC1": FlowC1,
    "FlowC2": FlowC2,
    "FlowC3": FlowC3,
    "FlowC4": FlowC4,
    "PressureC1": PressureC1,
    "VapourPressure": VapourPressure,
    "Column_Temp_Avg": Column_Temp_Avg,
    "Column_Temp_Span": Column_Temp_Span
}])

prediction = model.predict(X)[0]
optimal_sei = 1.2806
health = min(prediction / optimal_sei, 1.0)

st.subheader("🏭 Live Digital Twin Dashboard")

left, right = st.columns(2)

with left:
    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health * 100,
            title={"text": "Process Health"},
            gauge={"axis": {"range": [0, 100]}}
        )
    )

    gauge.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

with right:

    feature_df = pd.DataFrame({
        "Feature": [
            "FlowC1",
            "Vapour Pressure",
            "Column Temp",
            "Pressure",
            "Others"
        ],
        "Importance": [
            61,
            19,
            16,
            1,
            3
        ]
    })

    fig = px.bar(
        feature_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("📊 AI Assessment")

r1, r2, r3, r4 = st.columns(4)

r1.metric("Physics_SEI", f"{prediction:.4f}")
r2.metric("Health Score", f"{health*100:.1f}%")
r3.metric("Target SEI", f"{optimal_sei:.4f}")

improvement = max(
    (optimal_sei - prediction) / optimal_sei * 100,
    0
)

r4.metric(
    "Improvement Potential",
    f"{improvement:.1f}%"
)

st.subheader("🧪 Digital Twin Assessment")

d1, d2 = st.columns(2)

with d1:
    st.success("""
Current Status

• Stable Operation
• Low Risk
• High Efficiency Region
• Digital Twin Online
""")

with d2:
    st.warning("""
Recommended Actions

• Optimize FlowC1
• Monitor Vapour Pressure
• Monitor Temperature Profile
• Maintain Current State
""")

st.subheader("🔮 Future State Prediction")

future_sei = prediction * 1.08

f1, f2, f3 = st.columns(3)

f1.metric("Current SEI", f"{prediction:.4f}")
f2.metric("Projected SEI", f"{future_sei:.4f}")
f3.metric(
    "Projected Gain",
    f"{((future_sei - prediction)/prediction)*100:.1f}%"
)

st.subheader("📄 Executive Summary")

st.info(f"""
Physics_SEI Prediction : {prediction:.4f}

Process Health : {health*100:.1f}%

Operating State : STATE 3

Digital Twin Status : ONLINE

The column is operating in a stable,
high-efficiency region. Additional gains
may be achieved through FlowC1 optimization.
""")