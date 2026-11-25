inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status PC (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])

def evaluasi(data):
    ram = int(data[2])

    if data[1] == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("\nHasil Evaluasi:")

for data in inventaris:
    try:
        hasil = evaluasi(data)
    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + data[0] + '", "Status": "' + hasil + '" }')