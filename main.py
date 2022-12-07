meno=input('Zadaj meno suboru: ')

def otvor_subor(meno='text3.txt'):
    return open('data/'+meno,'r',encoding='UTF-8')

def spracuj_subor(fr):
    riadky=fr.readlines()
    temp=riadky[1].strip()
    slova=temp.split(' ')
    print("'"+temp+"'")
    print(slova[0])
    print(temp.count(' '))
    poc=0
    for i in temp:
        if i==' ':
            poc+=1
    print(poc)
#shift F6 good thing
def sirka(fr):
    maxlen= 0
    for riadok in fr:
        if len(riadok) >maxlen:
            maxlen=len(riadok)
    return maxlen
fr=otvor_subor(meno)
#spracuj_subor(fr)
print(sirka(fr))
print(*fr)

