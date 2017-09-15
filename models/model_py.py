# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 13:02:33
# @Author  : lileilei 
from models.dataconfig import db_session,Base,create_all
from sqlalchemy import  Column,Integer,DateTime,Boolean,String,ForeignKey,desc,asc,Text
from sqlalchemy.orm import  relationship,backref
from untils.common import encrypt
import datetime
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
	Projects=relationship('Project',backref='users')
	shebei=relationship('Shebei',backref='users')
	file=relationship('FilePan',backref='users')
	banben=relationship('BanbenWrite',backref='users')
	testresult=relationship('TestResult',backref='users')
	testcase=relationship('TestCase',backref='users')
	buglog=relationship('BugLog',backref='users')
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
class TestResult(Base):
	__tablename__='testresults'
	id=Column(Integer(),primary_key=True)
	porject_id=Column(Integer(),ForeignKey('projects.id'))
	creat_time=Column(DateTime())
	bug_first=Column(Integer())
	ceshirenyuan=Column(String(255))
	is_send=Column(Boolean(),default=True)
	filepath=Column(String(64))
	status=Column(Integer(),default=0)
	user_id=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.porject_name
	@classmethod
	def get_by_name(cls,name):
		item=db_session.query(TestResult).filter(TestResult.porject_name==name).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(TestResult).filter(TestResult.id==id).first()
		return item
	@classmethod
	def get_by_user_id(cls,user_id):
		item=db_session.query(TestResult).filter(TestResult.user_id==user_id).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(TestResult).count()
class BanbenWrite(Base):
	__tablename__='banbens'
	id=Column(Integer(),primary_key=True)
	porject_id=Column(Integer(),ForeignKey('projects.id'))
	creat_time=Column(DateTime(),default=datetime.datetime.now())
	banbenhao=Column(String(32))
	is_xian=Column(Boolean(),default=False)
	is_test=Column(Boolean(),default=False)
	status=Column(Integer())
	user_id=Column(Integer(),ForeignKey('users.id'))
	bugadmin=relationship('BugAdmin',backref='banbens')
	def __repr__(self):
		return self.banbenhao
	@classmethod
	def get_by_name(cls,name):
		item=db_session.query(BanbenWrite).filter(BanbenWrite.porject_name==name).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(BanbenWrite).filter(BanbenWrite.id==id).first()
		return item
	@classmethod
	def get_by_user_id(cls,user_id):
		item=db_session.query(BanbenWrite).filter(BanbenWrite.user_id==user_id).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(BanbenWrite).count()
class FilePan(Base):
	__tablename__='files'
	id=Column(Integer(),primary_key=True)
	file_fenlei=Column(String(64))
	file_name=Column(String(64))
	down_count=Column(Integer(),default=0)
	creat_time=Column(DateTime(),default=datetime.datetime.now())
	status=Column(Integer(),default=0)
	down_url=Column(String(64))
	is_tui=Column(Boolean(),default=False)
	user_id=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.file_name
	@classmethod
	def get_by_file_name(cls,name):
		item=db_session.query(FilePan).filter(FilePan.file_name==name).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(FilePan).filter(FilePan.id==id).first()
		return item
	@classmethod
	def get_by_user_id(cls,user_id):
		item=db_session.query(FilePan).filter(FilePan.user_id==user_id).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(FilePan).count()
class BugAdmin(Base):
	__tablename__='bugadmins'
	id=Column(Integer(),primary_key=True)
	porject_id=Column(Integer(),ForeignKey('projects.id'))
	bugname=Column(String(64))
	bugdengji=Column(String(64))
	bugtime=Column(DateTime(),default=datetime.datetime.now())
	bug_miaoshu=Column(String(255))
	ban_id=Column(Integer(),ForeignKey('banbens.id'))
	fujian=Column(String(64))
	is_que=Column(Boolean())
	bug_status=Column(String(64))
	bug_jiejuefangan=Column(String(64))
	bug_send=Column(String(64))
	status=Column(Integer(),default=0)
	bug_log=relationship('BugLog',backref='bugadmins')
	user_id=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.bugname
	@classmethod
	def get_by_bugname(cls,bugname):
		item=db_session.query(BugAdmin).filter(BugAdmin.bugname==bugname).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(BugAdmin).filter(BugAdmin.id==id).first()
		return item
	@classmethod
	def get_by_porject_name(cls,porject_name):
		item=db_session.query(BugAdmin).filter(BugAdmin.porject_name==porject_name).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(BugAdmin).count()
class TestCase(Base):
	__tablename__='testcases'
	id=Column(Integer(),primary_key=True)
	porject_id=Column(Integer(),ForeignKey('projects.id'))
	casename=Column(String(64))
	case_qianzhi=Column(String())
	case_buzhou=Column(String())
	case_yuqi=Column(String())
	status=Column(Integer(),default=0)
	case_crea_time=Column(DateTime(),default=datetime.datetime.now())
	user_id=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.casename
	@classmethod
	def get_by_project_name(Cls,project_name):
		item=db_session.query(TestCase).filter(TestCase.project_name==project_name).first()
		return item
	@classmethod
	def get_by_casename(Cls,casename):
		item=db_session.query(TestCase).filter(TestCase.casename==casename).first()
		return item
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(TestCase).filter(TestCase.id==id).first()
		return item
	@classmethod
	def get_count(cls):
		return db_session.query(TestCase).count()
class BugLog(Base):
	__tablename__='buglogs'
	id=Column(Integer(),primary_key=True)
	bug_id=Column(Integer(),ForeignKey('bugadmins.id'))
	caozuo=Column(String())
	caozuo_time=Column(DateTime())
	user_id=Column(Integer(),ForeignKey('users.id'))
	def __repr__(self):
		return self.caozuo
	@classmethod
	def get_by_id(Cls,id):
		item=db_session.query(BugLog).filter(BugLog.id==id).first()
		return item
	@classmethod
	def get_by_user_id(Cls,user_id):
		item=db_session.query(BugLog).filter(BugLog.user_id==user_id).first()
		return item
	@classmethod
	def get_by_bug_id(Cls,bug_id):
		item=db_session.query(BugLog).filter(BugLog.bug_id==bug_id).first()
		return item
class Project(Base):
	__tablename__='projects'
	id=Column(Integer(),primary_key=True)
	name=Column(String(64))
	user_id=Column(Integer(),ForeignKey('users.id'))
	bug_log=relationship('BugAdmin',backref='projects')
	banben=relationship('BanbenWrite',backref='projects')
	testresult=relationship('TestResult',backref='projects')
	testcase=relationship('TestCase',backref='projects')
	def __repr__(self):
		return self.name
	@classmethod
	def get_by_id(cls,id):
		item=db_session.query(Project).filter(Project.id==id).first()
		return item 
	@classmethod
	def get_by_name(cls,name):
		item=db_session.query(Project).filter(Project.name==name).first()
		return item