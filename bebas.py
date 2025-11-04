# ================================================
# Program: Analisis Nilai Mahasiswa dari Excel
# Library: pandas dan openpyxl
# ================================================

import pandas as pd

# 1️⃣ Import file Excel
file_path = "data_mahasiswa.xlsx"
data = pd.read_excel(file_path)

# 2️⃣ Hitung rata-rata untuk setiap mahasiswa
data['Rata-rata'] = data[['Nilai 1', 'Nilai 2', 'Nilai 3']].mean(axis=1)
data['Rata-rata'] = data['Rata-rata'].round(0)

# 3️⃣ Cari mahasiswa dengan nilai rata-rata tertinggi
nilai_tertinggi = data['Rata-rata'].max()
terbaik = data[data['Rata-rata'] == nilai_tertinggi]

# 4️⃣ Tampilkan hasil di console
print("=== Data Mahasiswa dengan Nilai Rata-rata ===")
print(data)
print("\nMahasiswa dengan Nilai Tertinggi:")
print(terbaik[['NIM', 'Nama Mahasiswa', 'Rata-rata']])

# 5️⃣ Simpan ke file Excel baru
output_file = "hasil_mahasiswa.xlsx"
data.to_excel(output_file, index=False)

print(f"\nFile hasil telah disimpan ke: {output_file}")