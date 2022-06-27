from itertools import count

course="Python Kursu:Python Programlama 2022"
website="http://www.sadullahdemirci.com"


# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

print('course karakterinde '+str(len(course))+' karakter bulunur.')

# 2- 'website' içinden www karakterlerini alın.
''''wwwSilme=website.replace("www", "")'''
wwwSilme1=website[:7]
wwwSilme2=website[10:30]
print(wwwSilme1+wwwSilme2)

# 3- 'website' içinden com karakterlerini alın.
'''comSilme=website.replace("com", "")'''
comSilme=website[:27]
print(comSilme)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
ilk15=course[:15]
son15=course[15:]
print(ilk15)
print(son15)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print('course tersten => '+str(course[::-1]))

name, surname, age, job = 'Ahmet','Yılmaz', 32, 'mühendis'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Ahmet Yılmaz, Yaşım 32 ve mesleğim mühendis.'
print(f'Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}.')

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
a = "Hello world!"
'''print(a.replace("w", "W"))'''
print(a[:6]+"W"+a[7:])

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
string="abc"
print(3 * string)