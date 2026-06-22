import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Distillation Intelligence Platform",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODELS
# --------------------------------------------------

model = joblib.load("models/physics_sei_model.pkl")
anomaly_model = joblib.load("models/anomaly_detector.pkl")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 Distillation Intelligence Platform")
st.subheader("Physics-Informed AI for Distillation Optimization")

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------

st.sidebar.header("Operating Conditions")

FlowC1 = st.sidebar.number_input(
    "FlowC1",
    value=235.73
)

FlowC2 = st.sidebar.number_input(
    "FlowC2",
    value=65.25
)

FlowC3 = st.sidebar.number_input(
    "FlowC3",
    value=6.82
)

FlowC4 = st.sidebar.number_input(
    "FlowC4",
    value=6.41
)

PressureC1 = st.sidebar.number_input(
    "PressureC1",
    value=227.78
)

VapourPressure = st.sidebar.number_input(
    "VapourPressure",
    value=60.88
)

Column_Temp_Avg = st.sidebar.number_input(
    "Column_Temp_Avg",
    value=276.93
)

Column_Temp_Span = st.sidebar.number_input(
    "Column_Temp_Span",
    value=893.15
)

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

if st.sidebar.button("Predict Physics_SEI"):

    # ----------------------------------------------
    # INPUT DATAFRAME
    # ----------------------------------------------

    X = pd.DataFrame([{
        "FlowC1": FlowC1,
        "FlowC2": FlowC2,
        "FlowC3": FlowC3,
        "FlowC4": FlowC4,
        "PressureC1": PressureC1,
        "VapourPressure": VapourPressure,
        "Column_Temp_Avg": Column_Temp_Avg,
        "Column_Temp_Span": Column_Temp_Span
    }])

    # ----------------------------------------------
    # PREDICTION
    # ----------------------------------------------

    prediction = model.predict(X)[0]

    # ----------------------------------------------
    # ANOMALY DETECTION
    # ----------------------------------------------

    anomaly_features = pd.DataFrame([{
        "FlowC1": FlowC1,
        "PressureC1": PressureC1,
        "VapourPressure": VapourPressure,
        "Column_Temp_Avg": Column_Temp_Avg,
        "Physics_SEI": prediction
    }])

    anomaly = anomaly_model.predict(
        anomaly_features
    )[0]

    # ----------------------------------------------
    # KPI DASHBOARD
    # ----------------------------------------------

    health = min(prediction / 1.28, 1.0)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Physics_SEI",
            round(prediction, 4)
        )

    with col2:
        st.metric(
            "Health Score (%)",
            round(health * 100, 1)
        )

    with col3:
        st.metric(
            "Operating Status",
            "Optimal" if prediction > 1.0 else "Suboptimal"
        )

    # ----------------------------------------------
    # STATUS MESSAGE
    # ----------------------------------------------

    if prediction > 1.0:
        st.success(
            "🟢 Excellent Operating Region"
        )

    elif prediction > 0.7:
        st.info(
            "🟡 Good Operating Region"
        )

    else:
        st.warning(
            "🔴 Low Efficiency Region"
        )

    # ----------------------------------------------
    # ANOMALY MESSAGE
    # ----------------------------------------------

    if anomaly == -1:
        st.error(
            "⚠️ Potential Abnormal Operation Detected"
        )
    else:
        st.success(
            "✅ Normal Operating Condition"
        )

    st.divider()

    # ----------------------------------------------
    # RECOMMENDED SETTINGS
    # ----------------------------------------------

    st.subheader(
        "🎯 Recommended Operating Conditions"
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

    # ----------------------------------------------
    # EXECUTIVE SUMMARY
    # ----------------------------------------------

    st.subheader(
        "📋 Executive Summary"
    )

    improvement = (
        (1.2806 - prediction)
        / prediction
    ) * 100

    st.write(
        f"""
        Current predicted Physics_SEI:
        **{prediction:.4f}**

        Recommended operating regime:
        **1.2806**

        Potential efficiency improvement:
        **{improvement:.2f}%**
        """
    )

    # ----------------------------------------------
    # PROCESS INSIGHTS
    # ----------------------------------------------

    st.subheader(
        "🔍 Process Insights"
    )

    st.markdown("""
    - FlowC1 is the dominant driver of separation performance.
    - Vapour Pressure strongly influences column behavior.
    - Column Temperature impacts separation efficiency.
    - Pressure contributes secondary effects.
    """)

    # ----------------------------------------------
    # PROCESS HEALTH
    # ----------------------------------------------

    st.subheader(
        "🏭 Process Health"
    )

    st.progress(health)

    st.write(
        f"Current Process Health: {health*100:.1f}%"
    )

    # ----------------------------------------------
    # REPORT GENERATION
    # ----------------------------------------------

    report_text = f"""
DISTILLATION INTELLIGENCE REPORT

Predicted Physics_SEI : {prediction:.4f}

Health Score : {health*100:.1f}%

Status :
{"Optimal" if prediction > 1.0 else "Suboptimal"}

Recommended Physics_SEI :
1.2806

Potential Improvement :
{improvement:.2f}%
"""

    st.download_button(
        "📄 Download Report",
        report_text,
        file_name="distillation_report.txt"
    )

# --------------------------------------------------
# BATCH PREDICTION
# --------------------------------------------------

st.sidebar.divider()

uploaded_file = st.sidebar.file_uploader(
    "Upload Distillation CSV",
    type=["csv"]
)

if uploaded_file:

    df_upload = pd.read_csv(uploaded_file)

    st.subheader(
        "📂 Uploaded Dataset"
    )

    st.dataframe(
        df_upload.head(),
        use_container_width=True
    )

    required_cols = [
        "FlowC1",
        "FlowC2",
        "FlowC3",
        "FlowC4",
        "PressureC1",
        "VapourPressure",
        "Column_Temp_Avg",
        "Column_Temp_Span"
    ]

    if all(
        col in df_upload.columns
        for col in required_cols
    ):

        df_upload[
            "Predicted_Physics_SEI"
        ] = model.predict(
            df_upload[required_cols]
        )

        st.subheader(
            "📈 Batch Prediction Results"
        )

        st.dataframe(
            df_upload.head(),
            use_container_width=True
        )

    else:
        st.error(
            "Required columns missing in uploaded file."
        )