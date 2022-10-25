# Menambahkan metode pembayaran QRIS
# Menambahkan pemilihan gula
# Menambahkan pemilihan Kondisi kopi panas atau dingin


import time

print("=========SELAMAT DATANG========")
time.sleep(1.5)

isi = [
    (" Cappuchino "),
    (" Macchiato "),
    (" Dolce "),
    (" Caffe Latte"),
    (" Espresso "),
    (" Chocolate "),
    (" White Coffe"),
    (" Mocha ")]
harga_isi = [(13000), (12000), (11000), (12000),
             (9000), (14000), (13000), (12000)]

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

list_nominal = [(1000), (2000), (5000), (10000), (20000)]
money_stored = 0


def Isi_saldo():
    global money_stored
    lanjut = True
    total_uang = 0
    while lanjut:
        # print("Masukkan saldo minimal Rp9000")
        for i in range(5):
            print(f"({i+1})", "Rp" + str(list_nominal[i]))

        # nominal = int(input("Pilih nominal: "))
        nominal = int(input("Pilih nominal uang yang dimasukkan: "))
        lembar = int(input("Jumlah lembar nominal: "))
        total_uang += list_nominal[nominal-1]*lembar
        p = "0"
        while p != "1" and p != "2":
            print("Masukkan uang lagi?")
            p = input(" (1) Ya / (2) Tidak : ")
            if p == "1":
                pass
            elif p == "2":
                lanjut = False
            else:
                print("Hanya menerima masukan 1 atau 2")
    money_stored += total_uang

    # print("Silahkan ambil cup sesuai ukuran")
    return Pembelian()


def Selamat_Tinggal():
    print("Have a nice day!")


def Pembelian_Ulang():
    global money_stored
    print("Sisa uang Anda adalah: ", money_stored)
    print("Beli lagi?")
    lagi = input(" (1) Ya / (2) Tidak : ")
    if lagi == "1":
        if money_stored > 9000:
            return Pembelian()
        else:
            isi = 0
            while isi != 1 or isi != 2:
                print(
                    "\nUang anda tidak cukup untuk melakukan pembelian ulang \nIngin mengisi saldo?")
                isi = int(input(" (1) Ya / (2) Tidak : "))
                print("")
                if isi == 1:
                    return Isi_saldo()
                elif isi == 2:
                    return Selamat_Tinggal()
                else:
                    print("Hanya menerima masukan 1 atau 2")
    elif lagi == "2":
        return Selamat_Tinggal()
    else:
        print("Hanya menerima masukan 1 atau 2")
        return Pembelian_Ulang()


def Pembelian():
    global money_stored
    print(f"\nJumlah uang: Rp{money_stored}")
    time.sleep(1.5)
    # print("Pilih Minuman\n", " ")
    for i in range(8):
        print(f"({i+1})", isi[i], harga_isi[i])
    minum = int(input("Pilih minuman: "))
    # print("Pilih Ukuran\n", " ")
    print("")
    for i in range(3):
        print(f"({i+1})", size_list[i], "++", harga_size[i])
    size = int(input("Pilih ukuran: "))
    harga = harga_isi[minum-1]+harga_size[size-1]

    if 9000 < money_stored < harga:
        while True:
            print("\nUang Anda tidak mencukupi \nIngin mengisi saldo?")
            isi_ulang = input(" (1) Ya / (2) Tidak : ")
            if isi_ulang == "1":
                return Isi_saldo()
            elif isi_ulang == "2":
                return Pembelian()
            else:
                print("Hanya menerima masukan 1 atau 2")

    elif money_stored < 9000:
        while True:
            print("\nUang Anda tidak mencukupi \nIngin mengisi saldo?")
            isi_ulang = input(" (1) Ya / (2) Tidak : ")
            if isi_ulang == "1":
                return Isi_saldo()
            elif isi_ulang == "2":
                return Selamat_Tinggal()

    money_stored -= harga

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
        "\nSilahkan Ambil\nSelamat Menikmati\n")
    return Pembelian_Ulang()


Isi_saldo()
