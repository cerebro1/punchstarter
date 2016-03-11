__author__ = 'sonali'
from punchstarter import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime)
    project = db.relationship('Project', backref = 'creator')
    pledges = db.relationship('Pledge', backref = 'pledgor', foreign_key = 'Pledge.member_id')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable = False)
    pledges = db.relationship('Pledge', backref = 'project', foreign_key = 'Pledge.project_id')
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Integer)
    date_of_start = db.Column(db.DateTime)
    date_of_end = db.Column(db.DateTime)

class Pledge(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable = False)
    amount = db.Column(db.Integer)
    time_created = db.Column(db.DateTime)