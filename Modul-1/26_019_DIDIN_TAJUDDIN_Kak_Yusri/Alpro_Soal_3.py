# program menghitung kebuutuhan bensin dimas

jarak_satu_arah = 100               # jarak satu arah 
pemakaian_bensin = 40               # kilometer per liter
sisa_bensin = 1.5                   # liter
harga_bensin = 10000                # ribu per liter

# menghitung jarak pulang pergi
total_jarak = jarak_satu_arah * 2

# menghitung kebutuhan bensin
total_bensin = total_jarak / pemakaian_bensin

# menghitung kebutuhan bensin yang harus dibeli
beli_bensin = total_bensin - sisa_bensin

# menghitung biaya bensin 
total_biaya = beli_bensin * harga_bensin

# output  
print(("Total jarak pulang pergi adalah: "), total_jarak, "km")
print(("Total bensin yang dibutuhkan adalah: "), total_bensin, "liter")
print(("Total bensin yang harus dibeli adalah: "), beli_bensin, "liter")
print(("Total biaya bensin adalah: "), total_biaya, "rupiah")