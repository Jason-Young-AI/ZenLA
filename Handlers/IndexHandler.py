#!/usr/bin/env python

from Handlers.BaseHandler import BaseHandler
from Definitions import Title

class IndexHandler(BaseHandler):
    def get(self, Lang):
        if Lang == "EN" :
            Change_To_Lang = u"CN"
            Lang_Expression = u"中文"
        elif Lang == "CN" :
            Change_To_Lang = u"EN"
            Lang_Expression = u"English"
        self.render("Index.html", Title=Title, Lang=Lang, Lang_Expression=Lang_Expression, Change_To_Lang=Change_To_Lang)