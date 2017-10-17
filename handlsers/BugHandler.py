# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:54:21
# @Author  : lileilei
from handlsers.Basehandler import BaseHandler
from models.model_py import BugAdmin,BugLog,db_session,Project,BanbenWrite,User
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
class AddbugView(BaseHandler):
    @tornado.web.authenticated
    def prepare(self):
        self.banbenhaos=db_session.query(BanbenWrite).all()
        self.porjects=db_session.query(Project).all()
        self.users=db_session.query(User).all()
    def get(self):
        self.render('addbug.html',banbenhaos=self.banbenhaos,porjects=self.porjects,users=self.users,error_message=None)
    def post(self):
        porject=self.get_argument('porject')
        banbenhao=self.get_argument('banbenhao')
        bug_send=self.get_argument('user')
        bug_tile=self.get_argument('title')
        miaoshu=self.get_argument('miaoshu')
        dengji=self.get_argument('dengji')
        if not (porject and banbenhao and bug_send and bug_tile and miaoshu and dengji):
            self.render('addbug.html',banbenhaos=self.banbenhaos,porjects=self.porjects,users=self.users,error_message='请准确填写bug信息')
        new_bug=BugAdmin(porject_id=int(porject),ban_id=banbenhao,bugname=bug_tile,
            bugdengji=dengji,bug_miaoshu=miaoshu,bug_send=bug_send,user_id=self.get_current_user().id)
        db_session.add(new_bug)
        try:
            db_session.commit()
            self.redirect('/bug')
        except Exception as e:
            db_session.rollback()
            self.render('addbug.html',banbenhaos=self.banbenhaos,porjects=self.porjects,users=self.users,error_message='添加失败')
class Delebug(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        bug=BugAdmin.get_by_id(id)
        if bug and bug.status==0:
            bug.status=1
            db_session.commit()
            self.redirect('/bug')
class Resetbug(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        bug=BugAdmin.get_by_id(id)
        if bug and bug.status==1:
            bug.status=0
            db_session.commit()
            self.redirect('/bug')
class GuanbiBug(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        bug=BugAdmin.get_by_id(id)
        if bug and bug.status==1:
            bug.status=0
            db_session.commit()
            self.redirect('/bug')
class CaozuoBug(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        try:
            bug=BugAdmin.get_by_id(id)
            self.render('caobug.html',bug=bug,error_message=None)
        except Exception as e:
           # raise e
            self.redirect('/bug')
        
        