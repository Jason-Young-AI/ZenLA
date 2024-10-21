#!/usr/bin/env python

from Handlers.ToIndexHandler import ToIndexHandler
from Handlers.IndexHandler import IndexHandler
from Handlers.SegHandler import SegHandler
from Handlers.OppsHandler import OppsHandler

Regex_Handler = [
    (r"/", ToIndexHandler),
    (r"/(?P<Lang>[CE]N)", IndexHandler),
    (r"/(?P<Lang>[CE]N)/Seg", SegHandler),
    (r"/.*", OppsHandler),
]