# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 13:02:33
# @Author  : lileilei 
from models.dataconfig import db_session,Base,create_all
from sqlalchemy import  Column,Integer,DateTime,Boolean,String,ForeignKey,desc,asc,Text
from sqlalchemy.orm import  relationship,backref
from untils.common import encrypt
class User(Base):
	__tablename__='users'
	id=Column(Integer(),primary_key=True)
	username=Column(String(64),unique=True,index=True)
	email=Column(String(64))
	password=Column(String(64))
	last_logtime=Column(DateTime())
	status=Column(Integer())
	leves=Column(Integer())
	iphone=Column(Integer())
	shebei=relationship('Shebei',backref='users')
	def __repr__(self):
		return self.username
	@classmethod
	def get_by_id(cls, id):
		item = db_session.query(User).filter(User.id==id).first()
		return item
	@classmethod
	def get_by_username(cls, username):
		item = db_session.query(User).filter(User.username== username).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(Shebei).count()
	@classmethod
	def add_new(cls,username,password,iphone,email,leves):
		new=User(username=username,iphone=iphone,email=email,leves=leves)
		new.password=encrypt(password)
		new.status=0
		db_session.add(new)
		try:
			db_session.commit()
		except:
			db_session.rollback()
class Shebei(Base):
	__tablename__='shebeis'
	id=Column(Integer(),primary_key=True)
	shebei_id=Column(String(32),unique=True)
	shebei_name=Column(String(64))
	shebei_xitong=Column(String(64))
	shebei_xinghao=Column(String(255))
	shebei_jiage=Column(Integer())
	shebei_fapiaobianhao=Column(String(64))
	shebei_quanxian=Column(Boolean())
	shebei_jie=Column(Boolean())
	shebei_shuyu=Column(String())
	shebei_date=Column(DateTime())
	shebei_user=Column(String())
	gou_date=Column(DateTime())
	shebei_status=Column(String(16))
	she_sta=Column(Integer(),default=0)
	ruku_user=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.shebei_name
	@classmethod
	def get_by_name(cls,name):
		item=db_session.query(Shebei).filter(Shebei.shebei_name==name).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(Shebei).filter(Shebei.id==id).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(Shebei).count()

