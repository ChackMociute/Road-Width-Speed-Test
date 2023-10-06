from app import app
from flask import render_template, redirect, request

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'begin' in request.form: return redirect('trials')
    return render_template("home.html")

@app.route('/trials', methods=['GET', 'POST'])
def trial():
    return render_template("base.html")