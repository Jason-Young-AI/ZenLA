#!/usr/bin/env python

import os

from Modules.Definitions import *
from Modules.Utilities import *

class Context(object):
    
    def __init__(self, ContextName):
        if not isinstance(ContextName, str):
            raise ValueError("Context.__init__ received wrong argument(s) type! ")
        else:
            self.__POSNumber = 0
            self.__POSList = []
            self.__TotalFrequency = 0
            self.__InitialFrequencyList = []
            self.__TransitionFrequencyMatrix = []
            self.__Load(ContextName)
    
    def __Load(self, ContextName):
    
        with open(os.path.join(DICT_PATH, ContextName), "rb") as ContextFile:
            
            self.__POSNumber = ReadInteger(ContextFile)
            
            for i in range(0, self.__POSNumber):
                POS = ReadInteger(ContextFile)
                self.__POSList.append(POS)
            
            FutureWillBeUsed = ReadInteger(ContextFile)
            
            self.__TotalFrequency = ReadInteger(ContextFile)
            
            for i in range(0, self.__POSNumber):
                InitialFrequency = ReadInteger(ContextFile)
                self.__InitialFrequencyList.append(InitialFrequency)
                
            for i in range(0, self.__POSNumber):
                TransitionFrequencyList = []
                for j in range(0, self.__POSNumber):
                    TransitionFrequency = ReadInteger(ContextFile)
                    TransitionFrequencyList.append(TransitionFrequency)
                self.__TransitionFrequencyMatrix.append(TransitionFrequencyList)
    def __FindPOSPlace(self, POS):
        posList = self.__POSList
        Left = 0
        Right = len(posList)
        while Left < Right:
            Middle = (Left + Right) // 2
            if posList[Middle] < POS:
                Left = Middle + 1
            else:
                Right = Middle
        
        if [Left] == len(posList):
            return False, -1
        if posList[Left] == POS:
            return True, Left
        return False, -1
    def GetPOSInitialFrequency(self, POS):
        isFound, index = self.__FindPOSPlace(POS)
        if isFound:
            return self.__InitialFrequencyList[index]
        return 0.000001
    
    def GetPOSTransitionFrequency(self, firstPOS, secondPOS):
        firstIsFound, firstIndex = self.__FindPOSPlace(firstPOS)
        secondIsFound, secondIndex = self.__FindPOSPlace(secondPOS)
        
        safeValue = 0.000001
        frequency = safeValue
        totalFreq = self.__TotalFrequency
        initialFreq = self.__InitialFrequencyList[firstIndex]
        transFreq = self.__TransitionFrequencyMatrix[firstIndex][secondIndex]
        
        
        if firstIsFound and secondIsFound:
            if initialFreq == 0 or transFreq == 0:
                return frequency
            #0.9 和 0.1 为经验值
            frequency = ( 0.9 * transFreq / initialFreq ) + ( 0.1 * initialFreq / totalFreq )
            
            
        return frequency
    