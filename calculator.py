from tkinter import *

dot_flag = 0

window = Tk()
window.title("Calculator")


entry_field = Entry(window, justify=RIGHT)
entry_field.grid(column=0, row=0, columnspan=4, padx=10, pady=10, ipadx=36, ipady=10)


def num_button_click(number):
   current = entry_field.get()
   entry_field.delete(0, END)
   entry_field.insert(0, str(current)+str(number))


def dot_button_click():
   global dot_flag
   if(dot_flag==0):
      old_value = entry_field.get()
      entry_field.delete(0, END)
      entry_field.insert(0, str(old_value) + ".")
   else:
      old_value = entry_field.get()
      entry_field.delete(0, END)
      entry_field.insert(0, str(old_value))
   dot_flag = 1


def clear_button_click():
   global dot_flag
   entry_field.delete(0, END)
   dot_flag = 0


def hello():
   print("hello")


clear_button = Button(text="C", command=lambda: clear_button_click())
divide_button = Button(text="/", command=hello())
mul_button = Button(text="x", command=hello())
min_button = Button(text="-", command=hello())

seven_button = Button(text="7", command=lambda: num_button_click(7))
eight_button = Button(text="8", command=lambda: num_button_click(8))
nine_button = Button(text="9", command=lambda: num_button_click(9))
plus_button = Button(text="+", command=hello())

four_button = Button(text="4", command=lambda: num_button_click(4))
five_button = Button(text="5", command=lambda: num_button_click(5))
six_button = Button(text="6", command=lambda: num_button_click(6))

one_button = Button(text="1", command=lambda: num_button_click(1))
two_button = Button(text="2", command=lambda: num_button_click(2))
three_button = Button(text="3", command=lambda: num_button_click(3))
equals_button = Button(text="=", command=hello())

zero_button = Button(text="0", command=lambda: num_button_click(0))
dot_button = Button(text=".", command=lambda: dot_button_click())


clear_button.grid(row=1, column=0, ipadx=17, ipady=15, padx=3, pady=3)
divide_button.grid(row=1, column=1, ipadx=17, ipady=15, padx=3, pady=3)
mul_button.grid(row=1, column=2, ipadx=17, ipady=15, padx=3, pady=3)
min_button.grid(row=1, column=3, ipadx=17, ipady=15, padx=3, pady=3)

seven_button.grid(row=2, column=0, ipadx=17, ipady=15, padx=3, pady=3)
eight_button.grid(row=2, column=1, ipadx=17, ipady=15, padx=3, pady=3)
nine_button.grid(row=2, column=2, ipadx=17, ipady=15, padx=3, pady=3)
plus_button.grid(row=2, column=3, rowspan=2, ipadx=17, padx=3, ipady=46, pady=3)

four_button.grid(row=3, column=0, ipadx=17, ipady=15, padx=3, pady=3)
five_button.grid(row=3, column=1, ipadx=17, ipady=15, padx=3, pady=3)
six_button.grid(row=3, column=2, ipadx=17, ipady=15, padx=3, pady=3)

one_button.grid(row=4, column=0, ipadx=17, ipady=15, padx=3, pady=3)
two_button.grid(row=4, column=1, ipadx=17, ipady=15, padx=3, pady=3)
three_button.grid(row=4, column=2, ipadx=17, ipady=15, padx=3, pady=3)
equals_button.grid(row=4, column=3, rowspan=2, ipadx=17, ipady=46, padx=3, pady=3)

zero_button.grid(row=5, column=0, columnspan=2, ipadx=46, ipady=15, padx=3, pady=3)
dot_button.grid(row=5, column=2, ipadx=19, ipady=15, pady=3)


window.mainloop()


