from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("300x400")

entry_field = Entry(window, width=45, justify=RIGHT)
entry_field.grid(column=0, row=0, columnspan=4,  pady=8, padx=13, ipady=8)

def helloCallBack():
   print( "Hello Python")

def hello():
   print("hello")


clear_button = Button(text="C", command=hello())
divide_button = Button(text="/", command=hello())
mul_button = Button(text="x", command=helloCallBack())
min_button = Button(text="-", command=hello())
seven_button = Button(text="7", command=hello())
eight_button = Button(text="8", command=helloCallBack())
nine_button = Button(text="9", command=hello())
plus_button = Button(text="+", command=hello())
four_button = Button(text="4", command=hello())
five_button = Button(text="5", command=helloCallBack())
six_button = Button(text="6", command=hello())
one_button = Button(text="1", command=hello())
two_button = Button(text="2", command=helloCallBack())
three_button = Button(text="3", commanad=hello())
equals_button = Button(text="=", command=hello())
zero_button = Button(text="0", command=hello())
dot_button = Button(text=".", command=hello())


clear_button.grid(row=1, column=0, ipadx=17, ipady=15, pady=3)
divide_button.grid(row=1, column=1, ipadx=17, ipady=15, pady=3)
mul_button.grid(row=1, column=2, ipadx=17, ipady=15, pady=3)
min_button.grid(row=1, column=3, ipadx=17, ipady=15, pady=3)
seven_button.grid(row=2, column=0, ipadx=17, ipady=15, pady=3)
eight_button.grid(row=2, column=1, ipadx=17, ipady=15, pady=3)
nine_button.grid(row=2, column=2, ipadx=17, ipady=15, pady=3)
plus_button.grid(row=2, column=3, rowspan=2, ipadx=17, ipady=46, pady=3)
four_button.grid(row=3, column=0, ipadx=17, ipady=15, pady=3)
five_button.grid(row=3, column=1, ipadx=17, ipady=15, pady=3)
six_button.grid(row=3, column=2, ipadx=17, ipady=15, pady=3)
one_button.grid(row=4, column=0, ipadx=17, ipady=15, pady=3)
two_button.grid(row=4, column=1, ipadx=17, ipady=15, pady=3)
three_button.grid(row=4, column=2, ipadx=17, ipady=15, pady=3)
equals_button.grid(row=4, column=3, rowspan=2, ipadx=17, ipady=46, pady=3)
zero_button.grid(row=5, column=0, columnspan=2, ipadx=54, ipady=15, pady=3)
dot_button.grid(row=5, column=2, ipadx=19, ipady=15, pady=3)


window.mainloop()


