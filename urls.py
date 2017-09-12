# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:55:23
# @Author  : lileilei
from handlsers.LoginHeadel import LoginView,LogoutView
from handlsers.Shebeihandlers import IndexView,ShebeiView,AddShebei,DongjieShebeiView,JieShebeiView,EditShebei
from handlsers.UserHaders import UserView,AddUserView,QuxiaoAdmin,ShezhiAdmin,DongjieUser,JieDUser,ChongzhiUser
url=[
    ('/login',LoginView),
    ('/logout',LogoutView),
    ('/index',IndexView),
     ('/shebei',ShebeiView),
    ('/shebei/(?P<page>\d*)',ShebeiView),
     ('/user',UserView),
    ('/user/(?P<page>\d*)',UserView),
    ('/addshebei',AddShebei),
    ('/dongjie/(?P<id>\d*)',DongjieShebeiView),
    ('/jie/(?P<id>\d*)',JieShebeiView),
    ('/adduser',AddUserView),
    ('/quxiao/(?P<id>\d*)',QuxiaoAdmin),
    ('/shezhi/(?P<id>\d*)',ShezhiAdmin),
    ('/dongjie1/(?P<id>\d*)',DongjieUser),
    ('/jiedong1/(?P<id>\d*)',JieDUser),
    ('/chongzhi/(?P<id>\d*)',ChongzhiUser),
    ('/edit_shebei/(?P<id>\d*)',EditShebei)
]