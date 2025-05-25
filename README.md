# 🧠 Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan Institut Jaya Jaya
[![Versi Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=Streamlit)](https://drop-out-predict.streamlit.app/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Model-brightgreen?style=for-the-badge&logo=XGBoost)](https://xgboost.ai/)
[![Metabase](https://img.shields.io/badge/Metabase-Dashboard-509EE3?style=for-the-badge&logo=Metabase)](https://www.metabase.com/)

## 📝 Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Tingginya angka mahasiswa dropout menjadi perhatian utama bagi Institut Jaya Jaya. Diperlukan solusi untuk mengidentifikasi mahasiswa berisiko secara proaktif.

### Cakupan Proyek
Proyek ini meliputi:
1.  Menganalisis data historis mahasiswa untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap dropout.
2.  Mengembangkan model machine learning prediktif (XGBoost) untuk mengidentifikasi mahasiswa yang berisiko dropout.
3.  Membuat aplikasi prototipe interaktif (menggunakan Streamlit) agar staf akademik dapat menggunakan model prediksi.
4.  Membangun dasbor bisnis (menggunakan Metabase) untuk memvisualisasikan metrik utama dan wawasan terkait kinerja mahasiswa dan prediksi dropout.

### Persiapan

Sumber data:  [students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Windows
venv\Scripts\activate

# MacOS/Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt

```

### Menjalankan Script Prediksi

```bash
python test_predict.py
```

---

## 📊 Business Dashboard

Dashboard ini dibangun menggunakan Metabase yang terhubung ke database PostgreSQL. Dashboard ini menampilkan informasi visual terkait:

- Jumlah siswa dropout vs non-dropout per semester
- Distribusi performa akademik siswa
- Analisis berdasarkan gender, tingkat pendidikan orang tua, dan faktor lainnya
- Daftar siswa dengan prediksi risiko dropout

### Akun Metabase

- Email: `root@mail.com`
- Password: `root123`

### Cuplikan Layar Dasbor
Berikut adalah beberapa contoh tampilan dasbor yang memberikan wawasan kunci:

* **Dasbor Ringkasan Umum:**
    Menampilkan gambaran keseluruhan metrik penting seperti total mahasiswa, persentase prediksi dropout, dan disribusi mahasiswa.
  
  ![ringkasan](https://github.com/user-attachments/assets/12063625-519f-43ae-ba2e-cc5981667623)

* **Analisis Faktor Risiko Dropout:**
    Menyajikan visualisasi berbagai faktor yang berkontribusi terhadap risiko dropout, membantu identifikasi pola dan area fokus.
    * **Faktor-faktor Umum:** Perbandingan rata-rata nilai, gender, dan status pembayaran UKT.
      
        ![Analisis Faktor Risiko Umum](https://github.com/user-attachments/assets/9d1c9e5b-b92e-409f-bd09-d1566d114539)
  
    * **Berdasarkan Program Studi dan Status Pernikahan:** Menampilkan 5 program studi dengan tingkat *dropout* tertinggi serta distribusi *dropout* berdasarkan status pernikahan mahasiswa.
      
        ![Analisis Dropout per Prodi dan Status Pernikahan](https://github.com/user-attachments/assets/36b584d9-d591-4ae9-9350-891aed37a7e0)
      
    * **Perbandingan Mahasiswa Internasional dan Lokal:** Menunjukkan perbedaan tingkat *dropout* antara mahasiswa internasional dan mahasiswa lokal.
      
        ![Analisis Dropout Internasional vs Lokal](https://github.com/user-attachments/assets/9eb94a5e-8267-4933-b456-d1022c7aeff3)

* **Daftar Mahasiswa Berisiko Tinggi untuk Tindak Lanjut:**
    Menyajikan daftar mahasiswa yang teridentifikasi memiliki risiko dropout tinggi, memungkinkan intervensi yang lebih fokus.
  
  ![zulfahmi17z_dashboard(4)](https://github.com/user-attachments/assets/d4f8fd97-17c3-4a67-9254-33c2db5a8a35)


### Video Penjelasan : 
[Tonton di Google Drive](https://drive.google.com/file/d/1tGv-VZaOavT4nUHSdPltAfbsRvWfl0Oy/view?usp=drive_link)

---

## 🚀 Menjalankan Sistem Machine Learning

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
   git clone https://github.com/7z1x/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git
   cd Menyelesaikan-Permasalahan-Institusi-Pendidikan
   ```

3.  **Buat dan Aktifkan Virtual Environment** (Sangat Direkomendasikan):
     ```
     python -m venv venv
     ```
     * Di Linux/Mac:
       ```
       source venv/bin/activate
       ```
     * Di Windows:
       ```
       venv\Scripts\activate
       ```

4. **Install Semua Dependency**  
   Pastikan Anda berada di dalam folder proyek dan jalankan:
   ```bash
   pip install -r requirements.txt
   ```

5. **Pastikan File Model dan Script Tersedia**  
   Pastikan file `app.py` dan (`model/dropout_model.joblib`), scaler 
   (`model/scaler.joblib`), dan urutan fitur (`model/feature_order.joblib`) ada 
   di direktori `model/`.

6. **Jalankan Aplikasi Streamlit**  
   Gunakan perintah berikut untuk menjalankan prototipe:
   ```bash
   streamlit run app.py
   ```

7. **Akses Aplikasi di Browser**  
   Setelah menjalankan perintah tersebut, browser akan otomatis membuka halaman prototipe. Jika tidak terbuka, akses secara manual melalui:
   ```
   http://localhost:8501
   ```

### 🔗 Akses Prototipe

Anda juga bisa langsung mencoba prototipe yang sudah dideploy tanpa menginstal apa pun melalui link berikut:

🌐 [Drop-out-predict.streamlit.app](https://drop-out-predict.streamlit.app/)

---


## 🌟 Conclusion

Berdasarkan analisis data dan pemodelan prediktif yang telah dilakukan, sistem berhasil mengidentifikasi mahasiswa berisiko *dropout* dengan akurasi pada data uji mencapai **0.8847** (atau **88.47%**) menggunakan model XGBoost. Beberapa faktor kunci yang teridentifikasi signifikan memengaruhi risiko *dropout* mahasiswa di Institut Jaya Jaya antara lain:
* **Performa Akademik Awal:** Nilai pada semester pertama dan kedua (`Curricular units 1st sem (grade)`, `Curricular units 2nd sem (grade)`) menjadi indikator kuat. Perolehan nilai yang rendah secara konsisten berkorelasi dengan peningkatan risiko *dropout*.
* **Status Keuangan:** Terutama kelancaran pembayaran UKT (`Tuition fees up to date`) dan status (`Debtor`). Mahasiswa dengan kesulitan finansial menunjukkan risiko *dropout* yang lebih tinggi.
* **Karakteristik Demografis dan Pribadi:** Faktor seperti usia saat pendaftaran (`Age at enrollment`), status pernikahan (`Marital status`), dan jenis kelamin (`Gender`) juga menunjukkan kontribusi terhadap variasi tingkat *dropout*.
* **Status Beasiswa (`Scholarship holder`):** Terdapat perbedaan profil risiko antara mahasiswa penerima beasiswa dan yang tidak, yang memerlukan perhatian khusus.

Pemahaman mendalam terhadap faktor-faktor ini, didukung oleh model prediksi yang akurat dan visualisasi dasbor, memberikan landasan kuat bagi Institut Jaya Jaya untuk merancang strategi intervensi yang lebih efektif dan terarah guna menekan angka *dropout* dan meningkatkan tingkat kelulusan mahasiswa.

---

### Rekomendasi Action Items
Untuk mengatasi permasalahan *dropout* mahasiswa secara strategis dan mencapai target peningkatan angka kelulusan, berikut adalah rekomendasi tindak lanjut yang dapat diimplementasikan oleh pimpinan Institut Jaya Jaya:

1.  **Penguatan Sistem Pendampingan Akademik Personal dan Responsif:**
    * **Monitoring Intensif Performa Akademik Awal:** Fokuskan perhatian pada mahasiswa dengan perolehan nilai rendah di semester 1 dan 2 (`Curricular units 1st sem (grade)`, `Curricular units 2nd sem (grade)`), sebagaimana teridentifikasi oleh model dan dasbor.
    * **Program Intervensi Akademik Terpadu:** Sediakan program pendampingan akademik yang lebih intensif dan personal, seperti kelompok belajar kecil, sesi tutorial tambahan dengan asisten dosen atau mahasiswa senior berprestasi, dan tutor mata kuliah untuk subjek-subjek sulit.
    * **Optimalisasi Peran Dosen Pembimbing Akademik (DPA):** Bekali DPA dengan data prediksi risiko mahasiswa bimbingannya. Wajibkan sesi konseling proaktif dan terstruktur dengan mahasiswa berisiko untuk membahas tantangan akademik, strategi belajar, dan penyesuaian rencana studi jika diperlukan.

2. **Implementasi Program Dukungan Keuangan dan Konseling Proaktif:**
    * **Deteksi Dini Kesulitan Finansial:** Manfaatkan sistem prediksi dan dasbor Metabase untuk secara *real-time* mengidentifikasi mahasiswa yang menunjukkan tanda-tanda kesulitan pembayaran UKT (berdasarkan fitur `Tuition fees up to date` dan `Debtor`).
    * **Intervensi Keuangan Terstruktur:** Segera tindak lanjuti mahasiswa teridentifikasi dengan menawarkan skema bantuan keuangan yang fleksibel (cicilan, penundaan dengan syarat), program beasiswa darurat, atau bantuan keringanan biaya berdasarkan evaluasi kasus per kasus. Sediakan layanan konseling manajemen keuangan bagi mahasiswa.
    * **Pengembangan Sistem Peringatan Dini Keuangan:** Integrasikan notifikasi otomatis ke tim dukungan kemahasiswaan atau DPA ketika mahasiswa terdeteksi memiliki risiko finansial tinggi.

3. **Pengembangan Kebijakan dan Program Dukungan Holistik Berbasis Profil Risiko Mahasiswa:**
    * **Analisis Lanjutan Faktor Risiko Spesifik:** Lakukan kajian lebih mendalam terhadap bagaimana faktor-faktor seperti status beasiswa (`Scholarship holder`), usia saat masuk (`Age at enrollment`), status pernikahan (`Marital status`), dan jenis kelamin (`Gender`) berinteraksi dan memengaruhi keputusan *dropout* di konteks Institut Jaya Jaya.
    * **Desain Program Dukungan yang Disesuaikan:** Kembangkan program dukungan yang spesifik untuk kelompok mahasiswa dengan profil risiko tertentu. Contoh: program mentoring khusus untuk mahasiswa penerima beasiswa agar dapat mempertahankan standar akademik; layanan dukungan bagi mahasiswa yang sudah menikah atau bekerja untuk membantu menyeimbangkan studi dengan tanggung jawab lain; program pengembangan komunitas dan dukungan psikososial yang peka gender.
    * **Penciptaan Lingkungan Kampus yang Mendukung dan Inklusif:** Pastikan semua kebijakan dan layanan kemahasiswaan dirancang untuk menciptakan lingkungan belajar yang positif, suportif, dan inklusif bagi seluruh mahasiswa, tanpa memandang latar belakang mereka.

4.  **Pemanfaatan Maksimal Dasbor Metabase dan Integrasi Sistem untuk Pengambilan Keputusan Strategis:**
    * **Budaya Pengambilan Keputusan Berbasis Data:** Dorong penggunaan dasbor Metabase di semua tingkatan manajemen (rektorat, dekanat, ketua program studi) sebagai alat utama untuk memantau tren *dropout* secara berkala, mengevaluasi efektivitas program intervensi yang berjalan, dan membuat keputusan strategis yang terinformasi.
    * **Pelatihan dan Kapasitasi Pengguna Dasbor:** Selenggarakan pelatihan reguler bagi staf akademik dan non-akademik terkait (dosen, DPA, staf administrasi, tim konseling) agar mahir dalam mengakses, menggunakan, dan menginterpretasikan data serta *insight* yang disajikan oleh dasbor.
    * **Roadmap Integrasi Sistem Informasi:** Susun rencana strategis untuk mengintegrasikan output model prediksi (misalnya, daftar mahasiswa berisiko tinggi) dan *insight* kunci dari dasbor Metabase ke dalam Sistem Informasi Akademik atau sistem manajemen pembelajaran (LMS) yang ada. Tujuannya adalah untuk mempermudah akses informasi dan koordinasi tindak lanjut oleh berbagai unit terkait secara *real-time* dan efisien.

5.  **Pembentukan Tim Gugus Tugas Penurunan Angka Dropout dan Evaluasi Berkelanjutan:**
    * **Tim Gugus Tugas Lintas Fungsi:** Bentuk tim khusus yang terdiri dari perwakilan pimpinan, fakultas, tim dukungan mahasiswa, DPA, dan bahkan perwakilan mahasiswa untuk secara aktif merancang, mengimplementasikan, dan memonitor strategi penurunan angka *dropout*.
    * **Siklus Evaluasi dan Iterasi Program:** Tetapkan mekanisme untuk evaluasi rutin (misalnya, per semester atau per tahun) terhadap dampak dari semua program intervensi yang dijalankan. Gunakan data dari dasbor dan model untuk mengukur keberhasilan dan mengidentifikasi area yang memerlukan perbaikan atau pendekatan baru.
    * **Pengumpulan Umpan Balik Kualitatif:** Selain data kuantitatif, secara aktif kumpulkan umpan balik dari mahasiswa (terutama yang berisiko atau yang berhasil dicegah dari *dropout*), dosen, dan staf mengenai tantangan yang dihadapi dan efektivitas program dukungan yang ada untuk penyempurnaan berkelanjutan.

Dengan mengimplementasikan rekomendasi ini secara komprehensif dan berkelanjutan, Institut Jaya Jaya diharapkan dapat secara signifikan mengurangi angka *dropout* mahasiswa dan mencapai target peningkatan angka kelulusan serta kualitas lulusan.

---
## 🗂️ Struktur Folder Proyek

```
submission/
│
├── Insight/
│   └── zulfahmi17z_dashboard(1).jpg
│   └── zulfahmi17z_dashboard(2).jpg
│   └── zulfahmi17z_dashboard(3).jpg
│   └── zulfahmi17z_dashboard(4).jpg
│   └── zulfahmi17z_dashboard.jpg
│   └── zulfahmi17z_video.mov 
│
├── dataset/
│   └── data.csv
│ 
├── model/
│   └── dropout_model.joblib
│   └── feature_order.joblib
│   └── scaler.joblib
│
├── app.py 
├── metabase.db.mv.db 
├── notebook.ipynb
├── requirements.txt
├── test_predict.py
└── README.md
```

---
