undangan = set()
webinar_a = set()
webinar_b = set()

print("===== INPUT DATA WEBINAR =====")

data_undangan = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan.update(map(str.strip, data_undangan.split(",")))
undangan.discard("")

data_a = input("Masukkan peserta Webinar A (pisahkan dengan koma): ")
webinar_a.update(map(str.strip, data_a.split(",")))
webinar_a.discard("")

data_b = input("Masukkan peserta Webinar B (pisahkan dengan koma): ")
webinar_b.update(map(str.strip, data_b.split(",")))
webinar_b.discard("")

semua_peserta = webinar_a | webinar_b
peserta_keduanya = webinar_a & webinar_b
peserta_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - (webinar_a | webinar_b)

print("\n===== HASIL PENGELOLAAN DATA =====")
print("Semua peserta webinar       :", sorted(semua_peserta))
print("Peserta kedua webinar       :", sorted(peserta_keduanya))
print("Peserta hanya satu webinar  :", sorted(peserta_satu))
print("Undangan yang tidak hadir   :", sorted(tidak_hadir))
