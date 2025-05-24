import streamlit as st
import pandas as pd
import joblib

# --- PEMETAAN KODE KE TEKS (BERDASARKAN DESKRIPSI) ---
# Ini akan digunakan untuk membuat menu dropdown yang ramah pengguna.
yes_no_map = {'Yes': 1, 'No': 0}
marital_status_map = {'Single': 1, 'Married': 2, 'Widower': 3, 'Divorced': 4, 'Facto Union': 5, 'Legally Separated': 6}
application_mode_map = {
    '1st phase - general contingent': 1, 'Ordinance No. 612/93': 2, '1st phase - special contingent (Azores Island)': 5,
    'Holders of other higher courses': 7, 'Ordinance No. 854-B/99': 10, 'International student (bachelor)': 15,
    '1st phase - special contingent (Madeira Island)': 16, '2nd phase - general contingent': 17, '3rd phase - general contingent': 18,
    'Ordinance No. 533-A/99, item b2) (Different Plan)': 26, 'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
    'Over 23 years old': 39, 'Transfer': 42, 'Change of course': 43, 'Technological specialization diploma holders': 44,
    'Change of institution/course': 51, 'Short cycle diploma holders': 53, 'Change of institution/course (International)': 57
}
course_map = {
    'Biofuel Production Technologies': 33, 'Animation and Multimedia Design': 171, 'Social Service (evening attendance)': 8014,
    'Agronomy': 9003, 'Communication Design': 9070, 'Veterinary Nursing': 9085, 'Informatics Engineering': 9119,
    'Equinculture': 9130, 'Management': 9147, 'Social Service': 9238, 'Tourism': 9254, 'Nursing': 9500,
    'Oral Hygiene': 9556, 'Advertising and Marketing Management': 9670, 'Journalism and Communication': 9773,
    'Basic Education': 9853, 'Management (evening attendance)': 9991
}
prev_qual_map = {
    'Secondary education': 1, "Higher education - bachelor's degree": 2, 'Higher education - degree': 3,
    "Higher education - master's": 4, 'Higher education - doctorate': 5, 'Frequency of higher education': 6,
    '12th year of schooling - not completed': 9, '11th year of schooling - not completed': 10,
    'Other - 11th year of schooling': 12, '10th year of schooling': 14, '10th year of schooling - not completed': 15,
    'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 19, 'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 38,
    'Technological specialization course': 39, 'Higher education - degree (1st cycle)': 40,
    'Professional higher technical course': 42, 'Higher education - master (2nd cycle)': 43
}
nationality_map = {
    'Portuguese': 1, 'German': 2, 'Spanish': 6, 'Italian': 11, 'Dutch': 13, 'English': 14, 'Lithuanian': 17,
    'Angolan': 21, 'Cape Verdean': 22, 'Guinean': 24, 'Mozambican': 25, 'Santomean': 26, 'Turkish': 32,
    'Brazilian': 41, 'Romanian': 62, 'Moldova (Republic of)': 100, 'Mexican': 101, 'Ukrainian': 103,
    'Russian': 105, 'Cuban': 108, 'Colombian': 109
}

# --- FUNGSI LOAD MODEL ---
@st.cache_data
def load_artifacts():
    model = joblib.load('model/dropout_model.joblib')
    scaler = joblib.load('model/scaler.joblib')
    feature_order = joblib.load('model/feature_order.joblib')
    return model, scaler, feature_order

try:
    model, scaler, feature_order = load_artifacts()
except FileNotFoundError:
    st.error("Failed to load model files. Make sure 'dropout_model.joblib', 'scaler.joblib', and 'feature_order.joblib' are in the 'model' folder.")
    st.stop()

# --- ANTARMUKA STREAMLIT ---
st.set_page_config(page_title="Student Status Prediction", layout="wide")
st.title('🎓 Student Graduation Status Prediction Prototype')
st.write("This application predicts a student's graduation status. Please fill out the form below with the relevant data.")

