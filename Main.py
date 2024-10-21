#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop

from Application import Application
from Definitions import Port

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(Port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()