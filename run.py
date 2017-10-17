# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:51:12
# @Author  : lileilei 
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define,options
import tornado.options
from tornado.web import RequestHandler
import  setting
from models.model_py import create_all
from models.dataconfig import db_session,drop_all
from urls import url
define("port", default=3387, type=int, help="run server on the given port")
class Application(tornado.web.Application):
	def __init__(self, *args, **kwargs):
		super(Application, self).__init__(*args, **kwargs)
		self.db=db_session
def main():
	tornado.options.parse_command_line()
	app = Application(url,**setting.settings)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
	main()
	# create_all()
