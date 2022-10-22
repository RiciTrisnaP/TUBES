
import time

print("=========SELAMAT DATANG========")
time.sleep(1.5)

isi = [
    (" Cappuchino "),
    (" Macchiato  "),
    (" Dolce      "),
    (" Caffe Latte"),
    (" Espresso   "),
    (" Chocolate  "),
    (" White Coffe"),
    (" Mocha      ")]
harga_isi = [(13000), (12000), (11000), (12000),
             (9000), (14000), (13000), (12000)]

size_list = [
    (" Small "),
    (" Medium"),
    (" Large ")]
harga_size = [(0), (2000), (4000)]

list_nominal = [(1000), (2000), (5000), (10000), (20000)]
lanjut = True
total_uang = 0
money_stored = 0

while lanjut:
    # print("Pilih nominal uang yang dimasukkan")
    for i in range(5):
        print(f"({i+1})", "Rp" + str(list_nominal[i]))

    # nominal = int(input("Pilih nominal: "))
    nominal = int(input("Pilih nominal uang yang dimasukkan: "))
    lembar = int(input("Jumlah lembar nominal: "))
    total_uang += list_nominal[nominal-1]*lembar
    print("Masukkan uang lagi?")
    print(" (1) Ya\n", "(2) Tidak")
    p = int(input())
    print("")
    if p == 2:
        lanjut = False

money_stored += total_uang

print(f"Jumlah uang yang dimasukkan: Rp{total_uang}")
time.sleep(1.5)
# print("Silahkan ambil cup sesuai ukuran")


# print("Pilih Minuman\n", " ")
for i in range(8):
    print(f"({i+1})", isi[i], harga_isi[i])

minum = int(input("Pilih minuman: "))

# print("Pilih Ukuran\n", " ")
print("")
for i in range(3):
    print(f"({i+1})", size_list[i], "++", harga_size[i])

size = int(input("Pilih ukuran: "))

print(f"\nAnda memilih {isi[minum-1]} ukuran {size_list[size-1]}")
time.sleep(1)
print("Brewing...")
time.sleep(1)

if size == 1:
    for i in range(3):
        print(i+1)
        time.sleep(1.3)
if size == 2:
    for i in range(5):
        print(i+1)
        time.sleep(1.3)
if size == 3:
    for i in range(7):
        print(i+1)
        time.sleep(1.3)
print(
    "Silahkan Ambil\n",
    "Selamat Menikmati")
