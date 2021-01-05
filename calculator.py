from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("300x400")

entry_field = Entry(window, width=45, justify=RIGHT)
entry_field.grid(column=0, row=0, columnspan=4,  pady=8, padx=13, ipady=8)

def helloCallBack():
   print( "Hello Python")


one_button = Button(text='1', command=helloCallBack())
one_button.grid(column=0, row=1, padx=13)

two_button = Button(text='2', command=helloCallBack())
one_button.grid(column=1, row=1)




window.mainloop()


