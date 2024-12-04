sys_kullanici_adi="Murat"
sys_parola="12345"
kullanici_adi=input("kullanici adi  girin:")
parola=input("parola girin:")
if(sys_kullanici_adi==kullanici_adi and sys_parola!=parola):
    print("Parola hatali ")
elif(kullanici_adi!=sys_kullanici_adi and sys_parola==parola):
    print("kullanici adi yalnis")
elif(sys_kullanici_adi!=kullanici_adi and sys_parola!=parola):
    print("her ikisi sehv")
else:
    print("her ikisi dogru")