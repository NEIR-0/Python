# tugas 1
# start
print("\n---------------------------------------------")
print("program hitung gaji karyawan\n".upper())

# input
nama = str(input("NAMA KARYAWAN: ".rjust(16)))
gol = int(input("Golongan jabatan : ".rjust(21)))
pen = str(input("Pendidikan       : ".rjust(21)))
jam = int(input("Jumlah jam kerja : ".rjust(21)))
gaji = 300000
print("\n=============================================\n")

#proses
# golongan
if gol == 1:
    total1 = int((5/100)*gaji)
    print("Karyawan yang bernama ",nama)
    print("Honor yang diterima")
    print("Tunjangan Jabatan     Rp.          ".rjust(38), total1)
elif gol == 2:
    total1 = int((10/100)*gaji)
    print("Karyawan yang bernama ",nama)
    print("Honor yang diterima")
    print("Tunjangan Jabatan     Rp.          ".rjust(38), total1)
elif gol == 3:
    total1 = int((15/100)*gaji)
    print("Karyawan yang bernama ",nama)
    print("Honor yang diterima")
    print("Tunjangan Jabatan     Rp.          ".rjust(38), total1)
else:
    print("Golongan tidak ada!!")

# pendidikan
if pen == "SMA" or pen =="sma" :
    total2 = int((2.5/100)*gaji)
    print("Tunjangan Pendidikan  Rp.           ".rjust(39), total2)
elif pen == "D1" or pen =="d1":
    total2 = int((5/100)*gaji)
    print("Tunjangan Pendidikan  Rp.          ".rjust(38), total2)
elif pen == "D3" or pen =="d3":
    total2 = int((20/100)*gaji)
    print("Tunjangan Pendidikan  Rp.          ".rjust(38), total2)
elif pen == "S1" or pen =="s1":
    total2 = int((30/100)*gaji)
    print("Tunjangan Pendidikan  Rp.          ".rjust(38), total2)
else:
    print("Pendidikan salah!!")

# lembur
if jam <= 8:
    print("Tidak ada lembur".rjust(19))
    print("____________+".rjust(45))
    tjg = gaji + total1 + total2 
    print("Total Gaji".rjust(13) + "Rp.  ".rjust(24), tjg)
elif jam == 9:
    total3 = int((jam-8)*3500)
    print("Honor Lembur          Rp.           ".rjust(39), total3)
    print("____________+".rjust(45))
    tjg = gaji + total1 + total2 + total3
    print("Total Gaji".rjust(13) + "Rp.  ".rjust(24), tjg)
elif jam == 10:
    total3 = int((jam-8)*3500)
    print("Honor Lembur          Rp.           ".rjust(39), total3)
    print("____________+".rjust(45))
    tjg = gaji + total1 + total2 + total3
    print("Total Gaji".rjust(13) + "Rp.  ".rjust(24), tjg)
elif jam <= 36:
    total3 = int((jam-8)*3500)
    print("Honor Lembur          Rp.          ".rjust(38), total3)
    print("____________+".rjust(45))
    tjg = gaji + total1 + total2 + total3
    print("Total Gaji".rjust(13) + "Rp.  ".rjust(24), tjg)
elif jam >= 37:
    total3 = int((jam-8)*3500)
    print("Honor Lembur          Rp.         ".rjust(37), total3)
    print("____________+".rjust(45))
    tjg = gaji + total1 + total2 + total3
    print("Total Gaji".rjust(13) + "Rp.  ".rjust(24), tjg)
else:
    print("ADA KESALAHAN INPUT!!")
print("---------------------------------------------\n")