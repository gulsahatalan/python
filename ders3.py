#Atama operatorleri

from re import S, X
from unittest import result

from pkg_resources import safe_extra

x, y, z = 2, 5, 10
numbers= 3,5,7,9,12,14

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
no1=input("bir sayi giriniz : ")
no2=input("bir sayi giriniz : ")

malt=int(no1) *int(no2)
print(malt-(x+y+z))
# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
print(y%x)
# 3- (x,y,z) toplamının mod 3' ü nedir ?
print((x+y+z)%3)
# 4- y' nin x. kuvvetini hesaplayınız.
print(y**x)
# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
x, *y ,z = numbers
print(z ** 3)
# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?

print(y[0]+y[1]+y[2]+y[3])



#karsılastırma operatorlerı

# 1- Girilen 2 sayıdan hangisi büyüktür ?
sayi1=input("bir sayi giriniz : ")
sayi2=input("bir sayi giriniz : ")
isSayi1Bigger=sayi1>sayi2
print (f'sayi 1 , sayi 2 den daha buyuktur: {str(isSayi1Bigger)}')


# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
sayi1=input("vize notunu giriniz : ")
sayi2=input("final notunu giriniz : ")
ortalama=(float(sayi1)*60+float(sayi2)*40)/100
print(ortalama)
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
isGecti=ortalama>= 50
print(f'Gecti mi ? : {isGecti}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi=input("bir sayi giriniz : ")
ciftMi=int(sayi)%2==0
tekMi=int(sayi)%2==1
print(f'{sayi} cifttir: {ciftMi}')
print(f'{sayi} tektir: {tekMi}')  
# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi=input("bir sayi giriniz : ")
isPozitif=int(sayi)>0
isNegatif=int(sayi)<0
print(f'{sayi} pozitiftir : {isPozitif}')
print(f'{sayi} negatiftir : {isNegatif}')      
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@gmail.com parola:abc123)
eMail=input("E mailinizi giriniz : ")
parola=input("parolanizi giriniz : ")

isMailTrue=eMail=="email@gmail.com"
isParolaTrue=parola=='abc123'

print(f'Email: {isMailTrue}')
print(f'Parola : {isParolaTrue}')      
#mantıksal operatorler

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi=input("bir sayi giriniz:")
isSayi=0<int(sayi)<100
print(f'{sayi} 0 ile 100 arasindadir: {isSayi}')
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi=input("bir sayi giriniz:")
isPozitifCift=int(sayi)>0 & int(sayi)%2==0
print(f'{sayi} pozitif cift sayidir : {isPozitifCift}')
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
eMail=input("E mailinizi giriniz : ")
parola=input("parolanizi giriniz : ")

isMailTrue=eMail=="email@gmail.com"
isParolaTrue=parola=='abc123'
dogru=isMailTrue and isParolaTrue
print(f'e mail ve parola bilgisi : {dogru}')   

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1=input("bir sayi giriniz:")
sayi2=input("bir sayi giriniz:")
sayi3=input("bir sayi giriniz:")

enBuyukSayi = (sayi1>sayi2) and (sayi1>sayi3)
print(f'sayi1 en büyük sayıdır : {enBuyukSayi}')

enBuyukSayi = (sayi2>sayi3) and (sayi2>sayi1)
print(f'sayi2 en büyük sayıdır : {enBuyukSayi}')

enBuyukSayi = (sayi3>sayi1) and (sayi3>sayi2)
print(f'sayi3 en büyük sayıdır : {enBuyukSayi}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
sayi1=input("1. vize notunu giriniz : ")
sayi2=input("2. vize notunu giriniz : ")
sayi3=input("final notunu giriniz:")
ortalama=(((float(sayi1)+float(sayi2))/2)*60+float(sayi3)*40)/100
print(ortalama)
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
if ortalama>= 50:
  print("Gectiniz.")
else: print("Kaldiniz.") 
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
if ortalama>= 50 and int(sayi3)>=50:
  print("Gectiniz.")
else: print("Kaldiniz.") 
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
if ortalama>= 50 or int(sayi3)>=70:
  print("Gectiniz.")
else: print("Kaldiniz.") 

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
ad=input("Adinizi giriniz : ")
kilo=input("kilonuzu giriniz : ")
boy=input(" m cinsinden  giriniz : ")
kiloIndex=float(kilo)/float(boy)**2
isZayif= 0<kiloIndex<18.4
isNormal=18.5<kiloIndex<24.9
isKilolu=25.0<kiloIndex<29.9
isObez=30.0<kiloIndex<34.9
print(f'{ad} `nin kilo indeksine göre zayif  : {isZayif}')
print(f'{ad} `nin kilo indeksine göre Normal  : {isNormal}')
print(f'{ad} `nin kilo indeksine göre Fazla Kilolu : {isKilolu}')
print(f'{ad} `nin kilo indeksine göre OBEZ : {isObez}')  






      