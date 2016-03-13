__author__ = 'sonali'

from flask import Flask, render_template, request, redirect, url_for, abort
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import datetime
app = Flask(__name__)
manager = Manager(app)

db = SQLAlchemy(app)
app.config.from_object('punchstarter.default_settings')
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from punchstarter.models import *

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/projects/create/", methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("create.html")
    if request.method == 'POST':
        time_start = request.form.get("start_date")
        time_start = datetime.datetime.strptime(time_start,"%Y-%m-%d")
        time_end = request.form.get("end_date")
        time_end = datetime.datetime.strptime(time_end,"%Y-%m-%d")
        new_project = Project(
            member_id = 1,
            name = request.form.get("project_name"),
            description = request.form.get("description"),
            goal_amount = request.form.get("goal_amount"),
            date_of_start = time_start,
            date_of_end = time_end
        )

        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('project_detail', project_id = new_project.id))

@app.route("/projects/<int:project_id>/")
def project_detail(project_id):
    project = db.session.query(Project).get(project_id)
    if project is None:
        abort(404)

    return render_template("project_detail.html", project=project)