# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:54:21
# @Author  : lileilei
import os 
settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=",
        xsrf_cookies=True,
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        debug=True
    )