# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Deskripsi Program

Program Rekap dan Analisis Nilai Matematika Kelas merupakan
program sederhana berbasis Python yang digunakan untuk membantu
guru dalam mengolah dan menganalisis nilai matematika siswa.

Program ini dapat membaca data nilai dari file teks,
memeriksa validitas nilai, menghitung statistik nilai,
menentukan status ketuntasan siswa berdasarkan KKM,
serta menyimpan hasil analisis ke dalam file laporan.

## 2. Tujuan Program

1. Mempermudah guru dalam merekap nilai siswa.
2. Mengurangi kesalahan dalam perhitungan nilai.
3. Mengetahui nilai rata-rata, tertinggi, dan terendah.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menghasilkan laporan nilai secara otomatis.

## 3. Fitur Program

- Membaca data nilai siswa dari file teks.
- Memvalidasi data dan rentang nilai 0–100.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menentukan status tuntas atau belum tuntas.
- Menyimpan hasil analisis ke file laporan.

## 4. Teknologi yang Digunakan

- Bahasa pemrograman Python.
- Visual Studio Code.
- Git dan GitHub.

## 5. Struktur Program

- main.py: menjalankan program utama.
- data_io.py: membaca data dan menyimpan laporan.
- analisis.py: melakukan perhitungan statistik.
- utilitas.py: melakukan validasi dan menentukan status.
- data/: menyimpan data nilai siswa.
- tests/: menyimpan pengujian program.
- output/: menyimpan laporan hasil analisis.

## 6. Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka folder proyek melalui Visual Studio Code.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah berikut:

   python src/main.py

5. Ikuti petunjuk yang muncul pada terminal.

## 7. Format Data

Data nilai siswa disimpan dalam file teks dengan format:

Nama Siswa,Nilai

Contoh:

Andi,80
Budi,70
Citra,90

Nilai harus berada pada rentang 0 sampai 100.

## 8. Pengujian

Pengujian dilakukan menggunakan beberapa kasus,
seperti data normal, nilai batas bawah, nilai batas atas,
nilai tidak valid, dan file yang tidak ditemukan.

## 9. Hasil Program

Program menampilkan hasil analisis pada terminal
dan menyimpan laporan dalam folder output.