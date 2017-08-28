# -*- coding: utf-8 -*-
# @Date    : 2017-08-24 12:46:34
# @Author  : lileilei
import datetime 
from models.model_py import User,Shebei
from handlsers.Basehandlers import BaseHandler
import tornado.web
from untils.pagination import Pagination
from models.model_py import db_session 
import re
class IndexView(BaseHandler):
    @tornado.web.authenticated
    def get(self):
    	user_num=db_session.query(User).count()
    	shebei_num=db_session.query(Shebei).count()
    	waijie_num=db_session.query(Shebei).filter_by(shebei_jie=True).count()
    	shebei_list=db_session.query(Shebei).order_by(Shebei.shebei_date.desc())[:5]
    	self.render('index .html',user_num=user_num,shebei_num=shebei_num,waijie_num=waijie_num,shebei_list=shebei_list)
class ShebeiView(BaseHandler):
    @tornado.web.authenticated
    def get(self,page=1):
        count=Shebei.get_count()
        obj=Pagination(page,count)
        shebei_list=db_session.query(Shebei).order_by(Shebei.shebei_date.desc())[int(obj.start):(int(page)) * (12)]
        str_page = obj.string_pager('/shebei/')
        self.render('shebei.html',shebei_list=shebei_list,str_page=str_page)
class UserView(BaseHandler):
    @tornado.web.authenticated
    def get(self,page=1):
        count=User.get_count()
        obj=Pagination(page,count)
        user_list=db_session.query(User).order_by(User.id)[int(obj.start):(int(page)) * (12)]
        str_page = obj.string_pager('/user/')
        self.render('user.html',user_list=user_list,str_page=str_page)
class AddShebei(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_list=db_session.query(User).all()
        self.render('addshebei.html',user_list=user_list,error_message=None)
    def post(self):
        user_list=db_session.query(User).all()
        bianhao=self.get_argument('shebeibianhao')
        fapiao=self.get_argument('fapiao')
        shebeiname=self.get_argument('shebeiname')
        xitong=self.get_argument('xitong')
        shebeixinghao=self.get_argument('shebeixinghao')
        quanxian=self.get_argument('quanxian')
        goumaidate=self.get_argument('goumai')
        jiage=self.get_argument('jiage')
        shebeizhuangtai=self.get_argument('shebeizhuangtai')
        tianjia=self.get_argument('tianjia')
        goumaidate=datetime.datetime.strptime(goumaidate,"%Y-%m-%d")
        if not (shebeiname and bianhao and shebeixinghao and fapiao):
            self.render('addshebei.html',user_list=user_list,error_message='请准确填写信息')
        try:
            jiage=int(jiage)
        except Exception as e:
            self.render('addshebei.html',user_list=user_list,error_message='价格只能是数字')
        new_shebei=Shebei(shebei_id=bianhao,shebei_name=shebeiname,shebei_xitong=xitong,shebei_xinghao=shebeixinghao,
            shebei_jiage=jiage,shebei_fapiaobianhao=fapiao,shebei_quanxian=quanxian,gou_date=goumaidate,shebei_status=shebeizhuangtai,ruku_user=int(tianjia))
        db_session.add(new_shebei)
        try:
            db_session.commit()
            self.redirect('/shebei')
        except Exception as e:
            db_session.rollback()
            self.render('addshebei.html',user_list=user_list,error_message='添加失败')
class DongjieShebeiView(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        dongjie=Shebei.get_by_id(id)
        if dongjie and dongjie.she_sta==0:
            dongjie.she_sta=1
            db_session.commit()
            self.redirect('/shebei')  
        self.render('shebei.html')  
class JieShebeiView(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        jie=Shebei.get_by_id(id)
        if jie and jie.she_sta==1:
            jie.she_sta=0
            db_session.commit()
            self.redirect('/shebei')  
        self.render('shebei.html')   
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
            User.add_new(username=username,password=password,iphone=iphone,email=email,leves=int(quanxian))
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
            self.render('user.html')
        print(self.get_current_user())
