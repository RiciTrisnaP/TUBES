#test gabung

import time

total_uang = 0
money_stored = 0
proses_minum = False
uang_proses = 0
list_nominal = [(1000), (2000), (5000), (10000), (20000)]

isi = [
(" Cappuchino "), 
(" Macchiato  "), 
(" Dolce      "), 
(" Caffe Latte"), 
(" Espresso   "), 
(" Chocolate  "), 
(" White Coffe"), 
(" Mocha      "),
(" Americano  ")]
harga_isi = [(13000), (12000), (11000), (12000), (9000), (14000), (13000), (12000), (10000)]

size_list = [
(" Small "), 
(" Medium"), 
(" Large ")]
harga_size = [(0), (2000), (4000)]

sugar_list = [
    (" No sugar    "),
    (" Less sugar  "), 
    (" Normal sugar"), 
    (" Extra sugar ")]

hotcold = [
    (" Hot  "), 
    (" Cold ")]

def input_uang ():
    global total_uang
    global money_stored
    lanjut = True
    while lanjut:
        print("Pilih nominal uang yang dimasukkan")
        for i in range (5):
            print(f"({i+1})", "Rp"+ str(list_nominal[i]))
        nominal = int(input("Pilih nominal: "))
        lembar= int(input("Jumlah lembar nominal: "))
        total_uang += list_nominal[nominal-1]*lembar
        print("Masukkan uang lagi?")
        print(" (1) Ya\n", "(2) Tidak")
        p = int(input())
        if p == 2:
            lanjut=False
    money_stored += total_uang
    print(f"Jumlah uang yang dimasukkan: Rp{total_uang}")

def cek_uang():
    global uang_proses
    global proses_minum
    harga_total = harga_isi[minum-1] + harga_size[size-1]
    uang_proses += total_uang - harga_total

    if uang_proses < 0:
        print("uang anda tidak mecukupi")
        time.sleep(1)
        print("silahkan masukkan uang lagi atau pilih minum sesuai jumlah uang")
        uang_proses += harga_total
        proses_minum = False
    elif uang_proses > 0 or uang_proses == 0:
        proses_minum = True


def pilih_minum():
    global hot
    global sugar
    global size
    global minum
    global total_uang
    print ("Pilih Minuman\n" , " ")
    for i in range (9):
        print (f"({i+1})",isi[i], harga_isi[i])
    minum = int(input("Pilih minuman: "))
    print ("(1) Hot/(2) Cold")
    hot = int(input())
    print ("Pilih Ukuran\n", " ")
    for i in range (3):
        print (f"({i+1})", size_list[i],"++", harga_size[i])
    size = int(input("Pilih ukuran: "))
    print ("Tingkat kemanisan\n", " ")
    for i in range (4):
        print (f"({i+1})", sugar_list[i])
    sugar = int(input("Pilih: "))
    cek_uang()
    if proses_minum:
        print(f"Anda memilih {isi[minum-1]} ukuran {size_list[size-1]}, {sugar_list[sugar-1]}")
    elif proses_minum == False:
        print("(1) Masukkan uang lagi\n"+
        "(2) Pilih Minum lain")
        a = int(input())
        if a == 1:
            total_uang = 0
            input_uang()
            time.sleep(2)
            pilih_minum()
        elif a == 2:
            total_uang = 0
            pilih_minum()


def brewing():
    print("Brewing...")
    time.sleep(1)
    if size == 1:
        for i in range (3):
            print(i+1)
            time.sleep(1.3)
    if size == 2:
        for i in range (5):
            print(i+1)
            time.sleep(1.3)
    if size == 3:
        for i in range (7):
            print(i+1)
            time.sleep(1.3)
    print("==Minuman siap==")
    time.sleep(1)
    print(
        " Silahkan Ambil\n" + 
        "Selamat Menikmati")


print("=========SELAMAT DATANG========")

print(" ")
print("            MENU  ")
for i in range (9):
        print (f"({i+1})",isi[i], harga_isi[i])
print(" ")
print("        Pilihan Size ")
for i in range (3):
        print (f"({i+1})", size_list[i],"++", harga_size[i])

print(" ")

print("tekan 1 untuk melanjutkan")

start = int(input())
proses = True


if start == 1:
    input_uang()
    time.sleep(2)
    while proses:
        pilih_minum()
        time.sleep(1.5)
        brewing()
        total_uang = 0
        if uang_proses == 0:
            print("Terima kasih")
            proses = False
        elif uang_proses > 0:
            print(f"uang tersisa Rp{uang_proses}")
            time.sleep(1)
            print("Beli lagi?")
            time.sleep(1.5)
            print(" (1) Ya\n", "(2) Tidak")
            q = int(input())
            if q == 2:
                print("Terima kasih")
                proses = False
else:
    print("Terima kasih")







    
