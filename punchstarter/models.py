from punchstarter import db
from sqlalchemy.sql import func
import cloudinary.utils


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime)
    project = db.relationship('Project', backref='creator')
    pledges = db.relationship('Pledge', backref='pledgor',
                              foreign_keys='Pledge.member_id')


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'),
                          nullable=False)
    pledges = db.relationship('Pledge', backref='project',
                              foreign_keys='Pledge.project_id')
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Integer)
    image_filename = db.Column(db.String(300))
    date_of_start = db.Column(db.DateTime)
    date_of_end = db.Column(db.DateTime)

    @property
    def num_pledges(self):
        return len(self.pledges)

    @property
    def total_pledges(self):
        total_pledges = db.session.query(func.sum(Pledge.amount)).filter(Pledge.project_id == self.id).one()[0]  # NOQA
        if total_pledges is None:
            total_pledges = 0

        return total_pledges

    @property
    def num_days_left(self):
        days_left = (self.date_of_end - self.date_of_start).days
        return days_left

    @property
    def image_path(self):
        return cloudinary.utils.cloudinary_url(self.image_filename)[0]

    @property
    def percentage_funded(self):
        return int(self.total_pledges * 100 / self.goal_amount)


class Pledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer,
                          db.ForeignKey('member.id'), nullable=False)
    project_id = db.Column(db.Integer,
                           db.ForeignKey('project.id'), nullable=False)
    amount = db.Column(db.Integer)
    time_created = db.Column(db.DateTime)
