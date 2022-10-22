# part two

# uang

import time

list_nominal = [(1000), (2000), (5000), (10000), (20000)]
lanjut = True
total_uang = 0
money_stored = 0
while lanjut:
    print("Pilih nominal uang yang dimasukkan")
    for i in range(5):
        print(f"({i+1})", "Rp" + str(list_nominal[i]))

    nominal = int(input("Pilih nominal: "))
    lembar = int(input("Jumlah lembar nominal: "))
    total_uang += list_nominal[nominal-1]*lembar
    print("Masukkan uang lagi?")
    print(" (1) Ya\n", "(2) Tidak")
    p = int(input())
    if p == 2:
        lanjut = False

money_stored += total_uang

print(f"Jumlah uang yang dimasukkan: Rp{total_uang}")
time.sleep(1.5)
print("Silahkan ambil cup sesuai ukuran")
