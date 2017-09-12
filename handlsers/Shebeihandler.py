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
class EditShebei(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        user_list=db_session.query(User).all()
        shebei=Shebei.get_by_id(id)
        if not shebei:
            self.redirect('/shebei')
        self.render('edit.html',shebei=shebei,error_message=None,user_list=user_list)
    def post(self,id):
        user_list=db_session.query(User).all()
        shebei=Shebei.get_by_id(id)
        if not shebei:
            self.redirect('/shebei',error_message='设备找不到')
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
        try:
            goumaidate=datetime.datetime.strptime(goumaidate,"%Y-%m-%d")
        except Exception as e:
            self.render('edit.html',user_list=user_list,error_message='日期格式不对，请填写例如2017-1-19',shebei=shebei)
        waijietime=self.get_argument('waijietime')
        try:
            waijietime=datetime.datetime.strptime(waijietime,"%Y-%m-%d")
        except Exception as e:
            self.render('edit.html',user_list=user_list,error_message='日期格式不对，请填写例如2017-1-19',shebei=shebei)
        waijie_user=self.get_argument('waijie')
        waijie_s=self.get_argument('waijie_s')
        if not (shebeiname and bianhao and shebeixinghao and fapiao and quanxian):
            self.render('edit.html',user_list=user_list,error_message='请准确填写信息',shebei=shebei)
        try:
            jiage=int(jiage)
        except Exception as e:
            self.render('edit.html',user_list=user_list,error_message='价格只能是数字',shebei=shebei)
        shebei.shebei_id=bianhao
        shebei.shebei_name=shebeiname
        shebei.shebei_xitong=xitong
        shebei.shebei_xinghao=shebeixinghao
        shebei.shebei_jiage=jiage
        shebei.shebei_fapiaobianhao=fapiao
        shebei.shebei_quanxian=quanxian
        shebei.shebei_jie=waijie_s
        shebei.shebei_date=waijietime
        shebei.shebei_user=waijie_user
        shebei.gou_date=goumaidate
        shebei.shebei_status=shebeizhuangtai
        shebei.ruku_user=tianjia
        try:
            db_session.commit()
            self.redirect('/shebei')
        except Exception as e:
            db_session.rollback()
            self.render('edit.html',shebei=shebei,user_list=user_list,error_message='编辑失败')