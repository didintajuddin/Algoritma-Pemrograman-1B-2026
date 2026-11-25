baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print(f"\nMemeriksa baris ke-, {i}")

    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Lampu nomor {j}: mengalami gangguan")
        else:
            print(f"Lampu nomor {j}: berfungsi normal")

print("\nPeriksa sumber listrik utama taman.")