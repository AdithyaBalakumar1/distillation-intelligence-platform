import streamlit as st

st.title("⚠️ Anomaly Monitor")

status = st.selectbox(
    "Current Status",
    [
        "Normal",
        "Warning",
        "Critical"
    ]
)

if status == "Normal":
    st.success(
        "✅ System Operating Normally"
    )

elif status == "Warning":
    st.warning(
        "⚠️ Potential Process Deviation"
    )

else:
    st.error(
        "🚨 Critical Process Condition"
    )

st.subheader("Likely Causes")

st.markdown("""
- Flow imbalance
- Pressure deviation
- Temperature instability
- Vapour pressure fluctuation
""")