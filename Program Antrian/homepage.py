import os
import time
from queue import Queue

q = Queue()

ulang = 1
while ulang == 1:
    ulang = 0
    print("""
   Program QUEUE
-------------------
    1. Eunqueue
    2. Dequeue
    3. Size
    4. Empty
    5. Peek
    6. Display
-------------------
    """)
    
    pilihan = (input("Masukkan angka : "))
    if pilihan == "1":
        print("")
        data = (input("Berapa banyak element yang akan di masukkan? [max = 5] : "))
        if data == "1" or data == "2" or data == "3" or data == "4" or data == "5" :      
            data = int(data)   
            print("-----------------")
            for i in range(data):
                print("")
                print("Data ke ", i+1)
                q.eunqueue()

            print("\n-----------------")
            lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
            if lanjut == "y" or lanjut == "Y":
                print("\nWait a sec .....")
                time.sleep(1)
                os.system("cls")
                ulang = 1
            else:
                print("\n-----------------")
                print("Program Berhenti !!!")
                print("-----------------\n")
        else:
            print("\n-----------------")
            print("Jumlah telah melebihi batas !!!")
            print("-----------------\n")

    elif pilihan == "2":
        print("")
        data = (input("Berapa banyak element yang akan dihapus? [max = 5] : "))
        if data == "1" or data == "2" or data == "3" or data == "4" or data == "5" :
            data = int(data)
            for i in range(data):
                    q.dequeue()
            lanjut = str(input("\nMau melanjutkan program? [Y/N] : "))
            if lanjut == "y" or lanjut == "Y":
                print("\nWait a sec .....")
                time.sleep(1)
                os.system("cls")
                ulang = 1
            else:
                print("\n-----------------")
                print("Program Berhenti !!!")
                print("-----------------\n")
        else:
            print("\n-----------------")
            print("Jumlah telah melebihi batas !!!")
            print("-----------------\n")


    elif pilihan == "3":
        print("-----------------\n")
        q.size()

        print("\n-----------------")
        lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
        if lanjut == "y" or lanjut == "Y":
            print("\nWait a sec .....")
            time.sleep(1)
            os.system("cls")
            ulang = 1
        else:
            print("\n")
            print("Program Berhenti !!!")
            print("\n")
    
    elif pilihan == "4":
        print("-----------------\n")
        q.ItsEmpty()

        print("\n-----------------")
        lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
        if lanjut == "y" or lanjut == "Y":
            print("\nWait a sec .....")
            time.sleep(1)
            os.system("cls")
            ulang = 1
        else:
            print("\n")
            print("Program Berhenti !!!")
            print("\n")
    
    elif pilihan == "5":
        print("-----------------\n")
        q.peek()

        print("\n-----------------")
        lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
        if lanjut == "y" or lanjut == "Y":
            print("\nWait a sec .....")
            time.sleep(1)
            os.system("cls")
            ulang = 1
        else:
            print("\n")
            print("Program Berhenti !!!")
            print("\n")
    
    elif pilihan == "6":
        print("-----------------\n")
        q.display()

        print("\n-----------------")
        lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
        if lanjut == "y" or lanjut == "Y":
            print("\n======================\n")
            ulang = 1
        else:
            print("\n")
            print("Program Berhenti !!!")
            print("\n")

    else:
        print("")
        print("Anda Salah Kode !!!")
        print("")
        lanjut = str(input("Mau melanjutkan program? [Y/N] : "))
        if lanjut == "y" or lanjut == "Y":
            print("\nWait a sec .....")
            time.sleep(1)
            os.system("cls")
            ulang = 1
        else:
            print("\n")
            print("Program Berhenti !!!")
            print("\n")