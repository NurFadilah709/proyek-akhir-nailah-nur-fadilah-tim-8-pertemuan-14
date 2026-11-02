from pathlib import Path
from utilitas import validasi_nilai


def baca_data(nama_file):
    """
    Membaca data siswa dari file teks.
    Data yang tidak valid akan dilewati
    dan dicatat sebagai kesalahan.
    """

    daftar_siswa = []
    daftar_kesalahan = []

    path_file = Path(nama_file)

    if not path_file.exists():
        raise FileNotFoundError(
            f"File {nama_file} tidak ditemukan."
        )

    with path_file.open("r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):

            baris = baris.strip()

            if not baris:
                continue

            if "," not in baris:
                daftar_kesalahan.append(
                    f"Baris {nomor_baris}: format data tidak sesuai."
                )
                continue

            nama, nilai_teks = baris.split(",", 1)

            nama = nama.strip()
            nilai_teks = nilai_teks.strip()

            if not nama:
                daftar_kesalahan.append(
                    f"Baris {nomor_baris}: nama siswa kosong."
                )
                continue

            valid, nilai, pesan = validasi_nilai(nilai_teks)

            if not valid:
                daftar_kesalahan.append(
                    f"Baris {nomor_baris}: {pesan}"
                )
                continue

            data_siswa = {
                "nama": nama,
                "nilai": nilai
            }

            daftar_siswa.append(data_siswa)

    return daftar_siswa, daftar_kesalahan


def simpan_laporan(laporan, nama_file):
    """
    Menyimpan laporan hasil analisis
    ke dalam file teks.
    """

    path_file = Path(nama_file)

    path_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path_file.open("w", encoding="utf-8") as file:
        file.write(laporan)

    return True