from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String,DateTime
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(100))
    created_at= db.Column(Date)
    comment=db.relationship('Job',backref='project')

    def __init__(self, name, status):
     self.name = name
     self.status = status
    

class Job(db.Model):
  id = db.Column(Integer, primary_key=True)
  title = db.Column(db.String(80))
  content = db.Column(db.String(120))
  session= db.relationship('Session',backref='job')
  comment=db.relationship('Comment',backref='job')
  status = db.Column(db.String(100))
  project_id=db.Column(db.Integer, db.ForeignKey('project.id'))

  def __init__(self, title, content,status):
    self.title = title
    self.content = content
    self.status = status


class Session(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at= db.Column(Date)
  job_id=db.Column(db.Integer, db.ForeignKey('job.id'))


  


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_at= db.Column(Date)
    job_id=db.Column(db.Integer, db.ForeignKey('job.id'))

    def __init__(self, title):
     self.title = title
     

 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


    def __init__(self, username,password):
     self.username =username
     self.password =password


db.create_all()
