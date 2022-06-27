# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def showName(name):
    print (name)

showName('gülsah')


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
def liste_oluştur(*args):
  print(args)

liste_oluştur(1,2,"as","asdsd@ch.com")
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

asalSayilar=[]
def asalSayi(sayi1,sayi2):
 for i in range(sayi1,sayi2 + 1):
    for a in range(2,i//2):
           if (i % a) == 0:
               break
               
    else:
     asalSayilar.append(i)

 print(asalSayilar)
asalSayi(10,33)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
def tamBölen(sayi):
    list=[]
    for i in range(1,sayi+1):
     if sayi % i == 0:
         list.append(i)
    print(list)
tamBölen(20)