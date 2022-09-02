import os
import time

class rumah_sakit:
    def rumahSakit(self):
            lanjut = 1
            while lanjut == 1:
                ulang = 1
                while ulang == 1 or ulang == "y" or ulang == "Y":
                    ulang = 0
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
1. Rumah Sakit Umum Kalideres
Alamat  : Jl. Satu Maret No.48, RT.1/RW.4, Pegadungan, Kec.
          Kalideres, Kota Jakarta Barat, 11830
Buka    : 24 Jam 
Tutup   : -
Telepon : (021) 22552766
    """)
                        print("""  
2. Rs. Mitra Keluarga Kalideres
Alamat  : Jl. Peta Selatan No.1, RT.7/RW.11, Kalideres, Kec.
          Kalideres, Kota Jakarta Barat, Daerah Khusus Ibukota
          Jakarta Barat, 11840
Buka	: 24 Jam 
Tutup   : -
Telepon : (021) 22523700
    """)
                        print("""
3. RS Hermina Daan Mogot
Alamat  : Jl. Kintamani Raya No.2, RT.1/RW.12, Kalideres, Kec. Kalideres,
          Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11840
Buka	: 24 Jam 
Tutup   : -
Telepon : (021) 5408989
    """)
                    elif pilih == 2:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("TAMBORA".center(50))
                        print("""
1. Rumah Sakit IBU dan ANAK Aries
Alamat  : Jalan Duri (Its Raya No.22, RT.2/RW.1, Duri Utara,
          Kec. Tambora, Kota Jakarta Barat, Daerah Khusus
          Ibukota Jakarta Barat, 11270
Buka	: 24 Jam
Tutup   : -
Telepon : (021) 6392920
    """)
                    elif pilih == 3:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("GROGOL PETAMBURAN".center(50))
                        print("""
1. Rumah Sakit Sumber Waras
Alamat  : Jl. Kyai Tapa No.1, RT,10/RW.10, Tomang,
          Kec. Grogol Petamburan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta, 11440
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5682011
    """)
                        print("""
2. Rumah Sakit Royal Taruma
Alamat  : Jl. Raya Daan Mogot Kedaung No.34, RT.8/RW.1,
          Kali Angke, Kec. Grogol Petamburan,
          Kota Jakarta Barat, Daerah khusus Ibukota Jakarta 11470
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 56958338
    """)
                    elif pilih == 4:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("KEMBANGAN".center(50))
                        print("""
1. RSUD Kembangan
Alamat  : Jl. Topas Blok FII No.3, RW.7, Meruya
          Kec. Kembangan, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11620
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5870834
    """)
                    elif pilih == 5:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("KEBON JERUK".center(50))
                        print("""
1. RS Grha Kedoya 
Alamat  : 15, Jl. Panjang No.26, RW.7, Kedoya Utara,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11520
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 29910999
    """)
                        print("""
2. RS Medika Permata Hijau 
Alamat  : Jl. Raya Kby. Lama No.64, RW.8, Sukabumi Sel.,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11560
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5347411
    """)
                        print("""
3. Siloam Hospitals Kebon Jeruk 
Alamat  : Jl. Perjuangan No.Kav.8, RT.14/RW.10, Kb. Jeruk,
          Kec. Kebon Jeruk, Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11530
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 25677888
    """)
                        print("""
4. Rumah Sakit Cendana 
Alamat  : Jl. Kedoya Raya No.2, RT.7/RW.3, Kedoya Sel.,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11520
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 29863838
    """)
                        print("""
5. Rumah Sakit Anggrek Mas 
Alamat  : Jl. Anggrek No.2, RT.9/RW.2, Kb. Jeruk,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11530
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5305720
    """)
                        print("""
6. Rumah Bersalin Perjuangan 
Alamat  : Jl. Kembangan Baru No.12, RT.9/RW.3, Kedoya Sel.,
          Kec. Kebon Jeruk, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11610
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5811502
    """)
                    elif pilih == 6:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("TAMAN SARI".center(50))
                        print("""
1. RSUD Taman Sari 
Alamat : Jl. Madu No.10A, RT.2/RW.4, Mangga Besar,
         Kec. Taman Sari, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11180
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 26075052
    """)
                    elif pilih == 7:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("CENGKARENG".center(50))
                        print("""
1. Rumah Sakit Umum Daerah (RSUD) Cengkareng
Alamat  : Jl. Bumi Cengkareng Indah No.1, Cengkareng Tim.,
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11730
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 54372874
    """)
                        print("""
2. Rumah Sakit Tzu Chi
Alamat  : Jl. Kamal Raya Outer Ring Road, Cengkareng Tim.,
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11730
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 55963600
    """)
                        print("""
3. Rumah Sehat Anang Cengkareng
Alamat  : City gardn blok A1 no 16, RT.7/RW.14, Kapuk,
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11730
Buka    : 08:00 WIB
Tutup   : 18:00 WIB
Telepon : 0821-1120-7576
    """)
                        print("""
4. Rs Pedongkelan Belakang
Alamat  : Jl. Samarasa, RT.9/RW.13, Kapuk,
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11720
Buka    : 08:00 WIB
Tutup   : 18:00 WIB (selasa-minggu tutup)
Telepon : 0815-8585-7577
    """)
                        print("""
5. Klinik Rizki Medika
Alamat  : Jl. Pelita 1 No.14, RT.7/RW.1, Cengkareng Tim.,
          Kecamatan Cengkareng, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11730 
Buka    : 24 jam
Tutup   : -
Telepon : (021) 42678675
    """)
                    elif pilih == 8:
                        print("Wait a Sec...".center(50))
                        time.sleep(1)
                        os.system("cls")
                        print("PALMERAH".center(50))
                        print("""
1. Rumah Sakit Patria IKKT
Alamat  : Komplek Kemhan TNI Slipi, Kel, Jl. Cendrawasih No.1,
          RT.5/RW.2, Palmerah, Kec. Palmerah, Kota Jakarta Barat, 
          Daerah Khusus Ibukota Jakarta 11480
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5308981
    """)
                        print("""
2. Rumah Sakit Bhakti Mulia
Alamat  : Jl. K.S. Tubun No.79, RT.9/RW.5, Slipi,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11410
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5481625
    """)
                        print("""
3. Instalasi Gawat Darurat RS Harapan Kita
Alamat  : Jalan Letjen S. Parman Kav. 87, RT. 1 / RW. 8, Kota Bambu Utara,
          Palmerah, RT.1/RW.8, Kota Bambu Utara,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11420
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5684090
    """)
                        print("""
4. Rumah sakit Pelni
Alamat  : Jl. K.S. Tubun No.92-94, RT.13/RW.1, Slipi,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11410
Buka    : 24 Jam
Tutup   : -
Telepon : (021) 5480608
    """)
                        print("""
5. Rumah sakit Dharmais
Alamat  : Jl. Letjen S. Parman No.Kav 84-86, RT.4/RW.9, Kota Bambu Sel.,
          Kec. Palmerah, Kota Jakarta Barat,
          Daerah Khusus Ibukota Jakarta 11420
Buka    : 07:30 WIB
Tutup   : 16:00 WIB
Telepon : (021) 5681570
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