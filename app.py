import streamlit as st
import joblib

rf_model = joblib.load("hospital_readmission_model.pkl")

st.title("🏥 AI-Based Hospital Readmission Prediction System")
st.write("Predicts whether a diabetic patient is at high or low risk of readmission.")

patient_name = st.text_input("Patient Name")
col1, col2 = st.columns(2)
with col1:
    age_ordinal = st.number_input("Age Ordinal", value=0)
    race_enc = st.number_input("Race Encoded", value=0)
    gender_enc = st.number_input("Gender Encoded", value=0)
    admission_type_id = st.number_input("Admission Type ID", value=0)
    discharge_disposition_id = st.number_input("Discharge Disposition ID", value=0)
    time_in_hospital = st.number_input("Time in Hospital", value=0)
    medical_specialty_enc = st.number_input("Medical Specialty Encoded", value=0)
    num_lab_procedures = st.number_input("Number of Lab Procedures", value=0)
    num_procedures = st.number_input("Number of Procedures", value=0)
    num_medications = st.number_input("Number of Medications", value=0)
    number_outpatient = st.number_input("Number of Outpatient Visits", value=0)
with col2:
    number_emergency = st.number_input("Number of Emergency Visits", value=0)
    number_inpatient = st.number_input("Number of Inpatient Visits", value=0)
    diag_1_enc = st.number_input("Diagnosis 1 Encoded", value=0)
    number_diagnoses = st.number_input("Number of Diagnoses", value=0)
    max_glu_serum_enc = st.number_input("Max Glucose Serum Encoded", value=0)
    A1Cresult_enc = st.number_input("A1C Result Encoded", value=0)
    change_enc = st.number_input("Change Encoded", value=0)
    diabetesMed_enc = st.number_input("Diabetes Medication Encoded", value=0)
    insulin_enc = st.number_input("Insulin Encoded", value=0)
    metformin_enc = st.number_input("Metformin Encoded", value=0)

if st.button("Predict"):
    patient_data = [[age_ordinal, race_enc, gender_enc, admission_type_id,
        discharge_disposition_id, time_in_hospital, medical_specialty_enc,
        num_lab_procedures, num_procedures, num_medications, number_outpatient,
        number_emergency, number_inpatient, diag_1_enc, number_diagnoses,
        max_glu_serum_enc, A1Cresult_enc, change_enc, diabetesMed_enc,
        insulin_enc, metformin_enc]]
    prediction = rf_model.predict(patient_data)[0]
    if prediction == 1:
        st.error(f"🔴 Patient: {patient_name}\n\nPrediction: High Risk of Readmission")
    else:
        st.success(f"🟢 Patient: {patient_name}\n\nPrediction: Low Risk of Readmission")
