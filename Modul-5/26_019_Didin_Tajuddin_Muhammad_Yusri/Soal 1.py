def fibonacci(hari):
    if hari == 1 or hari == 2:
        return 1
    else:
        return fibonacci(hari - 1) + fibonacci(hari - 2)

print("MENGHITUNG JUMLAH PELANGGAN")

hari = int(input("Masukkan hari ke-: "))

if hari > 0:
    hasil = fibonacci(hari)

    print("\nHASIL PERHITUNGAN")
    print("Hari ke-", hari)
    print("Jumlah pelanggan:", hasil)
else:
    print("Masukkan bilangan bulat positif!")
