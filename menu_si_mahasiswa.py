"""Program Menu Interaktif Sistem Informasi Mahasiswa."""


# =========================
# FUNGSI STATUS MAHASISWA
# =========================

def cek_status_mahasiswa():
    print("\n=== CEK STATUS MAHASISWA ===")

    while True:
        try:
            ipk = float(input("IPK: "))
            if 0.0 <= ipk <= 4.0:
                break
            print("Error: IPK harus antara 0.0 dan 4.0.")
        except ValueError:
            print("Error: Masukkan IPK berupa angka.")

    while True:
        try:
            sks = int(input("SKS: "))
            if 0 <= sks <= 24:
                break
            print("Error: SKS harus antara 0 dan 24.")
        except ValueError:
            print("Error: Masukkan SKS berupa angka.")

    if ipk >= 2.0 and sks >= 18:
        status = "Aktif"
    elif ipk >= 1.5:
        status = "Peringatan"
    else:
        status = "Tidak Aktif"

    print(f"\nStatus Mahasiswa: {status}")


# =========================
# FUNGSI DISKON BIAYA
# =========================

def hitung_diskon():
    print("\n=== HITUNG DISKON BIAYA ===")

    while True:
        try:
            biaya_spp = float(input("Biaya SPP: Rp"))
            if biaya_spp >= 0:
                break
            print("Error: Biaya SPP tidak boleh negatif.")
        except ValueError:
            print("Error: Masukkan biaya berupa angka.")

    while True:
        anak_karyawan = input("Anak karyawan? (y/n): ").lower()
        if anak_karyawan in ["y", "n"]:
            break
        print("Error: Masukkan y atau n.")

    while True:
        try:
            ipk = float(input("IPK: "))
            if 0.0 <= ipk <= 4.0:
                break
            print("Error: IPK harus antara 0.0 dan 4.0.")
        except ValueError:
            print("Error: Masukkan IPK berupa angka.")

    while True:
        tepat_waktu = input("Pembayaran tepat waktu? (y/n): ").lower()
        if tepat_waktu in ["y", "n"]:
            break
        print("Error: Masukkan y atau n.")

    if anak_karyawan == "y":
        diskon_utama = 0.25
        kategori = "Anak Karyawan"
    elif ipk >= 3.8:
        diskon_utama = 0.20
        kategori = "Prestasi Tinggi"
    elif ipk >= 3.5:
        diskon_utama = 0.15
        kategori = "Prestasi Baik"
    elif ipk >= 3.0:
        diskon_utama = 0.10
        kategori = "IPK Memuaskan"
    else:
        diskon_utama = 0.0
        kategori = "Tidak ada diskon"

    diskon_tambahan = 0.05 if tepat_waktu == "y" else 0.0
    total_diskon = diskon_utama + diskon_tambahan

    potongan = biaya_spp * total_diskon
    biaya_final = biaya_spp - potongan

    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Kategori        : {kategori}")
    print(f"Diskon Utama    : {diskon_utama:.0%}")
    print(f"Diskon Tambahan : {diskon_tambahan:.0%}")
    print(f"Total Diskon    : {total_diskon:.0%}")
    print(f"Potongan        : Rp{potongan:,.0f}")
    print(f"Biaya Final     : Rp{biaya_final:,.0f}")


# =========================
# FUNGSI PERINGATAN STOK
# =========================

def cek_peringatan_stok():
    print("\n=== CEK PERINGATAN STOK ===")

    while True:
        try:
            stok = int(input("Jumlah stok: "))
            if stok >= 0:
                break
            print("Error: Stok tidak boleh negatif.")
        except ValueError:
            print("Error: Masukkan stok berupa angka.")

    if stok == 0:
        status = "HABIS"
        rekomendasi = "URGENT: Restock segera!"
        prioritas = "CRITICAL"
    elif stok <= 10:
        status = "RENDAH"
        rekomendasi = "Restock dalam 1-3 hari"
        prioritas = "HIGH"
    elif stok <= 20:
        status = "PERINGATAN"
        rekomendasi = "Rencanakan restock 1-2 minggu"
        prioritas = "MEDIUM"
    else:
        status = "AMAN"
        rekomendasi = "Stok mencukupi"
        prioritas = "LOW"

    print(f"\nStatus       : {status}")
    print(f"Prioritas    : {prioritas}")
    print(f"Rekomendasi  : {rekomendasi}")


# =========================
# MENU UTAMA
# =========================

while True:
    print("\n" + "=" * 40)
    print("SISTEM INFORMASI MAHASISWA")
    print("=" * 40)
    print("1. Cek Status Mahasiswa")
    print("2. Hitung Diskon Biaya")
    print("3. Cek Peringatan Stok")
    print("0. Keluar")
    print("=" * 40)

    pilihan = input("Pilih menu (1/2/3/0): ")

    if pilihan == "1":
        cek_status_mahasiswa()
    elif pilihan == "2":
        hitung_diskon()
    elif pilihan == "3":
        cek_peringatan_stok()
    elif pilihan == "0":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Error: Pilihan menu tidak valid.")