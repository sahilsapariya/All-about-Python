# Getting Started With Flask

Auther : [Sahil Sapariya](https://github.com/sahilsapariya)

## Minimal App 
Let's begin our python web journy with Flask.

First of all we need to install the `flask` module so go to the terminal in your PC and run the below command to install the module.

```bash
pip install flask
```

After installing module, create one folder anywhere and open in code editor of your choice. Now create one python file and write the following code in it.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return "Hello world!"

app.run(debug=True)
```

Now run the above code snippate, that's it we created our first website with flask and it is running on _localhost_ and will display **Hello world** as output.

Let's take a look on each line of code in the above to see what exactly is going on.

- First we import the `Flask` class from `flask` module.

- then we created the object of `Flask` class as `app`.

- `@app.route('/')` is the endpoint of our url.

- Then we are creating one function for the endpoint of url. The result of the function will be displayed at the url of our web.

- Last command `app.run()` is for keep running our website. `debug=` parameter is used to automatically reload the website after we made the changes in website.

## Rendering Templates

As we are creating a website then we have to render the HTML files as a output for particular url so here is the concept coming _template_rendering_.

> Import the __render_template__ component from the __flask__ module

```python
from flask import Flask, render_template
```

Now create one folder named __templates__ in the present working directory in which we are going to create our HTML files.

Create one HTML file _index.html_ in _templates_ folder.

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimal app - Getting started with Flask</title>
</head>
<body>
    <h1>Hii there!👋</h1>
</body>
</html>
```

Now we have to modify the __app.py__ file:

**app.py**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

app.run(debug=True)
```

Here whatever the content in index.html file will be displayed in the home url.

## Create Multiple End-Points

Let's create another HTML file for another URL. So we are creating contact.html file for contact page.

**contact.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Let's get in touch!</h1>
    <a href="/">Home</a>
</body>
</html>
```

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimal app - Getting started with Flask</title>
</head>
<body>
    <h1>Hii there!👋</h1>
    <a href="/contact">Contact Us</a>
</body>
</html>
```

Now we have to create another end point for contact us page

**app.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/contact')
def Contact():
    return render_template('contact.html')

app.run(debug=True)
```

After doing till here you can see our website like this:

**Home Page**

![Home-page](./images/Home%20page.PNG)

**Contact Page**

![Contact-page](./images/Contact%20page.PNG)

I hope you like it, See you in next tutorial. 

Till then keep coding..!!