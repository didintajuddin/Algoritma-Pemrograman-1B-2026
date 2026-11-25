tugas = {}

while True:
    print("\n===== MENU TO-DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Hitung Tugas Selesai dan Belum Selesai")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ").strip()

        if nama == "":
            print("Nama tugas tidak boleh kosong!")
        elif nama in tugas:
            print("Tugas sudah tersedia!")
        else:
            tugas[nama] = "Belum selesai"
            print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            print("\n===== DAFTAR TUGAS =====")
            for nama, status in tugas.items():
                print(f"{nama} : {status}")

    elif pilihan == "3":
        nama = input("Masukkan nama tugas yang selesai: ").strip()

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas yang ingin dihapus: ").strip()

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0

        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("\n===== JUMLAH TUGAS =====")
        print("Tugas selesai       :", selesai)
        print("Tugas belum selesai :", belum_selesai)

    elif pilihan == "6":
        print("Program To-Do List selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")
