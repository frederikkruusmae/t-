from tkinter import *

#akna seaded
aken = Tk()
aken.title('MA EI TEA MIS LIPP')
aken.configure(background="White")

#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(50, 300, 450, 206,fill="red")
louend.create_arc(100, 160, 250, 250, extent=180,fill="red")
louend.create_arc(100, 160, 250, 250, extent=-180,fill="White")
aken.mainloop()