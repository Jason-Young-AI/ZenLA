#!/usr/bin/env python

import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    @property
    def DictionarySet(self):
        return self.application.DictionarySet
        
    @property
    def ContextSet(self):
        return self.application.ContextSet