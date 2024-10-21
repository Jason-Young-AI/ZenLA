#!/usr/bin/env python

from Handlers.BaseHandler import BaseHandler
from Definitions import Title

class ToIndexHandler(BaseHandler):
    def get(self):
        self.render("Index.html", Title=Title, Lang=u"EN", Lang_Expression=u"中文", Change_To_Lang=u"CN")