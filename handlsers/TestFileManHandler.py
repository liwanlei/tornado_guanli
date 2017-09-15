# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:52:29
# @Author  : lileilei
import tornado.web
from models.model_py import FilePan,db_session
from handlsers.Basehandler import BaseHandler
from untils.pagination import Pagination
import os
class TestfileView(BaseHandler):
	@tornado.web.authenticated
	def get(self,page=1):
		count=FilePan.get_count()
		obj=Pagination(page,count)
		testresults=db_session.query(FilePan).order_by(FilePan.creat_time.desc())[int(obj.start):(int(page)) * (12)]
		str_page = obj.string_pager('/filepan/')
		self.render('pan.html',filespans=testresults,str_page=str_page)
class AddtestfileView(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('addfile.html',error_message=None)
    def post(self):
        file=self.request.files.get('file', None)
        if not file:
            self.render('addfile.html',error_message='请选择上传测试文件')
        upload_path=os.path.join(os.path.dirname(__file__),'testfile')
        for meta in file:
            filename = meta['filename']
            file_path = os.path.join(upload_path, filename)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
        new_file=FilePan(file_name=filename,down_url=file_path,user_id=self.get_current_user().id)
        try:       
            db_session.add(new_file)
            db_session.commit()
            self.redirect('/filepan')
        except Exception as e:
            raise e
            self.render('daorutestcase.html',error_message='上传失败')
class DeletePan(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        filepan=FilePan.get_by_id(id)
        if filepan and filepan.status==0:
            filepan.status=1
            db_session.commit()
            self.redirect('/filepan')
        self.redirect('/filepan')
class ResetpanView(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        filepan=FilePan.get_by_id(id)
        if filepan and filepan.status==1:
            filepan.status=0
            db_session.commit()
            self.redirect('/filepan')
        self.redirect('/filepan')

