from tkinter import *

from gui_hangman import my_label

root = Tk()
root.title("Entry Widget")
root.iconbitmap("images/dakotaphonehq.ico")
root.geometry("500x350")

def answer():
    pass


my_label = Label(root, text="Enter your Name", font=("Times New Roman", 24))
my_label.pack(pady=20)

my_entry = Entry(root)
my_entry.pack(pady=20)

my_button = Button(root, text="answer", command=answer)
my_button.pack(pady=20)

#create hidden lable
hidden_label = Label(root, text="", font=("Times New Roman", 24))
hidden_label.pack(pady=20)

root.mainloop()