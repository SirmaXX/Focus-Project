from fastapi import APIRouter,Depends, Request, Form, status
from flask import jsonify
from Lib.models import User,SessionLocal,engine,get_db

usersroute = APIRouter()

from sqlalchemy.orm import Session




@usersroute.get('/')
async def get_users(req: Request, db: Session = Depends(get_db)):
   users=[]
   for user in  db.query(User).all():
      users.append(user.__dict__)
   return jsonify(users)





@usersroute.get('/{id}')
def get_user(id: int):
    user  = User.query.get(id)
    del user.__dict__['_sa_instance_state']
    return jsonify(user.__dict__)


