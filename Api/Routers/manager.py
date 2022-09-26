from fastapi import APIRouter,Depends, Request,HTTPException
from flask import jsonify
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from Lib.models import SessionLocal,Project,Job,Comment,Status
import json

#gün kontrolü için eklediğim tarihler
Now = datetime.today() 
Future=datetime.today() + timedelta(days=2)


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
    if not projects:
        raise HTTPException(status_code=404,detail="Kullanıcı bulunamadı")
    else :
        return projects
    


@managerroute.get("/projects/{id}")
async def get_project(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    project = db.query(Project).filter_by(id=id).first()
    if project != None:
        return project
    else :
        raise HTTPException(status_code=404,detail="Aranan Kullanıcı yoktur")


@managerroute.post("/projects/add")
async def add_project(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     name = req_info['name']
     project = Project( name= name)
     db.add(project)
     db.commit()
     




@managerroute.put("/projects/update/{id}")
async def update_project(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   name = req_info['name']
   status= req_info['status']
   project = db.query(Project).filter_by(id=id).first()
   if project != None:
     db.query(Project).filter_by(id=id).update(
     dict(name= name, status= status))
     db.commit()
     return "proje güncellendi"
   else :
        raise HTTPException(status_code=404,detail="Aranan proje yoktur")
  


@managerroute.delete("/projects/delete/{id}")
async def del_project(req: Request,id:int,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini silen  fonksiyon """
     project = db.query(Project).filter_by(id=id).first()
     if project != None:
       db.delete(project)
       db.commit()
       return "veri silindi"
     else :
       raise HTTPException(status_code=404,detail="Aranan proje yoktur")
     

#PROJELERİN APİ ÜZERİNDEN  CRUD REQUESTLERİ  BİTİŞ


#JOBS(işlerin) APİ ÜZERİNDEN  CRUD REQUESTLERİ
@managerroute.get('/jobs')
async def job_list(req: Request, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    jobs = db.query(Job).all()
    if not jobs:
        raise HTTPException(status_code=404,detail="İş bulunamadı")
    else :
        return jobs


@managerroute.get("/jobs/{id}")
async def get_job(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    job = db.query(Job).filter_by(id=id).first()
    if job != None:
         return job
    else :
        raise HTTPException(status_code=404,detail="Aranan iş yoktur")


@managerroute.post("/jobs/add")
async def add_job(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await  req.json()
     titlee = req_info['titlee']
     content = req_info['content']
     status= req_info['status']
     project_id=int(req_info['project_id'])
     job = Job( title=titlee,content= content, status= status,project_id=project_id,created_at=Now, finish_date=Future)
     db.add(job)
     db.commit()
    




@managerroute.put("/jobs/update/{id}")
async def update_job(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   title = req_info['title']
   content = req_info['content']
   status= req_info['status']
   job = db.query(Job).filter_by(id=id).first()
   if job  != None:
    db.query(Job).filter_by(id=id).update(
    dict(title=title,content=content, status= status,updated_at=Now))
    db.commit()
    return "item updated"
   else :
        raise HTTPException(status_code=404,detail="Aranan iş yoktur")

        
 


@managerroute.delete("/jobs/delete/{id}")
async def del_job(req: Request,id:int,db: Session = Depends(get_db)):
    """ kullanıcınun bilgilerini silen  fonksiyon """
    job = db.query(Job).filter_by(id=id).first()
    if job != None:
      db.delete(job)
      db.commit()
      return "veri silindi"
    else :
        raise HTTPException(status_code=404,detail="Aranan iş yoktur")

#JOBS(işlerin) APİ ÜZERİNDEN  CRUD REQUESTLERİ  BİTİŞ


#Comments (yorumların) APİ ÜZERİNDEN  CRUD REQUESTLERİ
@managerroute.get('/comments')
async def comment_list(req: Request, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    comments = db.query(Comment).all()
    if not comments:
        raise HTTPException(status_code=404,detail="Yorum bulunamadı")
    else :
        return comments


@managerroute.get("/comments/{id}")
async def get_comment(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    comment = db.query(Comment).filter_by(id=id).first()
    if comment  != None:
        return comment 
    else :
        raise HTTPException(status_code=404,detail="Aranan yorum yoktur")



@managerroute.post("/comments/add")
async def add_commentt(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     commentt = req_info['comment'] 
     job_id=int(req_info['job_id'])
     comment = Comment( comment=commentt,job_id=job_id)
     db.add(comment)
     db.commit()
     




@managerroute.put("/comments/update/{id}")
async def update_comment(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   comment = req_info['comment'] 
   job_id=int(req_info['job_id'])
   commentt = db.query(Comment).filter_by(id=id).first()
   if commentt!= None:
       db.query(Comment).filter_by(id=id).update(
       dict(comment=comment,job_id=job_id))
       db.commit()
       return "item updated"
   else :
        raise HTTPException(status_code=404,detail="Aranan Kullanıcı yoktur")

   



   



@managerroute.delete("/comments/delete/{id}")
async def del_comment(req: Request,id:int,db: Session = Depends(get_db)):
     """ yorum silen  fonksiyon """
     comment = db.query(Comment).filter_by(id=id).first()
     if comment != None:
      db.delete(comment)
      db.commit()
      return "yorum silindi"
     else :
        raise HTTPException(status_code=404,detail="Aranan Yorum yoktur")

#Comments (yorumların) APİ ÜZERİNDEN  CRUD REQUESTLERİ  BİTİŞ

#Status (durumlar) APİ ÜZERİNDEN  CRUD REQUESTLERİ
@managerroute.get('/status')
async def status_list(req: Request, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    statuss = db.query(Status).all()
    if not statuss:
        raise HTTPException(status_code=404,detail="Statüler bulunamadı")
    else :
        return statuss


@managerroute.get("/status/{id}")
async def get_status(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    status = db.query(Status).filter_by(id=id).first()
    if status != None:
        return status
    else :
        raise HTTPException(status_code=404,detail="Aranan durum yoktur")



@managerroute.post("/status/add")
async def add_status(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     status_name= req_info['status_name'] 
     status = Status( status_name=status_name)
     db.add(status)
     db.commit()
     




@managerroute.put("/status/update/{id}")
async def update_status(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   status_name= req_info['status_name']
   status = db.query(Status).filter_by(id=id).first()
   if status != None:
      db.query(Status).filter_by(id=id).update(
      dict(status_name=status_name))
      db.commit()
      return "item updated"
   else :
        raise HTTPException(status_code=404,detail="Aranan durum yoktur")

  



@managerroute.delete("/status/delete/{id}")
async def del_status(req: Request,id:int,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini silen  fonksiyon """
     comment = db.query(Status).filter_by(id=id).first()
     if comment != None:
      db.delete(comment)
      db.commit()
      return "veri silindi"
     else :
        raise HTTPException(status_code=404,detail="Aranan Kullanıcı yoktur")


#Status (durumlar) APİ ÜZERİNDEN  CRUD REQUESTLERİ BİTİŞ