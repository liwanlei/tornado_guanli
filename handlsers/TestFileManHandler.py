# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 20:52:29
# @Author  : lileilei
import tornado.web
from models.model_py import FilePan,db_session
from handlsers.Basehandler import BaseHandler
from untils.pagination import Pagination
from untils.shangChuan import sendfile
import os,urllib.request
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
        fenlei=self.get_body_argument('fenlei')
        if not file:
            self.render('addfile.html',error_message='请选择上传测试文件')
        upload_path=os.path.join(os.path.dirname(__file__),'testfile')
        for meta in file:
            filename = meta['filename']
            file_path = os.path.join(upload_path, filename)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
        m=sendfile(filename,file_path)
        if m==False:
            self.render('addtestresult.html',user_list=self.user_list,porjects=self.porjects,error_message='上传失败')
        file_url='http://owd1oye3g.bkt.clouddn.com/%s'%filename
        new_file=FilePan(file_name=filename,down_url=file_url,user_id=self.get_current_user().id,file_fenlei=fenlei)
        try:       
            db_session.add(new_file)
            db_session.commit()
            self.redirect('/filepan')
        except Exception as e:
           # raise e
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
class DownFile(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        file=FilePan.get_by_id(id)
        doempath=os.path.join(os.path.expanduser("~"), 'Desktop')
        local=os.path.join(doempath,file.down_url[-10:])
        urllib.request.urlretrieve(file.down_url,local)
        file.down_count+=1
        db_session.commit()
        self.redirect('/filepan')
