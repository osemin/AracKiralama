import sqlite3
db = sqlite3.connect("arackirala.sqlite")
imlec =db.cursor()

def Cikis():
    quit()

def Aracislemi():
    while True:
        print("""
         [1] Araç Ekle 
         [2] Araç Sil
         [3] Araç Bilgisi Güncelle
         [4] Araç Listele
         [Q] Ana Menüye  Geri Dön
         """)
        secim = input("İşleminizi Seçin: ")

        if secim == "Q" or secim =="q":
            break
        elif secim == "1":
            plaka = input("Araç Plaka Giriniz: ").upper()
            marka = input("Araç Markası Girin: ").capitalize()
            model = input("Araç Modeli Girin: ").capitalize()
            yil = int(input("Araç Yıl Girin: "))
            arac_km = int(input("Araç KM Giriniz: "))
            arac_durum  = input("Araç Durumu Giriniz: ").capitalize()
            imlec.execute("insert into aracislem(plaka,marka,model,yil,arac_km,arac_durum) values(?,?,?,?,?,?)",(plaka,marka,model,yil,arac_km,arac_durum))
            db.commit()
            print("{} Plakalı {} Markalı {} Modeli {} Model Yılında   {} KM de Olan Araç Sisteme Eklenmiştir.".format(plaka,marka,model,yil,arac_km))
            print("Üst Menüye Dönmek için Enter'a Basın!")
            input()
        elif secim == "2":
            plaka = input("Araç Plaka Giriniz: ").upper()
            imlec.execute("delete from aracislem where plaka=?",[plaka])
            db.commit()
            print("{} Plakalı Araç Silinmiştir.".format(plaka))
            print("Üst Menüye Dönmek için Enter'a Basın!")
            input()
        elif secim == "3":
            plaka = input("Araç Plaka Giriniz: ").upper()
            arac_km = int(input("Araç KM Giriniz: "))
            arac_durum = input("Araç Durumu Giriniz: ").capitalize()
            imlec.execute("update aracislem set arac_km=?,arac_durum=? where plaka=?",(arac_km,arac_durum,plaka))
            db.commit()
            print("{} Plakalı Araç İle İgili İşlemler Güncellenmiştir.".format(plaka))
            print("Üst Menüye Dönmek için Enter'a Basın!")
            input()
        elif secim == "4":
            plaka = input("Araç Plaka Giriniz: ").upper()
            sorgu = "select plaka,marka,model,arac_km from aracislem where plaka='{}'".format(plaka)
            imlec.execute(sorgu)
            arama = imlec.fetchall()
            for i in arama:
                print("{} Plakalı Araç Bilgileri".format(i))
                print("Üst Menüye Dönmek için Enter'a Basın!")
                input()


