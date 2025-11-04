import pandas as pd
pd.options.display.float_format
import matplotlib.pyplot as plt


# 1️⃣ Import file Excel
file_path = "Data Wisudawan.xlsx"
data = pd.read_excel(file_path)

# 2️⃣ Hitung jumlah wisudawan per program studi
jumlah_wisudawan = data['Program Studi'].value_counts()
print("Jumlah Wisudawan Per Program Studi : ")
print(jumlah_wisudawan)

# 3️⃣ Fungsi untuk menentukan Grade berdasarkan IPK
def grade_ipk(x):
    if 3.75 <= x <= 4.0:
        return 'A'
    elif 3.50 <= x <= 3.74:
        return 'B+'
    elif 3.00 <= x <= 3.49:
        return 'B'
    elif 2.50 <= x <= 2.99:
        return 'C'
    else:
        return 'D'

data['Grade'] = data['IPK'].apply(grade_ipk)

# 4️⃣ Fungsi klasifikasi predikat kelulusan
def predikat_kelulusan(y, lama_studi):
    if y >= 3.75 and lama_studi <= 8:
        return 'Cumlaude (Dengan Pujian)'
    elif y >= 3.50 and lama_studi <= 9:
        return 'Sangat Memuaskan'
    elif 3.00 <= y <= 3.49:
        return 'Memuaskan'
    else:
        return 'Cukup'

data['Predikat Kelulusan'] = data.apply(lambda row: predikat_kelulusan(row['IPK'], row['Lama Studi']), axis=1)

# 5️⃣ Simpan hasil ke Excel baru
output_file = "rekap_wisuda_final.xlsx"
kolom_akhir = ['NIM', 'Nama Mahasiswa', 'Program Studi', 'IPK', 'Lama Studi', 'Grade', 'Predikat Kelulusan', 'Tahun Wisuda']
data['NIM'] = data['NIM'].astype(str)
data['Tahun Wisuda'] = data['Tahun Wisuda'].astype(str)
data[kolom_akhir].to_excel(output_file, index=False)
print(f"✅ Data berhasil disimpan ke '{output_file}'.")

# 6️⃣ Visualisasi Grafik Batang
plt.figure(figsize=(10, 6))
jumlah_wisudawan.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Jumlah Wisudawan Per Program Studi')
plt.xlabel('Program Studi')
plt.ylabel('Jumlah Wisudawan')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(jumlah_wisudawan):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.show()

# 7️⃣ Hitung persentase predikat kelulusan
jumlah_predikat = data['Predikat Kelulusan'].value_counts()
total_wisudawan = len(data)
persentase_predikat = (jumlah_predikat / total_wisudawan) * 100

# 8️⃣ Visualisasi Pie Chart Predikat Kelulusan
plt.figure(figsize=(8, 8))
plt.pie(
    jumlah_predikat,
    labels=[f"{label}\n{persentase:.1f}%" for label, persentase in zip(jumlah_predikat.index, persentase_predikat)],
    startangle=140,
    colors=plt.cm.Pastel1.colors,
    wedgeprops={'edgecolor': 'black'}
)
plt.title('Persentase Predikat Kelulusan Wisudawan')
plt.tight_layout()
plt.show()

#9️⃣ Grafik perbandingan antar program studi
plt.figure(figsize=(10, 6))
data.groupby('Program Studi')['IPK'].mean().sort_values().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Rata-rata IPK per Program Studi')
plt.xlabel('Program Studi')
plt.ylabel('Rata-rata IPK')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(data.groupby('Program Studi')['IPK'].mean().sort_values()):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom')
plt.tight_layout()
plt.show()

#🔟 10 Mahasiswa dengan ipk tertinggi
top_10_ipk = data.nlargest(10, 'IPK')[['NIM', 'Nama Mahasiswa', 'Program Studi', 'IPK']]
plt.figure(figsize=(10, 6))
plt.barh(top_10_ipk['Nama Mahasiswa'], top_10_ipk['IPK'], color='orange', edgecolor='black')
plt.title('10 Mahasiswa dengan IPK Tertinggi')
plt.xlabel('IPK')
plt.ylabel('Nama Mahasiswa')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i , v in enumerate(top_10_ipk['IPK']):
    plt.text(v + 0.02, i, f"{v:.2f}", va='center')
plt.tight_layout()
plt.show()

#1️⃣1️⃣ 1 Mahasiswa dengan nilai tertinggi per program studi
top_ipk_per_prodi = data.loc[data.groupby('Program Studi')['IPK'].idxmax()][['NIM', 'Nama Mahasiswa', 'Program Studi', 'IPK']]
plt.figure(figsize=(10, 6))
plt.barh(top_ipk_per_prodi['Nama Mahasiswa'] + ' (' + top_ipk_per_prodi['Program Studi'] + ')', top_ipk_per_prodi['IPK'], color='purple', edgecolor='black')
plt.title('Mahasiswa dengan IPK Tertinggi per Program Studi')
plt.xlabel('IPK')
plt.ylabel('Program Studi')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(top_ipk_per_prodi['IPK']):
    plt.text(v + 0.02, i, f"{v:.2f}", va='center')
plt.tight_layout()
plt.show()
