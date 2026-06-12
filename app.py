import streamlit as st
import joblib

from utils import *

with open(".\outputs\model.pkl", "rb") as f:
    model = joblib.load(f)

from predictor import (
    analyze_antibody
)

st.set_page_config(
    page_title=
    "Antibody Humanization Predictor",
    layout="centered"
)

st.title(
    "🧬 Antibody Humanization Predictor"
)

st.write(
    """
    Enter an antibody amino-acid sequence
    to estimate its human-likeness.
    """
)

sequence = st.text_area(
    "Paste Antibody Sequence"
)

if st.button("Analyze"):

    result = analyze_antibody(
        sequence
    )

    if "error" in result:

        st.error(
            result["error"]
        )

    else:

        st.metric(
            "Human-Likeness Score",
            f"{result['score']}%"
        )

        st.success(
            result["category"]
        )

        st.info(
            f"Confidence: "
            f"{result['confidence']}"
        )

#Step 3: Sidebar Navigation
page = st.sidebar.radio(
    "Select Module",
    [
        "Humanization Score",
        "Region Analysis",
        "Research Findings"
    ]
)

#Module 1: Humanization Score
if page == "Humanization Score":

    seq = st.text_area(
        "Enter Antibody Sequence"
    )

    if st.button("Predict"):

        score = humanization_score(
            seq,
            model
        )

        st.metric(
            "Humanization Score",
            f"{score:.3f}"
        )

#Module 2: Region Analysis
if page == "Region Analysis":

    seq = st.text_area(
        "Sequence"
    )

    if st.button("Analyze Regions"):

        regions = get_regions(seq)

        for k,v in regions.items():

            st.write(
                f"**{k}** : {v}"
            )

#Module 3: Research Findings
st.subheader(
    "Framework Region Performance"
)
import pandas as pd

results = pd.DataFrame({
    "Region":[
        "FR1",
        "FR3",
        "FR4",
        "FR2"
    ],
    "Accuracy":[
        96.75,
        94.00,
        91.25,
        91.00
    ]
})

st.bar_chart(
    results.set_index("Region")
)
st.markdown("""
### Key Findings

- Full Model: 98.25%
- Framework Only: 96.50%
- CDR Only: 79.50%

FR1 is the strongest framework region.

Key hotspot positions:
12, 14, 19, 20, 21
""")
report_text = """
Antibody Humanization Report

Full Model Accuracy: 98.25%
Framework Only Accuracy: 96.50%
CDR Only Accuracy: 79.50%

Top FR1 Hotspots:
12
14
19
20
21
"""
st.download_button(
    "Download Humanization Report",
    report_text,
    file_name="humanization_report.txt"
)

