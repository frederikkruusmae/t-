#F.Kruusimäe
#17.10.2022
#harjutus04

#müük
hind = int(input("Pane siia oma hind"))
if hind<= 10:
    ale = 0.1
else:
    hind>= 10
    ale = 0.2
    









#Juubel
sp = "5.6.2002"
d,m,y = sp.split(".")
vanus = 2022-int(y)

if vanus%5 == 0:
    print("JUUBEL")
else: ("EI OLE JUUBEL")



#matem
a,b = 10,20
tehe = input("Vali tehe (+ - * /): ")
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus = a - b

else:
    vastus = "n/a"
print(f"{a} {tehe} {b} = {vastus} ")

#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")
