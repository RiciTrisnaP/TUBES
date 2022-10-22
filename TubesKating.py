isi = [
    ("1.soda", 8000),
    ("2.teh", 6000),
    ("3.jus", 10000),
    ("4.keripik", 8000),
    ("5.biskuit", 6000),
    ("6.permen", 5000),
    ("7.coklat", 12000),
    ("8.susu", 5000),
    ("9.air", 4000)
]


def beli_lagi():
    global total_uang
    print("Sisa uangmu sebesar",  total_uang, "rupiah")
    print("Apakah kamu ingin membeli lagi?\n"
          "1 untuk ya\n "
          "2 untuk tidak\n")
    lagi = input()
    if lagi == "1":
        return bisa_beli()
    elif lagi == "2":
        print("Selamat tinggal\n"
              "Have a good day!")
    else:
        print("Hanya menerima 1 atau 2")
        beli_lagi()


def bisa_beli():
    global total_uang
    beli = input("Ingin membeli apa?:")
    if beli == "1":
        if total_uang >= isi[0][1]:
            total_uang = total_uang - isi[0][1]
            print("Kamu telah memilih soda seharga", isi[0][1], "rupiah")
            print("Silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "2":
        if total_uang >= isi[1][1]:
            total_uang = total_uang - isi[1][1]
            print("Kamu telah memilih teh seharga", isi[1][1], "rupiah")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "3":
        if total_uang >= isi[2][1]:
            total_uang = total_uang - isi[2][1]
            print("Kamu telah memilih jus seharga", isi[2][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "4":
        if total_uang >= isi[3][1]:
            total_uang = total_uang - isi[3][1]
            print("Kamu telah memilih keripik seharga", isi[3][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "5":
        if total_uang >= isi[4][1]:
            total_uang = total_uang - isi[4][1]
            print("Kamu telah memilih biskuit seharga", isi[4][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "6":
        if total_uang >= isi[5][1]:
            total_uang = total_uang - isi[5][1]
            print("Kamu telah memilih permen seharga", isi[5][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "7":
        if total_uang >= isi[6][1]:
            total_uang = total_uang - isi[6][1]
            print("Kamu telah memilih coklat seharga", isi[6][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "8":
        print("Kamu telah memilih susu"), print("Rp5.000")
        if total_uang >= isi[7][1]:
            total_uang = total_uang - isi[7][1]
            print("Kamu telah memilih susu seharga", isi[7][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    elif beli == "9":
        if total_uang >= isi[8][1]:
            total_uang = total_uang - isi[8][1]
            print("Kamu telah memilih air seharga", isi[8][1], "rupiah")
            print("silakan mengambil barangmu")
            if total_uang < 4000:
                print("Selamat Tinggal\n"
                      "Have a Good day!")
            elif total_uang >= 4000:
                beli_lagi()
        else:
            print("Uangmu tidak mencukupi,kamu hanya punya", total_uang)
    else:
        print("Input mu tidak dikenali. Mohon mengisi sesuai dengan yang ada di isi")
        bisa_beli()


def menu_reparasi():
    print("                                                Menu Reparasi             ")
    print("1. Mengisi ulang isi")
    print("2. Reparasi Mesin   ")
    print("3. Mengambil uang   ")
    rep = int(input("Masukkan pilihanmu!:"))
    if rep == 1:
        print("Memasuki mode mengisi ulang\n"
              "Selamat Tinggal")
    elif rep == 2:
        print("Selamat mereparasi\n"
              "Selamat Tinggal")
    elif rep == 3:
        print("Silakan mengambil uang\n "
              "Selamat Tinggal")
    else:
        print("Input tidak dikenal, silakan mengulang!\n")
        menu_reparasi()


pecahan = [1000, 2000, 5000, 10000, 20000]
print("Selamat Datang di Vending Machine")
print("Pencet 1 untuk melanjutkan")
a = input()

if a == "1":
    print("Hanya menerima uang lembaran dari Rp1.000 hingga Rp20.000.")
    print("PERHATIAN! Tidak memberikan kembalian")
    for i in isi:
        print((i[0]), (i[1]))

    seribuan = int(
        input("Berapa banyak lembar Rp1.000 yang ingin dimasukan?:"))
    while seribuan < 0:
        seribuan = int(input("Masukkan angka positif:"))
    duaribu = int(
        input("Berapa banyak lembar Rp2.000 yang ingin dimasukkan?:"))
    while duaribu < 0:
        duaribu = int(input("Masukkan angka positif:"))
    limaribu = int(
        input("Berapa banyak lembar Rp5.000 yang ingin dimasukkan?:"))
    while limaribu < 0:
        limaribu = int(input("Masukkan angka positif:"))
    sepuluh = int(
        input("Berapa banyak lembar Rp10.000 yang ingin dimasukkan?:"))
    while sepuluh < 0:
        sepuluh = int(input("Masukkan angka positif:"))
    duapuluh = int(
        input("Berapa banyak lembar Rp20.000 yang ingin dimasukkan?:"))
    while duapuluh < 0:
        duapuluh = int(input("Masukkan angka positif:"))
    total_uang = (seribuan*pecahan[0])+(duaribu*pecahan[1]) + \
        (limaribu*pecahan[2])+(sepuluh*pecahan[3])+(duapuluh*pecahan[4])
    print("Total uang yang kamu masukkan sebesar", total_uang, "rupiah")
    bisa_beli()


elif a == "12105":
    menu_reparasi()
