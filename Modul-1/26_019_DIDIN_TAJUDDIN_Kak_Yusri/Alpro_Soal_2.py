# Program menghitung volume kerucut
# input
r = float(input("masukan jari-jari alas (cm):"))
t = float(input("masukan tinggi kerucut (cm):"))

# menghitung volume kerucut
pi = 22/7
volume = (1/3) * pi * r * r * t

# output
print("volume kerucut adalah:", volume, "cm³")  