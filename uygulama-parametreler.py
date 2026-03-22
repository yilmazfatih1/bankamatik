# Bankamatik uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    {
        "ad":"Fatih Yılmaz",
        "hesapNo":"123123",
        "bakiye":15000,
        "ekHesap":10000,
        "username":"fatihyilmaz",
        "password":"4321",
        "ekHesapLimit":10000
    },
     {
        "ad":"Patrick Jane ",
        "hesapNo":"123456",
        "bakiye":55000,
        "ekHesap":20000,
        "username":"patrickjane",
        "password":"1111",
        "ekHesapLimit":20000
    }  
]

def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap['ad']}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")
    print("4- Çıkış")
    
    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem == "4":
        cikis(hesap)
    else:
        print("Yanlış Seçim")
    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap['bakiye']}")
    print(f"ek bakiye: {hesap['ekHesap']}")

def paraCekme(hesap):
    miktar = float(input("çekmek istediğiniz miktar: "))
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzni = input("ek hesap kullanılsın mı ? (e/h): ")

            if ekHesapKullanimIzni == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print("izniniz olmadığı için ek hesaptan para çekilemedi")
        else:
                print("üzgünüz bakiyeniz yetersiz")

def paraYatirma(hesap):
    miktar = float(input("yatırmak istediğiniz miktar: "))
    if (hesap["ekHesap"] < hesap["ekHesapLimit"]):
        eklenen = hesap["ekHesapLimit"] - hesap["ekHesap"]
        if (miktar <= eklenen):
            hesap["ekHesap"] += miktar
            miktar = 0
        else:
            hesap["ekHesap"] = hesap["ekHesapLimit"]
            miktar -= eklenen
    hesap["bakiye"] += miktar
    print ("İşleminiz gerçekleştirilmiştir.")



def cikis(hesap):
    print("İyi günler dileriz!")
    print("\n")
    login()

        
def login():
    username = input("username: ")
    password = input("parola: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break
    if not(isLoggedIn):
        print("username yada parola hatalı")

login()