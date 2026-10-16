pin = int(input("Masukkan 3 pin: "))
jam = int(input("Masukkan jam 0-23: "))

digit1 = pin //100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else: 
    status = "Akses ditolak seluruhnya"

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Digit 1:", digit1)
print("Digit 2:", digit2)
print("Digit 3:", digit3)
print("Status Garasi:", status)
print("Status CCTV:", status_cctv)