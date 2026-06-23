import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

st.set_page_config(
page_title="Physics-SEI Prediction Engine",
layout="wide"
)

model = joblib.load(
"models/physics_sei_model.pkl"
)

anomaly_model = joblib.load(
"models/anomaly_detector.pkl"
)

# ---------------------------------------------------

# HEADER

# ---------------------------------------------------

st.title(
"🧠 Physics-SEI Prediction Engine"
)

st.caption(
"Digital Twin Based Distillation Performance Prediction"
)

# ---------------------------------------------------

# INPUTS

# ---------------------------------------------------

st.subheader(
"⚙️ Operating Conditions"
)

col1,col2,col3,col4 = st.columns(4)

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
"🚀 Run AI Prediction"
)

# ---------------------------------------------------

# PREDICTION

# ---------------------------------------------------

if predict:

```
X = pd.DataFrame([{
    "FlowC1":FlowC1,
    "FlowC2":FlowC2,
    "FlowC3":FlowC3,
    "FlowC4":FlowC4,
    "PressureC1":PressureC1,
    "VapourPressure":VapourPressure,
    "Column_Temp_Avg":Column_Temp_Avg,
    "Column_Temp_Span":Column_Temp_Span
}])

prediction = model.predict(X)[0]

anomaly_features = pd.DataFrame([{
    "FlowC1":FlowC1,
    "PressureC1":PressureC1,
    "VapourPressure":VapourPressure,
    "Column_Temp_Avg":Column_Temp_Avg,
    "Physics_SEI":prediction
}])

anomaly = anomaly_model.predict(
    anomaly_features
)[0]

health = min(
    prediction/1.28,
    1.0
)

st.divider()

# KPI DASHBOARD

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Physics_SEI",
        round(prediction,4)
    )

with c2:
    st.metric(
        "Process Health",
        f"{health*100:.1f}%"
    )

with c3:
    st.metric(
        "Operating Region",
        "Optimal"
        if prediction > 1
        else "Suboptimal"
    )

# GAUGE

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=health*100,
        title={
            "text":"Process Health"
        },
        gauge={
            "axis":{
                "range":[0,100]
            }
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# STATUS

if anomaly == -1:

    st.error(
        "⚠️ Potential Abnormal Operation"
    )

else:

    st.success(
        "✅ Normal Operating State"
    )

# RECOMMENDATIONS

st.subheader(
    "🎯 Recommended Operating Window"
)

recommended = pd.DataFrame([{
    "FlowC1":188.66,
    "PressureC1":227.78,
    "VapourPressure":60.88,
    "Expected_Physics_SEI":1.2806
}])

st.dataframe(
    recommended,
    use_container_width=True
)

# INSIGHTS

st.subheader(
    "🔍 Engineering Interpretation"
)

st.info(
    '''
    FlowC1 remains the dominant driver
    of separation performance.

    Vapour pressure and column
    temperature provide secondary
    influence.

    Current operating state can be
    improved by moving toward the
    recommended operating window.
    '''
)
```
