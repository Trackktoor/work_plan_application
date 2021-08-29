from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

work_plans_works = db.Table('work_plans_works',
                            db.Column('work_plan_id', db.Integer, db.ForeignKey('work_plan.id')),
                            db.Column('work_id', db.Integer, db.ForeignKey('work.id'))
                            )

class Work_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    version = db.Column(db.Integer)

    works = db.relationship('Work', secondary=work_plans_works, backref=db.backref(name='work_plans_works', lazy='dynamic'))

    def __repr__(self):
        return '<Work_plan id: {}, title: {}>'.format(self.id, self.title)

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_id = db.Column(db.Integer, db.ForeignKey('work.id'))

    works = db.relationship('Work', backref='workers')

    def __repr__(self):
        return '<Worker id: {}, work_id: {}>'.format(self.id, self.work_id)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_start = db.Column(db.DateTime, default=datetime.now())
    date_end = db.Column(db.DateTime, default=datetime.now())

    

    def __repr__(self):
        return '<Work id: {}, title: {}>'.format(self.id, self.title)

