%%writefile README.md
# Hospital Readmission Prediction App

Predicts whether a diabetic patient is at high or low risk of hospital
readmission within 30 days of discharge, using clinical data.

## About

This project uses the real **UCI "Diabetes 130-US Hospitals for years
1999-2008"** dataset (Strack et al., 2014) — 101,766 hospital encounters
from 130 US hospitals. A Random Forest classifier was trained on the
data and deployed as an interactive Streamlit app.

## Features

- Takes 21 clinical inputs (age, race, admission type, lab procedures,
  medications, diagnoses, etc.)
- Predicts readmission risk (High / Low) for a named patient
- Simple web interface, no coding required to use

## Tech Stack

- Python
- scikit-learn (Random Forest)
- Streamlit (web interface)
- joblib (model serialization)

## Running Locally

\`\`\`bash
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Dataset & Citation

Strack, B., DeShazo, J.P., Gennings, C., et al. (2014). *Impact of
HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000
Clinical Database Patient Records.* BioMed Research International.

## Disclaimer

This is a student/internship project for educational purposes only —
not intended for real clinical use.
