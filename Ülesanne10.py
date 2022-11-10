#F.Kruusimäe
#02.11.2022
#Harjutus10

import re

#sobilik parool
fh = open('lorem.txt.txt')
for line in fh:
    if re.search('^[A-Z0-9]+[A-Z]{1}', line):
         print(line,end='')
         
#sobilik ip

fh = open('lorem.txt.txt')
for line in fh:
    if re.search('^[A-Z]+$', line):
         print(line,end='')
