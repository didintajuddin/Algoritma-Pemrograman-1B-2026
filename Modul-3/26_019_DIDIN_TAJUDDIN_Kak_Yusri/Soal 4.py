jumlah_mahasiswa = 10
beasiswa_penuh = 0

for i in range(1, jumlah_mahasiswa + 1):
    print("\nMahasiswa ke-", i)
    
    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("\nNama:", nama)
        print("Tidak memenuhi syarat karena IPK kurang dari 3,00")
        continue
    penghasilan = float(input("Masukkan penghasilan orang tua per bulan: Rp"))

    if penghasilan <= 3000000:
        status = "Mendapat beasiswa penuh"
        beasiswa_penuh += 1

    elif penghasilan <= 5000000:
        status = "Mendapat beasiswa sebagian"

    else:
        status = "Tidak mendapat beasiswa"

    print("\nNama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)
    print("Jumlah penerima beasiswa penuh:", beasiswa_penuh)

    if beasiswa_penuh == 3:
        print("\nKuota 3 beasiswa penuh telah terpenuhi.")
        break

print("\nSeleksi beasiswa selesai.")