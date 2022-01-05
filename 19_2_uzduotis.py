"""
Patobulinti 1 užduoties programą, kad ji:
Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"
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

window.bind("<Return>", lambda event: spausdinti())

entry.pack()
label_1.pack()
button.pack()
label_2.pack()

window.mainloop()