#F.Kruusimäe
#27.10.22
#tekstifailiga mässamine

failike=open("s6pru_l6ustaraamatus.txt","r")

reformikad = 0
kesikud = 0
erakonnad = []

for rida in failike.readlines():
    ee,pe,era,kyl = rida.split(" ")
    if era=="RE":
        reformikad+=1
    elif era=="KE":
        kesikud+=1
    if era not in erakonnad:
        erakonnad.append(era)
    with open ("kirjutamine.txt","a") as fail_kirjutamiseks:
        fail_kirjutamiseks.write(ee+" "+pe+"\n")
        






        
print(f"Reformikaid kokku {reformikad}")
print(f"Kesikud kokku {kesikud}")
print(f"Erakondi kokku{len(erakonnad)}")
failike.close()
