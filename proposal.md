# PROPOSAL PROYEK AKHIR
## Program Rekap dan Analisis Nilai Matematika Kelas

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa  
**Pertemuan:** 14 – Perancangan Proyek  
**Tahun Ajaran:** 2026/2027 Ganjil  
**Nama Kelompok:** Nailah Nur Fadilah 
**Anggota Kelompok:** Nailah Nur Fadilah

### 1. Latar Belakang

Penilaian merupakan salah satu bagian penting dalam proses pembelajaran matematika. Setelah kegiatan pembelajaran dan evaluasi dilakukan, guru perlu mengolah nilai siswa untuk mengetahui gambaran hasil belajar dalam satu kelas. Pengolahan tersebut meliputi pemeriksaan data nilai, perhitungan rata-rata, pencarian nilai tertinggi dan terendah, serta penentuan jumlah siswa yang telah mencapai Kriteria Ketuntasan Minimal (KKM).

Apabila jumlah siswa cukup banyak, proses rekapitulasi secara manual dapat membutuhkan waktu dan berisiko menimbulkan kesalahan dalam perhitungan maupun pencatatan. Oleh karena itu, diperlukan sebuah alat bantu sederhana yang dapat membantu guru mengolah data nilai secara lebih cepat, teratur, dan konsisten.

Berdasarkan permasalahan tersebut, kelompok merancang **Program Rekap dan Analisis Nilai Matematika Kelas** menggunakan bahasa pemrograman Python. Program ini dirancang untuk membaca data nilai siswa dari file teks, memeriksa validitas data, menghitung statistik dasar, menentukan status ketuntasan berdasarkan KKM, serta menyimpan hasil rekapitulasi ke dalam file laporan.

Proyek ini memiliki ruang lingkup sederhana dan menerapkan materi Algoritma dan Pemrograman, seperti variabel, percabangan, perulangan, fungsi, list, dictionary, serta pengolahan file.

### 2. Identifikasi Pengguna dan Tujuan

**2.1 Pengguna**

Pengguna utama program adalah guru matematika yang membutuhkan bantuan untuk merekap dan menganalisis nilai siswa dalam satu kelas.

**2.2 User Story**

Sebagai guru matematika, saya ingin membaca data nilai siswa dari sebuah file dan memperoleh hasil analisis secara otomatis, agar saya dapat mengetahui statistik nilai serta jumlah siswa yang tuntas dan belum tuntas dengan lebih mudah.

**2.3 Tujuan Proyek**

1. Membantu guru membaca dan mengolah data nilai matematika siswa.
2. Memeriksa agar nilai yang diproses berada pada rentang 0 sampai 100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menghasilkan laporan rekapitulasi nilai dalam file teks.

### 3. Ruang Lingkup Proyek

**3.1 Fitur Wajib**

| Kode | Fitur | Penjelasan |
|---|---|---|
| F01 | Membaca data nilai | Membaca nama dan nilai siswa dari file teks. |
| F02 | Validasi data | Memeriksa format data dan rentang nilai 0–100. |
| F03 | Menghitung statistik | Menghitung rata-rata, nilai minimum, dan maksimum. |
| F04 | Menentukan ketuntasan | Mengelompokkan siswa berdasarkan KKM. |
| F05 | Menyimpan laporan | Menyimpan hasil analisis ke file teks. |

**3.2 Fitur Tambahan**

1. Menampilkan daftar siswa berdasarkan status ketuntasan.
2. Menampilkan persentase ketuntasan kelas.
3. Mengelompokkan statistik berdasarkan kategori nilai.

Fitur tambahan akan dikerjakan apabila seluruh fitur wajib telah berjalan dengan baik.

**3.3 Batasan Proyek**

1. Program berbentuk aplikasi console dan dijalankan melalui terminal VS Code.
2. Data masukan berasal dari file teks lokal.
3. Data yang digunakan merupakan data simulasi, bukan data pribadi siswa sebenarnya.
4. Nilai yang diterima berada pada rentang 0–100.
5. KKM dapat disesuaikan melalui pengaturan program.
6. Program hanya melakukan analisis statistik dasar.

### 4. Kebutuhan Sistem

**4.1 Kebutuhan Fungsional**

