# 🧬 Antibody Humanization Platform

An end-to-end computational immunology platform for antibody humanization prediction and framework region analysis.

This project combines machine learning, antibody sequence analysis, and immunoinformatics to identify humanization signals in antibody sequences and recommend potential humanization mutations.

---

## 🚀 Features

### 1. Humanization Prediction
- Predicts whether an antibody sequence is human-like or non-human.
- Built using a Random Forest classifier.
- Achieved **98.25% accuracy** on the evaluation dataset.

### 2. Region Analysis
Automatically extracts:

- FR1
- CDR1
- FR2
- CDR2
- FR3
- CDR3
- FR4

using IMGT antibody numbering.

### 3. Framework vs CDR Analysis
Determines which antibody regions contribute most to humanization prediction.

### 4. Hotspot Discovery
Identifies important framework positions associated with species-specific signatures.

### 5. Interactive Streamlit App
Provides:
- Humanization scoring
- Region extraction
- Research findings visualization

---

# 📊 Results

## Model Performance

| Model | Accuracy |
|---------|---------:|
| Full Sequence | 98.25% |
| Framework Only | 96.50% |
| CDR Only | 79.50% |

### Key Finding

Framework regions contain the majority of the humanization signal.

---

## Framework Region Analysis

| Region | Accuracy |
|---------|---------:|
| FR1 | 96.75% |
| FR3 | 94.00% |
| FR4 | 91.25% |
| FR2 | 91.00% |

### Key Finding

FR1 alone captures nearly all predictive power of the complete sequence model.

---

## Important FR1 Hotspots

The following positions were identified as highly informative:

| Position | Importance |
|-----------|-----------:|
| 19 | 0.186 |
| 14 | 0.168 |
| 20 | 0.138 |
| 21 | 0.089 |
| 12 | 0.072 |

### Example Species-Specific Patterns

| Position | Human | Non-Human |
|-----------|---------|-----------|
| 14 | T | G |
| 12 | T | Q |
| 20 | S | C |
| 21 | C | A |

These positions form the basis of the mutation recommendation engine.

---

# 🏗 Project Pipeline

```text
Antibody Sequence
        ↓
Feature Extraction
        ↓
Random Forest Classifier
        ↓
Humanization Score
        ↓
Framework Analysis
        ↓
FR1 Hotspot Discovery
```

---

# 📁 Project Structure

```text
IGEM PROJECT/

├── datasets/
│   ├── IGHV.fasta
│   ├── *.csv.gz
│
├── outputs/
│   ├── antibody_humanization_dataset.csv
│   ├── cdr_framework_analysis.csv
│   ├── humanization_scores.csv
│   ├── sequence_features.csv
│   ├── model.pkl
│   └── feature_columns.pkl
│
├── 01_Humanization_Classifier.ipynb
├── 02_CDR_Framework_Analysis.ipynb
│
├── app.py
├── predictor.py
├── utils.py
│
├── requirements.txt
└── README.md
```

---

# 🧪 Notebooks

## Notebook 1 – Humanization Classifier

- Dataset preparation
- Feature engineering
- Random Forest training
- Humanization score generation

Outputs:

```text
model.pkl
feature_columns.pkl
humanization_scores.csv
```

---

## Notebook 2 – CDR vs Framework Analysis

- IMGT numbering
- Region extraction
- CDR vs Framework comparison
- Framework region ranking
- Hotspot discovery

Outputs:

```text
cdr_framework_analysis.csv
```

---


# 💻 Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/antibody-humanization-platform.git

cd antibody-humanization-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📚 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- AbNumber
- IMGT Numbering
- Matplotlib
- Seaborn

---

# 🔬 Biological Significance

Antibody humanization is a critical step in therapeutic antibody development.

This project demonstrates that:

- Framework regions contribute more strongly to humanization than CDRs.
- FR1 contains highly informative species-specific signatures.
- Machine learning can identify potential humanization hotspots.

---

# 🎯 Future Work

- Mutation Suggestion from Hotspots
- AntiBERTa embeddings
- ESM2 protein language models
- Structural validation with ColabFold
- Developability prediction
- Immunogenicity prediction
- Therapeutic antibody optimization

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Shreshth Srinivas**

Computational Biology | Bioinformatics | Machine Learning | Immunology
