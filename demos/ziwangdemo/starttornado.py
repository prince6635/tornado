#coding=utf-8

import os
import tornado.ioloop
import tornado.web

# web的具体执行方法继承了RequestHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, get\n")

    def post(self):
        self.write("hello, post\n")

    def put(self):
        self.write("hello, put\n")

    def delete(self):
        self.write("hello, delete\n")

if __name__ == '__main__':
    # debug：True会在检查到文件改动的时候自动重启server，
    # 故千万不要放在prod上，因为一旦改动后的文件有错，重启后web server就有可能down掉
    settings = {
        'debug':True,
        # 放置静态文件的，上线后可以用nginx来做
        'static_path' : os.path.join(os.path.dirname(__file__), "static"),
        'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    }

    application = tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)
    application.listen(6666)
    tornado.ioloop.IOLoop.instance().start()
