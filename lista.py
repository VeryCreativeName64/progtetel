import random


lista=[]
for i in range(1,11):
    szam=random.randint(5,15)
    lista.append(szam)



def megszamlalas():
    i=0
    db=0
    while(i<len(lista)):
        if (lista[i]==13):
            db+=1
        i+=1
    print(f"{db} darab 13-as van.")

def osszegzes():
    i=0
    db=0
    while(i<len(lista)):
        db+=lista[i]
        i+=1
    print(f"{db} a 10 szám összege")

def min():
    m=0
    for i in range(1,len(lista),1):
        if lista[m]>lista[i]:
            m=lista[i]
    print(f"{m} a legkisebb szám")

def tizenharom():
    i=0
    while(i<len(lista) and lista[i]!=13):
        i+=1

def nagyobbtiz():
    i=0
    while(i<len(lista) and lista[i]>10):
        i+=1

def eldontes1():
    i=0
    while(i<len(lista) and lista[i]!=13):
        if lista[i]==13:
            print(lista[i])
            i+=1
        else:
            print(lista[i-1])
            i+=1







