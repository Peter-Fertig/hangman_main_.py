from tkinter import *




root = Tk()
root.title("Guess a letter")

root.geometry("500x500")

#create global switch variable
global switch
switch = True
def change():
    global switch
    if switch == True:
        my_label.config(text="Goodbye WOrld!")
        switch = False
    else:
        my_label.config(text="Hello World!")
        switch = True

my_label = Label(root, text="HelloWorld",font=("Helvetica",35))
my_label.grid(row=0, column=0)
my_button = Button(root, text="Click Here", command=change)
my_button.grid(row=1, column=1)

root.mainloop()