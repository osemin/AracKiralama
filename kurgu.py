if hasar == "E" or hasar == "e":
    hasar_durum = input("Hasar Durumunu Belirtin: ").capitalize()
    kira_durum = input("Araç Kirada Mı E/H: ").capitalize()
    if kira_durum == "E" or "e":
        kira_fiyati = int(input("Araç Kira Fiyatını Giriniz: "))
        imlec.execute(
            "insert into kiraislem(plaka,marka,model,km,kira_durum,hasar,hasar_durum,kira_fiyati) values(?,?,?,?,?,?,?,?)",
            (plaka, marka, model, km, kira_durum, hasar, hasar_durum, kira_fiyati))
        db.commit()
        print("{} Plakalı Araç Eklenmiştir.Kiralama Listesinden Kontrol Edebilirsin".format(plaka))
        print("Üst Menüye Dönmek için Enter'a Basın!")
        input()
elif hasar == "h" or hasar == "H":
    kira_durum = input("Araç Kirada Mı E/H: ").capitalize()
    if kira_durum == "E" or "e":
        kira_fiyati = int(input("Araç Kira Fiyatını Giriniz: "))
        imlec.execute(
            "insert into kiraislem(plaka,marka,model,km,kira_durum,hasar,hasar_durum,kira_fiyati) values(?,?,?,?,?,?,?,?)",
            (plaka, marka, model, km, kira_durum, hasar, hasar_durum, kira_fiyati))
        db.commit()
        print("{} Plakalı Araç Eklenmiştir.Kiralama Listesinden Kontrol Edebilirsin".format(plaka))
        print("Üst Menüye Dönmek için Enter'a Basın!")
        input()




