__author__ = 'sonali'
from punchstarter import db

class Member(db.Model):
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime)
    
