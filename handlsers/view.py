# -*- coding: utf-8 -*-
# @Date    : 2017-08-24 12:46:34
# @Author  : lileilei 
from models.model_py import User,Shebei
from handlsers.Basehandlers import BaseHandler
import tornado.web
from untils.pagination import Pagination
from models.model_py import db_session 
class IndexView(BaseHandler):
    # @tornado.web.authenticated
    def get(self):
    	user_num=db_session.query(User).count()
    	shebei_num=db_session.query(Shebei).count()
    	waijie_num=db_session.query(Shebei).filter_by(shebei_jie=True).count()
    	shebei_list=db_session.query(Shebei).order_by(Shebei.shebei_date.desc())[:5]
    	self.render('index .html',user_num=user_num,shebei_num=shebei_num,waijie_num=waijie_num,shebei_list=shebei_list)
class ShebeiView(BaseHandler):
	def get(self,page=1):
		count=Shebei.get_count()
		obj=Pagination(page,count)
		shebei_list=db_session.query(Shebei).order_by(Shebei.shebei_date.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/shebei/')
		self.render('shebei.html',shebei_list=shebei_list,str_page=str_page)
class UserView(BaseHandler):
    def get(self,page=1):
        count=User.get_count()
        obj=Pagination(page,count)
        user_list=db_session.query(User).order_by(User.id)[int(obj.start):(int(page)) * (12)]
        str_page = obj.string_pager('/user/')
        self.render('user.html',user_list=user_list,str_page=str_page)
