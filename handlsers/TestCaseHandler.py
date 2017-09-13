# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:51:06
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
import tornado.web
from models.model_py import TestCase,db_session
from untils.pagination import Pagination
class TestcaseView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=TestCase.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(TestCase).order_by(TestCase.case_crea_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/testcase/')
		self.render('case.html',cases=testresults,str_page=str_page)