| ID | Kebutuhan Fungsional | Prioritas |
|---|---|---|
| F01 | Program dapat membaca data nilai dari file. | Wajib |
| F02 | Program dapat memvalidasi format dan rentang nilai 0–100. | Wajib |
| F03 | Program dapat menghitung rata-rata, minimum, dan maksimum. | Wajib |
| F04 | Program dapat menentukan status tuntas atau belum tuntas berdasarkan KKM. | Wajib |
| F05 | Program dapat menyimpan hasil analisis ke file laporan. | Wajib |
| F06 | Program dapat menampilkan persentase atau kategori nilai. | Tambahan |

**4.2 Kebutuhan Nonfungsional**

1. Program mudah dijalankan melalui terminal Visual Studio Code.
2. Program menampilkan pesan kesalahan yang mudah dipahami.
3. Nama fungsi dan variabel menggunakan istilah yang jelas.
4. Program menggunakan data simulasi.
5. Program dapat diuji ulang menggunakan test case yang sama.
6. Struktur program dibagi menjadi beberapa file agar mudah dibaca dan dikembangkan.

### 5. Spesifikasi Input, Proses, dan Output (IPO)

| Input | Proses | Output |
|---|---|---|
| File berisi nama dan nilai siswa. | Membaca file dan memeriksa format setiap baris. | Data valid dan keterangan data tidak valid. |
| Nilai siswa 0–100. | Menghitung rata-rata, minimum, dan maksimum. | Statistik nilai kelas. |
| Nilai siswa dan KKM. | Membandingkan nilai siswa dengan KKM. | Status tuntas atau belum tuntas. |
| Hasil pengolahan data. | Menyusun dan menyimpan ringkasan. | File laporan rekap nilai. |

### 6. Algoritma dan Pseudocode

**6.1 Alur Utama**

1. Program dimulai.
2. Program membaca file data nilai.
3. Jika file tidak ditemukan, program menampilkan pesan kesalahan.
4. Program memeriksa format dan validitas setiap baris data.
5. Data yang valid disimpan untuk diproses.
6. Data yang tidak valid ditolak dan diberi keterangan.
7. Jika tidak ada data valid, program menampilkan pesan bahwa data tidak tersedia.
8. Program menghitung rata-rata, nilai minimum, dan maksimum.
9. Program menentukan status ketuntasan berdasarkan KKM.
10. Program menampilkan ringkasan hasil analisis.
11. Program menyimpan laporan ke file teks.
12. Program selesai.

**6.2 Pseudocode**

```text
MULAI

    tentukan lokasi file data
    tentukan nilai KKM

    baca data dari file

    JIKA file tidak ditemukan:
        tampilkan pesan kesalahan
        SELESAI

    buat daftar data_valid
    buat daftar data_tidak_valid

    UNTUK setiap baris data:
        periksa format baris
        ambil nama dan nilai

        periksa apakah nilai berupa angka
        periksa apakah nilai berada pada rentang 0–100

        JIKA valid:
            simpan data
        JIKA tidak valid:
            catat alasan penolakan

    JIKA data_valid kosong:
        tampilkan pesan
        SELESAI

    hitung rata-rata
    cari nilai minimum
    cari nilai maksimum

    tentukan status ketuntasan berdasarkan KKM

    tampilkan hasil analisis
    simpan laporan ke file

SELESAI
```

### 7. Rancangan Struktur Program

Program dirancang secara modular agar setiap file memiliki tugas yang jelas.

| File | Tanggung Jawab |
|---|---|
| `main.py` | Menjalankan alur utama program. |
| `data_io.py` | Membaca data dan menyimpan laporan. |
| `analisis.py` | Menghitung statistik dan menentukan ketuntasan. |
| `utilitas.py` | Memeriksa format data dan validitas nilai. |
| `nilai_contoh.txt` | Menyediakan data simulasi. |
| `test_case.md` | Mendokumentasikan skenario pengujian. |

### 8. Rancangan Struktur Data

| Struktur Data | Penggunaan | Alasan |
|---|---|---|
| String | Menyimpan nama siswa dan pesan laporan. | Karena berupa teks. |
| Integer/float | Menyimpan nilai dan KKM. | Digunakan dalam perhitungan. |
| List | Menampung kumpulan data siswa. | Memudahkan perulangan dan pengolahan data. |
| Dictionary | Menyimpan data siswa seperti nama dan nilai. | Memudahkan pengelolaan data berdasarkan pasangan kunci dan nilai. |
| File teks | Menyimpan data masukan dan laporan. | Agar data dapat dibaca dan disimpan. |

