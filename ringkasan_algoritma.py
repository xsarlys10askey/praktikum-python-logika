"""Program Ringkasan Algoritma."""


# Data mahasiswa
data_mahasiswa = [
    {"nama": "Key", "status": "Aktif"},
    {"nama": "Reswan", "status": "Peringatan"},
    {"nama": "Putri", "status": "Tidak Aktif"},
    {"nama": "Raharja", "status": "Peringatan"},
    {"nama": "Selina", "status": "Aktif"},
]

# Data diskon
data_diskon = [0.30, 0.20, 0.15, 0.05, 0.00]

# Data stok
data_stok = [
    {"nama": "Buku Python", "stok": 45},
    {"nama": "Buku Database", "stok": 15},
    {"nama": "Flashdisk 16GB", "stok": 7},
    {"nama": "Kabel USB", "stok": 0},
    {"nama": "Mouse Wireless", "stok": 18},
    {"nama": "Keyboard", "stok": 25},
    {"nama": "Headset", "stok": 4},
    {"nama": "Webcam", "stok": 10},
]


# 1. Persentase mahasiswa aktif vs tidak aktif
total_mahasiswa = len(data_mahasiswa)

jumlah_aktif = sum(
    1 for mahasiswa in data_mahasiswa
    if mahasiswa["status"] == "Aktif"
)

jumlah_tidak_aktif = sum(
    1 for mahasiswa in data_mahasiswa
    if mahasiswa["status"] == "Tidak Aktif"
)

persentase_aktif = (jumlah_aktif / total_mahasiswa) * 100
persentase_tidak_aktif = (jumlah_tidak_aktif / total_mahasiswa) * 100


# 2. Rata-rata diskon
rata_rata_diskon = sum(data_diskon) / len(data_diskon)


# 3. Persentase item yang perlu restock
total_item = len(data_stok)

jumlah_restock = sum(
    1 for item in data_stok
    if item["stok"] <= 10
)

persentase_restock = (jumlah_restock / total_item) * 100


# Tampilkan hasil dalam tabel
print("=" * 60)
print("RINGKASAN ALGORITMA")
print("=" * 60)

print(f"{'Indikator':<35} {'Hasil':>15}")
print("-" * 60)
print(f"{'Mahasiswa Aktif':<35} {persentase_aktif:>14.2f}%")
print(f"{'Mahasiswa Tidak Aktif':<35} {persentase_tidak_aktif:>14.2f}%")
print(f"{'Rata-rata Diskon':<35} {rata_rata_diskon:>14.2%}")
print(f"{'Item Perlu Restock':<35} {persentase_restock:>14.2f}%")
print("=" * 60)