import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Distillation Intelligence Platform",
    page_icon="🏭",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Background */

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #111827 50%,
        #1E293B 100%
    );
}

/* Hero Title */

.big-title {
    text-align:center;
    font-size:64px;
    font-weight:800;

    background: linear-gradient(
        90deg,
        #38BDF8,
        #22D3EE,
        #10B981
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* Subtitle */

.subtitle {
    text-align:center;
    color:#CBD5E1;
    font-size:22px;
    margin-bottom:20px;
}

/* Glass Card */

.glass {
    background: rgba(
        255,
        255,
        255,
        0.05
    );

    backdrop-filter: blur(12px);

    border-radius:20px;

    padding:30px;

    border:1px solid rgba(
        255,
        255,
        255,
        0.1
    );

    box-shadow:
        0 8px 32px rgba(
            0,
            0,
            0,
            0.35
        );
}

/* Section Header */

.section-header {

    color:#38BDF8;

    font-size:32px;

    font-weight:700;

    margin-top:20px;

    margin-bottom:10px;
}

/* Badge */

.badge {

    background:#10B981;

    color:white;

    padding:10px 25px;

    border-radius:50px;

    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="glass">

<p class="big-title">
🏭 Distillation Intelligence Platform
</p>

<p class="subtitle">
Physics-Informed Process Analytics,
Optimization & Digital Twin Intelligence
</p>

<center>
<span class="badge">
Optimal Operating State Identified
</span>
</center>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# EXECUTIVE DASHBOARD
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Executive Dashboard</p>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Model Accuracy",
        "95.6%"
    )

with col2:
    st.metric(
        "Operating States",
        "4"
    )

with col3:
    st.metric(
        "Best State",
        "State 3"
    )

with col4:
    st.metric(
        "Physics_SEI",
        "0.813"
    )

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Project Overview</p>',
    unsafe_allow_html=True
)

st.info("""
This platform combines chemical engineering principles,
physics-informed feature engineering, machine learning,
optimization and digital twin technologies to identify
high-efficiency operating regions in a distillation column.

The objective is to move beyond black-box prediction and
develop interpretable process intelligence for industrial
decision support.
""")

# --------------------------------------------------
# RESEARCH CONTRIBUTIONS
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Research Contributions</p>',
    unsafe_allow_html=True
)

st.success("""
✅ Physics-Informed Feature Engineering

✅ Relative Volatility Proxy Development

✅ Separation Efficiency Index (SEI)

✅ Physics_SEI Formulation

✅ Operating State Discovery using K-Means

✅ Random Forest Process Modeling

✅ Digital Twin Simulation

✅ Explainable AI Analysis

✅ Process Optimization Framework
""")

# --------------------------------------------------
# KEY ENGINEERING FINDINGS
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Key Engineering Findings</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.success("""
    🎯 Optimal Operating Window

    FlowC1 = 235.73

    PressureC1 = 231.57

    Vapour Pressure = 44.56

    Avg Temperature = 296.02

    Physics_SEI = 0.813
    """)

with col2:

    st.warning("""
    🔍 Process Insight

    FlowC1 contributed

    61%

    of total predictive influence.

    Vapour Pressure and
    Column Temperature
    were the next most
    influential variables.
    """)

# --------------------------------------------------
# RECOMMENDED OPERATING CONDITIONS
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Recommended Operating Conditions</p>',
    unsafe_allow_html=True
)

recommended_df = pd.DataFrame({

    "Parameter":[
        "FlowC1",
        "PressureC1",
        "VapourPressure",
        "Column_Temp_Avg",
        "Physics_SEI"
    ],

    "Optimal Value":[
        235.73,
        231.57,
        44.56,
        296.02,
        0.813
    ]
})

st.dataframe(
    recommended_df,
    use_container_width=True
)

# --------------------------------------------------
# PLATFORM CAPABILITIES
# --------------------------------------------------

st.markdown(
    '<p class="section-header">Platform Modules</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.success("📈 Physics_SEI Prediction")

    st.success("⚠️ Anomaly Detection")

    st.success("🎯 Process Optimization")

with col2:

    st.success("🧪 Digital Twin")

    st.success("📊 Trend Analytics")

    st.success("📄 Engineering Reports")

# --------------------------------------------------
# SYSTEM WORKFLOW
# --------------------------------------------------

st.markdown(
    '<p class="section-header">System Workflow</p>',
    unsafe_allow_html=True
)

st.code("""
Plant Data
      ↓
Feature Engineering
      ↓
Physics_SEI
      ↓
Operating State Discovery
      ↓
Machine Learning
      ↓
Optimization Engine
      ↓
Digital Twin
      ↓
Decision Support Dashboard
""")

# --------------------------------------------------
# PROJECT STATUS
# --------------------------------------------------

st.success(
    "✅ Platform Ready for Demonstration"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
"""
Physics-Informed Machine Learning Framework for
Distillation Column Analytics, Operating State
Discovery, Process Optimization and Digital Twin
Applications.
"""
)