import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker,relationship # type: ignore
from sqlalchemy import  Column, Integer, String,Date,ForeignKey
from starlette.requests import Request


DB_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DB_URL, connect_args={"check_same_thread": True})

SessionLocal = sessionmaker( bind=engine)

Base = declarative_base() 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    status = Column(String(100))
    created_at= Column(Date)
    comments=relationship("Job",primaryjoin="Project.id == Job.project_id",cascade="all, delete-orphan")

    def __init__(self, name, status):
     self.name = name
     self.status = status
    




class Job(Base):
  __tablename__ = "jobs"

  id = Column(Integer, primary_key=True)
  title =Column(String(80))
  content = Column(String(120))
  session= relationship("Session",primaryjoin="Job.id == Session.job_id",cascade="all, delete-orphan")
  comment=relationship("Comment",primaryjoin="Job.id == Comment.job_id",cascade="all, delete-orphan")
  status = Column(String(100))
  project_id=Column(Integer,ForeignKey('projects.id'),nullable=False)

  def __init__(self, title, content,status):
    self.title = title
    self.content = content
    self.status = status





class Session(Base):
  __tablename__ = "sessions"
  
  id = Column(Integer, primary_key=True)
  created_at= Column(Date)
  job_id=Column(Integer,ForeignKey('jobs.id'),nullable=False)


  


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    created_at= Column(Date)
    job_id=Column(Integer,ForeignKey('jobs.id'),nullable=False)

    def __init__(self, title):
     self.title = title
     

 
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=True, nullable=False)


    def __init__(self, username,password):
     self.username =username
     self.password =password




