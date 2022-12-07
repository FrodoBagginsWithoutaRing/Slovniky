fr=open('data/zvieratka.txt','r')
zoo={}
zoo3={}
for row in fr:
    temp = row.strip().split(' ') #zretazenie funkcii nejde to naopak
    zoo[temp[0]] = int(temp[1])
print(zoo)
zoo2= sorted(zoo)
for zviera in zoo2:
    zoo3[zviera]=zoo[zviera]  #hodne skarede, kuk ako triedit slovniky


vaha=0
for zviera in zoo:
    vaha+= zoo[zviera]

print(vaha // len(zoo2))
#print(vaha)
#print(zoo3)


# naj=list(zoo.keys())[0]
#
# for kluc in zoo.keys():
#     if zoo[kluc]>zoo[naj]:
#         naj= zoo[kluc]
# print(naj,zoo[naj])


def tazsie_ako_zviera(vz:str)->dict:
    new_zoo={}
    for zviera in zoo:
        if zoo[zviera] > zoo[vz]:
            new_zoo[zviera]= zoo[zviera]
    return new_zoo

print(tazsie_ako_zviera('diviak'))
