from tkinter import *

root = Tk()
root.title("Basic calculator")


entry = Entry(root, width=35)
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5)


def click_button(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear_number():
    entry.delete(0, END)

def add_number():
    first_number = entry.get()
    global f_num 
    global math 
    math = "add"
    if first_number.isdigit(): f_num = int(first_number)
    entry.delete(0, END)

def substract_number():
    first_number = entry.get()
    global f_num 
    global math 
    math = "substract"
    if first_number.isdigit(): f_num = int(first_number)
    entry.delete(0, END)

def divide_number():
    first_number = entry.get()
    global f_num 
    global math 
    math = "divide"
    if first_number.isdigit(): f_num = int(first_number)
    entry.delete(0, END)

def multiply_number():
    first_number = entry.get()
    global f_num 
    global math 
    math = "multiply"
    if first_number.isdigit(): f_num = int(first_number)
    entry.delete(0, END)

def answer():
    second_number = entry.get()
    entry.delete(0, END)
    
    if math == "add": ans = int(f_num) + int(second_number)
    elif math == "substract": ans = int(f_num) - int(second_number)
    elif math == "divide": ans = int(f_num) / int(second_number)
    elif math == "multiply": ans = int(f_num) * int(second_number)

    entry.insert(0, str(ans))


# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click_button(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click_button(0))

button_add = Button(root, text="+", padx=40, pady=20, command=lambda: add_number())
button_substract = Button(root, text="-", padx=40, pady=20, command=lambda: substract_number())
button_multiply = Button(root, text="x", padx=40, pady=20, command=lambda: multiply_number())
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: divide_number())


button_equal = Button(root, text="=", padx=85, pady=20, command=lambda: answer())
button_clear = Button(root, text="clear", padx=75, pady=20, command=lambda: clear_number())


# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_substract.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)

root.mainloop()