'''
temel seviye python kursu aşağıdaki bölümlerden oluşuyor.
8:55
1. Tanıtım
2. Gerekli Ortamın Hazırlanması
3. Python Objeleri ve Veri Yapıları
4. Python Operatörleri
5. Pythonda Koşul İfadeleri
6. Pythonda Döngüler
7. Pythonda Fonksiyonlar
8. Pythonda Nesne Tabanlı Programlama
9. Pythonda Modüller
10. Pythonda Hata ve Hata Yönetimi
11. Pythonda Dosya Yönetimi
12. Pythonda Fonksiyonların İleri Seviye Özellikleri
13. Pythonda Iterators
14. Python Generators
15. İleri Seviye Python Modülleri & Web Scraping
'''

'''
python firstLesson.py

python
print("hello world")
exit()

'''

print("Hello, World!")

'''Legal variable names'''

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


'''String Format'''
'''
age = 36
txt = "My name is John, I am " + age
print(txt)
'''
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
