import os
import time

class Cek:
  def covid(self):
    lanjut = 1
    while lanjut == 1:
      ulang = 1
      while ulang == 1:
        ulang = 0
        print("_"*50,"\n")
        print('\n"Kasus Covid di Indonesia hari ini berjumlah 4,5 juta kasus. Dengan angka kematian 144.000 jiwa"')
        print("""

  ^  ^
( ͡❛ ⏥ ͡❛)
""")
        print("Mengerikan... Kamu harus Jaga Kesehatan ya!!\n")
        print("Mau tes Covid ?")

      ulang = 1 
      ulang = (str(input("yes/no : ")))
      if ulang == "y" or ulang == "yes":
        print("\nWait a Sec...".center(50))
        time.sleep(1)
        os.system("cls")
        from pertanyaan_Covid import pertanyaan
        buka = pertanyaan()
        buka.pertanyaan_covid()
        break
      elif ulang == "n" or ulang == "no":
        print("")
        break
      else:
        print("\nWait a Sec...".center(50))
        time.sleep(1)
        os.system("cls")
        print("\nHarap jawab pertanyaan sesuai jawaban yang tersedia".upper())
        continue
      
        
