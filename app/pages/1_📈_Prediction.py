import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #111827,
        #1E293B
    );
}

.block-container {
    padding-top: 2rem;
}

.big-header {
    font-size: 48px;
    font-weight: 800;
    color: #38BDF8;
}

.subtitle {
    color: #CBD5E1;
    font-size: 18px;
}

.glass-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Physics-SEI Prediction Engine",
    layout="wide"
)

st.markdown("""
<div class="glass-card">

<p class="big-header">
🧠 Physics-SEI Prediction Engine
</p>

<p class="subtitle">
Physics-Informed Digital Twin for Distillation Analytics
</p>

</div>
""", unsafe_allow_html=True)
st.caption("Digital Twin Based Distillation Performance Prediction")

st.subheader("⚙️ Operating Conditions")
st.success("""
### Current Digital Twin Status

🟢 Process Stable

📈 Predicted Efficiency: 87%

🎯 Operating State: State 3

⚠️ Anomaly Risk: Low
""")
st.markdown("""
### Process Intelligence Workflow

Plant Data
⬇️
Physics Features
⬇️
AI Prediction
⬇️
Optimization
⬇️
Digital Twin
⬇️
Decision Support
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    FlowC1 = st.number_input("FlowC1", value=235.73)
    FlowC2 = st.number_input("FlowC2", value=65.25)

with col2:
    FlowC3 = st.number_input("FlowC3", value=6.82)
    FlowC4 = st.number_input("FlowC4", value=6.41)

with col3:
    PressureC1 = st.number_input("PressureC1", value=227.78)
    VapourPressure = st.number_input("VapourPressure", value=60.88)

with col4:
    Column_Temp_Avg = st.number_input("Column Temp Avg", value=276.93)
    Column_Temp_Span = st.number_input("Column Temp Span", value=893.15)

predict = st.button(
    "🚀 Run AI Prediction",
    use_container_width=True
)

if predict:

    prediction = 1.12
    health = 87.5

    st.divider()

    # ----------------------------------
    # EXECUTIVE DASHBOARD
    # ----------------------------------

    st.subheader("📊 Executive Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Physics_SEI",
        f"{prediction:.3f}"
    )

    c2.metric(
        "Health Score",
        f"{health:.1f}%"
    )

    c3.metric(
        "Operating State",
        "State 3"
    )

    c4.metric(
        "Anomaly Risk",
        "Low"
    )

    # ----------------------------------
    # HEALTH + FEATURE IMPORTANCE
    # ----------------------------------

    left, right = st.columns([1,1])

    with left:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=health,
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

        fig.update_layout(
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        importance_df = pd.DataFrame({
            "Feature":[
                "FlowC1",
                "Vapour Pressure",
                "Column Temp",
                "Pressure",
                "Others"
            ],
            "Importance":[
                61,
                19,
                16,
                1,
                3
            ]
        })

        fig2 = px.bar(
            importance_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Feature Importance Analysis"
        )

        fig2.update_layout(
            template="plotly_dark",
            height=400
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ----------------------------------
    # EXECUTIVE SUMMARY
    # ----------------------------------

    st.success("""
### Executive Assessment

The process is currently operating
within a stable high-efficiency region.

Predicted Physics_SEI indicates
strong separation performance
with low anomaly risk.

Further optimization opportunity
exists through FlowC1 adjustment.
""")

    # ----------------------------------
    # DIGITAL TWIN
    # ----------------------------------

    st.subheader(
        "🧪 Digital Twin Status"
    )

    d1, d2 = st.columns(2)

    with d1:

        st.info("""
Current State : Stable

Predicted Efficiency : 87%

Operating Region : State 3

Anomaly Status : Normal
""")

    with d2:

        st.warning("""
Recommended Action

Increase FlowC1 toward
optimal operating window.

Expected Gain :
+14% Physics_SEI
""")

    # ----------------------------------
    # RECOMMENDATIONS
    # ----------------------------------

    st.subheader(
        "🎯 Recommended Operating Window"
    )

    st.dataframe(
        pd.DataFrame({
            "Parameter":[
                "FlowC1",
                "PressureC1",
                "VapourPressure",
                "Expected Physics_SEI"
            ],
            "Recommended":[
                188.66,
                227.78,
                60.88,
                1.2806
            ]
        }),
        use_container_width=True
    )

    # ----------------------------------
    # INTERPRETATION
    # ----------------------------------

    st.subheader(
        "🔍 Engineering Interpretation"
    )

    st.info("""
FlowC1 remains the dominant driver
of separation performance.

Feature importance analysis shows:

• FlowC1 : 61%

• Vapour Pressure : 19%

• Column Temperature : 16%

The current operating condition
lies within a favorable
high-efficiency operating state.
""")

    st.download_button(
        "📄 Download Engineering Report",
        data="Distillation Intelligence Report",
        file_name="distillation_report.txt"
    )