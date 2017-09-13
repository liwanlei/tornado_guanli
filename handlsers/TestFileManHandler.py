# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:52:29
# @Author  : lileilei
import tornado.web
from models.model_py import FilePan,db_session
from handlsers.Basehandler import BaseHandler
from untils.pagination import Pagination
class TestfileView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=FilePan.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(FilePan).order_by(FilePan.creat_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/filepan/')
		self.render('pan.html',filespans=testresults,str_page=str_page)