print("*****************\nfaktöriyel bulma\n*****************\nprogramdan çıkmak \niçin a ya basın\n*****************")
while True:
    sayı = input("faktöriyelini almak istediğiniz sayıyı girin:")
    if(sayı == "a"):
        print("programdan çıkılıyor")
        break
    else:
        sayı = int(sayı)
        f = 1
        for i in range(1,sayı+1):
            f *= i
    print(sayı,"sayısının faktöriyeli:",f)