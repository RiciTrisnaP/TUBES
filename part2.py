#part one

#list

import time

isi = [
(" Cappuchino "), 
(" Macchiato  "), 
(" Dolce      "), 
(" Caffe Latte"), 
(" Espresso   "), 
(" Chocolate  "), 
(" White Coffe"), 
(" Mocha      ")]
harga_isi = [(13000), (12000), (11000), (12000), (9000), (14000), (13000), (12000)]

size_list = [
(" Small "), 
(" Medium"), 
(" Large ")]
harga_size = [(0), (2000), (4000)]

print ("Pilih Minuman\n" , " ")
for i in range (8):
    print (f"({i+1})",isi[i], harga_isi[i])

minum = int(input("Pilih minuman: "))

print ("Pilih Ukuran\n", " ")
for i in range (3):
    print (f"({i+1})", size_list[i],"++", harga_size[i])

size = int(input("Pilih ukuran: "))

print(f"Anda memilih {isi[minum-1]} ukuran {size_list[size-1]}")
time.sleep(1)
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
print(
    " Silahkan Ambil\n" , 
    "Selamat Menikmati")


