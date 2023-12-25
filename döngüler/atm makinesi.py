print("****************************\natm programı\n------------\n1.bakiye sorgulama\n2.para yatırma\n3.para çekme\n"
"(çıkmak için q ya basınız.)\n****************************")
bakiye = 1000
while True:
    işlem = input("yapmak istediğiniz işlemi seçiniz:")
    if(işlem == "q"):
        print("yine bekleriz.....")
        break
    elif(işlem == "1"):
        print(bakiye)
    elif(işlem == "2"):
       miktar = int(input("miktar giriniz:"))
       bakiye += miktar
    elif(işlem == "3"):
        miktar = int(input("miktar giriniz:"))
        if(miktar > bakiye):
            print("bu miktarı çekemezsiniz")
        else:
            bakiye -= miktar
    else:
        print("geçersiz işlem")