### 9. Rancangan Test Case

KKM simulasi yang digunakan adalah 75.

| ID | Skenario | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Data normal | Nilai 80, 70, 90 | Data diterima dan rata-rata = 80. |
| TC02 | Nilai batas bawah | Nilai 0 | Nilai diterima sebagai data valid. |
| TC03 | Nilai batas atas | Nilai 100 | Nilai diterima sebagai data valid. |
| TC04 | Nilai di luar batas | Nilai 105 | Data ditolak dan pesan validasi ditampilkan. |
| TC05 | File tidak ditemukan | Lokasi file tidak tersedia | Program menampilkan pesan kesalahan. |
| TC06 | Semua siswa mencapai KKM | Semua nilai valid lebih besar atau sama dengan KKM | Jumlah siswa tuntas sama dengan jumlah data valid. |
| TC07 | Tidak ada data valid | File kosong atau semua baris tidak valid | Program menampilkan pesan bahwa tidak ada data valid. |

### 10. Pembagian Tugas Anggota Kelompok

| No. | Nama Anggota | Peran/PIC | Tanggung Jawab |
|---|---|---|---|
| 1 | [Nama anggota 1] | Koordinator | Mengatur pembagian tugas dan memantau kemajuan proyek. |
| 2 | [Nama anggota 2] | Programmer data I/O | Merancang pembacaan data dan penyimpanan laporan. |
| 3 | [Nama anggota 3] | Programmer logika | Merancang perhitungan statistik dan ketuntasan. |
| 4 | [Nama anggota 4] | Tester/QA | Menyusun test case dan memeriksa hasil program. |
| 5 | [Nama anggota 5] | Dokumentasi | Menyusun proposal, README, dan dokumentasi. |

*Catatan: Nama dan pembagian PIC disesuaikan dengan anggota kelompok sebenarnya.*

### 11. Rencana Jadwal Pengerjaan

| Tahap | Kegiatan | Hasil yang Diharapkan |
|---|---|---|
| Pertemuan 14 | Menentukan masalah, pengguna, kebutuhan, IPO, pseudocode, struktur folder, test case, dan pembagian tugas. | Proposal dan rancangan proyek. |
| Sebelum Pertemuan 15 | Memulai implementasi fitur wajib. | Kerangka dan implementasi awal program. |
| Pertemuan 15 | Integrasi modul, pengujian, debugging, dan dokumentasi. | Program berjalan dan hasil pengujian terdokumentasi. |
| Pertemuan 16 | Presentasi, demonstrasi, dan evaluasi proyek. | Program akhir dan presentasi. |

### 12. Kriteria Keberhasilan

Proyek dinyatakan selesai apabila:

1. Seluruh fitur wajib dapat dijalankan.
2. Program dapat membaca data nilai dari file.
3. Program dapat menolak data yang tidak sesuai.
4. Perhitungan statistik dan ketuntasan memberikan hasil yang benar.
5. Laporan dapat disimpan ke file.
6. Test case telah dijalankan dan hasilnya didokumentasikan.
7. Program dapat menangani kesalahan yang telah diantisipasi.
8. README menjelaskan cara menjalankan program.
9. Repository GitHub memuat dokumen dan perkembangan proyek.

### 13. Pengelolaan GitHub

Repository kelompok direncanakan menggunakan nama:

```text
proyek-akhir-nama-tim
```

Repository menggunakan branch `main` sebagai versi stabil. Seluruh anggota kelompok dapat ditambahkan sebagai collaborator.

Contoh commit rancangan awal:

```bash
git add README.md proposal.md tests/
git commit -m "docs: menambahkan proposal dan test case proyek"
git push
```

**URL Repository GitHub:** [Isi tautan repository kelompok]

### 14. Penutup

Program Rekap dan Analisis Nilai Matematika Kelas dirancang sebagai solusi sederhana untuk membantu guru mengolah data hasil belajar siswa. Melalui program ini, proses membaca data, memeriksa validitas nilai, menghitung statistik dasar, dan menentukan ketuntasan dapat dilakukan secara lebih terstruktur.

Proyek ini juga menjadi penerapan materi Algoritma dan Pemrograman, khususnya penggunaan fungsi, percabangan, perulangan, struktur data, serta pengolahan file. Rancangan ini akan menjadi dasar implementasi, pengujian, dan penyempurnaan program pada tahap berikutnya.