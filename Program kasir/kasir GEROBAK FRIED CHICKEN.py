#start
print("\n     GEROBAK FRIED CHICKEN")
print("-------------------------------")
print("Kode     Jenis Potong    Harga" )
print("-------------------------------")
print("D          Dada         Rp.2500")
print("P          Paha         Rp.2000")
print("S          Sayap        Rp.1500")
print("-------------------------------")

# data di bawah bisa pake __.append tapi gak bisa langsung di taro di "print()"
# kecuali pake [] format rangenya

list_kode = []
list_jumlahBeli = []
list_jumlahHarga = []
harga = []
artiKode = []
# total = 0, kita gunakan untuk di taro di "print()"
total = 0


data = int(input("\nBanyak Jenis : "))
for i in range(data):
    print("Jenis Ke - ", str(i+1))
    list_kode.append(str(input("Kode Potong [D/P/S] : ")))
    list_jumlahBeli.append(int(input("Banyak Potong : ")))

    # harus sejalan penempatannya gak boleh kelebihan atau kurang
    if list_kode[i] == "D" or list_kode[i] == "d":
        artiKode.append("Dada ") 
        harga.append(2500)
    elif list_kode[i] == "P" or list_kode[i] == "p":
        artiKode.append("Paha ") 
        harga.append(2000)
    elif list_kode[i] == "S" or list_kode[i] == "s":
        artiKode.append("Sayap") 
        harga.append(1500)
    else :
        artiKode.append("Tidak Ditemukan") 
        harga.append(0)

    # ini contoh salah, akan terjadi error index out of range
# if list_kode[i] == "D" or list_kode[i] == "d":
#     artiKode.append("Dada ") 
#     harga.append(2500)
# elif list_kode[i] == "P" or list_kode[i] == "p":
#     artiKode.append("Paha ") 
#     harga.append(2000)
# elif list_kode[i] == "S" or list_kode[i] == "s":
#     artiKode.append("Sayap") 
#     harga.append(1500)
# else :
#     artiKode.append("Tidak Ditemukan") 
#     harga.append(0)

# bikin range baru di setiap proses baru dan menghidari eror out of range karena beda line
for i in range(data):
    list_jumlahHarga.append(list_jumlahBeli[i]*harga[i])
    total = total+list_jumlahHarga[i]

# disini kita buat out of line, supaya gak kehitung if/elif/else
# dan supaya bisa dipake di next proses
pajak = int(10/100*total)
totalBayar = total-pajak

print("\n")
print("GEROBAK FRIED CHICKEN".rjust(28))
print("-----------------------------------")
print("No", "Jenis".center(7), "Harga".rjust(6), "Banyak".rjust(8), "jumlah".rjust(7))
print("Potong".rjust(10), "Satuan".rjust(7), "Beli".rjust(5), "Harga".rjust(8) )
print("-----------------------------------")

# bikin range baru di setiap proses baru menghidari eror out of range karena beda line
for i in range(data):
    print("%i   %s    %i     %i    Rp.%i" % (i+1, artiKode[i], harga[i], list_jumlahBeli[i], list_jumlahHarga[i] ))
print("-----------------------------------")
print("        Jumlah Bayar   Rp.   ", total)
print("        Pajak 10%      Rp.   ", pajak)
print("        Total Bayar    Rp.   ", totalBayar )







# # contoh kalo lu pake while, kalo pake while 2 variable disini gw pake (i dan p)
# kode = """ 
# as
# bs
# cs
# """
# print(kode)

# harga = []
# nama = []
# jumlah = []
# m = []
# s = []
# total = 0

# # i while nomor variable satu
# i = 0
# data = int(input("masukkan jumlah jenis : "))
# while i < data:
#     print("data ke - ", 1+i)
#     m.append(str(input("masukkan kode = ")))
#     s.append(int(input("masukkan jumlah beli = ")))

#     # harus sejalan penempatannya gak boleh kelebihan atau kurang
#     if m[i] == "as":
#                 nama.append("anis_sajya")
#                 harga.append(250000)
#     elif m[i] == "bs":
#                 nama.append("babysites")
#                 harga.append(150000)
#     elif m[i] == "cs":
#                 nama.append("conterstrom")
#                 harga.append(300000)
#     i+=1

# total = 0
# # p while variabel dua
# p = 0
# while p < data:
#     jumlah.append(s[p]*harga[p])
#     total = total+jumlah[p]
#     print("no.", p+1, nama[p], harga[p])
#     print("jumlah bayar : ", total)
#     p+=1