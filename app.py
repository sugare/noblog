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
from orm import noblog,rightbarDate,rightbarHot,latest,dateData,PagerPerItem, PagerTotalItem
from memcache_mysql import getData



from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/?', IndexHandler),
            (r'/archives/?(.*)', ArchivesHandler),
            (r'/page/(\d+)/?', PageHandler),
            (r'/date/(.*)/?', DateHandler),
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
        for i in range(1,10):
            getData(i)
        self.render('index.html')

class ArchivesHandler(BaseHandler):
    def get(self, page):
        perPage = 8
        totalItem = PagerTotalItem()
        totalPage = totalItem // perPage if totalItem % perPage == 0 else totalItem // perPage + 1

        if page:
            try:
                if int(page) <= totalPage and int(page) >= 1:
                    dataPool = PagerPerItem(int(page), perPage)
                    self.render('archives.html', dataPool=dataPool, rightbarDatePool=rightbarDate(),
                            rightbarHotPool=rightbarHot(), totalPage=totalPage,currentPage=int(page))
                else:
                    self.write_error(404)
            except:
                    self.write_error(404)


        else:
            dataPool = PagerPerItem(1, perPage)
            self.render('archives.html', dataPool=dataPool, rightbarDatePool=rightbarDate(), rightbarHotPool=rightbarHot(),totalPage=totalPage,currentPage=1)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write_error(404)

class PageHandler(BaseHandler):
    def get(self, blog_id):
        try:
            blog = getData(blog_id)
        except:
            self.write_error(404)
        self.render('page.html',blog=blog, rightbarDatePool=rightbarDate(), rightbarHotPool=rightbarHot(),latest=latest())

class DateHandler(BaseHandler):
    def get(self, date):
        try:
            datePool = dateData(date)
        except:
            self.write_error(404)
        self.render('date.html',datePool=datePool, rightbarDatePool=rightbarDate(), rightbarHotPool=rightbarHot(),latest=latest())


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()