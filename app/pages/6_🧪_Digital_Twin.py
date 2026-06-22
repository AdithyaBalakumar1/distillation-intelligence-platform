import streamlit as st
import pandas as pd
import joblib

st.title("🧪 Digital Twin Simulator")

model = joblib.load("models/physics_sei_model.pkl")

st.subheader(
    "Simulate Operating Conditions"
)

FlowC1 = st.slider(
    "FlowC1",
    100.0,
    300.0,
    188.66
)

FlowC2 = st.slider(
    "FlowC2",
    10.0,
    100.0,
    65.25
)

FlowC3 = st.slider(
    "FlowC3",
    1.0,
    20.0,
    6.82
)

FlowC4 = st.slider(
    "FlowC4",
    1.0,
    20.0,
    6.41
)

PressureC1 = st.slider(
    "PressureC1",
    100.0,
    400.0,
    227.78
)

VapourPressure = st.slider(
    "VapourPressure",
    10.0,
    100.0,
    60.88
)

Column_Temp_Avg = st.slider(
    "Column_Temp_Avg",
    200.0,
    400.0,
    276.93
)

Column_Temp_Span = st.slider(
    "Column_Temp_Span",
    500.0,
    1200.0,
    893.15
)

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

improvement = (
    (optimal_sei - prediction)
    / optimal_sei
) * 100

st.divider()

st.subheader("📊 What-If Analysis")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Current Physics_SEI",
        round(prediction, 4)
    )

with col2:
    st.metric(
        "Optimal Physics_SEI",
        optimal_sei
    )

if prediction < optimal_sei:

    st.warning(
        f"Potential improvement opportunity: {improvement:.2f}%"
    )

else:

    st.success(
        "Operating near optimal conditions."
    )

st.subheader("🛠 Engineering Recommendations")

if FlowC1 > 188.66:
    st.write(
        "• Consider reducing FlowC1 toward optimal range."
    )

if VapourPressure < 60.88:
    st.write(
        "• Vapour pressure below target operating window."
    )

if Column_Temp_Avg > 300:
    st.write(
        "• Elevated column temperature may reduce efficiency."
    )

if prediction > 1.0:
    st.write(
        "• Column operating in high-efficiency region."
    )

st.metric(
    "Predicted Physics_SEI",
    round(prediction,4)
)

health = min(prediction/1.28,1.0)

st.progress(health)

st.write(
    f"Process Health: {health*100:.1f}%"
)