# -*- coding: utf-8 -*-
# @Date    : 2017-09-16 16:53:11
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
import tornado.web
import re
from models.model_py import db_session,User
from untils.common import encrypt
class PersonCenter(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        self.user=User.get_by_id(id)
        self.render('person.html',user=self.user,error_message=None)
    def post(self,id):
        self.user=User.get_by_id(id)
        password=self.get_body_argument('yuanmima')
        xinmima=self.get_body_argument('newpass')
        querenmima=self.get_body_argument('newpass_que')
        if not (xinmima and querenmima):
            self.render('person.html',user=self.user,error_message='请输入修改密码!')
        if encrypt(password) != self.user.password:
            self.render('person.html',user=self.user,error_message='原密码有误!')
        if xinmima !=querenmima:
            self.render('person.html',user=self.user,error_message='新密码输入不一致!')
        self.user.password=encrypt(xinmima)
        db_session.commit()
        self.redirect('/logout')
class AdminSet(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin.html',error_message=None)
    def post(self):
        email=self.get_body_argument('email')
        password=self.get_body_argument('password')
        p3 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}|[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
        emailor = p3.match(email)
        if not emailor:
            self.render('admin.html',error_message='邮箱格式不对')
        

