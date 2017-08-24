# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 13:01:14
# @Author  : lileilei 
from sqlalchemy import  create_engine
from  sqlalchemy.orm import  scoped_session,sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
engine=create_engine('sqlite:///shebei.db',convert_unicode=True)
Base=declarative_base()
db_session=scoped_session(sessionmaker(bind=engine))
def create_all():
    Base.metadata.create_all(engine)
def drop_all():
    Base.metadata.drop_all(engine)