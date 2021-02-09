import os
import  isleFonk
import time
import  sqlite3



def main():
    while True:
        os.system("cls")
        print("""
        [1] Genel Araç İşlemleri
        [2] Kiralama İşlemleri
        [Q] Çıkış
        """)

        secim = input("İşleminizi Seçin: ")

        if secim == "1":
            isleFonk.Aracislemi()
        elif secim == "2":
            isleFonk.Kiralamaislemi()
        elif secim == "Q" or secim =="q":
            isleFonk.Cikis()






main()
