import streamlit as st

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