from pathlib import Path

from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik
from utilitas import tentukan_status


def buat_laporan(daftar_siswa, statistik, kkm):
    """
    Membuat isi laporan berdasarkan
    data dan hasil analisis.
    """

    laporan = []

    laporan.append("=" * 50)
    laporan.append("LAPORAN REKAP NILAI MATEMATIKA SISWA")
    laporan.append("=" * 50)

    laporan.append(f"Jumlah siswa : {statistik['jumlah_siswa']}")
    laporan.append(f"KKM          : {kkm}")
    laporan.append(f"Rata-rata    : {statistik['rata_rata']:.2f}")
    laporan.append(f"Nilai tertinggi : {statistik['nilai_tertinggi']:.2f}")
    laporan.append(f"Nilai terendah  : {statistik['nilai_terendah']:.2f}")

    laporan.append("\nDAFTAR NILAI SISWA")
    laporan.append("-" * 50)

    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for siswa in daftar_siswa:

        status = tentukan_status(siswa["nilai"], kkm)

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

        laporan.append(
            f"{siswa['nama']} | "
            f"Nilai: {siswa['nilai']:.2f} | "
            f"Status: {status}"
        )

    laporan.append("\nREKAP KETUNTASAN")
    laporan.append("-" * 50)

    laporan.append(f"Jumlah siswa tuntas        : {jumlah_tuntas}")
    laporan.append(
        f"Jumlah siswa belum tuntas  : {jumlah_belum_tuntas}"
    )

    persentase_tuntas = (
        jumlah_tuntas / statistik["jumlah_siswa"]
    ) * 100

    laporan.append(
        f"Persentase ketuntasan      : {persentase_tuntas:.2f}%"
    )

    laporan.append("=" * 50)

    return "\n".join(laporan)


def main():
    """
    Fungsi utama untuk menjalankan program.
    """

    print("=" * 50)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("=" * 50)

    folder_proyek = Path(__file__).resolve().parent.parent

    file_data = folder_proyek / "data" / "nilai_contoh.txt"

    folder_output = folder_proyek / "output"

    try:
        kkm = float(input("Masukkan nilai KKM (default 75): ") or 75)

        if kkm < 0 or kkm > 100:
            print("KKM harus berada antara 0 sampai 100.")
            return

        daftar_siswa, daftar_kesalahan = baca_data(file_data)

        if daftar_kesalahan:
            print("\nPERINGATAN DATA:")
            for kesalahan in daftar_kesalahan:
                print("-", kesalahan)

        if not daftar_siswa:
            print("\nTidak terdapat data siswa yang valid.")
            return

        statistik = hitung_statistik(daftar_siswa)

        laporan = buat_laporan(
            daftar_siswa,
            statistik,
            kkm
        )

        print("\n")
        print(laporan)

        file_laporan = folder_output / "laporan_nilai.txt"

        simpan_laporan(laporan, file_laporan)

        print("\nLaporan berhasil disimpan.")
        print(f"Lokasi laporan: {file_laporan}")

    except FileNotFoundError as error:
        print(f"\nTerjadi kesalahan: {error}")

    except ValueError:
        print("\nInput KKM harus berupa angka.")

    except OSError as error:
        print(f"\nTerjadi kesalahan saat mengakses file: {error}")


if __name__ == "__main__":
    main()