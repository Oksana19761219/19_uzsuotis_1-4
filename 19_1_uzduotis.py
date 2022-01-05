"""
Sukurti programą su grafine sąsaja, kuri:
Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"
"""

from tkinter import Tk, Label, Entry, Button

window = Tk()
window.geometry("200x100")

def spausdinti():
    result = entry.get()
    label_2["text"] = f"Labas, {result}"


entry = Entry(window)
label_1 = Label(window, text="Įveskite vardą")
label_2 = Label(window, text="")
button = Button(window, text="vykdyti", command=spausdinti)


entry.pack()
label_1.pack()
button.pack()
label_2.pack()

window.mainloop()