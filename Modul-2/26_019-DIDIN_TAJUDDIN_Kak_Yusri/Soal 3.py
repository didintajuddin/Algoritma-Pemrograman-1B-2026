suhu = int(input("Masukkan suhu reaktor: "))
tekanan = int(input("Masukkan tekanan gas: "))


if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu < 1000:
    if suhu > 500:
        status = "Cek tekanan gas"
    elif tekanan > 30:
        status = "peringatan Tekanan Tidak Stabil"
    else:
        status = "Belum Cukup Panas."

status_pompa = "Pompa Maksimal" if suhu >800 else "Pompa Normal"

print("Suhu Reaktor :", suhu, "°C")
print("Tekanan Gas  :", tekanan, "Bar")
print("Status Bahaya:", status)
print("Status Pompa :", status_pompa)