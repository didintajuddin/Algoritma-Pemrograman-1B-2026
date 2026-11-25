anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    anggota.append(nama)

print("\nHasil Pemeriksaan Nama:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "- Nama tidak valid")
    else:
        print(nama, "- Nama valid")

hapus = input("\nMasukkan nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan dalam daftar anggota.")

print("\nDaftar Anggota Akhir:", anggota)
