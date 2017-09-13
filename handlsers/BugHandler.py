# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:54:21
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
from models.model_py import BugAdmin,BugLog,db_session
import tornado.web 
from untils.pagination import Pagination
class BugadminView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=BugAdmin.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(BugAdmin).order_by(BugAdmin.bugtime.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/bug/')
		self.render('bugadmin.html',bugs=testresults,str_page=str_page)