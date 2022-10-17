#F.Kruusimäe
#11.10.22
#harjutus04

#palindroom
# Drive code

num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")






#tundide arv
a1,a2 = "8:30","14:15"
h1,m1 = a1.split(":")
minut1 = int(h1)*60+int(m1)
h2,m2 = a2.split(":")
minut2 = int(h2)*60+int(m2)
ajavahe = minut2-minut1
hh = ajavahe//60
mm = ajavahe%60
print(f"Ajavahe on {hh}:{mm}")



#email
email = "sasdas@asdasd.rer"
print("@" in email)





#vandumine
tekst = input("ütle kurat küll!:")
print(tekst.lower().replace("kurat","***"))

