from collections import Counter
import pandas as pd
import joblib

model = joblib.load(".\outputs\model.pkl")

AMINO_ACIDS = list(
    "ACDEFGHIKLMNPQRSTVWY"
)

VALID_AA = set(
    "ACDEFGHIKLMNPQRSTVWY"
)

def validate_sequence(seq):

    seq = seq.upper().strip()

    if len(seq) < 80:
        return False, "Sequence too short"

    if not set(seq).issubset(VALID_AA):
        return False, "Invalid amino acids"

    return True, "Valid"


def sequence_to_features(seq):

    counts = Counter(seq)

    length = len(seq)

    return pd.DataFrame([{
        aa: counts.get(aa, 0)/length
        for aa in AMINO_ACIDS
    }])


def get_category(score):

    if score >= 90:
        return "Highly Human-Like"

    elif score >= 70:
        return "Moderately Human-Like"

    elif score >= 40:
        return "Partially Humanized"

    return "Non-Human"


def get_confidence(score):

    distance = abs(score - 50)

    if distance >= 40:
        return "Very High"

    elif distance >= 25:
        return "High"

    elif distance >= 10:
        return "Moderate"

    return "Low"


def analyze_antibody(sequence):

    valid, msg = validate_sequence(
        sequence
    )

    if not valid:

        return {
            "error": msg
        }

    feat = sequence_to_features(
        sequence
    )

    score = (
        model.predict_proba(
            feat
        )[0][1] * 100
    )

    return {

        "score":
            round(score,2),

        "category":
            get_category(score),

        "confidence":
            get_confidence(score)
    }