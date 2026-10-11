"""Program Peringatan Stok Barang."""

# Konstanta aturan bisnis
BATAS_AMAN = 20
BATAS_PERINGATAN = 10


def cek_status_stok(stok):
    """Menentukan status, rekomendasi, dan prioritas stok."""
    if stok == 0:
        return "HABIS", "URGENT: Restock segera!", "CRITICAL"
    elif stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari", "HIGH"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu", "MEDIUM"
    else:
        return "AMAN", "Stok mencukupi", "LOW"


# Data inventaris
inventaris = [
    {"kode": "B001", "nama": "Buku Python", "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database", "stok": 15, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB", "stok": 7, "harga": 50000},
    {"kode": "B004", "nama": "Kabel USB", "stok": 0, "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless", "stok": 18, "harga": 120000},
    {"kode": "B006", "nama": "Keyboard", "stok": 25, "harga": 150000},
    {"kode": "B007", "nama": "Headset", "stok": 4, "harga": 100000},
    {"kode": "B008", "nama": "Webcam", "stok": 10, "harga": 200000},
]


# Proses dan laporan
print("=" * 75)
print("LAPORAN STATUS INVENTARIS")
print("=" * 75)

total_nilai = 0
count_perlu_tindakan = 0

for item in inventaris:
    status, rekomendasi, prioritas = cek_status_stok(item["stok"])

    nilai = item["stok"] * item["harga"]
    total_nilai += nilai

    if prioritas in ["HIGH", "CRITICAL"]:
        count_perlu_tindakan += 1

    print(
        f"{item['kode']} {item['nama']:<18} "
        f"Stok:{item['stok']:>3} "
        f"Status:{status:<12} "
        f"[{prioritas}]"
    )

    if prioritas != "LOW":
        print(f" -> {rekomendasi}")


# Ringkasan
print("\n" + "=" * 75)
print("RINGKASAN")
print("=" * 75)

print(f"Total Nilai Inventaris : Rp{total_nilai:,}")
print(
    f"Item Perlu Tindakan   : "
    f"{count_perlu_tindakan} dari {len(inventaris)}"
)