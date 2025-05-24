# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

📁 **Repository:** [`ProyekAkhir-MenyelesaikanPermasalahanInstitusiPendidikan`](https://github.com/ZidanAlfarizaPutraPratama/ProyekAkhir-MenyelesaikanPermasalahanInstitusiPendidikan)

![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat&logo=xgboost&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Metabase](https://img.shields.io/badge/Metabase-5D47B4?style=flat&logo=metabase&logoColor=white)
![Data Science](https://img.shields.io/badge/Data%20Science-FF6F61?style=flat&logo=databricks&logoColor=white)

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan berbasis teknologi (edutech) yang mengalami permasalahan dalam mempertahankan siswanya. Terjadi peningkatan signifikan dalam jumlah siswa yang mengalami dropout dari tahun ke tahun. Untuk itu, dibutuhkan sebuah sistem yang mampu memprediksi siswa mana yang berpotensi dropout agar pihak institusi dapat mengambil tindakan preventif lebih awal.

### Permasalahan Bisnis

- Tingginya angka dropout siswa dari semester ke semester.
- Belum adanya sistem yang bisa membantu pihak akademik dalam memantau risiko siswa yang berpotensi keluar.
- Kurangnya wawasan berbasis data yang bisa digunakan manajemen untuk melakukan intervensi tepat sasaran.

### Cakupan Proyek

- Melakukan analisis data historis performa siswa.
- Membangun model machine learning untuk memprediksi potensi siswa dropout.
- Membuat prototype sistem prediksi berbasis web menggunakan Streamlit.
- Membangun dashboard visualisasi performa siswa dan prediksi dropout menggunakan Metabase.
- Menyimpan hasil prediksi ke dalam database PostgreSQL.

### Persiapan

Sumber data:  
[students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Dashboard ini dibangun menggunakan Metabase yang terhubung ke database PostgreSQL. Dashboard ini menampilkan informasi visual terkait:

- Jumlah siswa dropout vs non-dropout per semester
- Distribusi performa akademik siswa
- Analisis berdasarkan gender, tingkat pendidikan orang tua, dan faktor lainnya
- Daftar siswa dengan prediksi risiko dropout

### Akun Metabase

- Email: `root@mail.com`
- Password: `root123`

---

## Menjalankan Sistem Machine Learning

Sistem prototype ini dibangun menggunakan Streamlit dan dapat digunakan oleh pihak akademik untuk memprediksi status dropout siswa berdasarkan data input.

### Langkah-Langkah Menjalankan Aplikasi Prototype

1. **Pastikan Python Sudah Terinstal**  
   Aplikasi ini membutuhkan Python versi 3.10 atau lebih tinggi. Cek versi Python dengan perintah:
   ```bash
   python --version
   ```

2. **Clone atau Unduh Proyek Ini**  
   Jika Anda belum memiliki folder proyek, unduh dari GitHub atau salin dengan git:
   ```bash
   git clone https://github.com/ZidanAlfarizaPutraPratama/ProyekAkhir-MenyelesaikanPermasalahanInstitusiPendidikan.git
   cd ProyekAkhir-MenyelesaikanPermasalahanInstitusiPendidikan
   ```

3. **Buat dan Aktifkan Virtual Environment (Opsional, tapi Disarankan)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. **Install Semua Dependency**  
   Pastikan Anda berada di dalam folder proyek dan jalankan:
   ```bash
   pip install -r requirements.txt
   ```

5. **Pastikan File Model dan Script Tersedia**  
   Pastikan file `streamlit_app.py` dan model hasil pelatihan (`model.pkl` atau sejenisnya) sudah ada di direktori.

6. **Jalankan Aplikasi Streamlit**  
   Gunakan perintah berikut untuk menjalankan prototipe:
   ```bash
   streamlit run streamlit_app.py
   ```

7. **Akses Aplikasi di Browser**  
   Setelah menjalankan perintah tersebut, browser akan otomatis membuka halaman prototipe. Jika tidak terbuka, akses secara manual melalui:
   ```
   http://localhost:8501
   ```

### 🔗 Akses Versi Online (Jika Tidak Ingin Install Manual)

Anda juga bisa langsung mencoba prototipe tanpa menginstal apa pun melalui link berikut:

🌐 [DropoutPrototype.streamlit.app](https://proyekakhir-menyelesaikanpermasalahaninstitusipendidikan.streamlit.app/)

---

## Visualisasi Tambahan dari Dashboard Metabase

Beberapa grafik berikut memperkuat insight terkait faktor-faktor yang memengaruhi prediksi dropout siswa:

- **Dropout berdasarkan Curricular Units 2nd Sem Approved**  
  Mayoritas siswa yang dropout hanya menyelesaikan sedikit mata kuliah di semester kedua, menunjukkan korelasi antara performa semester 2 dengan dropout.

- **Dropout berdasarkan Application Mode**  
  Terdapat pola dropout yang cukup tinggi pada siswa dengan mode pendaftaran tertentu, menunjukkan bahwa cara siswa mendaftar ke institusi dapat menjadi indikator awal risiko.

- **Dropout berdasarkan Kualifikasi Sebelumnya**  
  Siswa dengan latar belakang kualifikasi rendah (bahkan nol) dari pendidikan sebelumnya menunjukkan angka dropout yang jauh lebih tinggi.

- **Dropout berdasarkan Curricular Units 2nd Sem Enrolled**  
  Semakin sedikit jumlah mata kuliah yang diambil di semester kedua, semakin besar kemungkinan siswa mengalami dropout. Hal ini bisa menjadi indikator bahwa siswa mulai kehilangan motivasi atau memiliki hambatan akademik lainnya.

Dengan visualisasi ini, pihak manajemen dapat menargetkan intervensi pada semester awal dan memfokuskan perhatian pada siswa dengan ciri-ciri tersebut untuk menurunkan angka dropout secara signifikan.

---

## Conclusion

Proyek ini berhasil membangun sistem prediksi dropout dengan akurasi mencapai **90%**. Model XGBoost terbukti memberikan performa terbaik berdasarkan metrik akurasi dan F1-score. Dashboard Metabase berhasil menyediakan insight visual untuk mendukung keputusan manajerial secara data-driven.

### Rekomendasi Action Items

- Menggunakan hasil prediksi dropout untuk melakukan intervensi akademik lebih awal.
- Meningkatkan komunikasi dan bimbingan terhadap siswa dengan risiko tinggi.
- Melakukan monitoring berkala terhadap faktor-faktor yang paling berpengaruh terhadap dropout.
- Melanjutkan pengembangan fitur seperti integrasi dengan sistem akademik internal dan notifikasi otomatis.
