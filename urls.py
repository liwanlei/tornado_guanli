# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:55:23
# @Author  : lileilei
from handlsers.login_headerl import LoginView,LogoutView
from handlsers.view import IndexView
url=[
    ('/login',LoginView),
    ('/logout',LogoutView),
    ('/index',IndexView),
]