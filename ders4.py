'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
sayi=int(input("1 ile 100 arasinda bir sayi giriniz : "))
if 0<sayi<100:
   print("dogru")
else:
   print("yanlis")
   
'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''
sayi=int(input("Bir sayi giriniz : "))
if sayi%2==0:
   print("Cift sayi")
else:
   print("tek sayi")

'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = 'email@gamil.com'
password = 'abc123'
'''

email=input("E-mail giriniz : ")
passwort=input("passwort giriniz : ")
if email=='email@gamil.com' and passwort=='abc123':
   print("e-mail ve passwort dogru")
else:
   print("e-mail veya passwort yanlis")

'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

'''

sayi1=input("bir sayi giriniz : ")
sayi2=input("bir sayi giriniz : ")
sayi3=input("bir sayi giriniz : ")
if sayi1==sayi2 and sayi2==sayi3:
   print(sayi3+" = "+sayi1+" = "+sayi2)
elif sayi1>=sayi2 and sayi1>=sayi3 and sayi2==sayi3:
      print(sayi1+" > "+sayi2+" = "+sayi3)
elif  sayi2==sayi3 and sayi1<sayi2:
      print(sayi1+" < "+sayi2+" = "+sayi3) 
elif sayi1>=sayi2 and sayi1>=sayi3 and sayi2>sayi3:
      print(sayi1+" > "+sayi2+" > "+sayi3) 
elif sayi1>=sayi2 and sayi1>=sayi3 and sayi3>sayi2 :
      print(sayi1+" > "+sayi3+" > "+sayi2)
elif sayi2>=sayi1 and sayi2>=sayi3 and sayi1==sayi3 :
      print(sayi2+" > "+sayi1+" = "+sayi3)
elif sayi2>=sayi1 and sayi2>=sayi3 and sayi1>sayi3:
      print(sayi2+" > "+sayi1+" > "+sayi3)
elif sayi2>=sayi1 and sayi2>=sayi3 and sayi1<sayi3 :
      print(sayi2+" > "+sayi3+" > "+sayi1)
elif sayi3>=sayi1 and sayi3>=sayi2 and sayi2==sayi1 :
      print(sayi3+" > "+sayi2+" = "+sayi1)
elif sayi3>=sayi1 and sayi3>=sayi2 and sayi2>sayi1:
      print(sayi3+" > "+sayi2+" > "+sayi1)
elif sayi3>=sayi1 and sayi3>=sayi2 and sayi2<sayi1:
      print(sayi3+" > "+sayi1+" > "+sayi2)
      

'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''

sayi1=float(input("1. vize notunu giriniz : "))
sayi2=float(input("2. vize notunu giriniz : "))
sayi3=float (input("final notunu giriniz:"))
ortalama=(((sayi1+sayi2)/2)*60+sayi3*40)/100
print(ortalama)
if ortalama>= 50 and int(sayi3)>=50:
  print("Gectiniz.")
elif int(sayi3)>=70:
  print("Gectiniz.")
else:
  print("Kaldiniz.") 

'''

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)
   
'''
ad=input("Adinizi giriniz : ")
kilo=float(input("kilonuzu giriniz : "))
boy=float(input(" m cinsinden  giriniz : "))

kiloIndex=kilo/boy**2

if 0<kiloIndex<18.4:
   print(ad +'adli kisi kilo indeksine göre zayif ')
elif 18.5<kiloIndex<24.9:
   print(ad +'adli kisi kilo indeksine göre Normal')
elif 25.0<kiloIndex<29.9:
   print(ad +'adli kisi kilo indeksine göre Fazla Kilolu')
elif 30.0<kiloIndex<34.9:
   print(ad +'adli kisi kilo indeksine göre OBEZ')
   
#===========================================================================================
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
for i in sehirler:
   if len(i)<=5:
      print(i)

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0

for i in urunler:
    a = int(i["price"])
    print (i["price"])
    
    toplam += a

print(toplam)
   
  
   
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for i in urunler:
    a = int(i["price"])
  
    if a <= 5000:
        print(i["name"], a)

#=================================================================================================
sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

i=0
while i<len(sayilar):
   print(sayilar[i])
   i += 1
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın

baslangic=int(input("bir baslangic degeri giriniz : "))
bitis=int(input("bir bitis degeri giriniz : "))
i=baslangic
while i<bitis:
   if i%2==1:
      print(i)
   i += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
for n in range(100,0,-1):
 print(n)



# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
i=0
a=[]
while i<5:
   sayi=int(input("bir sayi giriniz: "))
   a.append(sayi)
   i += 1
print(a)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

ürünSayisi=int(input("Kac ürün gireceksiniz? : "))
i=0
ürünList={}
while i<ürünSayisi:
 ürünName=input(str(i+1)+ " ürünün ismini giriniz : ")
 ürünPrice=int(input(str(i+1)+" ürünün fiyatini giriniz : "))
 ürünList.update({ürünName:ürünPrice})
 i += 1
print(ürünList)

