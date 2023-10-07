import pandas as pd
from app import app, db, admin
from flask import render_template, redirect, url_for
from flask_admin.contrib.sqla import ModelView
from .forms import ParticipantForm, ResponseForm
from .models import Participant, Response

admin.add_view(ModelView(Participant, db.session))
admin.add_view(ModelView(Response, db.session))


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ParticipantForm()
    if form.validate_on_submit():
        trial = check_participant(form.name.data)
        return redirect(url_for('trial', name=form.name.data, trial=trial))
    return render_template("home.html", form=form)

@app.route('/trial/<name>/<trial>', methods=['GET', 'POST'])
def trial(name, trial):
    form = ResponseForm()
    img = get_image(name, int(trial))
    if form.validate_on_submit():
        return redirect(url_for('trial', name=name, trial=int(trial) + 1))
    return render_template("trial.html", form=form, trial=trial, img=img)

def check_participant(name):
    # If participant is new, create particpiant
    if not name in [p.name for p in Participant.query.all()]:
        db.session.add(Participant(name=name))
        db.session.commit()
        return 0
    
    # Else, find out how many trials have been completed
    for i, r in enumerate(Participant.query.filter_by(name=name).first().images):
        if r.response is None: return i

def get_image(name, trial):
    for i, r in enumerate(Participant.query.filter_by(name=name).first().images):
        if i == trial: return r.filename