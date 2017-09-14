# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:45:29
# @Author  : lileilei
import datetime 
from models.model_py import User,Shebei
from handlsers.Basehandler import BaseHandler
import tornado.web
from untils.pagination import Pagination
from models.model_py import db_session 
import re
from untils.common import encrypt
class UserView(BaseHandler):
    @tornado.web.authenticated
    def get(self,page=1):
        count=User.get_count()
        obj=Pagination(page,count)
        user_list=db_session.query(User).order_by(User.id)[int(obj.start):(int(page)) * (12)]
        str_page = obj.string_pager('/user/')
        self.render('user.html',user_list=user_list,str_page=str_page)
class AddUserView(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('adduser.html',error_message=None)
    def post(self):
        username=self.get_argument('username')
        password=self.get_argument('password')
        email=(self.get_argument('email'))
        iphone=(self.get_argument('iphone'))
        quanxian=(self.get_argument('quanxian'))
        new=User.get_by_username(username)
        if new:
            self.render('adduser.html',error_message='用户名不能重复')
        if not(username and password and email and iphone):
            self.render('adduser.html',error_message='请完整填写信息')
        user=User.get_by_username(username)
        p3 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}|[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
        emailor = p3.match(email)
        if not emailor:
            self.render('adduser.html',error_message='邮箱格式不对')
        if user:
            self.render('adduser.html',error_message='用户已经存在')
        try:
            User.add_new(username=username,password=encrypt(password),iphone=iphone,email=email,leves=int(quanxian))
            self.redirect('/user')
            return
        except Exception as e:
            raise e
            self.render('adduser.html',error_message='添加失败')
class QuxiaoAdmin(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            self.redirect('/user')
        login_user=self.get_current_user()
        if login_user.leves!=1:
            self.redirect('/user')
        if login_user ==user:
            self.redirect('/user')
        user.leves=0
        try:
            db_session.commit()
            self.redirect('/user')
        except:
            db_session.rollback()
            self.redirect('/user')
class ShezhiAdmin(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            self.redirect('/user')
        login_user=self.get_current_user()
        if login_user.leves!=1:
            self.redirect('/user')
        if login_user ==user:
            self.redirect('/user')
        user.leves=1
        try:
            db_session.commit()
            self.redirect('/user')
        except:
            db_session.rollback()
            self.redirect('/user')
class DongjieUser(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            self.redirect('/user')
        login_user=self.get_current_user()
        if login_user.leves!=1:
            self.redirect('/user')
        if login_user ==user:
            self.redirect('/user')
        user.status=1
        try:
            db_session.commit()
            self.redirect('/user')
        except:
            db_session.rollback()
            self.redirect('/user')
class JieDUser(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            self.redirect('/user')
        login_user=self.get_current_user()
        if login_user.leves!=1:
            self.redirect('/user')
        if login_user ==user:
            self.redirect('/user')
        user.status=0
        try:
            db_session.commit()
            self.redirect('/user')
        except:
            db_session.rollback()
            self.redirect('/user')
class ChongzhiUser(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            self.redirect('/user')
        login_user=self.get_current_user()
        if login_user.leves!=1:
            self.redirect('/user')
        if login_user ==user:
            self.redirect('/user')
        user.password=encrypt('111111')
        try:
            db_session.commit()
            self.redirect('/user')
        except:
            db_session.rollback()
            self.redirect('/user')      