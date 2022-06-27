names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]


# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
print(names)
# 3-  "Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)
# 4-  "Deniz" isminin indeksi nedir ?
# print(names.index('Deniz')) deniz listede yok
print(names.index('Hakan'))
names.pop()
# 5-  "Ali" listenin bir elemanı mıdır ?
print('Ali' in names)
# 6-  Liste elemanlarını ters çevirin
names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)
# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)
# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
print(str.split(','))
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min = min(years)
max = max(years)
print(min, max)
# 11- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka1= input("marka: ")
markalar.append(marka1)

marka2 = input("marka: ")
markalar.append(marka2)

marka3 = input("marka: ")
markalar.append(marka3)

print(markalar)


