from timeit import default_timer
from app import app, db, admin, IMAGES_PER_PARTICIPANT
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
        return redirect(url_for('trial', name=form.name.data, trial=trial, start=default_timer()))
    return render_template("home.html", form=form)

@app.route('/trial/<name>/<trial>/<start>', methods=['GET', 'POST'])
def trial(name, trial, start):
    form = ResponseForm()
    img = get_image(name, int(trial))
    if form.validate_on_submit():
        add_response(img, form.speed.data, (default_timer() - float(start)) * 1000)
        return redirect(url_for('trial', name=name, trial=int(trial) + 1, start=default_timer()))
    return render_template("trial.html", form=form, trial=trial, img=img.filename, i=trial, N=IMAGES_PER_PARTICIPANT)

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
        if i == trial: return r

def add_response(response, speed, RT):
    response.response = speed
    response.response_time = RT
    db.session.commit()