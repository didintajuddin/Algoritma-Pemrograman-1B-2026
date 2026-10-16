n = 0
while True:
    n = int(input("Masukkan angka (2-15): "))
    if 2 <= n <= 15:
        break
    else:
        print("Input tidak valid. masukkan angka antara 2 hingga 15.")

for i in range(1, n + 1):
    naik = ""
    for angka in range(1, i + 1):
        naik += str(angka % 10)

    turun = ""
    for angka in range(i - 1, 0, -1):
        turun += str(angka % 10)

    print((naik + turun).center(2 * n - 1))

for i in range(n - 1, 0, -1):
    naik = ""
    for angka in range(1, i + 1):
        naik += str(angka % 10)

    turun = ""
    for angka in range(i - 1, 0, -1):
        turun += str(angka % 10)

    print((naik + turun).center(2 * n - 1))