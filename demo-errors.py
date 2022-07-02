liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
for i in liste:
   try:
    print(int(i))
   except Exception as ex:
    print(i+" sayisal deger degil")

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.
import re

sayiInput= input("Input: ")

for i in sayiInput:
    if re.search("[q]",sayiInput):
     print("input kabul edildi!")
    elif  re.search("[a-z]",sayiInput):
        raise Exception("input kücük harf icermemelidir.")
    elif  re.search("[A-Z]",sayiInput):
        raise Exception("input BUYÜK harf icermemelidir.")
    elif  re.search("[_@$]",sayiInput):
        raise Exception("input alfa numeric karakter icermemelidir.")
    elif  re.search("[/s]",sayiInput):
        raise Exception("input bosluk icermemelidir.")

print("Parola kabul edildi!")

# 3: Girilen parola içinde türkçe karakter hatası veriniz.
tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")


# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin
def faktöriyel():
 sayi=int(input ("bir sayi giriniz : "))   
 result=1
 for i in range(1,sayi+1):
   result = i*result
 print (result)
try:
  faktöriyel()
except ValueError:
  print("Lütfen tam  bir sayi giriniz")

# integer a cevirdigim icin value error dan baska hata olmuyor.Bunun baska bir yapimi var mi?

