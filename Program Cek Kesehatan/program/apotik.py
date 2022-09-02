import os
import time

class apotik:
    def apotik_1(self):
            lanjut = 1
            while lanjut == 1:
                ulang = 1
                while ulang == 1 or ulang == "y" or ulang == "Y":
                    ulang = 0
                    print("_"*50,"\n")
                    print("""
   ^  ^
 ( ͡ᵔ ᴗ ͡ᵔ)
 """)
                    print("Dimana Anda tinggal : ")
                    print("""
1. Kalideres
2. Tambora	
3. Grogol Petamburan	
4. Kembangan
5. Kebon Jeruk	
6. Taman Sari
7. Cengkareng	
8. Palmerah
""")
                    pilih = int(input("Masukkan angka (1-8) : "))
                    print("_"*50,"\n")
                    if pilih == 1 :
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("KALIDERES".center(50))
                        print("""
1. Apotek Kalideres
Alamat  : Ruko Kalideres Indah 1 Blok B No. 2, Jl. Raya Pete
          Selatan, Kalideres, RT.7/RW.11, Kalideres,
          Kec. Kalideres, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11840
Jam     : 08:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 54373366
    """)
                        print("""
2. Apotek Alam Sehat 18
Alamat  : Jl. Peta Selatan Blok B No.1, RT.7/RW11, Kalideres,
          Kec. Kalideres, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11840
Jam     : 09:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 5452930
    """)
                        print("""
3. Theresa Apotek 
Alamat  : Ruko Permata Taman Palem Blok B1 No. 18,
          RT.7/RW.3, Pegadungan, Kec. Kalideres, Kota Jakarta
          Barat, Daerah Khusus Ibukota Jakarta, 11830 
Jam     : 08:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 46492802
    """)

                    elif pilih == 2:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("TAMBORA".center(50))
                        print("""
1. Apotek DJEMBATAN LIMA
Alamat  : Jl. KH Moch Mansyur 113 RT.005/01, RT.3/RW.1,
          Duri Sel., Kec. Tambora, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11270 
Buka    : 09:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 63855915
    """)
                        print("""
2. Jembatan Besi Apotek
Alamat  : Jl. Jembatan Besi VIII No. 8, RT.2/RW.6, Jemb. Besi,
          Kec. Tambora, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11320
Buka    : 08:00 WIB
Tutup   : 21:30 WIB
Telepon : (021) 6326512
    """)
                        print("""
3. Apotek Kita Sehat
Alamat  : Jl. Jembatan Besi VIII No. 37, RT.3/RW.5, Jembatan
          Besi, Kec. Tambora, Jakarta barat 11320
Buka	: 08:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 6253800
    """)
                    elif pilih == 3:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("GROGOL PETAMBURAN".center(50))
                        print("""
1. Apotek Talita
Alamat  : Jl. Dr. Muwardi I No.18D, RT.15/RW.3, Grogol, Kec.
          Grogol Petamburan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11450
Buka    : 09:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 29337555
    """)
                        print("""
2. Apotek Muwardi
Alamat  : Jl. Muwardi II No.17A, RT.8/RW.3, Grogol, Kec.
          Grogol Petamburan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11450
Buka    : 09:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 56940428
    """)
                        print("""
3. Apotek Lautan Berkah
Alamat  : Jl. Tanjung Duren Raya No. 25, RT.4/RW.2, Tj Duren
          Sel, Kec. Grogol Petamburan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11470
Buka    : 08:00 WIB
Tutup   : 21:30 WIB
Telepon : (021) 5644478
    """)
                    elif pilih == 4:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("KEMBANGAN".center(50))
                        print("""
1. Kembangan Apotik
Alamat  : Jl. Kembangan Raya No.17, RT.1/RW.2, Kembangan
          Sel, Kec. Kembangan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11610
Buka    : 09:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 5806279
    """)
                        print("""
2. Apotek Generik Kembangan Utara
Alamat  : Jl. Kembangan Utara No.67, RT.8/RW.2, Kembangan
          Utara, Kec. Kembangan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11610
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 58354728
    """)
                        print("""
3. Apotek Kejora Farma
Alamat  : Jl. Basmol Raya No.149, RT.8/RW.4, Kembangan
          Utara, Kec. Kembangan, Kota Jakarta Barat, Kec.
          Kembangan, Daerah Khusus Ibukota Jakarta 11610
Buka    : 08:00 WIB
Tutup   : 20:00 WIB
Telepon : (021) 5658020
    """)
                        print("""
4. Apotik Medicastore
Alamat  : Jl. Pos Pengumben Lama No.24, RT.8/RW.3, Srengseng Kec. 
          Kembangan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11630
Buka    : 08:00 WIB
Tutup   : 17:00 WIB
Telepon : (021) 29323456
    """)
                    elif pilih == 5:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("KEBON JERUK".center(50))
                        print("""
1. Sari Husada Apotik  
Alamat  : Jl. Kedoya Raya A Kedoya Selatan No.20, RT.11/RW.1,
          Kedoya Sel, Kec Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11520
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 5492832
    """)
                        print("""
2. Apotik Bahagia 
Alamat  : Jl. Raya Kb. Jeruk No.61, RT.1/RW.2, Kb. Jeruk,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11530
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 5482427
    """)
                        print("""
3. Apotik Usaha Sehat
Alamat  : Jl. Kedoya Duri No.4, RT.19/RW.4, Kedoya Sel.,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11520
Buka    : 08:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 58351756
    """)
                        print("""
4. Apotek Generik Assurur Kebon Jeruk
Alamat  : Jl. Masjid As Surur No.29, RT.2/RW.1,
          Kec. Kebon Jeruk, Kota Jakarta Barat, 
          Daerah Khusus Ibukota Jakarta 11530
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 53665406
    """)
                        print("""
5. Apotek Golden Sehat Duri Raya
Alamat  : Duri Raya No. 87 RT/RW 002/007, RT.1/RW.7, Kedoya Sel., 
          Kec.Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11510
Buka    : 10:00 WIB
Tutup   : 19:00 WIB
Telepon : (021) 21251925
    """)
                        print("""
6. Apotik Trio Sada
Alamat  : Jl. Kemanggisan Raya No.9, RT.11/RW.5, Kb. Jeruk,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11530
Buka    : 08:00 WIB
Tutup   : 17:00 WIB
Telepon : (021) 5323736
    """)
                    elif pilih == 6:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("TAMAN SARI".center(50))
                        print("""
1. Apotik Berlian Baru
Alamat  : Jalan Pancoran Raya No.9, RT.2/RW.6, Glodok,
          Kec. Taman Sari, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11120
Buka    : 08:00 WIB
Tutup   : 16:00 WIB
Telepon : (021) 6294590
    """)
                        print("""
2. Apotik Djakarta Raya 
Alamat  : Jl. Taman Sari Raya No.80, RT.11/RW.7, Taman Sari,
          Kec. Taman Sari, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11150
Buka    : 09:00 WIB
Tutup   : 18:00 WIB
Telepon : (021) 6240742
    """)
                        print("""
3. Apotik Sena 
Alamat  : Jl. Keadilan II No.21 A, RT.4/RW.4, Glodok,
          Kec. Taman Sari, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11120
Buka    : 09:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 6250985
    """)
                        print("""
4. Apotik Victory Gloria
Alamat  : Lindeteves Trade Centre (LTC Glodok) Lt.1 Blok B No.7-8, 
          Jl. Hayam Wuruk, RT.1/RW.6, Mangga Besar,
          Kec. Taman Sari, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11180 
Buka    : 08:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 6347310
    """)
                        print("""
5. Apotek Kharisma
Alamat  : Jl. Kebon Jeruk IX No.36, RT.10/RW.5, Maphar,
          Kec. Taman Sari, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11160 
Buka    : 10:00 WIB
Tutup   : 20:00 WIB
Telepon : (021) 6499260
    """)
                    elif pilih == 7:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("CENGKARENG".center(50))
                        print("""
1. Apotek Cengkareng Indah Farma
Alamat  : Komplek Perumahan Taman Cengkareng Indah Kapuk,
          Cengkareng, RT.2/RW.14, Kapuk, Kecamatan Cengkareng,
          Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11720
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 6193783
    """)
                        print("""
2. Apotek Sheila
Alamat  : Ruko taman Palem Lestari, Jl. Taman Palem Lestari No.B18,
          RT.6/RW.13, West Cengkareng, West Jakarta City, Jakarta 11730
Buka    : 10:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 55951990
    """)
                        print("""
3. Apotik Malibu
Alamat  : The City Resort Residence Rukan Malibu Bl. I, 
          Jl. Boulevard Raya, RT.7/RW.14, Cengkareng Tim.,
          Kecamatan Cengkareng, Kota Jakarta Barat, 
          Daerah Khusus Ibukota Jakarta 11730
Buka    : 08:00 WIB
Tutup   : 23:00 WIB
Telepon : (021) 56944911
    """)
                        print("""
4. Apotik Interkota
Alamat  : Interkota, Komplek Perumahan, Jl. Raya Duri Kosambi No.16,
          RT.9/RW.7, Rw. Buaya, Kecamatan Cengkareng,
          Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11740
Buka    : 07:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 5414489
    """)
                        print("""
5. Keluarga Apotik
Alamat  : Jl. Raya Duri Kosambi No.74, RT.3/RW.2, Duri Kosambi, 
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11750
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 6198520
    """)
                    elif pilih == 8:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("PALMERAH".center(50))
                        print("""
1. Apotek Panel Sehat
Alamat  : Jl. K.S. Tubun, RT.1/RW.1, Slipi, Kec. Palmerah,
          Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10260
Buka    : 09:00 WIB
Tutup   : 21:00 WIB
Telepon : (021) 5490040
    """)
                        print("""
2. Apotik Matra
Alamat  : Jl. Rw. Belong No.15, RT.8/RW.15, Palmerah,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11540
Buka    : 24 jam
Tutup   : -
Telepon : (021) 5494694
    """)
                        print("""
3. Apotek Kimia Farma Slipi
Alamat  : Jl. Kemanggisan Raya.26e, RT.4/RW.13, Kel. Palmerah, 
          Kec, Kemanggisan, Daerah Khusus Ibukota Jakarta 11480
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : 0813-8387-8810
    """)
                        print("""
4. Apotek An-Nuur
Alamat  : Jl. Kemanggisan Ilir III No.17G, RT.8/RW.1, Palmerah,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11480 
Buka    : 08:00 WIB
Tutup   : 22:00 WIB
Telepon : (021) 5305056
    """)                
                    else:
                        print("\nnomor tidak terdaftar".upper())
                        break
                ulang = 1
                        
                ulang = str(input("Ingin mencoba kembali? [Y/N] : "))
                if ulang == "y" or ulang == "Y":
                    print("")
                    print("Wait a Sec...".center(50))
                    time.sleep(2)
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
