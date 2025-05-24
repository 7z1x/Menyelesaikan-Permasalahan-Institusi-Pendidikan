import joblib 
import pandas as pd
import warnings

# Abaikan warning yang mungkin muncul
warnings.filterwarnings('ignore')

# --- KONFIGURASI ---
# Muat semua file yang sudah diekspor
try:
    model = joblib.load('model/dropout_model.joblib')
    scaler = joblib.load('model/scaler.joblib')
    feature_order = joblib.load('model/feature_order.joblib')
except FileNotFoundError:
    print("Error: Pastikan file 'dropout_model.joblib', 'scaler.joblib', dan 'feature_order.joblib' ada di folder yang sama.")
    exit()

# Mapping hasil prediksi (sesuai dengan yang Anda buat di notebook)
# 0 = Bukan Dropout, 1 = Dropout
LABEL_MAPPING = {
    0: 'Bukan Dropout',
    1: 'Dropout'
}

def predict_dropout(student_data):
    """
    Fungsi untuk memprediksi status dropout dari data mahasiswa baru.
    Input: sebuah dictionary berisi data mahasiswa.
    Output: dictionary berisi label prediksi dan probabilitasnya.
    """
    # 1. Konversi data input menjadi DataFrame
    df_new = pd.DataFrame([student_data])

    # 2. Pastikan urutan kolom sesuai dengan saat training
    df_new = df_new[feature_order]

    # 3. Lakukan scaling pada data baru
    scaled_data = scaler.transform(df_new)

    # 4. Lakukan prediksi
    prediction_numeric = model.predict(scaled_data)[0]
    prediction_proba = model.predict_proba(scaled_data)[0]

    # 5. Terjemahkan hasil ke label
    prediction_label = LABEL_MAPPING[prediction_numeric]

    # 6. Buat dictionary probabilitas
    probabilities = {
        'Bukan Dropout': prediction_proba[0],
        'Dropout': prediction_proba[1]
    }

    return {
        'prediksi': prediction_label,
        'probabilitas': probabilities
    }

# --- CONTOH PENGGUNAAN ---
if __name__ == "__main__":
    # Isi data mahasiswa baru yang ingin diprediksi
    # PENTING: Nama key harus sama persis dengan nama kolom di data training
    # Contoh data mahasiswa baru yang ingin diprediksi
# Nilai-nilai ini adalah data dummy dan harus diganti dengan data asli.
    data_mahasiswa_baru = {
    # --- Fitur Utama (Profil Berisiko) ---
    'Curricular_units_2nd_sem_approved': 2,
    'Tuition_fees_up_to_date': 0,
    'Curricular_units_1st_sem_approved': 5,
    'Debtor': 1,
    'Curricular_units_1st_sem_enrolled': 6,
    'Gender': 1,
    'Scholarship_holder': 0,
    'Curricular_units_2nd_sem_enrolled': 6,
    'Curricular_units_2nd_sem_credited': 0,
    'Curricular_units_2nd_sem_grade': 10.5,

    # --- Fitur Lainnya (Data Dummy) ---
    'Marital status': 1,
    'Application mode': 17,
    'Application order': 1,
    'Course': 9238,
    'Daytime/evening attendance': 1,
    'Previous qualification': 1,
    'Previous qualification (grade)': 125.3,
    'Nacionality': 1,
    'Mother\'s qualification': 19,
    'Father\'s qualification': 19,
    'Mother\'s occupation': 5,
    'Father\'s occupation': 7,
    'Admission grade': 124.7,
    'Displaced': 1,
    'Educational special needs': 0,
    'Age at enrollment': 19,
    'International': 0,
    'Curricular units 1st sem (credited)': 0,
    'Curricular units 1st sem (evaluations)': 8,
    'Curricular units 1st sem (grade)': 12.4,
    'Curricular units 1st sem (without evaluations)': 0,
    'Curricular units 2nd sem (evaluations)': 7,
    'Curricular units 2nd sem (without evaluations)': 0,
    'Unemployment rate': 12.4,
    'Inflation rate': 1.3,
    'GDP': 0.51
    }

    # Untuk memastikan semua kolom ada, lengkapi sisanya dengan 0
    for feature in feature_order:
        if feature not in data_mahasiswa_baru:
            data_mahasiswa_baru[feature] = 0

    # Panggil fungsi untuk mendapatkan prediksi
    hasil = predict_dropout(data_mahasiswa_baru)

    # Tampilkan hasilnya dengan format yang mudah dibaca
    print("\n✅--- Hasil Prediksi ---✅")
    print(f"Prediksi Status Mahasiswa: {hasil['prediksi']}")
    print("\nDetail Probabilitas:")
    print(f"  - Kemungkinan Dropout: {hasil['probabilitas']['Dropout']:.2%}")
    print(f"  - Kemungkinan Bukan Dropout: {hasil['probabilitas']['Bukan Dropout']:.2%}")