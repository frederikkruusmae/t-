from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.configure
aken.geometry("300x300")

#funktsioonid
def arvuta():
    hind = float(sisestus.get())
    kmaks = var.get()
    vastus = hind*kmaks
    silt1.config(text=str(vastus)+"€")
    silt2.config(text=str(vastus+hind)+"€")
    print(hind, kmaks, vastus)
#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)
silt = Label(aken, text="Käibemaksumäär:")
silt.grid(row=1,column=0)
silt = Label(aken, text="______________________________________________________________")
silt.grid(row=3,column=0,columnspan=2)
silt = Label(aken, text="Käibemaks:")
silt.grid(row=4,column=0)
silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=5,column=0)
silt1 = Label(aken, text="0.00€")
silt1.grid(row=4,column=1)
silt2 = Label(aken, text="0.00€")
silt2.grid(row=5,column=1)
#valikud
var = DoubleVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=0.09)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=0.2)
valikukast.grid(row=2, column=1)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupud
nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=6, column=1)

aken.mainloop()