import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker,relationship # type: ignore
from sqlalchemy.sql import expression
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from datetime import datetime

DB_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DB_URL)

SessionLocal = sessionmaker( bind=engine)

Base = declarative_base() 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



Now = datetime.utcnow()



class Project(Base):
    """Proje oluşturmamızı sağlayan Sınıf"""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    status = Column(Boolean, unique=False, default=True)
    created_at= Column(Date,default=Now)
    

    def __init__(self, name):
     """ Dışardan gelen requestler için başlangıç fonksiyonu"""
     self.name = name
    
    
 







class Job(Base):
  """Proje oluşturmamızı sağlayan Sınıf """
  __tablename__ = "jobs"
  id = Column(Integer, primary_key=True)
  title =Column(String(80))
  content = Column(String(120))
  status = Column(Integer, ForeignKey("status.id"))
  created_at= Column(Date,default=Now)
  updated_at= Column(Date,default=Now,onupdate=Now)
  finish_date= Column(Date)
  project_id=Column(Integer, ForeignKey("projects.id"))
 




class Comment(Base):
    """ Yorum oluşturmamızı sağlayan Sınıf """
     
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column(String(80))
    created_at= Column(Date,default=Now)
    job_id=Column(Integer, ForeignKey("jobs.id"))

  

  

class Status(Base):
    """ İşler için durum oluşturmamızı sağlayan Sınıf """
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    status_name= Column(String(80))
    created_at= Column(Date,default=Now)
    

    



class User(Base):
    """ Kullanıcı oluşturmamızı sağlayan Sınıf """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=True, nullable=False)


    def __init__(self, username,password):
     self.username =username
     self.password =password



Base.metadata.create_all(bind=engine)


