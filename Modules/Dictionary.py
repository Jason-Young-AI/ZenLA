#!/usr/bin/env python

import os

from Modules.Items import Word, WordIndex
from Modules.Definitions import *
from Modules.Utilities import *

class Dictionary(object):
    
    def __init__(self, DictName):
        if not isinstance(DictName, str):
            raise ValueError("Dictionary.__init__ received wrong argument(s) type! ")
        else:
            self.__WordIndices = []
            self.__Load(DictName)
    
    def __Load(self, DictName):
    
        with open(os.path.join(DICT_PATH, DictName), "rb") as DictFile:
        
            for i in range(0,WI_COUNT):
                
                Count = ReadInteger(DictFile)
                WI = WordIndex()
                
                if Count == 0: 
                    self.__WordIndices.append(WI)
                    continue
                
                for j in range(0,Count):
                    TmpFrequency = ReadInteger(DictFile)
                    TmpByteStrLength = ReadInteger(DictFile)
                    TmpPOS = ReadInteger(DictFile)
                    
                    W = Word()
                    if TmpByteStrLength != 0:
                        W.Content = ReadChineseWord(DictFile, TmpByteStrLength)
                    
                    W.Frequency = TmpFrequency
                    W.POS = TmpPOS
                    
                    WI.Words.append(W)
                    
                self.__WordIndices.append(WI)
    
    def FindFirstMatchWord(self, ID, Str):
        #查找WordIndices[ID]中第一个大于Str的词条的位置
        wordID = self.__WordIndices[ID]
        
        """
        if ID == 3755:
            x = 0
            for i in self.__WordIndices[3755].Words:
                print(x,end = " : \t")
                x+=1
                print(i.Content)
                
            print("#########################################")
        """
            
        words = wordID.Words
        
        Left = 0
        Right = wordID.Number
        
        while Left < Right:
            Middle = (Left + Right) // 2
            if CompareChineseStrID(words[Middle].Content, Str) == -1:
                Left = Middle + 1
            else:
                Right = Middle
        
        if Left == wordID.Number:
            return False, -1
        
        if words[Left].Content == Str:
            return True, Left
            
        return False, -1
    
    def FindOnlyMatchWord(self, ID, Str, POS):
        wordID = self.__WordIndices[ID]
        words = wordID.Words
        
        Left = 0
        Right = wordID.Number
        
        while Left < Right:
            Middle = (Left + Right) // 2
            compValue = CompareChineseStrID(words[Middle].Content, Str)
            if compValue == 0 and words[Middle].POS == POS:
                return True, Middle
            elif compValue < 0 or (compValue == 0 and words[Middle].POS < POS):
                Left = Middle + 1
            elif compValue > 0 or (compValue == 0 and words[Middle].POS > POS):
                Right = Middle - 1
        
        return False, -1
        
    def MatchAll(self, Str):
        
        words = []
        """
        print(Str, end = " - - ")
        """
        isChanged, fcharID, wordStr = ChangeToDictWordFormat(Str)
        """
        print(Str)
        """
        """
        print(wordStr, " #### " ,fcharID)
        """
        if isChanged:
            isFound, place = self.FindFirstMatchWord(fcharID, wordStr)
            if isFound:
                while place < self.__WordIndices[fcharID].Number and self.__WordIndices[fcharID].Words[place].Content == wordStr:
                    words.append(self.__WordIndices[fcharID].Words[place])
                    place = place + 1
        return words
    
    def MatchOne(self, Str):
        isChanged, fcharID, wordStr = ChangeToDictWordFormat(Str)
        if isChanged:
            i = 0
            while i < self.__WordIndices[fcharID].Number:
                if self.__WordIndices[fcharID].Words[i].Content.startswith(wordStr):
                    if isInGBKBlankSpace(fcharID):
                        fullWordContent = self.__WordIndices[fcharID].Words[i].Content
                    else:
                        fullWordContent = ChineseChar(fcharID) + self.__WordIndices[fcharID].Words[i].Content
                    return True, fullWordContent
                i = i + 1
                
        return False, ""
    
    def MatchOnly(self, Str, POS):
        isChanged, fcharID, wordStr = ChangeToDictWordFormat(Str)
        if isChanged:
            isFound, place = self.FindOnlyMatchWord(fcharID, wordStr, POS)
            if isFound:
                return True, self.__WordIndices[fcharID].Words[place]
            return False, None
        else:
            return False, None
    
    
    @property
    def WordIndices(self):
        return self.__WordIndices