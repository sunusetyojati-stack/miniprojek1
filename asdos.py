#list
matkul = []
#input jumlah
n = int(input("Masukan Jumlah Matkul : "))
#input data 
for i in range(n):
    namatkul = input("Masukan Nama Matkul : ")
    sks = int(input("Masukan Jumlah SKS : "))
    nilai = int(input("Masukan Nilai : "))
    if nilai>=80:
        bobot = 4.0
    elif nilai>=70:
        bobot = 3.0
    elif nilai>=60:
        bobot = 2.0
    elif nilai>=50:
        bobot = 1.0
    else :
        bobot = 0.0
    nilaiakhir = sks*bobot
    matkul.append([namatkul, sks, nilai, bobot, nilaiakhir])
    

#tampilkan data mobil
print("\nDaftar Mobiil : ")
for m in matkul:
    print(f"{m[0]} - {m[1]} - {m[2]} - {m[3]} - {m[4]}")
total_sks = sum(m[1] for m in matkul)
print(f"Total SKS Adalah : {total_sks}")
total_nilai_akhir = sum(m[4] for m in matkul)
print(f"Total Nilai Akhir Adalah : {total_nilai_akhir}")
ipk = total_nilai_akhir/total_sks
print(f"IPK Adalah : {ipk}")