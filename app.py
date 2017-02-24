#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-23 上午9:41
# @Author  : Sugare
# @mail    : 30733705@qq.com
# @File    : app.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
from orm import db,noblog,tags



from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/?', IndexHandler),
            (r'/archives/?', ArchivesHandler),
            (r'/page/(\d+)/?', PageHandler),
            (r'/.*', ErrorHandler),
        ]

        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            debug=True
        )

        super(Application,self).__init__(handlers, **settings)





class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class ArchivesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('archives.html')

class ErrorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write_error(404)

class PageHandler(BaseHandler):
    def get(self, blog_id):
        print(blog_id)
        blog = noblog.select().where(noblog.id == blog_id).get()
        print((blog.essay).encode('utf8'))
        self.render('page.html',blog=blog)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()