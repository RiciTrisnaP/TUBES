# part three

# sistem beli

import time

harga_isi = [(13000), (12000), (11000), (12000),
             (9000), (14000), (13000), (12000)]
harga_size = [(0), (2000), (4000)]

total_uang = 20000  # asusmsi

minum = int(input("Pilih minuman: "))
size = int(input("Pilih ukuran: "))

harga_total = harga_isi[minum-1] + harga_size[size-1]
uang_sisa = total_uang - harga_total

if uang_sisa < 0:
    print("uang anda tidak mecukupi")
    time.sleep(1)
    print("silahkan masukkan uang atau pilih minum sesuai jumalah uang")
    uang_sisa = total_uang

if uang_sisa == 0:
    print("Terima kasih")

if uang_sisa > 0:
    print(f"uang tersisa Rp{uang_sisa}")
    time.sleep(1)
    print("Beli lagi?")
    time.sleep(1.5)
    print(" (1) Ya\n", "(2) Tidak")
    q = int(input())