# --- FORM INPUT (LABEL YANG SUDAH DIRAPIKAN) ---
with st.form("prediction_form"):
    
    st.header("Personal & Application Information")
    marital_status_sel = st.selectbox('Marital Status', options=list(marital_status_map.keys()))
    gender_sel = st.selectbox('Gender', options=['Male', 'Female'])
    displaced_sel = st.selectbox('Displaced', options=list(yes_no_map.keys()))
    age_at_enrollment = st.number_input('Age At Enrollment', min_value=17, max_value=70, value=19)
    nationality_sel = st.selectbox('Nacionality', options=list(nationality_map.keys()))
    international_sel = st.selectbox('International', options=list(yes_no_map.keys()))
    debtor_sel = st.selectbox('Debtor', options=list(yes_no_map.keys()))
    tuition_fees_up_to_date_sel = st.selectbox('Tuition Fees Up To Date', options=list(yes_no_map.keys()))
    scholarship_holder_sel = st.selectbox('Scholarship Holder', options=list(yes_no_map.keys()))
    educational_special_needs_sel = st.selectbox('Educational Special Needs', options=list(yes_no_map.keys()))

    st.header("Academic & Qualification Information")
    application_mode_sel = st.selectbox('Application Mode', options=list(application_mode_map.keys()))
    application_order = st.number_input('Application Order', min_value=0, max_value=9, value=1)
    course_sel = st.selectbox('Course', options=list(course_map.keys()))
    prev_qual_sel = st.selectbox('Previous Qualification', options=list(prev_qual_map.keys()))
    previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=120.0, step=0.1)
    admission_grade = st.number_input('Admission Grade', min_value=0.0, max_value=200.0, value=120.0, step=0.1)
    daytime_evening_attendance_sel = st.selectbox('Daytime Evening Attendance', options=['Daytime', 'Evening'])
    
    st.subheader("Parents' Qualification & Occupation")
    mothers_qualification = st.number_input("Mothers Qualification", min_value=1, max_value=44, value=37)
    fathers_qualification = st.number_input("Fathers Qualification", min_value=1, max_value=44, value=38)
    mothers_occupation = st.number_input("Mothers Occupation", min_value=0, max_value=194, value=9)
    fathers_occupation = st.number_input("Fathers Occupation", min_value=0, max_value=195, value=9)

    st.header("Curricular & Economic Data")
    st.subheader("1st Semester")
    curricular_units_1st_sem_credited = st.number_input('Curricular Units 1st Sem Credited', min_value=0, value=0)
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0, value=6)
    curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', min_value=0, value=6)
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0, value=6)
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0.0, max_value=20.0, value=13.0, step=0.1)
    curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Sem Without Evaluations', min_value=0, value=0)
    
    st.subheader("2nd Semester")
    curricular_units_2nd_sem_credited = st.number_input('Curricular Units 2nd Sem Credited', min_value=0, value=0)
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0, value=6)
    curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', min_value=0, value=6)
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0, value=6)
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0.0, max_value=20.0, value=13.0, step=0.1)
    curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Sem Without Evaluations', min_value=0, value=0)
    
    st.subheader("Macroeconomic Indicators")
    unemployment_rate = st.number_input('Unemployment Rate', value=12.4, step=0.1)
    inflation_rate = st.number_input('Inflation Rate', value=1.2, step=0.1)
    gdp = st.number_input('GDP', value=0.32, step=0.01)

    submit_button = st.form_submit_button(label='Predict Status')

# --- LOGIKA PREDIKSI ---
if submit_button:
    # (Logika di bagian ini tidak ada yang diubah, tetap sama seperti sebelumnya)
    marital_status = marital_status_map[marital_status_sel]
    gender = 1 if gender_sel == 'Male' else 0
    displaced = yes_no_map[displaced_sel]
    nationality = nationality_map[nationality_sel]
    international = yes_no_map[international_sel]
    debtor = yes_no_map[debtor_sel]
    tuition_fees_up_to_date = yes_no_map[tuition_fees_up_to_date_sel]
    scholarship_holder = yes_no_map[scholarship_holder_sel]
    educational_special_needs = yes_no_map[educational_special_needs_sel]
    application_mode = application_mode_map[application_mode_sel]
    course = course_map[course_sel]
    previous_qualification = prev_qual_map[prev_qual_sel]
    daytime_evening_attendance = 1 if daytime_evening_attendance_sel == 'Daytime' else 0
    
    input_dict = {
        'Marital_status': marital_status, 'Application_mode': application_mode, 'Application_order': application_order, 'Course': course,
        'Daytime_evening_attendance': daytime_evening_attendance, 'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_qualification_grade, 'Nacionality': nationality, 'Mothers_qualification': mothers_qualification,
        'Fathers_qualification': fathers_qualification, 'Mothers_occupation': mothers_occupation, 'Fathers_occupation': fathers_occupation,
        'Admission_grade': admission_grade, 'Displaced': displaced, 'Educational_special_needs': educational_special_needs, 'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date, 'Gender': gender, 'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment, 'International': international, 'Curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled, 'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved, 'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations, 'Curricular_units_2nd_sem_credited': curricular_units_2nd_sem_credited,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled, 'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved, 'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations, 'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate, 'GDP': gdp
    }
    
    input_df = pd.DataFrame([input_dict])
    # Pastikan nama kolom di input_dict sama persis dengan yang ada di feature_order
    input_df = input_df[feature_order] 
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)
    
    status_mapping = {0: 'Dropout', 1: 'Graduate', 2: 'Enrolled'}
    predicted_status = status_mapping.get(prediction[0], "Unknown")

    st.header('Prediction Result')
    if predicted_status == 'Dropout':
        st.error(f'**Predicted Status: {predicted_status}**')
    elif predicted_status == 'Graduate':
        st.success(f'**Predicted Status: {predicted_status}**')
    else:
        st.info(f'**Predicted Status: {predicted_status}**')

    st.write('**Probability for each status:**')
    proba_df = pd.DataFrame(prediction_proba, columns=[status_mapping[i] for i in model.classes_])
    st.dataframe(proba_df.style.format("{:.2%}"))