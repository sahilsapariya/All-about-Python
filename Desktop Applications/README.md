# Desktop Application with Python

We are using Tkinter for building desktop app in python

Installing _tkinter_ using _pip_ command

```bash
pip install tkinter
```

Let's create Hello world program using tkinter

```python
from tkinter import *

root = Tk()

myLabel = Label(root, text="hello world")
myLabel.pack()

root.geometry("500x500")
root.mainloop()
```