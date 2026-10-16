jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukan jarak penumpang:"))
    if jarak == 0:
            break
    if jarak < 0:
        print("jarak tidak valid")
        continue
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak-5) * 1000
    else:
        tarif = 13000 + (jarak-15) *500
    
    jumlah_penumpang += 1    
    
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
    print("Tarif yang harus dibayar: Rp", tarif)

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang

print("Jarak_terjauh:", jarak_terjauh, "km")
print("Rata-rata jarak:", round(rata_rata, 2), "km")
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)