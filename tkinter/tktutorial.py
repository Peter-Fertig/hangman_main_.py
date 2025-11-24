import Rafiki_contribution as Rafiki
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Simple App")

def add_to_list(event = None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)


frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky="EW")

#entry.bind("<Return>", add_to_list)

entry_btn = ttk.Button(frame, text = "Yo yo whatsup", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = ttk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="NSEW")


################################################################

def add_to_list2(event = None):
    text = entry2.get()
    if text:
        text_list2.insert(tk.END, text)
        entry2.delete(0, tk.END)

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="NSEW", padx=5, pady=5)



frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry2 = tk.Entry(frame2)
entry2.grid(row=0, column=0, sticky="EW")

entry2.bind("<Return>", add_to_list2)

entry_btn = tk.Button(frame2, text = "button002", command=add_to_list2)
entry_btn.grid(row=0, column=1)

text_list2 = tk.Listbox(frame2)
text_list2.grid(row=1, column=0, columnspan=2, sticky="NSEW")

root.mainloop()