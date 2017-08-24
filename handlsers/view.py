# -*- coding: utf-8 -*-
# @Date    : 2017-08-24 12:46:34
# @Author  : lileilei 
from models.model_py import User,Shebei
from handlsers.Basehandlers import BaseHandler
import tornado.web
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
	def get(self):
		pass