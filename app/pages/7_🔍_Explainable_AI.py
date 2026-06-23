import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Explainable AI",
    page_icon="🔍",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🔍 Explainable AI Engine")
st.caption(
    "Understanding the Physics-Informed Machine Learning Model"
)

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

st.success("""
### Why Explainable AI?

Industrial engineers need to understand WHY a prediction was made.

This module translates machine learning outputs into
engineering insights that can support process decisions.
""")

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.subheader("📊 Feature Importance Analysis")

importance_df = pd.DataFrame({
    "Feature": [
        "FlowC1",
        "Vapour Pressure",
        "Column Temperature",
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
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Model Feature Importance"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# DRIVER ANALYSIS
# --------------------------------------------------

st.subheader("⚙️ Process Driver Analysis")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Primary Driver",
        "FlowC1"
    )

with c2:
    st.metric(
        "Influence",
        "61%"
    )

with c3:
    st.metric(
        "Impact",
        "High"
    )

# --------------------------------------------------
# ENGINEERING INTERPRETATION
# --------------------------------------------------

st.subheader("🧪 Engineering Interpretation")

st.info("""
FlowC1 is the dominant process variable affecting
Physics_SEI and overall separation efficiency.

Vapour pressure contributes significantly by
influencing phase equilibrium behaviour.

Column temperature provides secondary influence
through its effect on relative volatility.

Pressure contributes minimally under the current
operating window.
""")

# --------------------------------------------------
# WHAT-IF ANALYSIS
# --------------------------------------------------

st.subheader("🔮 What-If Scenario Analysis")

scenario_df = pd.DataFrame({
    "Scenario": [
        "Increase FlowC1 by 10%",
        "Decrease FlowC1 by 10%",
        "Increase Vapour Pressure by 10%",
        "Decrease Vapour Pressure by 10%"
    ],
    "Expected Effect": [
        "Increase Physics_SEI",
        "Decrease Physics_SEI",
        "Moderate Improvement",
        "Performance Reduction"
    ]
})

st.dataframe(
    scenario_df,
    use_container_width=True
)

# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------

st.subheader("📄 Executive Summary")

st.success("""
Key Findings

• FlowC1 is the most influential variable.

• Vapour pressure is the second most important driver.

• Column temperature has moderate impact.

• The model is interpretable and aligns with
  process-engineering expectations.

• Results support the use of Physics-Informed
  Machine Learning for distillation optimization.
""")