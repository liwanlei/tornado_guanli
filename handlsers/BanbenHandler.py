# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:53:57
# @Author  : lileilei
import tornado.web
from handlsers.Basehandler import BaseHandler
from models.model_py import db_session,BanbenWrite,Project
from untils.pagination import Pagination
class BanbenView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=BanbenWrite.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(BanbenWrite).order_by(BanbenWrite.creat_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/banben/')
		self.render('banben.html',banbnens=testresults,str_page=str_page)
class AddbanbenView(BaseHandler):
	@tornado.web.authenticated
	def prepare(self):
		self.porjects=db_session.query(Project).all()
	def get(self):
		self.render('addbanben.html',error_message=None,porjects=self.porjects)
	def post(self):
		porject=self.get_argument('porject')
		banbenhao=self.get_argument('banbenhao')
		new=BanbenWrite.get_by_name(banbenhao)
		if new:
			self.render('addbanben.html',error_message='版本号不能重复',porjects=self.porjects)
		shangxian=self.get_argument('shangxian')
		test=self.get_argument('test')
		login_user=self.get_current_user()
		if not banbenhao:
			self.render('addbanben.html',error_message='版本号不能为空',porjects=self.porjects)
		new_ban=BanbenWrite(porject_id=int(porject),banbenhao=banbenhao,is_xian=shangxian,is_test=test,user_id=login_user.id)
		db_session.add(new_ban)
		try:
			db_session.commit()
			self.redirect('/banben')
		except Exception as e:
			db_session.rollback()
			self.render('addbanben.html',error_message='添加失败',porjects=self.porjects)
class Addproject(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render('addporject.html',error_message=None)
	def post(self):
		porject=self.get_argument('project')
		new=Project.get_by_name(porject)
		if new:
			self.render('addporject.html',error_message='项目名不能重复！')
		login_user=self.get_current_user()
		if not porject:
			self.render('addporject.html',error_message='项目名不能为空')
		new_pro=Project(name=porject,user_id=login_user.id)
		db_session.add(new_pro)
		try:
			db_session.commit()
			self.redirect('/banben')
		except Exception as e:
			db_session.rollback()
			self.render('addporject.html',error_message='添加项目失败')
class Desetbanben(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		banben=BanbenWrite.get_by_id(id)
		if banben and banben.status==0:
			banben.status=1
			db_session.commit()
			self.redirect('/banben')
		self.redirect('/banben')
class Resetbanben(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		banben=BanbenWrite.get_by_id(id)
		if banben and banben.status==1:
			banben.status=0
			db_session.commit()
			self.redirect('/banben')
		self.redirect('/banben')
class EditbanbenView(BaseHandler):
	@tornado.web.authenticated
	def prepare(self):
		self.porjects=db_session.query(Project).all()
	def get(self,id):
		banben=BanbenWrite.get_by_id(id)
		self.render('editbanben.html',banben=banben,porjects=self.porjects,error_message=None)
	def post(self,id):
		banben=BanbenWrite.get_by_id(id)
		porject=self.get_argument('porject')
		banbenhao=self.get_argument('banbenhao')
		shangxian=self.get_argument('shangxian')
		test=self.get_argument('test')
		if not banbenhao:
			self.render('editbanben.html',banben=banben,porjects=self.porjects,error_message='请准确填写版本信息')
		banben.banbenhao=banbenhao
		banben.is_xian=shangxian
		banben.is_test=test
		banben.porject_id=int(porject)
		try:
			db_session.commit()
			self.redirect('/banben')
		except Exception as e:
			raise e
			self.render('editbanben.html',banben=banben,porjects=self.porjects,error_message='编辑失败')

