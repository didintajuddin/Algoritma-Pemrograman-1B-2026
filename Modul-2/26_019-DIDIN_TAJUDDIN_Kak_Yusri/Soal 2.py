total_belanja = int(input("Masukan total belanja: Rp."))

if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50/100
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80/100
elif total_belanja >= 200000:
    total_bayar = total_belanja * 90/100
else:
    total_bayar = total_belanja

status_poin = ("Poin Bertambah" if total_belanja > 0 else "Poin Tidak Bertambah" )

print("Total Belanja Sebelum Diskon:", total_belanja)
print("Total Harga Akhir:", total_bayar)
print("Status Poin:", status_poin)

