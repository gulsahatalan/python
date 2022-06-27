from re import S


website = "http://www.sadullahdemirci.com&quot;"
course  = "Python Kursu: Temel Seviye Python Programlama"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin. left rıght
a=' Hello World '
print(a+":"+a.strip())
# 2- 'www.sadullahdemirci.com&#39; içindeki sadullahdemirci bilgisi haricindeki her karakteri silin.
string= 'www.sadullahdemirci.com&#39;'
newString=string.strip("w,o,m,&,#,3,9,;,.")
print(newString.rstrip("c,."))
# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

print(course.lower())
print(course.upper())
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

print(website.count("a"))
print(website.count("e"))
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith("www"))
print(website.endswith("com"))
# 6-  'website' içinde '.com' ifadesi var mı? find and index
print(website.find(".com"))
print(website.index(".com"))
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(course.isalpha())
print(course.isdigit())
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.ljust rjust
print('Contents'.center(50, '*'))
# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(course.replace(' ', '-'))
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print('Hello World'.replace('World','There'))
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
print(course.split(' '))