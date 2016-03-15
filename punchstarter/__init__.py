from flask import Flask, render_template, request, redirect, url_for, abort
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import datetime
import cloudinary.uploader

app = Flask(__name__)
manager = Manager(app)

db = SQLAlchemy(app)
app.config.from_object('punchstarter.default_settings')
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from punchstarter.models import Pledge, Project, Member  # NOQA


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/projects/create/", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("create.html")
    if request.method == 'POST':
        time_start = request.form.get("start_date")
        time_start = datetime.datetime.strptime(time_start, "%Y-%m-%d")
        time_end = request.form.get("end_date")
        time_end = datetime.datetime.strptime(time_end, "%Y-%m-%d")

        # upload cover_photo
        cover_photo = request.files['cover_photo']
        uploaded_image = cloudinary.uploader.upload(
            cover_photo,
            crop='limit',
            width=600,
            height=400
        )
        image_filename = uploaded_image["public_id"]

        new_project = Project(
            member_id=1,  # hardcode member id
            name=request.form.get("project_name"),
            description=request.form.get("description"),
            goal_amount=request.form.get("goal_amount"),
            image_filename=image_filename,
            date_of_start=time_start,
            date_of_end=time_end
        )

        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('project_detail', project_id=new_project.id))


@app.route("/projects/<int:project_id>/")
def project_detail(project_id):
    project = db.session.query(Project).get(project_id)
    if project is None:
        abort(404)

    return render_template("project_detail.html", project=project)


@app.route("/projects/<int:project_id>/pledge/", methods=['GET', 'POST'])
def pledge(project_id):
    project = db.session.query(Project).get(project_id)
    if project is None:
        abort(404)
    if request.method == 'GET':
        return render_template("pledge.html", project=project)
    if request.method == 'POST':
        # hard code member id but change whwn create login form
        guest_pledgor = db.session.query(Member).filter_by(id=2).one()
        new_pledge = Pledge(
            member_id=guest_pledgor.id,
            project_id=project.id,
            amount=request.form.get("amount"),
            time_created=datetime.datetime.now()
        )

        db.session.add(new_pledge)
        db.session.commit()

        return redirect(url_for('project_detail', project_id=project.id))


@app.route("/search/")
def search():
    query = request.args.get("quer") or ""
    projects = db.session.query(Project).filter(
        Project.name.ilike('%'+query+'%') |
        Project.description.ilike('%'+query+'%')
    ).all()

    project_count = len(projects)

    return render_template("search.html", query_text=query,
                           projects=projects, project_count=project_count)
