import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# --------------------------------------------------

# PAGE CONFIG

# --------------------------------------------------

st.set_page_config(
page_title="Physics-SEI Prediction Engine",
layout="wide"
)

# --------------------------------------------------

# LOAD MODELS

# --------------------------------------------------

model = joblib.load("models/physics_sei_model.pkl")
anomaly_model = joblib.load("models/anomaly_detector.pkl")

# --------------------------------------------------

# HEADER

# --------------------------------------------------

st.title("🧠 Physics-SEI Prediction Engine")
st.caption("Digital Twin Based Distillation Performance Prediction")

# --------------------------------------------------

# INPUT SECTION

# --------------------------------------------------

st.subheader("⚙️ Operating Conditions")

col1, col2, col3, col4 = st.columns(4)

with col1:
FlowC1 = st.number_input(
"FlowC1",
value=235.73
)

```
FlowC2 = st.number_input(
    "FlowC2",
    value=65.25
)
```

with col2:
FlowC3 = st.number_input(
"FlowC3",
value=6.82
)

```
FlowC4 = st.number_input(
    "FlowC4",
    value=6.41
)
```

with col3:
PressureC1 = st.number_input(
"PressureC1",
value=227.78
)

```
VapourPressure = st.number_input(
    "VapourPressure",
    value=60.88
)
```

with col4:
Column_Temp_Avg = st.number_input(
"Column Temp Avg",
value=276.93
)

```
Column_Temp_Span = st.number_input(
    "Column Temp Span",
    value=893.15
)
```

predict = st.button(
"🚀 Run AI Prediction",
use_container_width=True
)

# --------------------------------------------------

# PREDICTION

# --------------------------------------------------

if predict:

```
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

anomaly_features = pd.DataFrame([{
    "FlowC1": FlowC1,
    "PressureC1": PressureC1,
    "VapourPressure": VapourPressure,
    "Column_Temp_Avg": Column_Temp_Avg,
    "Physics_SEI": prediction
}])

anomaly = anomaly_model.predict(
    anomaly_features
)[0]

health = min(
    prediction / 1.2806,
    1.0
)

st.divider()

# ----------------------------------------------
# KPI DASHBOARD
# ----------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Physics_SEI",
        f"{prediction:.4f}"
    )

with c2:
    st.metric(
        "Process Health",
        f"{health*100:.1f}%"
    )

with c3:
    st.metric(
        "Operating Region",
        "Optimal" if prediction > 1.0 else "Suboptimal"
    )

# ----------------------------------------------
# PROCESS HEALTH GAUGE
# ----------------------------------------------

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=health * 100,
        title={"text": "Process Health Score"},
        gauge={
            "axis": {"range": [0, 100]}
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------------------
# STATUS
# ----------------------------------------------

if prediction > 1.0:
    st.success("🟢 Excellent Operating Region")

elif prediction > 0.7:
    st.info("🟡 Good Operating Region")

else:
    st.warning("🔴 Low Efficiency Region")

if anomaly == -1:
    st.error(
        "⚠️ Potential Abnormal Operation Detected"
    )
else:
    st.success(
        "✅ Normal Operating Condition"
    )

# ----------------------------------------------
# RECOMMENDED CONDITIONS
# ----------------------------------------------

st.subheader(
    "🎯 Recommended Operating Window"
)

recommended = pd.DataFrame([{
    "FlowC1": 188.66,
    "PressureC1": 227.78,
    "VapourPressure": 60.88,
    "Expected_Physics_SEI": 1.2806
}])

st.dataframe(
    recommended,
    use_container_width=True
)

# ----------------------------------------------
# IMPROVEMENT POTENTIAL
# ----------------------------------------------

improvement = (
    (1.2806 - prediction)
    / max(prediction, 0.0001)
) * 100

st.subheader(
    "📈 Improvement Potential"
)

st.metric(
    "Potential Improvement",
    f"{improvement:.2f}%"
)

# ----------------------------------------------
# ENGINEERING INSIGHTS
# ----------------------------------------------

st.subheader(
    "🔍 Engineering Interpretation"
)

st.info(
    """
```

FlowC1 remains the dominant driver of separation performance.

Vapour pressure and column temperature provide
secondary influence on Physics_SEI.

The current operating condition can be improved
by moving closer to the recommended operating window.

State 3 remains the highest-efficiency operating regime
identified by the optimization framework.
"""
)

```
# ----------------------------------------------
# DOWNLOAD REPORT
# ----------------------------------------------

report_text = f"""
```

DISTILLATION INTELLIGENCE REPORT

Physics_SEI : {prediction:.4f}

Health Score : {health*100:.1f}%

Operating Region :
{"Optimal" if prediction > 1 else "Suboptimal"}

Potential Improvement :
{improvement:.2f}%
"""

```
st.download_button(
    "📄 Download Engineering Report",
    report_text,
    file_name="distillation_report.txt"
)
```

