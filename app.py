from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('contact.html', title='Contact')

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')

if __name__ == '__main__':
  app.run(debug=True)