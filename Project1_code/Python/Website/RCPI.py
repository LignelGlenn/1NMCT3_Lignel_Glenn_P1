from flask import Flask, render_template
from DbClass import DbClass
app = Flask(__name__)

@app.route('/')
def home1():
    return render_template('Home.html')

@app.route('/home')
def home2():
    return render_template('Home.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/login')
def login():
    return render_template('Log_in.html')

@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/stats')
def statsA():
    return render_template('statsA.html')

@app.route('/stats/general')
def statsB():
    return render_template('statsB.html')

@app.errorhandler(404)
def error(error):
    return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
