import tkinter as tk
from tkinter import *
from tkinter import ttk




root = tk.Tk()
root.title("Guess a letter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
secret = "M"

ttk.Label(mainframe, text="Guess a letter").grid(column=2, row=2, sticky="WE")

letter = tk.StringVar()
letter_entry = ttk.Entry(mainframe, width=7, textvariable=letter)
letter_entry.grid(column=2, row=1, sticky="WE")
ttk.Label(mainframe, textvariable =letter ).grid(column=4, row=2, sticky="WE")

ttk.Button(mainframe, text="guess", command=  letter).grid(column=3, row=3, sticky="W")


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)





root.mainloop()