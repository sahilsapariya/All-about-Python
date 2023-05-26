# Basics of Tkinter

## Hello world program

```python
from tkinter import *

root = Tk()

# creating a label widget
myLabel = Label(root, text="hello world")
# shoving it onto the screen
myLabel.pack()

root.mainloop()
```

## Grid system

```python
from tkinter import *

root = Tk()

myLabel1 = Label(root, text="hello world")
myLabel2 = Label(root, text="sahil sapariya")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
```

## Buttons

```python
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


myButton = Button(root, text="click me!", 
                  padx=50, 
                  pady=10, 
                  command=myClick,  # calls the myClick function
                  
                  # adding the style to button
                  fg='white', 
                  bg="black", 
                  activebackground="#333333" 
                )
myButton.pack()

root.mainloop()
```

## Input Field

```python
from tkinter import *

root = Tk()

entry = Entry(root, 
              width=50,
              bg="#434343",
              fg="white"
            )
entry.pack()

def myClick():
    myLabel = Label(root, text=entry.get())
    myLabel.pack()


myButton = Button(root, text="click me!", 
                  padx=50, 
                  pady=10, 
                  command=myClick
                )


myButton.pack()

root.geometry("500x500")
root.mainloop()
```

We can also add default text in input field using `insert()` method. For example
`entry.insert(0, "Enter your name: ")`