def Kiralamaislemi():
    while True:
        print("""
         [1] Araç Ekle
         [2] Araç Listele
         [3] Araç Kirala
         [4] Araç Kiralama Güncelle 
         [5] Kiralık Araç Listesi
         [Q] Ana Menüye  Geri Dön
         """)
        secim = input("İşleminizi Seçin: ")

        if secim == "Q" or secim =="q":
            break
        elif secim == "1":
            plaka = input("Araç Plaka Giriniz: ").upper()
            marka = input("Araç Markası Girin: ").capitalize()
            model = input("Araç Modeli Girin: ").capitalize()
            km = int(input("Araç KM Giriniz: "))
            hasar = input("Araç Hasar  Var Mı E/H: ").capitalize()
            if hasar == "e" or hasar =="E":
                hasar_durum = input("Hasar Durumunu Belirtin: ").capitalize()
                kira_durum = input("Araç Kirada Mı E/H: ").capitalize()
                if kira_durum == "e" or kira_durum == "E":
                    kira_fiyati = int(input("Araç Kira Fiyatını Giriniz: "))
                    imlec.execute(
                        "insert into kiraislem(plaka,marka,model,km,kira_durum,hasar,hasar_durum,kira_fiyati) values(?,?,?,?,?,?,?,?)",
                        (plaka, marka, model, km, kira_durum, hasar, hasar_durum, kira_fiyati))
                    db.commit()
                    print("{} Plakalı Araç Eklenmiştir.Kiralama Listesinden Kontrol Edebilirsin".format(plaka))
                    print("Üst Menüye Dönmek için Enter'a Basın!")
                    input()
            elif hasar == "h" or hasar =="H":
                kira_durum = input("Araç Kirada Mı E/H: ").capitalize()
                if kira_durum == "e" or kira_durum == "E":
                    kira_fiyati = int(input("Araç Kira Fiyatını Giriniz: "))
                    imlec.execute(
                        "insert into kiraislem(plaka,marka,model,km,kira_durum,hasar,hasar_durum,kira_fiyati) values(?,?,?,?,?,?,?,?)",
                        (plaka, marka, model, km, kira_durum, hasar, hasar_durum, kira_fiyati))
                    db.commit()
                    print("{} Plakalı Araç Eklenmiştir.Kiralama Listesinden Kontrol Edebilirsin".format(plaka))
                    print("Üst Menüye Dönmek için Enter'a Basın!")
                    input()
                elif kira_durum == "H" or kira_durum == "h":
                     imlec.execute(
                         "insert into kiraislem(plaka,marka,model,km,kira_durum,hasar) values(?,?,?,?,?,?)",
                         (plaka, marka, model, km, kira_durum, hasar))
                     db.commit()
                     print("Seçimleriniz Kayıt Edildi.")
                     print("Üst Menüye Dönmek için Enter'a Basın!")
                     input()

        elif secim == "2":
            plaka = input("Araç Plaka Giriniz: ").upper()
            sorgu = "select * from aracislem where plaka='{}'".format(plaka)
            imlec.execute(sorgu)
            arama = imlec.fetchall()
            for i in arama:
                print("{} Plakalı Araç Bilgileri".format(i))
                print("Üst Menüye Dönmek için Enter'a Basın!")
                input()


        elif secim == "5":
            plaka = input("Araç Plaka Giriniz: ").upper()
            sorgu = "select kira_durumu,kira_fiyati from kiraislem where plaka='{}'".format(plaka)
            imlec.execute(sorgu)
            arama = imlec.fetchall()
            for i in arama:
                print("{} Plakalı Araç Bilgileri".format(i))
                print("Üst Menüye Dönmek için Enter'a Basın!")
                input()

        elif secim == "3":
            plaka = input("Araç Plakasını Giriniz: ")
            kiraci_isim = input("Kiracı İsmini Girin: ")
            kiraci_soyisim = input("Kiracı Soyisim Girin: ")
            kiraci_tel = int(input("Kiracı Telefon Girin: "))
            baslama_tarihi = int(input("Kira Başlangıç Tarihi Girin: "))
            bitis_tarihi = int(input("Kira Bitiş Tarihi Girin: "))
            fiyat_hesaplama= bitis_tarihi - baslama_tarihi
            sonuc = fiyat_hesaplama
            if sonuc <7:
                print("Fiyatınız 100 TL'dir")
            elif sonuc >=8:
                print("Fiyatınız 200 TL'dir")

            fiyat = int(input("Kira Ücretini Giriniz: "))
            kira_d = input("Araç Kiralaması Başlasın Mı? E/H")
            if kira_d == "e" or kira_d =="E":
                imlec.execute("insert into kirala(plaka,kiraci_isim,kiraci_soyisim,kiraci_tel,baslama_tarihi,bitis_tarihi,fiyat,kira_d) values (?,?,?,?,?,?,?,?)",(plaka,kiraci_isim,kiraci_soyisim,kiraci_tel,baslama_tarihi,bitis_tarihi,fiyat,kira_d))
                db.commit()
                print("Seçimleriniz Kayıt Edildi.Kiralama İşlemi Başlatıldı.")
                print("Üst Menüye Dönmek için Enter'a Basın!")
                input()
            elif kira_d == "h" or kira_d =="H":
                print("Kiralama İşlemi Başlatılamadı..")
        elif secim == 4:
            plaka = input("Araç Plaka Giriniz: ").upper()
            kira_d = input("Araç Kira Durumunu Güncelleyin: E/H").capitalize()
            if kira_d == "e" or kira_d =="E":
                imlec.execute("update kirala set kira_d=? where plaka=?", (plaka, kira_d, ))
                db.commit()
                print("{} Plakalı Araç İle İgili İşlemler Güncellenmiştir.".format(plaka))
                print("Üst Menüye Dönmek için Enter'a Basın!")
                input()
            elif kira_d == "h" or kira_d == "H":
                print("Güncelleme İşlemi Başlatılamadı..")
