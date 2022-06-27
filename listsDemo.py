# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabaMarkalari = ['Bmw','Mercedes','Opel','Mazda']
# 2-  Liste Kaç elemanlıdır ?
print(len(arabaMarkalari))
# 3-  Listenin ilk ve son elemanı nedir ?
print(arabaMarkalari[0])
print(arabaMarkalari[-1])
# 4-  Mazda değerini Toyota ile değiştirin.
arabaMarkalari[-1]= 'Toyota'
print(arabaMarkalari)

# 5-  Mercedes listenin bir elemanı mıdır ?
print('Mercedes' in arabaMarkalari)
# 6-  Listenin -2 indeksindeki değer nedir ?
print(arabaMarkalari[-2])
# 7-  Listenin ilk 3 elemanını alın.
print(arabaMarkalari[0:3])
# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabaMarkalari[2]= 'Totoya'
arabaMarkalari[3]= 'Renault'
print(arabaMarkalari)
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
print(arabaMarkalari + ['Audi','Nissan'])
print(arabaMarkalari)
# 10- Listenin son elemanını silin.
del arabaMarkalari[-1]
print(arabaMarkalari)
# 11- Liste elemanlarını tersten yazdırınız.
print(arabaMarkalari[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız.
      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Demir  1999, (80,80,70)
      # studentC: Ahmet Demir 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA[0]+" , "+studentA[1]+" , "+str(studentA[2])+" , "+str(studentA[3][0])+" , "+str(studentA[3][1])+" , "+str(studentA[3][2]))
print(studentB[0]+" , "+studentB[1]+" , "+str(studentB[2])+" , "+str(studentB[3][0])+" , "+str(studentB[3][1])+" , "+str(studentB[3][2]))
print(studentC[0]+" , "+studentC[1]+" , "+str(studentC[2])+" , "+str(studentC[3][0])+" , "+str(studentC[3][1])+" , "+str(studentC[3][2]))

print(f"{studentA[0]} {studentA[1]} {studentA[2]} dogumlu ve notlari {studentA[3][0] ,studentA[3][1] , studentA[3][2]} dir")

print(f"{studentB[0]} {studentB[1]} {studentB[2]} dogumlu ve notlari {studentB[3][0] ,studentB[3][1] , studentB[3][2]} dir")

print(f"{studentC[0]} {studentC[1]} {studentC[2]} dogumlu ve notlari {studentC[3][0] ,studentC[3][1] , studentC[3][2]} dir")