# -*- coding: utf-8 -*-
# filename: main.py
#主文件，pythone main.py 80  参数为端口号
import web

#调用GET POST模块
from index import Index


#usrl = ("公有DNS/应用目录","getpost所在的类名")
urls = (
    '/pywx', 'Index',
)


#如果该文件被直接执行
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()