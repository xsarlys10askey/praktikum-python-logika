"""Program Penentuan Status Mahasiswa."""

# Konstanta aturan bisnis
IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18


def tentukan_status(mhs):
    """Tentukan status mahasiswa berdasarkan IPK dan SKS."""
    ipk = mhs["ipk"]
    sks = mhs["sks"]

    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"
    else:
        return "Tidak Aktif"


# Input data 5 mahasiswa
daftar_mhs = []

for i in range(5):
    print(f"\nData Mahasiswa ke-{i + 1}")

    nim = input("NIM: ")
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    sks = int(input("SKS: "))

    mahasiswa = {
        "nim": nim,
        "nama": nama,
        "ipk": ipk,
        "sks": sks
    }

    daftar_mhs.append(mahasiswa)


# Tampilkan laporan
print("\n" + "=" * 60)
print("LAPORAN STATUS MAHASISWA")
print("=" * 60)

print(f"{'NIM':<12} {'Nama':<15} {'IPK':>5} {'SKS':>4} {'Status':<15}")
print("-" * 60)

for mhs in daftar_mhs:
    status = tentukan_status(mhs)

    print(
        f"{mhs['nim']:<12} "
        f"{mhs['nama']:<15} "
        f"{mhs['ipk']:>5.2f} "
        f"{mhs['sks']:>4} "
        f"{status:<15}"
    )