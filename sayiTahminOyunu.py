'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
      üzerinden hesaplansın.
'''

import random


bulunacakSayi = random.randint(0, 100)
hakSayisi=int(input("Kac hakkiniz olsun? :"))
tahmin=int(input ("0 ile 100 arasinda bir sayi giriniz."))
i=0
while i < hakSayisi-1:
 if tahmin==bulunacakSayi:
  print("PUANINIZ :  "+str((hakSayisi-i)*100/hakSayisi))
  break
 elif tahmin<bulunacakSayi :
  if i<hakSayisi-1 :
   tahmin=int(input (str(tahmin)+' den büyük bir sayi giriniz.'))
   i += 1
   if i==hakSayisi-1:
     print("Haklarin bitti, tekrar dene")
 else: 
  if i<hakSayisi-1:
   tahmin=int(input (str(tahmin)+' den kücük bir sayi giriniz.'))
   i += 1
   if i==hakSayisi-1:
     print("Haklarin bitti, tekrar dene")
  
 
   
