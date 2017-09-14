# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:51:06
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
import tornado.web
from models.model_py import TestCase,db_session,Project
from untils.pagination import Pagination
class TestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=TestCase.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(TestCase).order_by(TestCase.case_crea_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/testcase/')
		self.render('case.html',cases=testresults,str_page=str_page)
class AddtestcaseView(BaseHandler):
	@tornado.web.authenticated
	def prepare(self):
		self.project=db_session.query(Project).all()
	def get(self):
		self.render('addtestcase.html',porjects=self.project,error_message=None)
	def post(self):
		porject=self.get_argument('porject')
		testcasename=self.get_argument('casename')
		testcaseqianzhi=self.get_argument('qianzhitiaojian')
		testcasebuzhou=self.get_argument('buzhou')
		testcaseyuqi=self.get_argument('yuqi')
		logurl=self.get_current_user()
		if not(porject and testcasename and testcasebuzhou and testcaseyuqi):
			self.render('addtestcase.html',porjects=self.project,error_message='请确认用例必要信息填写是否完整')
		new_testcas=TestCase(porject_id=int(porject),casename=testcasename,case_qianzhi=testcaseqianzhi,case_buzhou=testcasebuzhou,case_yuqi=testcaseyuqi,user_id=logurl.id)
		db_session.add(new_testcas)
		try:
			db_session.commit()
			self.redirect('/testcase')
		except Exception as e:
			raise e
			self.render('addtestcase.html',porjects=self.porjects,error_message='添加用例失败！')
class DeletestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		testcase=TestCase.get_by_id(id)
		if testcase and testcase.status==0:
			testcase.status=1
			db_session.commit()
			self.redirect('/testcase',error_message='删除成功')
		self.redirect('/testcase',error_message='删除失败')
class ResettestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		testcase=TestCase.get_by_id(id)
		if testcase and testcase.status==1:
			testcase.status=0
			db_session.commit()
			self.redirect('/testcase',error_message='恢复成功')
		self.redirect('/testcase',error_message='恢复失败')

