asisten_awal = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

tambahan = input("\nMasukkan nama asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari_tugas = []

while True:
    hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if hari == "cukup":
        break

    hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)

nama_pengecualian = input("\nNama asisten yang dikecualikan: ")
hari_pengecualian = input("Hari yang dikecualikan: ")

print("\nDaftar Jadwal Shift:")

for asisten in asisten_akhir:
    for hari in hari_tugas:

        if asisten == nama_pengecualian and hari == hari_pengecualian:
            continue

        print(asisten, "-", hari)
