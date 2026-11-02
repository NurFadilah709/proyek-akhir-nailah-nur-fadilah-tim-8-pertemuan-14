# TEST CASE PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA

## TC01 - Data Normal

Input:
Andi,80
Budi,70
Citra,90

Proses:
Program membaca data dan menghitung statistik.

Hasil yang diharapkan:
- Jumlah siswa: 3
- Rata-rata: 80
- Nilai tertinggi: 90
- Nilai terendah: 70

Status: Berhasil jika hasil sesuai.

---

## TC02 - Nilai Batas Bawah

Input:
Andi,0

Hasil yang diharapkan:
Nilai 0 diterima sebagai data valid.

Status: Berhasil jika nilai diterima.

---

## TC03 - Nilai Batas Atas

Input:
Budi,100

Hasil yang diharapkan:
Nilai 100 diterima sebagai data valid.

Status: Berhasil jika nilai diterima.

---

## TC04 - Nilai Melebihi Batas

Input:
Citra,105

Hasil yang diharapkan:
Data ditolak karena nilai melebihi 100.

Status: Berhasil jika data ditolak.

---

## TC05 - File Tidak Ditemukan

Input:
Nama file yang tidak tersedia.

Hasil yang diharapkan:
Program menampilkan pesan bahwa file tidak ditemukan.

Status: Berhasil jika kesalahan ditangani.

---

## TC06 - Seluruh Siswa Tuntas

Input:
Andi,80
Budi,90
Citra,85

KKM: 75

Hasil yang diharapkan:
Seluruh siswa mendapatkan status Tuntas.

Status: Berhasil jika seluruh siswa dinyatakan tuntas.

---

## TC07 - Data Tidak Valid

Input:
Andi,80
Budi,abc
Citra,90

Hasil yang diharapkan:
Data Andi dan Citra tetap diproses.
Data Budi ditolak karena nilai bukan angka.

Status: Berhasil jika data valid tetap diproses.