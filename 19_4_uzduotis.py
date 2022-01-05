"""
Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:

Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą
"""

from tkinter import Tk, Label, Entry, Button, Menu, StringVar, SUNKEN, W, BOTTOM, X

window = Tk()
window.geometry("200x100")

text = StringVar("")

def spausdinti():
    result = entry.get()
    label_2["text"] = f"Labas, {result}"
    status_bar["text"] = "Sukurta"

def isvalyti():
    text.set(label_2["text"])
    label_2["text"] = ""
    status_bar["text"] = "Išvalyta"

def atkurti():
    label_2["text"] = text.get()
    status_bar["text"] = "Atkurta"

def iseiti():
    window.destroy()


entry = Entry(window)
label_1 = Label(window, text="Įveskite vardą")
label_2 = Label(window, text="")
button = Button(window, text="vykdyti", command=spausdinti)
status_bar = Label(window, text="", bd=1,relief=SUNKEN, anchor=W)


menu_ = Menu(window)
window.config(menu=menu_)
submenu = Menu(menu_, tearoff = 0)
menu_.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Išvalyti", command=isvalyti)
submenu.add_command(label="Atkurti", command=atkurti)
submenu.add_separator()
submenu.add_command(label="Išeiti", command=iseiti)

window.bind("<Return>", lambda event: spausdinti())
window.bind("<Escape>", lambda event: iseiti())

entry.pack()
label_1.pack()
button.pack()
label_2.pack()
status_bar.pack(side=BOTTOM, fill=X)

window.mainloop()