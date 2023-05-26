# Basic Components

## Adding icon to our window

We can add title by using method `iconbitmap` 

```python
root.iconbitmap("pathToIcon")
```

## Creating exit button

Create a button and give command `root.quit` in _command_ parameter in button

```python
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
```

## Adding images 

we have to imoprt `ImageTK` and `Image` from `PIL` module.

```python
from PIL import ImageTk, Image
```

```python
my_img = ImageTk.PhotoImage(Image.open("pathToImage"))
my_label = Label(image=my_img)
my_label.pack()
```

