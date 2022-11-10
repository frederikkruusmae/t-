#F.Kruusimae
#25.10.2022
#Harjutus05


#vanused
vanused = [1,2,3,4,5]
print(sum(vanused))
print(max(vanused))
print(min(vanused))
print(len(vanused))




print("-------------")
#Dublikaadid
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for opilane in opilased:
    if opilane not in puh_opilased:
        puh_opilased.append(opilane)
        
print(puh_opilased)


print()

print("---------")

#õpilased
jrk = 1
opilased = ["Juan","Kati","Maarja","Mario","Mati"]

for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
number = int(input("Mitmendat nime soovid muuta: "))-1
opilane = input("Lisa nimi siia: ")
del opilased[number]
opilased.insert(number,opilane)
print(opilased)



#Nimede lisamine loendisse
print("----------")
nimed = []
for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)

print(f"Viimane nimi: {nimed[-1]}")
nimed.sort()
print(nimed)
