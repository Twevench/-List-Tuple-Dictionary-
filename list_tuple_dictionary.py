# Program sederhana untuk menyimpan data siswa

# List berisi tuple data siswa (nama, usia, kelas)
siswa_list = [
    ("Andi", 12, "6A"),
    ("Budi", 13, "6B"),
    ("Citra", 12, "6A")
]

# Dictionary berisi alamat siswa dengan nama sebagai kunci
alamat_dict = {
    "Andi": "Jl. Merpati No. 1",
    "Budi": "Jl. Elang No. 2",
    "Citra": "Jl. Kenari No. 3"
}

# Menampilkan data siswa
print("Data Siswa:")
for siswa in siswa_list:
    print(f"Nama: {siswa[0]}, Usia: {siswa[1]}, Kelas: {siswa[2]}")

# Menampilkan alamat siswa berdasarkan nama
print("\nAlamat Siswa:")
for nama, alamat in alamat_dict.items():
    print(f"Nama: {nama}, Alamat: {alamat}")
