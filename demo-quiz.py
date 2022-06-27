from operator import index


class Soru:
    def __init__(self, text,options,answer):
        self.text = text
        self.options = options
        self.answer=answer
    
p1 = Soru("En sevdigin renk hangisidir?",["sari","mavi","kirmizi","beyaz"],"sari") 
p2 = Soru("En sevdigin gün hangisidir?",["pazar","pazartesi","cuma","cumartesi"],"pazar")
sorular=[p1,p2]
def showSoru():
    return 
#def checkSoru(printSoru):
     #return i.answer==cevap
def printSoru():
    dogruCevapSayisi=0
    for i in sorular:
     print(f'{sorular.index(i)+1}) {i.text}  \n  {i.options}')
     cevap=input("cevabi giriniz : ")
     if(cevap==i.answer):
        dogruCevapSayisi += 1
        print("tebrikler,dogru cevap")
     else:
        print("dogru cevap : "+ i.answer)
    print(f'dogru cevap sayisi: {dogruCevapSayisi}  \n toplam soru sayisi: {len(sorular)}')      
printSoru()    