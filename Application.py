#!/usr/bin/env python

import tornado.web

from Regex_Handler import Regex_Handler
from Settings import Settings

from Modules.Dictionary import Dictionary
from Modules.Context import Context

class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, Regex_Handler, **Settings)
        
        self.__CoreDict = Dictionary("CoreDict.dct")
        self.__BiGramDict = Dictionary("BiGramDict.dct")
        self.__LexicalContext = Context("LexicalContext.ctx")
        
        self.__PlaceDict = Dictionary("PlaceDict.dct")
        self.__PlaceContext = Context("PlaceContext.ctx")
        self.__PersonDict = Dictionary("PersonDict.dct")
        self.__PersonContext = Context("PersonContext.ctx")
        self.__ForeignPersonDict = Dictionary("ForeignPersonDict.dct")
        self.__ForeignPersonContext = Context("ForeignPersonContext.ctx")
        
        
        self.__DictionarySet = dict(
            CoreDict = self.__CoreDict,
            BiGramDict = self.__BiGramDict,
            PlaceDict = self.__PlaceDict,
            PersonDict = self.__PersonDict,
            ForeignPersonDict = self.__ForeignPersonDict,
        )
        
        self.__ContextSet = dict(
            PlaceContext = self.__PlaceContext,
            PersonContext = self.__PersonContext,
            ForeignPersonContext = self.__ForeignPersonContext,
            LexicalContext = self.__LexicalContext
        )
        
    @property
    def DictionarySet(self):
        return self.__DictionarySet
        
    @property
    def ContextSet(self):
        return self.__ContextSet