# test gabung
import time

total_uang = 0
uang_masuk = 0
proses_minum = False
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
harga_isi = [(13000), (12000), (11000), (12000), (9000),
             (14000), (13000), (12000), (10000)]

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


# def cek_input_valid():
#     pass


def input_uang():
    global total_uang
    global uang_masuk
    lanjut = True
    uang_masuk = 0
    while lanjut:
        print("\nPilih nominal uang yang dimasukkan")
        for i in range(5):
            print(f"({i+1})", "Rp" + str(list_nominal[i]))
        nominal = input("Pilih nominal: ")
        while nominal not in ["1", "2", "3", "4", "5"]:
            print("Hanya menerima input 1 sampai 5")
            nominal = input("Pilih nominal: ")
        lembar = input("Jumlah lembar nominal: ")
        while lembar.isdigit() == False:
            print("Hanya menerima input bilangan bulat positif")
            lembar = input("Jumlah lembar nominal: ")
        # while lembar not in ""
        uang_masuk += list_nominal[int(nominal)-1]*int(lembar)
        total_uang += list_nominal[int(nominal)-1]*int(lembar)
        p = "0"
        while p != "1" and p != "2":
            print("Masukkan uang lagi?")
            p = input(" (1) Ya / (2) Tidak: ")
            if p == "1":
                pass
            elif p == "2":
                lanjut = False
            else:
                print("Hanya menerima masukkan 1 atau 2")
    # money_stored += total_uang
    print(f"\nJumlah uang yang dimasukkan: Rp{uang_masuk}")
    # time.sleep(1)


def cek_uang():
    global proses_minum
    global total_uang
    harga_total = harga_isi[int(minum)-1] + harga_size[int(size)-1]

    if total_uang < harga_total:
        print("uang anda tidak mencukupi")
        time.sleep(1)
        print("silahkan masukkan uang lagi atau pilih minum sesuai jumlah uang")
        proses_minum = False
    else:
        proses_minum = True
        total_uang -= harga_total


def pilih_minum():
    global hot
    global sugar
    global size
    global minum
    global total_uang
    print(f"Jumlah uang Anda: Rp{total_uang}")
    print("            MENU  ")
    for i in range(9):
        print(f"({i+1})", isi[i], harga_isi[i])
    minum = input("Pilih minuman: ")
    while minum not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("            MENU  ")
        for i in range(9):
            print(f"({i+1})", isi[i], harga_isi[i])
        print("Maaf hanya menerima input dari 1 sampai 9")
        minum = input("Pilih minuman: ")
    hot = input(" (1) Hot / (2) Cold: ")
    while hot != "1" and hot != "2":
        print("Maaf hanya menerima input 1 atau 2")
        hot = input(" (1) Hot / (2) Cold: ")
    print("\nPilih Ukuran", " ")
    for i in range(3):
        print(f"({i+1})", size_list[i], "++", harga_size[i])
    size = input("Pilih ukuran: ")
    while size not in ["1", "2", "3"]:
        print("\nPilih Ukuran", " ")
        for i in range(3):
            print(f"({i+1})", size_list[i], "++", harga_size[i])
        print("Maaf hanya menerima input 1, 2 atau 3")
        size = input("Pilih ukuran: ")
    print("\nTingkat kemanisan", " ")
    for i in range(4):
        print(f"({i+1})", sugar_list[i])
    sugar = input("Pilih: ")
    while sugar not in ["1", "2", "3", "4"]:
        print("\nTingkat kemanisan", " ")
        for i in range(4):
            print(f"({i+1})", sugar_list[i])
        print("Maaf hanya menerima input dari 1 sampai 4")
        sugar = input("Pilih: ")
    cek_uang()
    if proses_minum:
        print(
            f"Anda memilih {hotcold[int(hot)-1]} {isi[int(minum)-1]} ukuran {size_list[int(size)-1]}, {sugar_list[int(sugar)-1]}")
    elif proses_minum == False:
        a = input("(1) Masukkan uang lagi / (2) Pilih Minum lain: ")
        while a != "1" and a != "2":
            print("Maaf hanya menerima input 1 atau 2")
            a = input("(1) Masukkan uang lagi / (2) Pilih Minum lain: ")
        if a == "1":
            input_uang()
            time.sleep(2)
            pilih_minum()
        elif a == "2":
            pilih_minum()


def brewing():
    print("Brewing...")
    time.sleep(1)
    if size == "1":
        for i in range(3):
            print(i+1)
            time.sleep(1.3)
    if size == "2":
        for i in range(5):
            print(i+1)
            time.sleep(1.3)
    if size == "3":
        for i in range(7):
            print(i+1)
            time.sleep(1.3)
    print("==Minuman siap==")
    time.sleep(1)
    print(
        " Silahkan Ambil\n" +
        "Selamat Menikmati")


print("=========SELAMAT DATANG========")
time.sleep(1)
print(" ")
print("            MENU  ")
for i in range(9):
    print(f"({i+1})", isi[i], harga_isi[i])
print(" ")
time.sleep(2)
print("        Pilihan Size ")
for i in range(3):
    print(f"({i+1})", size_list[i], "++", harga_size[i])
time.sleep(2)

proses = True
input_uang()
time.sleep(2)
while proses:
    pilih_minum()
    time.sleep(1.5)
    brewing()
    if total_uang == 0:
        print("Terima kasih")
        proses = False
    elif total_uang > 0:
        print(f"uang tersisa Rp{total_uang}")
        time.sleep(1)
        print("Beli lagi?")
        time.sleep(1.5)
        q = input(" (1) Ya / (2) Tidak: ")
        while q != "1" and q != "2":
            print("Maaf hanya menerima input 1 atau 2")
            q = input(" (1) Ya / (2) Tidak: ")
        print("")
        if q == "1":
            if total_uang < 9000:
                print(
                    "Uang anda tidak mencukupi untuk melakukan pembelian kembali\nSilakan masukkan uang lagi")
        if q == "2":
            print("Terima kasih")
            proses = False
