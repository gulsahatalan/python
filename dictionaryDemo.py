
    
students = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
'''
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.'''
students = {}
for i in range(3):
 number = input("Student no: ")
 name = input("Student first name: ")
 surname = input("Student last name: ")
 phone = input("Student phone: ")

 students.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
 print(students)

   # 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
studentNo = input('student no: ')
stdent = students[studentNo]
print(stdent)

