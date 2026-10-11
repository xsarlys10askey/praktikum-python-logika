"""Program Validasi Data Mahasiswa."""


def validasi_nim(nim):
    """Validasi NIM 10 digit dengan tahun 2000-2037."""
    error = []

    if not isinstance(nim, str):
        error.append("NIM harus berupa string")
    elif len(nim) != 10:
        error.append("NIM harus 10 digit")
    elif not nim.isdigit():
        error.append("NIM harus berisi angka saja")
    else:
        tahun = int(nim[:4])
        if tahun < 2000 or tahun > 2037:
            error.append("Tahun masuk harus antara 2000-2037")

    return error


def validasi_ipk(ipk):
    """Validasi IPK 0.0-4.0."""
    error = []

    if not isinstance(ipk, (int, float)):
        error.append("IPK harus berupa angka")
    elif ipk < 0.0 or ipk > 4.0:
        error.append("IPK harus antara 0.0-4.0")

    return error


def validasi_sks(sks):
    """Validasi SKS 0-24."""
    error = []

    if not isinstance(sks, int):
        error.append("SKS harus berupa angka bulat")
    elif sks < 0 or sks > 24:
        error.append("SKS harus antara 0-24")

    return error


def validasi_semester(semester):
    """Validasi semester 1-14."""
    error = []

    if not isinstance(semester, int):
        error.append("Semester harus berupa angka bulat")
    elif semester < 1 or semester > 14:
        error.append("Semester harus antara 1-14")

    return error


def validasi_data_mahasiswa(nim, ipk, sks, semester):
    """Menggabungkan seluruh validasi data mahasiswa."""
    errors = []

    errors.extend(validasi_nim(nim))
    errors.extend(validasi_ipk(ipk))
    errors.extend(validasi_sks(sks))
    errors.extend(validasi_semester(semester))

    return errors


# Input data mahasiswa
print("=== VALIDASI DATA MAHASISWA ===")

nim = input("NIM: ")

while True:
    try:
        ipk = float(input("IPK: "))
        break
    except ValueError:
        print("Error: IPK harus berupa angka.")

while True:
    try:
        sks = int(input("SKS: "))
        break
    except ValueError:
        print("Error: SKS harus berupa angka bulat.")

while True:
    try:
        semester = int(input("Semester: "))
        break
    except ValueError:
        print("Error: Semester harus berupa angka bulat.")


# Validasi
errors = validasi_data_mahasiswa(nim, ipk, sks, semester)


# Tampilkan hasil
print("\n=== HASIL VALIDASI ===")

if len(errors) == 0:
    print("Data mahasiswa VALID.")
else:
    print("Data mahasiswa TIDAK VALID.")
    print("Daftar error:")
    for error in errors:
        print(f"- {error}")