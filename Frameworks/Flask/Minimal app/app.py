from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/contact')
def Contact():
    return render_template('contact.html')

app.run(debug=True)