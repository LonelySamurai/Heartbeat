from flask import Flask, render_template, flash, redirect, url_for, sessions, logging


app = Flask(__name__)
# app.debug = True


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/map')
def map():
    return render_template('gmap.html')


@app.route('/profile2')
def profile():
    return render_template('profile2.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
