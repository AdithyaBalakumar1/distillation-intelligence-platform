import streamlit as st

st.set_page_config(
    page_title="Distillation Intelligence Platform",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.big-title {
    text-align:center;
    color:#00E5FF;
    font-size:50px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    font-size:22px;
    color:white;
}

.card {
    background-color:#1E293B;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# HERO SECTION
# --------------------------

st.markdown(
    '<p class="big-title">🚀 Distillation Intelligence Platform</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Physics-Informed AI for Process Monitoring, Optimization & Digital Twin Analytics</p>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------
# KPI CARDS
# --------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Models", "2")

with col2:
    st.metric("Modules", "6")

with col3:
    st.metric("Platform", "Online")

with col4:
    st.metric("Version", "1.0")

st.divider()

# --------------------------
# PLATFORM OVERVIEW
# --------------------------

st.subheader("Platform Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.success("📈 Physics_SEI Prediction")
    st.success("⚠️ Anomaly Detection")
    st.success("🎯 Process Optimization")

with col2:
    st.success("🧪 Digital Twin")
    st.success("📊 Trend Analytics")
    st.success("📄 Engineering Reports")

st.divider()

# --------------------------
# ARCHITECTURE
# --------------------------

st.subheader("System Architecture")

st.code("""
Plant Data
     ↓
Feature Engineering
     ↓
Physics_SEI
     ↓
Machine Learning
     ↓
Optimization Engine
     ↓
Digital Twin
     ↓
Engineering Dashboard
""")

st.success("✅ Platform Ready for Deployment")