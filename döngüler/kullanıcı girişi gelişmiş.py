print("***********\nkullanıcı giriş programı\n************")
sys_kullanıcı_adı = "simanur"
sys_parola = "123456"
giriş_hakkı = 3
while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola:")
    if( kullanıcı_adı != sys_kullanıcı_adı  and parola == sys_parola):
        print("kullanıcı adı hatalı")
        giriş_hakkı -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("parola hatalı")
        giriş_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("giriş başarısız...")
        giriş_hakkı -= 1
    else:
        print("giriş başarılı :)")
        break
    if(giriş_hakkı == 0):
        print("sisteme giriş hakkınız dolmuştur.")
        break