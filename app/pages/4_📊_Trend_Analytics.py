import streamlit as st
import pandas as pd

st.title("📊 Trend Analytics")

uploaded_file = st.file_uploader(
    "Upload Distillation Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if "FlowC1" in df.columns:
        st.subheader("FlowC1 Trend")
        st.line_chart(df["FlowC1"])

    if "PressureC1" in df.columns:
        st.subheader("Pressure Trend")
        st.line_chart(df["PressureC1"])

    if "VapourPressure" in df.columns:
        st.subheader("Vapour Pressure Trend")
        st.line_chart(df["VapourPressure"])