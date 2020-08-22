from flask import render_template
from mainapp.forms import ContactForm
from mainapp import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route('/education')
def education():
    return render_template('education.html', title='Education')

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', title='Contact', form=form)

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')