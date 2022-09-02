import os
import time

print("="*50,"\n")
print("C E K    K E S E H A T A N    Y U K !".center(50),"\n")
print('"versi - Jakarta Barat."'.center(48), "\n")
print("="*50,"\n")

#input pertama
nama = str(input("Masukkan Nama Anda : "))
usia = str(input("Masukkan Usia Anda : "))
kelamin = str(input("Masukkan kelamin (Perempuan/Laki-laki) : "))
print("")
print("="*50,"\n")  
print("Selamat Datang! --- Kak, ",  nama,"\n")

lanjut = 1
while lanjut == 1:
  ulang = 1
  while ulang == 1 or ulang == "y":
    print("""
  ^  ^
( ͡❛ ‿ ͡❛)
""")
    print("apa yang bisa aku bantu?")
    print("""
1. Tentang Covid
2. Tes obesitas
3. Apotik terdekat
4. Rumah sakit terdekat
""")  
    pilih_1 = (int(input("Pilih Nomor : ")))  
    if pilih_1 == 1:
      print("\nWait a Sec...".center(50))
      time.sleep(1)
      os.system("cls")
      from cek_Covid import Cek
      buka = Cek()
      buka.covid()
      break

    elif pilih_1 == 2:
      print("\nWait a Sec...".center(50))
      time.sleep(1)
      os.system("cls")
      from test_Obesitas import loop
      buka = loop()
      buka.obesitas()
      break

    elif pilih_1 == 3:
      print("\nWait a Sec...".center(50))
      time.sleep(1)
      os.system("cls")
      from apotik import apotik
      buka = apotik()
      buka.apotik_1()
      break

    elif pilih_1 == 4:
      print("\nWait a Sec...".center(50))
      time.sleep(1)
      os.system("cls")
      print("_"*50,"\n")
      from rumah_sakit import rumah_sakit
      buka = rumah_sakit()
      buka.rumahSakit()
      break



  ulang = 1
  ulang = str(input("ingin mengulang program? [Y/N] : "))
  if ulang == "y" or ulang == "Y":
    print("\nWait a Sec...".center(50))
    time.sleep(1)
    os.system("cls")
    print("_"*50,"\n")
    lanjut = 1
  elif ulang == "n" or ulang == "N":
    print("""
__________________________________________________ 



^  ^
( ͡ᵔ ᴗ ͡ᵔ)

"Terima kasih atas kunjungannya!!"
""")
    break
  else:
    print("\nHarap jawab pertanyaan sesuai jawaban yang tersedia".upper())
    print("\nWait a Sec...".center(50))
    time.sleep(4)
    os.system("cls")
    continue
    


