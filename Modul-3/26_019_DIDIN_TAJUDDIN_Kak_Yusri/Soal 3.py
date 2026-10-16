jumlah_mahasiswa = 10
data_mahasiswa = []

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai_akhir = 0

for i in range(1, jumlah_mahasiswa + 1):
    print("Mahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    data_mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir,
        "kategori": kategori
    })
    total_nilai_akhir += nilai_akhir

print("\n DAFTAR NILAI MAHASISWA ")

for m in data_mahasiswa:
    print("Nama:", m["nama"])
    print("Nilai tugas:", m["tugas"])
    print("Nilai UTS:", m["uts"])
    print("Nilai UAS:", m["uas"])
    print("Nilai akhir:", round(m["akhir"], 2))
    print("Kategori:", m["kategori"])

tertinggi = data_mahasiswa[0]
terendah = data_mahasiswa[0]

for mahasiswa in data_mahasiswa:
    if mahasiswa["akhir"] > tertinggi["akhir"]:
        tertinggi = mahasiswa

    if mahasiswa["akhir"] < terendah["akhir"]:
        terendah = mahasiswa

rata_rata = total_nilai_akhir / jumlah_mahasiswa

print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)

print("\nNilai akhir tertinggi:", round(tertinggi["akhir"], 2))
print("Nama mahasiswa:", tertinggi["nama"])

print("\nNilai akhir terendah:", round(terendah["akhir"], 2))
print("Nama mahasiswa:", terendah["nama"])
