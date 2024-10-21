#!/usr/bin/env python

from Handlers.BaseHandler import BaseHandler
from Definitions import Title

class OppsHandler(BaseHandler):
    def get(self):
        self.render("Opps.html", Title=Title)