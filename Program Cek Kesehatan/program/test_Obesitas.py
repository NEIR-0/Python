import os
import time

class loop:
    def obesitas(self):
        lanjut = 1
        while lanjut == 1:
            ulang = 1
            while ulang == 1 or ulang == "y" or ulang == "Y":
                ulang = 0
                print("\n")
                print("="*50)
                print("""\n
 ^  ^
( ͡❛ ᴗ ͡❛)

"ini contoh penulisannya ya!!"

masukkan tinggi badan anda (cm) : 165.5 
masukkan berat badan anda (kg) : 46.8 
""")
                print("_"*50,"\n")
                tinggi_badan = str(input("masukkan tinggi badan anda (cm) : "))
                berat_badan = str(input("masukkan berat badan anda (kg) : "))
                Tb_convert = float(tinggi_badan.replace(",","."))
                Bb_convert = float(berat_badan.replace(",", "."))
                total = (Bb_convert)/((Tb_convert/100)**2)
                print("_"*50)
                if total <= 17.0:
                    print("Wait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nResult:")
                    print("Kurus, kekurangan berat badan -- berat")
                    print("""

 ^   ^
( ° - ° )

"Tunggu... Sepertinya ini cukup buruk..." 

Sepertinya kamu harus berusaha menaikkan berat badan mu, kalau tidak akan banyak penyakit yang 
akan menyerang tubuh mu...


 ^  ^
( ͡❛ ᴗ ͡ ) b

"Semangat ya, kamu pasti bisa!!!!"
    """)
                elif total <= 18.4:
                    print("Wait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nResult:")
                    print("Kurus, kekurangan berat badan -- ringan")
                    print("""

 ^   ^
( ° ⏥ °)

"Tunggu!!!, Apakah kamu model?!!"

Tapi tetap berat badan ideal itu lebih baik, karena menandakan tubuh mu itu sehat dan tidak kekurang nutrisi
    """)
                elif total <= 25.0:
                    print("Wait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nResult:")
                    print("Berat badan anda Normal")
                    print("""

   ^ ^
d ( ͡ ᴗ ͡❛) 

"Good job!! Berat badan mu ideal, pertahankan itu ya!!"    
    """)
                elif total <= 27.0:
                    print("Wait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nResult:")
                    print("Gemuk, kelebihan berat badan tingkat -- ringan")
                    print("""

  ^  ^
(つ≧▽≦)つ

"Percayalah Gemuk itu adalah kurus yang kebablasan. Tetap percaya diri ya!!" 
""")
                elif total >= 27.1:
                    print("Wait a Sec...".center(50))
                    time.sleep(1)
                    os.system("cls")
                    print("\nResult:")
                    print("Gemuk, kelebihan berat badan tingkat -- berat")
                    print("""

  ^  ^
( • ︵ • )

"ini... Cukup parah sepertinya. Karena ini bisa digolongkan obesitas" 

Sepertinya kamu harus berusaha menurunkan berat badan mu, karena akan banyak penyakit yang 
akan menyerang tubuh mu...


 ^ ^
( ͡❛ ᴗ ͡ ) b

"Semangat ya, kamu pasti bisa!!!!"
""")
                else:
                    print("\nharap membaca petunjuk dan perhatikan pertanyaan secara teliti")
                    break
            ulang = 1
            
            ulang = str(input("Ingin mencoba kembali? [Y/N] : "))
            if ulang == "y" or ulang == "Y":
                print("Wait a Sec...".center(50))
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