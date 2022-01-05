"""
Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys
"""

from tkinter import Tk, Label, Entry, Button, Menu, StringVar

window = Tk()
window.geometry("200x100")

text = StringVar("")

def spausdinti():
    result = entry.get()
    label_2["text"] = f"Labas, {result}"

def isvalyti():
    text.set(label_2["text"])
    label_2["text"] = ""

def atkurti():
    label_2["text"] = text.get()

def iseiti():
    window.destroy()


entry = Entry(window)
label_1 = Label(window, text="Įveskite vardą")
label_2 = Label(window, text="")
button = Button(window, text="vykdyti", command=spausdinti)

menu_ = Menu(window)
window.config(menu=menu_)
submenu = Menu(menu_, tearoff = 0)
menu_.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Išvalyti", command=isvalyti)
submenu.add_command(label="Atkurti", command=atkurti)
submenu.add_separator()
submenu.add_command(label="Išeiti", command=iseiti)

window.bind("<Return>", lambda event: spausdinti())

entry.pack()
label_1.pack()
button.pack()
label_2.pack()

window.mainloop()