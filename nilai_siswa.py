nilaiA = int(input("Masukkan angka nilai siswa (A): "))
nilaiB = int(input("Masukkan angka nilai siswa (B): "))
rataRata = (nilaiA + nilaiB) / 2
if rataRata >= 65:
    status = ("Lulus")   
else :
    status = ("Tidak Lulus")

print("nilaiA =", nilaiA)
print("nilaiB =", nilaiB)
print ("Rata-rata nilai siswa adalah : ", rataRata)
print("Status nilai siswa adalah : ", status)

