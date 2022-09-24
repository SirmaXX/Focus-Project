from operator import truediv
from fastapi import APIRouter,Depends, Request, Form, status
from flask import jsonify

from Lib.models import SessionLocal,User
usersroute = APIRouter()

from sqlalchemy.orm import Session
import json

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



@usersroute.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    """ bütün kullanıcıların sıralandığı fonksiyon"""
    users = db.query(User).all()
    return users


@usersroute.get("/{id}")
async def get_user(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    user = db.query(User).filter_by(id=id).first()
    return user


@usersroute.post("/add")
async def add_user(req: Request,db: Session = Depends(get_db)):
     """ kullanıcı ekleyen fonksiyon """
     req_info = await req.json()
     username = req_info['username']
     password = req_info['password']
     new_user = User(username=username,password=password)
     db.add(new_user)
     db.commit()
     return print(username,password)





@usersroute.put("/update/{id}")
async def update_user(req: Request,id:int,db: Session = Depends(get_db)):
   """ kullanıcınun bilgilerini editleyen  fonksiyon """
   req_info = await  req.json()
   username = req_info['username']
   password = req_info['password']
   db.query(User).filter_by(id=id).update(
    dict(username=username, password=password))
   db.commit()
   return "item updated"




@usersroute.get("/delete/{id}")
async def del_user(req: Request,id:int,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini silen  fonksiyon """
     user = db.query(User).filter_by(id=id).first()
     db.delete(user)
     db.commit()
     return "veri silindi"
   


@usersroute.post("/login")
async def check_user(req: Request,db: Session = Depends(get_db)):
     """ kullanıcınun bilgilerini kontrol eden  fonksiyon """
     req_info = await  req.json()
     username = req_info['username']
     password = req_info['password']
     user = db.query(User).filter(User.username ==  username, User.password== password).first()
     if user != None:
        return True
     else :
        return False                                   

  
   