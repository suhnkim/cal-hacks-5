# serve.py

from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import main

# creates a Flask application, named app
app = Flask(__name__)
app._static_folder = './static'
app.config['SECRET_KEY'] = 'briant'

class ReusableForm(Form):
    name = TextField('URL:', validators=[validators.required(), validators.url()], default = "Url Here")

# a route where we will display a welcome message via an HTML template
@app.route("/", methods=['GET', 'POST'])
def index():
    message = "Hello, World"
    form = ReusableForm(request.form)
    print("errors: ", form.errors)
    if request.method == 'POST':
        url = request.form['name']
        print("url: ", url) 
        if form.validate():
            
        else:
            flash('Invalid URL')
    return render_template('index.html', message=message, form=form)


@app.route("/result")
def result():
    message = "Hello, World"
    return render_template('result.html', message=message)


@app.route("/test1")
def test():
    message = "Hello, World"
    return render_template('test1.html', message=message)

# run the application
if __name__ == "__main__":  
    app.run(debug=True)
