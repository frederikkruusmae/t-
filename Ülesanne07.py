#F.Kruusimäe
#27.10.22
#Funktsioonid
import math
def kuup(a):
    print(f"Kuubi ruumala on {a**3}")
def kera(r):
    print(f"Kera ruumala on {round(4/3*math.pi*r**3,2)}")
def koonus(r,h):
    ???
def silinder(r,h):
    ???
loop = 1
while loop == 1:
    print("********** LEIAME RUUMALA **********")
    valik = int(input("1. Kuup\n2. Kera\n3. Koonus\n4 Silinder\n5. Välju\nTee valik 1-5: "))
    if valik == 1:
        a = int(input("Lisa kuubi üks külg: "))
        kuup(a)
    elif valik == 2:
        kera()
    elif valik == 3:
        koonus()
    elif valik == 4:
        silinder()
    elif valik == 5:
        loop == 0
    else:
        print("Sellist valikut pole!")
    





#loome argumentitega funktsiooni
def tevita(nimi="tundmatu",keel="ge"):
    if keel=="et":
        print(f"Tere {nimi}")
    elif keel=="en":
        print(f"Hi {nimi}")
    else:
        print(f"Hallo {nimi}")
    
tevita()
tevita("mari","en")
