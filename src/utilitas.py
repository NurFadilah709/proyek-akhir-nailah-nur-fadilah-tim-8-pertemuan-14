def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berupa angka
    dan berada pada rentang 0 sampai 100.
    """

    try:
        nilai = float(nilai)

        if nilai < 0 or nilai > 100:
            return False, None, "Nilai harus berada antara 0 sampai 100."

        return True, nilai, "Nilai valid."

    except ValueError:
        return False, None, "Nilai harus berupa angka."


def tentukan_status(nilai, kkm):
    """
    Menentukan status ketuntasan siswa
    berdasarkan nilai KKM.
    """

    if nilai >= kkm:
        return "Tuntas"

    return "Belum Tuntas"