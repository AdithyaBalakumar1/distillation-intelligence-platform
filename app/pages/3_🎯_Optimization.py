import streamlit as st
import pandas as pd

st.title("🎯 Process Optimization")

st.subheader(
    "AI Recommended Operating Conditions"
)

recommended = pd.DataFrame([{
    "FlowC1": 188.66,
    "FlowC2": 65.25,
    "FlowC3": 6.82,
    "FlowC4": 6.41,
    "PressureC1": 227.78,
    "VapourPressure": 60.88,
    "Column_Temp_Avg": 276.93,
    "Column_Temp_Span": 893.15,
    "Expected_Physics_SEI": 1.2806
}])

st.dataframe(
    recommended,
    use_container_width=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Expected Physics_SEI",
        "1.2806"
    )

with col2:
    st.metric(
        "Process Health",
        "100%"
    )

with col3:
    st.metric(
        "Operating Region",
        "Optimal"
    )

st.success(
    "Recommended operating regime identified from optimization analysis."
)

st.subheader("📋 Operator Actions")

st.markdown("""
- Maintain FlowC1 near 188.66
- Maintain stable Vapour Pressure
- Avoid excessive temperature fluctuations
- Operate within recommended pressure window
- Monitor Physics_SEI continuously
""")