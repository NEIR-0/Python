import os
import time

class pertanyaan:
    def pertanyaan_covid(self):
            lanjut = 1
            while lanjut == 1:
                ulang = 1
                while ulang == 1:
                    ulang = 0
                    print('\n"Okay, aku akan berikan kamu beberapa pertanyaan. Silahkan Jawab yes atau no (yes/no)"\n')
                    print("""
  ^  ^
( ͡❛ ‿ ͡❛)

aku mulai ya!
    """)
                    print("_"*50,"\n")
                    print("pertanyaan pertama,")
                    pertanyaan = str(input("Apakah suhu badan anda diatas 38 Celcius : "))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_1 = 1 
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_1 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan kedua,")
                    pertanyaan = str(input("Apakah anda sering sekali batuk : "))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_2 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_2 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan ketiga,")
                    pertanyaan = (str(input("Apakah anda mudah kelelahan : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_3 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_3 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan keempat,")
                    pertanyaan = (str(input("Apakah anda kehilangan indra pengecap : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_4 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_4 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan kelima,")
                    pertanyaan = (str(input("Apakah anda kehilangan indra penciuman : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_5 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_5 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    jumlah_1 = (point_1+point_2+point_3+point_4+point_5)
                    if jumlah_1 == 0:
                        print("""\n


 ^  ^
( ͡❛ ▿ ͡❛)

"ohh!! Ini cukup baik!"
    """)
                        print("ayo kita lanjutkan ke pertanyaan berikutnya!\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    elif jumlah_1 == 5:
                        print("""\n


 ^ ^
( ͡❛ . ͡❛)

"sepertinya cukup buruk..."
    """)
                        print("ayo kita lanjutkan ke pertanyaan berikutnya...\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    elif jumlah_1 <= 4:
                        print("""\n


 ^  ^
( ͡• ᴗ ͡•)

"hmmmm..... Sepertinya masih aman"
    """)
                        print("ayo kita lanjutkan ke pertanyaan berikutnya.\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    print("_"*50,"\n")
                    print("\npertanyaan keenam,")
                    pertanyaan = (str(input("apakah tenggorokan anda sakit : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_6 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_6 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan ketujuh,")
                    pertanyaan = (str(input("apakah anda mengalami sakit kepala : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_7 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_7 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan kedelapan,")
                    pertanyaan = (str(input("apakah anda merasakan sakit dan nyeri pada tubuh anda : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_8 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_8 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break
                
                    print("\npertanyaan kesembilan,")
                    pertanyaan = (str(input("apakah anda sering diare : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_9 = 1
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_9 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan kesepuluh,")
                    pertanyaan0 = (str(input("apakah ada ruam pada kulit, atau perubahan warna pada jari tangan atau jari kaki : ")))
                    if pertanyaan0 == "y" or pertanyaan0 == "yes":
                        point_10 = 1
                    elif pertanyaan0 == "n" or pertanyaan0 == "no":
                        point_10 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan kesebelas,")
                    pertanyaan1 = (str(input("apakah anda mengalami iritasi pada mata atau mata merah : ")))
                    if pertanyaan1 == "y" or pertanyaan1 == "yes":
                        point_11 = 1
                    elif pertanyaan1 == "n" or pertanyaan1 == "no":
                        point_11 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    jumlah_2 = (point_6+point_7+point_8+point_9+point_10+point_11)
                    if jumlah_2 == 0:
                        print("""\n


 ^  ^
( ͡ᵔ ▿ ͡ᵔ)

"Wahhhh!! Bukannya ini semakin bagus!!"
    """)
                        print("ayo kita lanjutkan ke tiga pertanyaan terakhir!\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    elif jumlah_2 == 6:
                        print("""\n


 ^ ^
( ͡• - ͡•)

"Tunggu... Bukannya ini semakin buruk?!!"
    """)
                        print("Baiklah... aku akan berikan tiga pertanyaan terakhir... Tolong dijawab dengan jujur!\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    elif jumlah_2 <= 5:
                        print("""\n


 ^  ^
( ͡─ ᴗ ͡─)

"Hmmm... Bukankah ini, mulai memburuk..."
    """)
                        print("ayo kita lanjutkan ke tiga pertanyaan terakhir...\n")
                        print("\nWait a Sec...".center(50))
                        time.sleep(3)
                        os.system("cls")

                    print("_"*50,"\n")
                    print("\npertanyaan kedua belas,")
                    pertanyaan = (str(input("apakah mengalami kesulitan bernapas atau sesak napas : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_12 = 50
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_12 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan ketiga belas,")
                    pertanyaan = (str(input("apakah anda kesulitan berbicara atau bergerak : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_13 = 50
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_13 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    print("\npertanyaan keempat belas,")
                    pertanyaan = (str(input("apakah anda merasakan nyeri pada dada anda : ")))
                    if pertanyaan == "y" or pertanyaan == "yes":
                        point_14 = 50
                    elif pertanyaan == "n" or pertanyaan == "no":
                        point_14 = 0
                    else:
                        print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                        break

                    jumlah_3 = (jumlah_1+jumlah_2+point_12+point_13+point_14)

                    if jumlah_3 == 0:
                        print("")
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("_"*50)
                        print("""\nHASIL TES ANDA :



 ^  ^
( ͡ᵔ ▿ ͡ᵔ)

"okayy!! Sepertinya kondisi mu sungguh Baik!"
    """)
                        print("""
Tapi ingat, walaupun kondisi kamu baik. Masih ada presentase kamu terpapar virus corona
Untuk pencegahan lakukanlah hal-hal berikut : 

1. Selalu jaga jarak aman dari orang lain (minimal 1 meter), meskipun mereka tidak tampak 
sakit.
2. Kenakan masker di ruang publik, terutama di dalam ruangan dengan pembatasan fisik yang
tidak dimungkinkan.
3. Sebaiknya pilih ruang terbuka dan berventilasi baik. Buka jendela jika berada di dalam 
ruangan.
4. Cuci tangan Anda secara rutin. Gunakan sabun dan air, atau cairan pembersih tangan 
berbahan alkohol.
5. Ikuti vaksinasi ketika giliran Anda. Ikuti panduan setempat terkait vaksinasi.
6. Saat batuk atau bersin, tutup mulut dan hidung Anda dengan lengan atau tisu.
7. Jangan keluar rumah jika merasa tidak enak badan.

        """)
                            

                    elif jumlah_3 <=49:
                        print("")
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("_"*50)
                        print("""\nHASIL TES ANDA :



 ^  ^
( ͡• ‿ ͡•)

"okay, sepertinya kondisi kamu kurang baik. Untuk jaga-jaga tolong lakukan isolasi madiri di rumah ya!!"
    """)
                        print("""
Dan lakukan tindakan berikut ini:

1. Hubungi penyedia layanan kesehatan atau hotline COVID-19 untuk mendapatkan informasi 
terkait tempat dan waktu untuk menjalani tes.
2. Taati prosedur pelacakan kontak untuk menghentikan penyebaran virus.
3. Jika tes tidak tersedia, tetaplah di rumah dan jangan lakukan kontak dengan orang lain 
selama 14 hari.
4. Selama masa karantina, jangan pergi ke kantor, sekolah, atau tempat-tempat umum. 
Mintalah seseorang mencukupi kebutuhan Anda.
5. Jaga jarak minimal 1 meter dari orang lain, termasuk anggota keluarga Anda.
6. Kenakan masker medis untuk melindungi orang lain, termasuk jika/ketika Anda perlu 
meminta perawatan medis.
7. Cuci tangan Anda secara rutin.
8. Gunakan ruangan yang terpisah dari anggota keluarga lain, dan jika tidak memungkinkan, 
selalu kenakan masker medis.
9. Pastikan ventilasi ruangan selalu baik.
10. Jika menggunakan kamar bersama orang lain, beri jarak antar-tempat tidur minimal 1 meter.
11. Amati diri Anda sendiri apakah ada gejala apa pun selama 14 hari.
12. Segera hubungi penyedia layanan kesehatan jika Anda mengalami salah satu tanda bahaya berikut: 
    sulit bernapas, sulit berbicara atau bergerak, bingung, atau merasakan nyeri di dada.
13. Tetaplah positif, dengan terus berinteraksi dengan orang-orang terdekat melalui telepon atau 
    internet, dan dengan berolahraga di rumah.

    """)
                    elif jumlah_3 >= 50:
                        print("")
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("_"*50)
                        print("""\nHASIL TES ANDA :



 ^  ^
( ͡❛  ͟ʖ ͡❛)

"ok... Ini sangat buruk, Aku akan mencarikan kamu rumah sakit terdekat "
        """)
                        from rumah_sakit import rumah_sakit
                        buka = rumah_sakit()
                        buka.rumahSakit()

                ulang = 1
                        
                ulang = str(input("Ingin mencoba kembali? [Y/N] : "))
                if ulang == "y" or ulang == "Y":
                    print("\nWait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    lanjut = 1
                elif ulang == "n" or  ulang == "N":
                    print("")
                    break
                else:
                    print("\nWait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nHarap jawab pertanyaan sesuai jawaban yang tersedia".upper())
                    continue