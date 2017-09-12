# encoding: utf-8
"""
@author: lileilei
@time: 2017/8/23 15:16
"""
from handlsers.Basehandlers import BaseHandler
from models.model_py import User,Shebei
from untils.common import encrypt
class LoginView(BaseHandler):
    def get(self):
        self.render('login.html',errmsg=None)
    def post(self):
        error_message1={
            '100':'信息不全',
            '101':'用户不存在',
            '102':'密码错误'
        }
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        if not(username and password):
            self.write(dict(errmsg=error_message1['100']))
        user = User.get_by_username(username)
        if not user:
            self.render('login.html', errmsg=error_message1['101'])
        if user.password != encrypt(password):
            self.render('login.html', errmsg=error_message1['102'])
        self.set_secure_cookie("user_id", str(user.id), expires_days=7)
        self.redirect('/index')
class LogoutView(BaseHandler):
    def get(self):
        self.clear_cookie('user_id')
        self.redirect('/login')
