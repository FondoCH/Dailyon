from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)



@app.route('/')
def index():
    return '<p>Welcome to Dailyon investment Ltd</p><p>Where quality, transparency and accountability is our oxygen.</p>'


@app.route('/home')
def home():
    return 'Greetings customer, its our please to serve you and we are happy you gave us the opportunit to do so.'


@app.route('/contact')
def contact():
    return 'Feel free to reach us on our 24/7 hotline number +254 XXX XXX XX'


@app.route('/feedback')
def feedback():
    return 'We will really appreciate and feel privileged to hear from you on where we can serve you better. Thank you. Expecting to here from you'
















if __name__ == '__main__':
    app.run(debug=True)
