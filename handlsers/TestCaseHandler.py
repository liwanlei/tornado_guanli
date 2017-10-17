# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:51:06
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
import tornado.web
from models.model_py import TestCase,db_session,Project
from untils.pagination import Pagination
from untils.parseexcel import datacel
import os
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
		if len(testcasename)>30 or len(testcasename)<0:
			self.render('addtestcase.html',porjects=self.project,error_message='用例名字不能过长')
		if not(porject and testcasename and testcasebuzhou and testcaseyuqi):
			self.render('addtestcase.html',porjects=self.project,error_message='请确认用例必要信息填写是否完整')
		new_testcas=TestCase(porject_id=int(porject),casename=testcasename,case_qianzhi=testcaseqianzhi,case_buzhou=testcasebuzhou,case_yuqi=testcaseyuqi,user_id=logurl.id)
		db_session.add(new_testcas)
		try:
			db_session.commit()
			self.redirect('/testcase')
		except Exception as e:
			#raise e
			self.render('addtestcase.html',porjects=self.porjects,error_message='添加用例失败！')
class DeletestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		testcase=TestCase.get_by_id(id)
		if testcase and testcase.status==0:
			testcase.status=1
			db_session.commit()
			self.redirect('/testcase')
		self.redirect('/testcase',error_message='删除失败')
class ResettestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,id):
		testcase=TestCase.get_by_id(id)
		if testcase and testcase.status==1:
			testcase.status=0
			db_session.commit()
			self.redirect('/testcase')
		self.redirect('/testcase',error_message='恢复失败')
class EditTestcase(BaseHandler):
	@tornado.web.authenticated
	def prepare(self):
		self.project=db_session.query(Project).all()
	def get(self,id):
		testcase=TestCase.get_by_id(id)
		self.render('editcase.html',porjects=self.project,case=testcase,error_message=None)
	def post(self,id):
		testcase=TestCase.get_by_id(id)
		porject=self.get_argument('porject')
		testcasename=self.get_argument('casename')
		testcaseqianzhi=self.get_argument('qianzhitiaojian')
		testcasebuzhou=self.get_argument('buzhou')
		testcaseyuqi=self.get_argument('yuqi')
		logurl=self.get_current_user()
		if not(porject and testcasename and testcasebuzhou and testcaseyuqi):
			self.render('editcase.html',porjects=self.project,case=testcase,error_message='请准确填写用例信息')
		testcase.porject_id=int(porject)
		testcase.casename=testcasename
		testcase.case_qianzhi=testcaseqianzhi
		testcase.case_buzhou=testcasebuzhou
		testcase.case_yuqi=testcaseyuqi
		testcase.user_id=logurl.id
		try:
			db_session.commit()
			self.redirect('/testcase')
		except Exception as e:
			#raise e
			self.render('editcase.html',porjects=self.porjects,case=testcase,error_message='编辑用例信息失败')
class Daorutestcase(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render('daorutestcase.html',error_message=None)
	def post(self):
		file=self.request.files.get('file', None)
		if not file:
			self.render('daorutestcase.html',error_message='请选择上传文件')
		upload_path=os.path.join(os.path.dirname(__file__),'tease')
		for meta in file:
			filename = meta['filename']
			file_path = os.path.join(upload_path, filename)
			with open(file_path, 'wb') as up:
				up.write(meta['body'])
		porject_id_list,casename_list,case_qianzhi_list,case_buzhou_list,case_yuqi_list=datacel(file_path)
		if len(porject_id_list)<0:
			self.render('daorutestcase.html',error_message='上传失败')
		try:
			for i in range(len(porject_id_list)):
				project=Project.get_by_name(porject_id_list[i]).first().id
				new_case=TestCase(porject_id=project,casename=casename_list[i],case_qianzhi=case_qianzhi_list[i],case_buzhou=case_buzhou_list[i],case_yuqi=case_yuqi_list[i],user_id=self.get_current_user().id)
				db_session.add(new_case)
			db_session.commit()
			self.redirect('/testcase')
		except Exception as e:
			#raise e
			self.render('daorutestcase.html',error_message='上传失败')