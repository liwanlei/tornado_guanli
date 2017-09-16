# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:51:52
# @Author  : lileilei
import tornado.web
from handlsers.Basehandler import BaseHandler
from models.model_py import TestResult,db_session,Project,User
from untils.pagination import Pagination
import os,datetime 
from untils.shangChuan import sendfile
class TestresultView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=TestResult.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(TestResult).order_by(TestResult.creat_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/testre/')
		self.render('TestResult.html',testresults=testresults,str_page=str_page)
class AddtestresultView(BaseHandler):
	@tornado.web.authenticated
	def prepare(self):
		self.user_list=db_session.query(User).all()
		self.porjects=db_session.query(Project).all()
	def get(self):
		self.render('addtestresult.html',user_list=self.user_list,porjects=self.porjects,error_message=None)
	def post(self):
		porject=self.get_argument('porject')
		bugnum=self.get_argument('firstbug')
		file=self.request.files.get('file', None)
		ceshizhe=self.get_arguments('ceshizhe')
		fasong=self.get_argument('fasong')
		testtime=self.get_argument('testtime')
		user_shang=self.get_argument('user_shang')
		if not(porject and file and ceshizhe):
			self.render('addtestresult.html',user_list=self.user_list,porjects=self.porjects,error_message='请填充必选项')
		upload_path=os.path.join(os.path.dirname(__file__),'testresult')
		for meta in file:
			filename = meta['filename']
			file_path = os.path.join(upload_path, filename)
			with open(file_path, 'wb') as up:
				up.write(meta['body'])
		m=sendfile(filename,file_path)
		if m==False:
			self.render('addtestresult.html',user_list=self.user_list,porjects=self.porjects,error_message='上传失败')
		file_url='http://owd1oye3g.bkt.clouddn.com/%s'%filename
		if bugnum=='':
			bugnum=0
		try:
			bugnum=int(bugnum)
		except:
			self.render('addtestresult.html',user_list=self.user_list,porjects=self.porjects,error_message='bug数量为数字')
		new_test=TestResult(porject_id=int(porject),creat_time=datetime.datetime.strptime(testtime,"%Y-%m-%d"),
			bug_first=bugnum,ceshirenyuan=str(ceshizhe),is_send=fasong,filepath=file_url,user_id=int(user_shang))
		db_session.add(new_test)
		try:
			db_session.commit()
			self.redirect('/testre')
		except Exception as e:
			print(e)
			db_session.rollback()
			self.redirect('/addtestresult')
class Deleresult(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		delet=TestResult.get_by_id(id)
		if delet and delet.status==0:
			delet.status=1
			db_session.commit()
			self.redirect('/testre')
		self.redirect('/testre')
class Resetresult(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		reset=TestResult.get_by_id(id)
		if reset and reset.status==1:
			reset.status=0
			db_session.commit()
			self.redirect('/testre')
		self.redirect('/testre')
	
