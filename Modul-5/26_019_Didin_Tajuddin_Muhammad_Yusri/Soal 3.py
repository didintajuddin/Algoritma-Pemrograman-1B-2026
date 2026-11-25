def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        Grade = "A"
    elif nilai_akhir >= 70:
        Grade = "B"
    elif nilai_akhir >= 55:
        Grade = "C"
    else:
        Grade = "D"

    if Grade == "A" or Grade == "B" or Grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("\n===== HASIL NILAI MAHASISWA =====")
    print("Nama         :", nama)
    print("Nilai Tugas  :", tugas)
    print("Nilai UTS    :", uts)
    print("Nilai UAS    :", uas)
    print("Nilai Akhir  :", round(nilai_akhir, 2))
    print("Grade        :", Grade)
    print("Status       :", status)

print("PROGRAM PENGHITUNGAN NILAI MAHASISWA")

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)
