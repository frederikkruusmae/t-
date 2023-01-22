from tkinter import *

# Akna.seaded 
aken = Tk()
aken.title("ul 03")
aken.configure(background="#000000")
aken.geometry("400x150")
aken.minsize(200,100)
aken.maxsize(800,400)
aken.resizable(0, 0)

#font
font = ("Tahoma", 12, "bold italic")
aken.option_add("*font",(font))
#font

#tekst
label = Label(aken, text="Nimi: Frederik Kruusimäe\nRühm: IT-22\n2022",foreground="red", background="#000000",padx=2, pady=2)
label.pack()

aken.mainloop()