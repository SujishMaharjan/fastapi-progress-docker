# import datetime as _dt
# import sqlalchemy as _sql
# # from sqlalchemy.sql import func

# import database as _database


# class Contact(_database.Base):
#     __tablename__ = "contacts"

#     id = _sql.Column(_sql.Integer, primary_key= True, index=True)
#     first_name = _sql.Column(_sql.String, index = True)
#     phone_number = _sql.Column(_sql.String, index = True, unique=True)
#     # date_created = _sql.column(_sql.DateTime, default = _dt.datetime.now)
     


from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey

class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer,primary_key=True,index=True)
    question_text=Column(String, index=True)

class Choices(Base):
    __tablename__ ="choices"

    id = Column(Integer,primary_key=True,index=True)
    choice_text=Column(String, index=True)
    is_correct = Column(Boolean,default=False)
    question_id= Column(Integer,ForeignKey("questions.id"))




# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer,primary_key=True,nullable=False)
#     name = Column(String,index= True)
#     email = Column(String,unique=True,index= True)
#     password = Column(String)