from app import app
from flask import render_template, redirect, request
from .forms import ResponseForm

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'begin' in request.form: return redirect('trials')
    return render_template("home.html")

@app.route('/trials', methods=['GET', 'POST'])
def trial():
    form = ResponseForm()
    if form.validate_on_submit():
        print('test')
        return redirect('trials')
    return render_template("trial.html", form=form)