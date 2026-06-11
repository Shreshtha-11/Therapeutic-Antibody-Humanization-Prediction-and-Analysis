#Feature Extraction
AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

def extract_features(seq):

    return {
        aa: seq.count(aa)/len(seq)
        for aa in AMINO_ACIDS
    }

#Humanization Score
import pandas as pd

def humanization_score(seq, model):

    X = pd.DataFrame(
        [extract_features(seq)]
    )

    return model.predict_proba(X)[0][1]

#Region Extraction
from abnumber import Chain

def get_regions(seq):

    chain = Chain(
        seq,
        scheme="imgt"
    )

    return {
        "FR1": str(chain.fr1_seq),
        "CDR1": str(chain.cdr1_seq),

        "FR2": str(chain.fr2_seq),
        "CDR2": str(chain.cdr2_seq),

        "FR3": str(chain.fr3_seq),
        "CDR3": str(chain.cdr3_seq),

        "FR4": str(chain.fr4_seq)
    }


