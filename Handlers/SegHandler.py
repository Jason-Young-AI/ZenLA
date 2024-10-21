#!/usr/bin/env python

import re

from Handlers.BaseHandler import BaseHandler
from Definitions import Title
from Modules.MainSegmentation import MainSegmentation
from Modules.Definitions import MAP_COLOR

class SegHandler(BaseHandler):
    
    def get(self, Lang):
        if Lang == "EN" :
            Lang_Expression = u"English"
        elif Lang == "CN" :
            Lang_Expression = u"中文"
        
        NoInput = False
        
        InputText = u"Zen分析的确实在理！"
        
        OutputItems = [[[("Zen","外文字符串",MAP_COLOR["nx"]),("分析","名动词",MAP_COLOR["vn"]),("的","结构助词 - \"的\"",MAP_COLOR["uj"]),("确实","副形词",MAP_COLOR["ad"]),("在理","形容词",MAP_COLOR["a"]),("！","标点符号",MAP_COLOR["w"])],],]
                
        self.render("Seg.html", Title=Title, Lang=Lang, Lang_Expression=Lang_Expression, InputText=InputText, OutputItems=OutputItems, NoInput=NoInput, NKind=2, Smooth=0.1, isPerson=True, isPlace=False, isForeign=False, isHidden="true")

    def post(self, Lang):
        if Lang == "EN" :
            Lang_Expression = u"English"
        elif Lang == "CN" :
            Lang_Expression = u"中文"
        
        NoInput = False
        
        InputText = self.get_argument('InputText')
        
        OutputItems = None
        
        
        isPerson = self.get_argument('isPerson')
        if isPerson == "True":
            isPerson = True
        else:
            isPerson = False
        
        isForeign = self.get_argument('isForeign')
        if isForeign == "True":
            isForeign = True
        else:
            isForeign = False
        
        isPlace = self.get_argument('isPlace')
        if isPlace == "True":
            isPlace = True
        else:
            isPlace = False
            
        isHidden = self.get_argument('isHidden')
        if isHidden == "true":
            isHidden = "true"
        else:
            isHidden = "false"
            
        NKind = self.get_argument('NKind')
        if re.match("^[-+]?[0-9]*\.?[0-9]+$", NKind):
            NKind = int(NKind)
        else:
            NKind = 2
            
        Smooth = self.get_argument('Smooth')
        if re.match("^[-+]?[0-9]*\.?[0-9]+$", Smooth):
            Smooth = float(Smooth)
        else:
            Smooth = 0.1
            
        if Smooth>1:
            Smooth = 1
        #print(NKind,isPerson,isForeign,isPlace,Smooth)
        
        if len(InputText) == 0:
            NoInput = True
        else:
            segmain = MainSegmentation(InputText, self.DictionarySet, self.ContextSet, Smooth, NKind, isPerson, isForeign, isPlace)
            OutputItems = segmain.Results
            
        self.render("Seg.html", Title=Title, Lang=Lang, Lang_Expression=Lang_Expression, InputText=InputText, OutputItems=OutputItems, NoInput=NoInput, NKind=NKind, Smooth=Smooth, isPerson=isPerson, isPlace=isPlace, isForeign=isForeign, isHidden=isHidden)
        
        
        
        