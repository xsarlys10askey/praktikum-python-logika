"""Program Kalkulator Diskon Biaya Kuliah."""

# Konstanta aturan bisnis
DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20
DISKON_PRESTASI_BAIK = 0.15
DISKON_MEMUASKAN = 0.10
DISKON_TEPAT_WAKTU = 0.05


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    """Hitung diskon berdasarkan aturan bisnis."""

    # Diskon utama: hanya ambil yang terbesar
    if is_anak_karyawan:
        diskon_utama = DISKON_ANAK_KARYAWAN
        kategori = "Anak Karyawan"
    elif ipk >= 3.8:
        diskon_utama = DISKON_PRESTASI_TINGGI
        kategori = "Prestasi Tinggi"
    elif ipk >= 3.5:
        diskon_utama = DISKON_PRESTASI_BAIK
        kategori = "Prestasi Baik"
    elif ipk >= 3.0:
        diskon_utama = DISKON_MEMUASKAN
        kategori = "IPK Memuaskan"
    else:
        diskon_utama = 0.0
        kategori = "Tidak ada diskon"

    # Diskon tambahan untuk pembayaran tepat waktu
    diskon_tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0.0

    total_diskon = diskon_utama + diskon_tambahan

    return total_diskon, kategori, diskon_utama, diskon_tambahan


# Input data
print("=== KALKULATOR DISKON BIAYA KULIAH ===")

biaya_spp = float(input("Biaya SPP: Rp"))
anak_karyawan = input("Anak karyawan? (y/n): ").lower() == "y"
ipk = float(input("IPK: "))
tepat_waktu = input("Pembayaran tepat waktu? (y/n): ").lower() == "y"

# Hitung diskon
total_diskon, kategori, diskon_utama, diskon_tambahan = hitung_diskon(
    ipk,
    anak_karyawan,
    tepat_waktu
)

# Hitung biaya
potongan = biaya_spp * total_diskon
biaya_final = biaya_spp - potongan

# Tampilkan hasil
print("\n" + "=" * 50)
print("HASIL PERHITUNGAN DISKON")
print("=" * 50)

print(f"Kategori diskon : {kategori}")
print(f"Diskon utama    : {diskon_utama * 100:.0f}%")
print(f"Diskon tambahan : {diskon_tambahan * 100:.0f}%")
print(f"Total diskon    : {total_diskon * 100:.0f}%")
print(f"Biaya SPP       : Rp{biaya_spp:,.0f}")
print(f"Potongan biaya  : Rp{potongan:,.0f}")
print(f"Biaya final     : Rp{biaya_final:,.0f}")