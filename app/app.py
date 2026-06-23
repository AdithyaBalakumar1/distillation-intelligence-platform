# Replace your current app.py with this file
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Distillation Intelligence Platform", page_icon="🏭", layout="wide")

st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#0f172a,#111827,#1e293b);}
.hero{padding:35px;border-radius:25px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);}
.big{font-size:58px;font-weight:800;text-align:center;color:#38BDF8;}
.sub{text-align:center;font-size:22px;color:#CBD5E1;}
.section{font-size:30px;font-weight:700;color:#38BDF8;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><div class="big">🏭 Distillation Intelligence Platform</div><div class="sub">Physics‑Informed AI • Optimization • Explainable Analytics • Digital Twin</div></div>', unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)
c1.metric("Model Accuracy","95.6%")
c2.metric("Operating States","4")
c3.metric("Best State","State 3")
c4.metric("Physics_SEI","0.813")

st.markdown('<div class="section">Executive Summary</div>', unsafe_allow_html=True)

l,r=st.columns(2)

with l:
    fig=go.Figure(go.Indicator(mode="gauge+number",value=81.3,title={"text":"Process Intelligence Score"},gauge={"axis":{"range":[0,100]}}))
    st.plotly_chart(fig,use_container_width=True)

with r:
    imp=pd.DataFrame({"Feature":["FlowC1","Vapour Pressure","Column Temp Avg","Pressure","Others"],"Importance":[61,19,16,1,3]})
    fig2=px.bar(imp,x="Importance",y="Feature",orientation="h",title="Feature Importance")
    fig2.update_layout(template="plotly_dark")
    st.plotly_chart(fig2,use_container_width=True)

st.markdown('<div class="section">Optimal Operating Window</div>', unsafe_allow_html=True)
st.dataframe(pd.DataFrame({"Parameter":["FlowC1","PressureC1","VapourPressure","Column_Temp_Avg","Physics_SEI"],"Optimal Value":[235.73,231.57,44.56,296.02,0.813]}),use_container_width=True)

st.markdown('<div class="section">System Workflow</div>', unsafe_allow_html=True)
a,b,c,d,e,f=st.columns(6)
a.info("📡 Plant Data")
b.info("⚙ Features")
c.info("🧠 ML")
d.info("🎯 Optimization")
e.info("🧪 Digital Twin")
f.info("📊 Decision Support")

