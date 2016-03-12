__author__ = 'sonali'

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
manager = Manager(app)

db = SQLAlchemy(app)
app.config.from_object('punchstarter.default_settings')
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
@app.route("/")
def hello():
    return render_template("index.html")