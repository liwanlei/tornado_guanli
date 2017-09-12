# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:57:31
# @Author  : lileilei 
from tornado.web import RequestHandler
from models.model_py import User
class BaseHandler(RequestHandler):
	@property
	def db(self):
		return self.application.db
	def get_current_user(self):
		user_id = self.get_secure_cookie('user_id')
		if not user_id:
			return None
		return User.get_by_id(int(user_id))
