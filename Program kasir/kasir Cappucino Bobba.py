print("          Cappucino Bobba")
print("------------------------------------")
print("Kode      Ukuran Gelas       Harga")
print("------------------------------------")
print("M         Medium           Rp. 15000")
print("S         Small            Rp. 12000")
print("L         Large            Rp. 17000")
print("------------------------------------")


list_kode = []
list_jumlahBeli = []
list_jumlahHarga = []
arti_kode = []
harga = []
total = 0

print("\n")
data = int(input("Masukkan banyak jenis : "))
for i in range(data):
    print("jenis ke - ", 1+i)
    list_kode.append(str(input("Kode Ukuran [M/S/L]: ")))
    list_jumlahBeli.append(int(input("Banyak beli : ")))

    if list_kode[i] == "M" or list_kode[i] == "m":
        arti_kode.append("Medium")
        harga.append(15000)
    elif list_kode[i] == "S" or list_kode[i] == "s":
        arti_kode.append("Small ")
        harga.append(12000)
    elif list_kode[i] == "L" or list_kode[i] == "l":
        arti_kode.append("Large ")
        harga.append(17000)

for i in range(data):
    list_jumlahHarga.append(list_jumlahBeli[i] * harga[i])
    total = total  + list_jumlahHarga[i]

ppn = int(10/100*total)
totalHarga = total - ppn

print("\n")
print("              Cappucino Bobba")
print("----------------Struk Bayar----------------")
print(" Kode  Jenis  Jumlah  Harga    Total Harga")

for i in range(data):
    print("  %s    %s   %i    Rp.%i   Rp.%i" % (list_kode[i], arti_kode[i], list_jumlahBeli[i], harga[i], list_jumlahHarga[i]))
print("-------------------------------------------")
print("        Jumlah Bayar  : Rp. " , total)
print("        PPN 10%       : Rp. " , ppn)
print("        Total Bayar   : Rp. " , totalHarga)
print("-------------------------------------------")
bayar = int(input("Masukkan Jumlah Bayar : Rp. ")) 
kembalian = bayar - totalHarga
print("Uang Kembalian : Rp. ", kembalian)
print("""-------------------------------------------
--------------Terima Kasih-----------------""")