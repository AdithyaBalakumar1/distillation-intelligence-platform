import streamlit as st

st.set_page_config(
    page_title="Distillation Intelligence Platform",
    layout="wide"
)

st.title("🚀 Distillation Intelligence Platform")

st.markdown("""
### Physics-Informed AI for Distillation Operations

This platform provides:

- 📈 Physics_SEI Prediction
- ⚠️ Anomaly Detection
- 🎯 Process Optimization
- 📊 Trend Analytics
- 📄 Engineering Reports

Use the navigation panel on the left.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Models", "2")

with col2:
    st.metric("Analytics Modules", "5")

with col3:
    st.metric("Platform Status", "Online")