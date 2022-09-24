from fastapi import APIRouter,Depends, Request
from flask import jsonify
from sqlalchemy.orm import Session
from datetime import datetime
import time
from Lib.models import SessionLocal,Project,Job


# Must use UTC datetime.
Now = datetime.utcnow()

managerroute = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


#PROJELERİN APİ ÜZERİNDEN  CRUD REQUESTLERİ
@managerroute.get('/projects')
async def project_list(req: Request, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    projects = db.query(Project).all()
    return projects


@managerroute.get("/projects/{id}")
async def get_project(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    project = db.query(Project).filter_by(id=id).first()
    return project


@managerroute.post("/projects/add")
async def add_project(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     name = req_info['name']
     status= req_info['status']
     project = Project( name= name, status= status,created_at=Now)
     db.add(project)
     db.commit()
     return print(name,status)




@managerroute.put("/projects/update/{id}")
async def update_project(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   name = req_info['name']
   status= req_info['status']
   db.query(Project).filter_by(id=id).update(
    dict(name= name, status= status))
   db.commit()
   return "item updated"


@managerroute.get("/projects/delete/{id}")
async def del_project(req: Request,id:int,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini silen  fonksiyon """
     project = db.query(Project).filter_by(id=id).first()
     db.delete(project)
     db.commit()
     return "veri silindi"

#PROJELERİN APİ ÜZERİNDEN  CRUD REQUESTLERİ  BİTİŞ


#JOBS(işlerin) APİ ÜZERİNDEN  CRUD REQUESTLERİ
@managerroute.get('/jobs')
async def job_list(req: Request, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    jobs = db.query(Job).all()
    return jobs


@managerroute.get("/jobs/{id}")
async def get_job(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    job = db.query(Job).filter_by(id=id).first()
    return job


@managerroute.post("/jobs/add")
async def add_job(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     title = req_info['title']
     content = req_info['content']
     status= req_info['status']
     project_id=int(req_info['project_id'])
     job = Job( title=title,content= content, status= status,project_id=project_id)
     db.add(job)
     db.commit()
     return print(content,status)




@managerroute.put("/jobs/update/{id}")
async def update_job(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   title = req_info['title']
   content = req_info['content']
   status= req_info['status']
   db.query(Job).filter_by(id=id).update(
    dict(title=title,content=content, status= status))
   db.commit()
   return "item updated"


@managerroute.get("/jobs/delete/{id}")
async def del_job(req: Request,id:int,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini silen  fonksiyon """
     job = db.query(Job).filter_by(id=id).first()
     db.delete(job)
     db.commit()
     return "veri silindi"

#JOBS(işlerin) APİ ÜZERİNDEN  CRUD REQUESTLERİ  BİTİŞ