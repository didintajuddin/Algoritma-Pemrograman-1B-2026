total_gaji = 0
gaji_harian = 100000

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = -1
    while lembur not in [0, 1, 2, 3, 4, 6, 8]:
        lembur = int(input("Masukkan jam lembur: "))

        if lembur > 8:
            print("Lembur melebihi batas!")
        elif lembur not in [0, 1, 2, 3, 4, 6, 8]:
            print("Jam lembur tidak sesuai. Coba lagi.")

    if lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    else:
        upah_lembur = 300000

    shift = input("Shift malam? (ya/tidak): ")

    while shift != "ya" and shift != "tidak":
        print("Masukkan ya atau tidak!")
        shift = input("Shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji_harian + upah_lembur + tambahan_shift
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji 7 hari: Rp", total_gaji)