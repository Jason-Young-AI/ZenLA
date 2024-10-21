#!/usr/bin/env python

import math

from Modules.Items import *
from Modules.Definitions import *
from Modules.Utilities import *
from Modules.Dictionary import Dictionary
from Modules.Context import Context

class MainSegmentation(object):

    """TmpStr = InputText
    TmpList = []
    for TmpChar in TmpStr:
        TmpList.append([TmpChar, str(TmpChar.encode("GBK"))])
        
    Results = CoreDict.WordIndices[1].Words
    for Result in Results:
        Result = (Result.Content, str(Result.Content.encode('GBK')))
    """
    def __init__(self, SMInputText, SMDictionarySet, SMContextSet, SMSmoothParameter = 0.1, SMNKind = 2, SMPersonRecognition = False, SMTransRecognition = False, SMPlaceRecognition = False):
        if isinstance(SMInputText, str) and isinstance(SMSmoothParameter, (float,int)) and isinstance(SMNKind, int) and isinstance(SMPersonRecognition, bool) and isinstance(SMTransRecognition, bool) and isinstance(SMPlaceRecognition, bool):
            self.__InputText = SMInputText
            self.__DictionarySet = SMDictionarySet
            self.__ContextSet = SMContextSet
            self.__SmoothParameter = SMSmoothParameter
            self.__NKind = SMNKind
            self.__PersonRecognition = SMPersonRecognition
            self.__TransRecognition = SMTransRecognition
            self.__PlaceRecognition = SMPlaceRecognition
        else:
            raise ValueError("MainSegmentation.__init__ received wrong argument(s) type! ")
        self.__Results = []
        self.__SegMain()

    @property
    def Results(self):
        return self.__Results
        
    def __SegMain(self):
        
        SourceString = self.__InputText
        
        sens = self.__SentenceSeg(SourceString)
        
        for sen in sens:
            senResults = []
            if sen.isSegmentable:
                
                #原子切分
                atoms = self.__AtomSeg(sen)
                #生成2-Gram切分词图结点
                nodes = self.__GenerateBiGramWordSegGraphNodes(atoms, self.__DictionarySet["CoreDict"])
                
                #生成2-Gram切分词图边
                edges = self.__GenerateBiGramWordSegGraphEdges(nodes, self.__SmoothParameter, self.__DictionarySet["CoreDict"], self.__DictionarySet["BiGramDict"])
                #结点和边进行合并
                biGramGraph = BiGramWordSegGraph(nodes, edges)
                #使用Viterbi改进算法得到N-最短路
                paths = self.__GenerateNKindShortestPaths(biGramGraph, self.__NKind)
                #生成初步切分结果(2-Gram初分词图路径，初分最优化2-Gram切分词图结点)
                optimumPaths = self.__FirstGenerateOptimumPaths(paths, nodes)
                
                optimumNodes = BiGramWordSegGraphNodeList()
                
                #对每一条初分路径进行未登录词识别、同时不断最优化初分结果
                for optimumPath in optimumPaths:
                    nodes = optimumPath.ChangeLinkToList
                    for node in nodes:
                        optimumNodes.InsertNode(node)
                    if self.__PersonRecognition:
                        self.__OOVRecognition(TT_PERSON, optimumPath, optimumNodes, self.__DictionarySet["CoreDict"], self.__DictionarySet["PersonDict"], self.__ContextSet["PersonContext"])
                    
                    if self.__TransRecognition:
                        self.__OOVRecognition(TT_FOREIGN, optimumPath, optimumNodes, self.__DictionarySet["CoreDict"], self.__DictionarySet["ForeignPersonDict"], self.__ContextSet["ForeignPersonContext"])
                    
                    if self.__PlaceRecognition:
                        self.__OOVRecognition(TT_PLACE, optimumPath, optimumNodes, self.__DictionarySet["CoreDict"], self.__DictionarySet["PlaceDict"], self.__ContextSet["PlaceContext"])
                """
                print("######################################")
                for optimumPath in optimumPaths:
                    nodes = optimumPath.ChangeLinkToList
                    for i in nodes:
                        print(i.Content,"\t",i.SrcContent,"\t")
                    print("######################################")
                """

                """
                print("######################################")
                point = optimumNodes.Head
                while not point is None:
                    print(point.Content,"\t",point.SrcContent,"\t",point.Frequency,"\t",point.POS,"\t",point.AtomStart,"\t",point.AtomEnd,"\t")
                    point = point.Next
                print("######################################")
                """
                #由最优化结点生成初分最优化
                optimumEdges = self.__GenerateBiGramWordSegGraphEdges(optimumNodes, self.__SmoothParameter, self.__DictionarySet["CoreDict"], self.__DictionarySet["BiGramDict"])
                #结点和边进行合并
                biGramGraph = BiGramWordSegGraph(optimumNodes, optimumEdges)
                #使用Viterbi改进算法得到最优化N-最短路
                paths = self.__GenerateNKindShortestPaths(biGramGraph, 3)
                #生成最终切分结果(2-Gram词图路径，最优化2-Gram词图结点)
                optimumPaths = self.__FirstGenerateOptimumPaths(paths, optimumNodes) #self.__FinalGenerateOptimumPaths(paths, optimumNodes)

                #词性标注
                for optimumPath in optimumPaths:
                    pathResult = self.__POSTaggingAndGenerateResult( optimumPath, self.__DictionarySet["CoreDict"], self.__ContextSet["LexicalContext"])
                    senResults.append(pathResult)
 
                self.__Results.append(senResults)
            
                """
                print("######################################")
                for result in self.__Results:
                    for i in result:
                        print(i)
                    print("######################################")
                """
                """
                x = BiGramWordSegGraphNodeList()
                y = BiGramWordSegGraphEdgeList()
                x.InsertNode(BiGramWordSegGraphNode(0,1,"始##始",0,1))
                x.InsertNode(BiGramWordSegGraphNode(1,2,"A",0,1))
                x.InsertNode(BiGramWordSegGraphNode(2,3,"B",0,1))
                x.InsertNode(BiGramWordSegGraphNode(3,4,"C",0,1))
                x.InsertNode(BiGramWordSegGraphNode(4,5,"D",0,1))
                x.InsertNode(BiGramWordSegGraphNode(5,6,"E",0,1))
                x.InsertNode(BiGramWordSegGraphNode(6,7,"末##末",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(0,1,"始##始@A",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(1,2,"A@B",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(1,3,"A@C",0,2))
                y.InsertEdge(BiGramWordSegGraphEdge(2,3,"B@C",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(2,4,"B@D",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(3,4,"C@D",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(3,6,"C@末##末",0,2))
                y.InsertEdge(BiGramWordSegGraphEdge(4,5,"D@E",0,1))
                y.InsertEdge(BiGramWordSegGraphEdge(4,6,"D@末##末",0,3))
                y.InsertEdge(BiGramWordSegGraphEdge(5,6,"E@末##末",0,1))
                biGramGraph = BiGramWordSegGraph(x, y)
                point = x.Head
                while not point is None:
                    print("Content: %s\tFrequency: %f\tPOS: %f" %( point.Content, point.Frequency, point.POS))
                    point = point.Next
                point = y.Head
                while not point is None:
                    print("Content: %s\tWeight: %f\tPOS: %f" %( point.Content, point.Weight, point.POS))
                    print(point.NodeStart, point.NodeEnd)
                    point = point.Next
                print(biGramGraph.NodesNumber)
                """
        
    def __SentenceSeg(self, SourceString):
        
        characters = SourceString
        
        sens = []
        
        Content = ""
        isSenBegin = True
        for character in characters:
            if isSentenceSeperator(character):
                #必须假设用户输入没有错误，比如，一个词的各个字之间不允许出现空白分隔符，若出现，属于用户的意外输入错误，应由用户排除这种干扰。
                if character in BLANK_SEP:
                    #若句子中间出现了空白分隔符，那么应该先将空白分隔符前面的整句存入Sens
                    if not isSenBegin:
                        sen = Sentence(Content, True)
                        sens.append(sen)
                        
                    #不管空白分隔符是否出现在句子开头处，都应该将空白分隔符单独插入
                    sen = Sentence(character, False)
                    sens.append(sen)
                    
                else:
                    sen = Sentence(Content + character, True)
                    sens.append(sen)
                
                Content = ""
                isSenBegin = True
                    
            else:
                Content = Content + character
                isSenBegin = False
        
        #句子未遇到结束符号，即，非正常结束，但是仍需要加入sens进行后续分析。
        if 0 < len(Content):
            sen = Sentence(Content, True)
            sens.append(sen)
        
        return sens


    def __AtomSeg(self, Sen):
        
        atoms = []
        
        senSrcContent = Sen.SrcContent
        senSrcLength = Sen.SrcLength
        # [ pointStart, pointEnd )
        pointStart = 0
        pointEnd = senSrcLength
        
        atomBeginTmp = Atom()
        atomEndTmp = Atom()
        
        #清除句子的开始标记和结束标记
        if senSrcContent.startswith(SEN_BEGIN):
            atomBeginTmp = Atom(SEN_BEGIN, SEN_BEGIN_POS)
            pointStart = pointStart + len(SEN_BEGIN)
            
        if senSrcContent.endswith(SEN_END):
            atomEndTmp = Atom(SEN_END, SEN_END_POS)
            pointEnd = pointEnd - len(SEN_END)
            
        atoms.append(atomBeginTmp)
        
        chars = senSrcContent[ pointStart : pointEnd ]
        charTypes = []
        
        flag = True #True代表"."前面没有数字字符或英文字符
        for i in range(0, len(chars)):
            char = chars[i]
            charType = CheckCharType(char)
            if char == ".":
                if flag:
                    if i+1 < len(chars) and (isNumber(chars[i+1]) or isLetter(chars[i+1])):
                        charType = CT_SINGLE
                else:
                    charType = CT_SINGLE
            elif charType in {CT_CN_CHARACTER, CT_CN_DELIMITER, CT_EN_DELIMITER, CT_CN_INDEX, CT_UNCLEAR}:
                flag = False
            elif charType == CT_SINGLE:
                flag = True
            
            charTypes.append(charType)
        
        point = 0
        while point < len(chars):
            char = chars[point]
            charType = charTypes[point]
            
            if charType in {CT_CN_CHARACTER, CT_CN_DELIMITER, CT_EN_DELIMITER, CT_CN_INDEX, CT_UNCLEAR}:
                atomType = charType
                atomTmp = Atom(chars[point],atomType)
                atoms.append(atomTmp)
                point = point + 1
                
            elif point+1 < len(chars) and charType == CT_SINGLE:
                    
                atomSrcContent = chars[point]
                isBreak = False
                while point+1 < len(chars):
                    point = point + 1
                    nchar = chars[point]
                    ncharType = charTypes[point]
                    if charType == ncharType:
                        atomSrcContent = atomSrcContent + nchar
                    else:
                        isBreak = True
                        break
                atomType = charType
                atomTmp = Atom(atomSrcContent,atomType)
                atoms.append(atomTmp)
                if not isBreak:
                    point = point + 1

            else:
                atomType = charType
                atomTmp = Atom(chars[point],atomType)
                atoms.append(atomTmp)
                point = point + 1
                
        atoms.append(atomEndTmp)
        
        """
        for i in atoms:
            print(i.SrcContent,"\t",i.Type)
        """
        return atoms

    def __GenerateBiGramWordSegGraphNodes(self, Atoms, CoreDict):

        nodes = BiGramWordSegGraphNodeList()
            
        atoms = Atoms
        for i in range(0, len(atoms)):
            nodeCont = atoms[i].SrcContent
            nodeSrcCont = atoms[i].SrcContent
            nodePOS = atoms[i].Type
            nodeFreq = MAX_FREQUENCY
            atomType = atoms[i].Type
            if atomType == CT_CN_INDEX:
            
                nodePOS = - NUM
                nodeCont = WORD_OOV_NUM
                nodeFreq = 0
                
            elif atomType in (CT_EN_DELIMITER, CT_CN_DELIMITER):
            
                nodePOS = PUNC
                
            elif atomType == CT_UNCLEAR:
            
                nodePOS = UNSET_POS
                
            elif atomType == CT_SINGLE:
                if isNumberStr(nodeCont):
                
                    nodePOS = - NUM
                    nodeCont = WORD_OOV_NUM
                    nodeFreq = 0
                    
                else:
                
                    nodePOS = - LETTER_BLOCK
                    nodeCont = WORD_OOV_LETTER
                    nodeFreq = 0
                    
            node = BiGramWordSegGraphNode(i, i+1, nodeCont, nodeSrcCont, nodePOS, nodeFreq)
            nodes.InsertNode(node)
            
        for i in range(0, len(atoms)):
            nodeCont = atoms[i].SrcContent
            nodeSrcCont = atoms[i].SrcContent
            for j in range(i+1, len(atoms)+1):
                #获取词典中第一条以该词开头的词条
                isMatched, matchedContent = CoreDict.MatchOne(nodeCont)
                if(isMatched and nodeCont == matchedContent):
                    #禁止"2017年底"、"5月初"这类的以"年"、"月"开头的词进行组合。
                    #若出现，则跳过所有以"年"、"月"开头的组合的检索(break)。
                    if len(nodeCont) == 2 and (nodeCont.startswith("年") or nodeCont.startswith("月")):
                        if 0 < i:
                            latomSrcCont = atoms[i-1].SrcContent
                            if isNumberStr(latomSrcCont) or isChineseBigNumberStr(latomSrcCont):
                                if nodeCont[1] in "初末前后底中间内":
                                    break
                    
                    #获取所有在词典中与该词匹配的词条
                    """
                    print("########## ",nodeCont," ##########")
                    """
                    matchedAll = CoreDict.MatchAll(nodeCont)
                    
                    #设置结点词频率
                    nodeFreq = 0
                    for item in matchedAll:
                        nodeFreq = nodeFreq + item.Frequency
                    

                    #设置结点词词性
                    if len(matchedAll) == 1:
                        nodePOS = matchedAll[0].POS
                    else:
                        nodePOS = UNSET_POS
                        
                    node = BiGramWordSegGraphNode(i, j, nodeCont, nodeSrcCont, nodePOS, nodeFreq)
                    nodes.InsertNode(node)
                if j < len(atoms):
                    nodeCont = nodeCont + atoms[j].SrcContent
                    nodeSrcCont = nodeSrcCont + atoms[j].SrcContent
        """
        point = nodes.Head
        while not point is None:
            print("Content: %s\tFrequency: %f\tPOS: %f" %( point.Content, point.Frequency, point.POS))
            point = point.Next
        
        """
        return nodes
        
    def __GenerateBiGramWordSegGraphEdges(self, Nodes, SmoothParameter, CoreDict, BiGramDict):
        edges = BiGramWordSegGraphEdgeList()
        
        nodes = Nodes
        
        nodeStart = nodes.Head
        edgeStart = 0
        while not nodeStart is None:
            #二元语法模型
            #计算分割为 first @ second 的概率
            # P(first @ second) = P(first)*P(second | first)
            # originalWeight 即 P(first @ second)
            # firstFreq 即 P(first)
            #POS小于0说明是未登录词OOV
            firstFreq = 0
            if nodeStart.POS >= 0:
                firstFreq = nodeStart.Frequency
            else:
                isFound, wordTmp = CoreDict.MatchOnly(nodeStart.Content, OOV)
                if isFound:
                    firstFreq = wordTmp.Frequency
                else:
                    firstFreq = 0
                
            nodeEnd, step  = nodes.FindEdgeEnd(nodeStart)
            
            while (not nodeEnd is None) and nodeStart.AtomEnd == nodeEnd.AtomStart:
            
                edgeContent = nodeStart.Content + WORD_CONNECTOR + nodeEnd.Content
                isFound, wordTmp = BiGramDict.MatchOnly(edgeContent, BIGRAM_POS)
                if isFound:
                    originalFreq = wordTmp.Frequency
                else:
                    originalFreq = 0
                
                #对于零概率的未登录词的平滑处理
                pr = 1 / MAX_FREQUENCY
                
                edgeWeight = SmoothParameter * (1 + firstFreq) / (MAX_FREQUENCY + 80000)
                edgeWeight += (1 - SmoothParameter) * ((1 - pr) * originalFreq / (1 + firstFreq) + pr )
                edgeWeight = - math.log(edgeWeight)
                
                #未登录词: P(Wi|Ci);已知词汇:P = 1
                if nodeStart.POS < 0:
                    edgeWeight = edgeWeight + nodeStart.Frequency
                
                edgeEnd = edgeStart + step
                edge = BiGramWordSegGraphEdge(edgeStart, edgeEnd, edgeContent, nodeStart.POS, edgeWeight)
                edges.InsertEdge(edge)
                
                nodeEnd = nodeEnd.Next
                step = step + 1
            nodeStart = nodeStart.Next
            edgeStart = edgeStart + 1
        """
        point = edges.Head
        while not point is None:
            print("Content: %s\tWeight: %f\tPOS: %f" %( point.Content, point.Weight, point.POS))
            print(point.NodeStart, point.NodeEnd)
            point = point.Next
        """
        return edges
    
    def __GenerateNKindShortestPaths(self, BiGramGraph, NKind):
        nodesNumber = BiGramGraph.NodesNumber
        
        """
        print(nodesNumber)
        """
        
        ##初始化
        ##
        nodePathInfo = []
        for i in range(0, nodesNumber):
            nkLists = []
            for kind in range(0, NKind):
                nkList = NKindShortestNodeList()
                nkLists.append(nkList)
            nodePathInfo.append(nkLists)
        ##
        ####
        
        
        ##不考虑始点的前趋，故从1开始处理
        ##
        for edgeEndNodeNum in range(1,nodesNumber):
            
            candidates = []
            ##根据edgeEndNodeNum的所有入边和其前趋结点最短的N类距离，
            ##计算出候选距离
            ##结果存入candidates
            ##
            edge = BiGramGraph.EdgeList.FindFirstEdgeByEndNum(edgeEndNodeNum)
            while (not edge is None) and edge.NodeEnd == edgeEndNodeNum:
                parentNode = edge.NodeStart
                edgeWeight = edge.Weight
                for parentIndex in range(0, NKind):
                    distToParentNode = nodePathInfo[parentNode][parentIndex].Distance
                    if parentNode == 0:
                        candidates.append((edgeWeight, parentNode, 0))
                        break
                    if distToParentNode == INFINITE_DIST:
                        break
                    candidates.append((distToParentNode + edgeWeight, parentNode, parentIndex))
                edge = edge.Next
            ##
            ####
            
            ##对candidates[]按照路径长度进行排序
            ##
            candidates.sort(key = lambda x : x[0])
            ##
            ####
            

            ##对candidates中的候选结果进行整理
            ##结果放入nodePathInfo[edgeEndNodeNum]中
            ##第K短的路径的距离放入nodePathInfo[edgeEndNodeNum][K].Distance
            ##相应的，具有相同距离的该点（edgeEndNodeNum）前趋结点们存入nodePathInfo[edgeEndNodeNum][K].ParentNodes[]中
            ##
            current = edgeEndNodeNum
            for kind in range(0, NKind):
                if len(candidates) == 0:
                    break
                (distance, parentNode, parentKind) = candidates.pop(0)
                nodePathInfo[current][kind].Distance = distance
                nodePathInfo[current][kind].ParentNodesStack.append((parentNode, parentKind))
                while len(candidates) != 0 and candidates[0][0] == distance:
                    (distance, parentNode, parentKind) = candidates.pop(0)
                    nodePathInfo[current][kind].ParentNodesStack.append((parentNode, parentKind))
            
            ##
            ####
        ##
        ####
        """
        for a in range(0, nodesNumber):
            print("node ",a," : ")
            for b in range(0, NKind):
                print("\tkind ",b," : ",end=" ")
                for i in range(0,len(nodePathInfo[a][b].ParentNodesStack)):
                    print(nodePathInfo[a][b].ParentNodesStack[i],end="->")
                print()
            print()
        """
        ##根据nodePathInfo生成最终的N类完整的路径信息
        ##第x条路径的各个结点存入paths[x]
        ##
        paths = []
        stack = []
        pathinfo = nodePathInfo[:]
        for kind in range(0, NKind):
            first = (nodesNumber - 1, kind)
            second = pathinfo[nodesNumber - 1][kind].Top
            """
            print("### ",nodesNumber - 1," ### ",kind," ### ",second," ### ")
            """
            while not second is None:
                (firstNode, firstKind) = first
                (secondNode, secondKind) = second
                stack.append((firstNode, firstKind))
                stack.append((secondNode, secondKind))
                
                while secondNode != 0:
                    (secondNode, secondKind) = pathinfo[secondNode][secondKind].Top
                    stack.append((secondNode, secondKind))
                
                path = []
                tmp = stack[:]
                while len(tmp) != 0:
                    path.append(tmp.pop()[0])
                paths.append(path)
                
                
                (secondNode, secondKind) = stack.pop()
                while secondNode == 0 or (len(stack) != 0 and pathinfo[secondNode][secondKind].TouchTheBottom):
                    (secondNode, secondKind) = stack.pop()
                
                first = (secondNode, secondKind)
                second = pathinfo[secondNode][secondKind].Pop
        ##
        ####
        """
        for path in paths:
            for node in path:  
               print(node,end="->")
            print()
        """
        return paths
    
    #将相邻的各种类型数字全部结合，从而保证在重求最短路时排除歧义
    def __MergeContinueNumberTogether(self, TmpPath):
        if TmpPath.Number <= 3:
            return
        current = TmpPath.Head
        """
        print(current.Content)
        """
        next = current.Next
        """
        print(next.Content)
        """
        while not next is None:
            if (isNumberStr(current.SrcContent) or isChineseBigNumberStr(current.SrcContent)) and (isNumberStr(next.SrcContent) or isChineseBigNumberStr(next.SrcContent)):
                tmpstr = current.SrcContent + next.SrcContent
                if isNumberStr(tmpstr) or isChineseBigNumberStr(tmpstr):
                    #current.Content/current.POS将会在后续的识别过程中设置
                    #即在__CleanDateElements第4部分进行标注
                    #current.Start必然是原值
                    current.SrcContent = tmpstr
                    current.AtomEnd = next.AtomEnd
                    TmpPath.DeleteNextNode(current)
                    next = current.Next
                    continue
            current = current.Next
            next = current.Next
            
    #为特殊标点符号标注词性，在之前的分词过程中很有可能被识别为数字，或"－－"，"―"，"-"
    #"-"和"－"在原子切分阶段被识别为数字(WORD_OOV_NUM,NUM)
    #"—"应该在原子切分阶段就被识别为标点符号了，并在词图结点生成阶段标注好了词性(PUNC)
    #但是由于频率设置的是MAX_FREQUENCY因此需要重新进行记录
    def __ChangeDelimiterPOS(self, TmpPath):
        current = TmpPath.Head
        while not current is None:
            tmpstr = current.SrcContent
            if tmpstr == "－－" or tmpstr == "―" or tmpstr == "-":
                #current.Start/current.End/current.SrcContent必然为原值
                current.Content = current.SrcContent
                current.POS = PUNC
                current.Frequency = 0
            current = current.Next
            
            
            
    #如果前一个词是数字(NUM)或时间词(TIME)，当前词以"－"或"-"开始，且不为标点符号
    #即当前词应该是在词图生成结点阶段被识别为一个数字
    #那么应该将此"－"或"-"符号从当前词中分离出来。
    #例如 "3-4月"应当拆分成"3|-|4|月"
    #在初次切分的时候并不会识别出时间词(TIME)
    #但是经过初切分优化之后，会产生时间词，因此在重求阶段仍需要将这种情况考虑进来
    #重求阶段可能会产生前一个词是时间词的情况(TIME)
    def __SplitSlashBetweenDigital(self, TmpPath):
        if TmpPath.Number <= 3:
            return
        last = TmpPath.Head
        current = last.Next
        
        while not current is None:
            if abs(last.POS) == NUM or abs(last.POS) == TIME:
                tmpstr = current.SrcContent
                if isNumberStr(tmpstr) or isChineseBigNumberStr(tmpstr):
                    if tmpstr[0] in "-－" and len(tmpstr) > 1:
                        nextnode = TmpNode()
                        
                        nextnode.AtomStart = current.AtomStart + 1
                        nextnode.AtomEnd = current.AtomEnd
                        nextnode.SrcContent = current.SrcContent[1:]
                        nextnode.Content = nextnode.SrcContent
                        #current本身就是一个NUM因此nextnode应继承current的POS和Frequency
                        #因为是此处的分离为既定情况，故不用进行未登录词的负数标记
                        nextnode.POS = NUM
                        nextnode.Frequency = current.Frequency
                        
                        #current.Start必然不变
                        current.AtomEnd = current.AtomStart + 1
                        #current.Content保持NUM不变，因为还要在图中进行运算
                        current.SrcContent = current.SrcContent[0:1]
                        #处理完nextnode后current应改变为分离出来的"-"或"－"
                        #因此词性改变为PUNC，频率不应使用NUM类词语的词频，而应始词频降至0
                        #因为是被识别为标点符号，故不用进行未登录词的负数标记
                        current.POS = PUNC
                        current.Frequency = 0
                        
                        TmpPath.InsertNextNode(current,nextnode)
            last = last.Next
            current = current.Next
            
            
            
    #1、如果当前词是数字，下一个词是“月、日、时、分、秒、月份”中的一个，则合并且当前词词性是时间
    #2、如果当前词是可以作为年份的数字，下一个词是“年”，则合并，词性为时间，否则为数字。
    #3、如果当前串最后一个汉字是"点" ，则认为当前数字是时间
    #4、如果当前串最后一个汉字不是"∶・．／"和半角的'.''/'，那么是数
    #5、如果当前串最后一个汉字是"∶・．／"和半角的'.''/'，且长度大于1，那么认为最后一个字符为标点符号。例如"1."
    def __CleanDateElements(self, TmpPath):
        if TmpPath.Number <= 2:
            return
        current = TmpPath.Head
        next = current.Next
        while not next is None:
            """
            print(current.SrcContent," ### ",next.SrcContent)
            """
            if isNumberStr(current.SrcContent) or isChineseBigNumberStr(current.SrcContent):
                nextStr = next.SrcContent
                ## 1
                if nextStr in {"月","日","时","分","秒","月份"}:
                    #current.Start必然不变
                    current.AtomEnd = next.AtomEnd
                    current.Content = WORD_OOV_TIME
                    current.SrcContent = current.SrcContent + nextStr
                    current.POS = - TIME
                    #current原来是NUM，现在变为TIME，因此current.Frequency仍为OOV的词频0
                    
                    TmpPath.DeleteNextNode(current)
                    
                ## 2
                elif nextStr == "年":
                    if isYearTime(current.SrcContent):
                        #current.Start必然不变
                        current.AtomEnd = next.AtomEnd
                        current.Content = WORD_OOV_TIME
                        current.SrcContent = current.SrcContent + nextStr
                        current.POS = - TIME
                        #current原来是NUM，现在变为TIME，因此current.Frequency仍为OOV的词频0
                        TmpPath.DeleteNextNode(current)
                    else:
                        #current未变，恢复图点信息
                        #current.Start/current.End必然不变
                        current.Content = WORD_OOV_NUM
                        #current.SrcContent必然不变
                        current.POS = - NUM
                        #current.Frequency显然未变
                else:
                    ## 3
                    if current.SrcContent.endswith("点"):
                        #current.Start/current.End必然不变
                        current.Content = WORD_OOV_TIME
                        #current.SrcContent必然不变
                        current.POS = - TIME
                        #current.Frequency不变最为稳妥，即保持原有词频
                    else:
                        tmpstr = current.SrcContent[-1]
                        ## 4
                        if not tmpstr in "∶・．／./":
                            #current.Start/current.End必然不变
                            current.Content = WORD_OOV_NUM
                            #current.SrcContent必然不变
                            current.POS = - NUM
                            #current.Frequency不变最为稳妥，即保持原有词频
                            
                        ## 5
                        elif len(current.SrcContent) > 1:
                            nextnode = TmpNode()
                            
                            nextnode.AtomStart = current.AtomStart - 1
                            nextnode.AtomEnd = current.AtomEnd
                            nextnode.SrcContent = current.SrcContent[-1]
                            nextnode.Content = nextnode.SrcContent
                            nextnode.POS = PUNC
                            nextnode.Frequency = 0
                            
                            #current.Start必然不变
                            current.AtomEnd = current.AtomEnd - 1
                            current.Content = WORD_OOV_NUM
                            current.SrcContent = current.SrcContent[:-1]
                            #分离后变为纯数字，应当设为未登录数字WORD_OOV_NUM
                            current.POS = - NUM
                            current.Frequency = 0
                            
                            TmpPath.InsertNextNode(current,nextnode)
                            
            current = current.Next
            next = current.Next
        
    def __FirstGenerateOptimumPaths(self, Paths, Nodes):
        OptimumPaths = []
        
        paths = Paths
        nodes = Nodes.ChangeLinkToList
        for path in paths:
            OptimumPath = BiGramWordSegGraphNodeList()
            for i in range(0, len(path)):
            
                optimumNode = BiGramWordSegGraphNode()
                optimumNode.AtomStart = nodes[path[i]].AtomStart
                optimumNode.AtomEnd = nodes[path[i]].AtomEnd
                optimumNode.Content = nodes[path[i]].Content
                optimumNode.POS = nodes[path[i]].POS
                optimumNode.Frequency = nodes[path[i]].Frequency
                optimumNode.SrcContent = nodes[path[i]].SrcContent
                OptimumPath.InsertNode(optimumNode)
                
            self.__MergeContinueNumberTogether(OptimumPath)
            self.__ChangeDelimiterPOS(OptimumPath)
            self.__SplitSlashBetweenDigital(OptimumPath)
            self.__CleanDateElements(OptimumPath)
            
            OptimumPaths.append(OptimumPath)
            
        return OptimumPaths
        
    def __ClearTagList(self, OptimumPath):
        current = OptimumPath.Head
        while not current is None:
            current.TagList = []
            current = current.Next
        
    def __RoleTagging(self, TaggingType, OptimumPath, CoreDict, OOVDict, Context):

        previousNode = None
        currentNode = OptimumPath.Head
        
        while not currentNode is None:
            if TaggingType == TT_FOREIGN and not previousNode is None:
                if CheckCharType(previousNode.SrcContent[0]) == CT_CN_CHARACTER:
                    if currentNode.SrcContent == ".":
                        currentNode.SrcContent = "．"
                    elif currentNode.SrcContent == "-":
                        currentNode.SrcContent = "－"
            
            matchedAll = OOVDict.MatchAll(currentNode.SrcContent)
            posNum = len(matchedAll)
            if len(matchedAll):
                for item in matchedAll:
                    pos = item.POS
                    freq = - ( math.log( item.Frequency + 1 ) - math.log( Context.GetPOSInitialFrequency(pos) + posNum + 1 ) ) # - log( C(w_i,t_i)/C(t_i) )
                    tag = Tag(pos, freq)
                    currentNode.TagList.append(tag)
            
            if currentNode.SrcContent == SEN_BEGIN:
                tag = Tag(100, 0)
                currentNode.TagList.append(tag)
            elif currentNode.SrcContent == SEN_END:
                tag = Tag(101, 0)
                currentNode.TagList.append(tag)
            else:
                matchedAll = CoreDict.MatchAll(currentNode.SrcContent)
                if len(matchedAll):
                    freq = 0
                    for item in matchedAll:
                        freq = freq + item.Frequency
                    pos = 0  #设置其角色为"其他无关词(A)",并计算频率
                    freq = - ( math.log( freq + 1 ) - math.log( Context.GetPOSInitialFrequency(pos) + posNum + 1 ) )  # - log( C(w_i,t_i)/C(t_i) )
                    tag = Tag(pos, freq)
                    currentNode.TagList.append(tag)
            
            if len(currentNode.TagList) == 0:
                self.__GuessTag(TaggingType, currentNode, Context)
            
            previousNode = currentNode
            currentNode = currentNode.Next

    
    def __GenerateBestPOSByViterbi(self, OptimumPath, Context):
        previousNode = OptimumPath.Head
        currentNode = previousNode.Next
        while not currentNode is None:
            previousTagList = previousNode.TagList
            currentTagList = currentNode.TagList
            for curtag in currentTagList:
                minIndex = 0
                minFreq = MAX_FREQUENCY
                for index in range(0, len(previousTagList)):
                    pos = previousTagList[index].POS
                    freq = previousTagList[index].Frequency + ( - math.log(Context.GetPOSTransitionFrequency(pos,curtag.POS)) )
                    if freq < minFreq:
                        minFreq = freq
                        minIndex = index
                
                curtag.PrevIndex = minIndex
                curtag.Frequency = minFreq + curtag.Frequency
            previousNode = currentNode
            currentNode = currentNode.Next
            
        self.__TagBestPOS(OptimumPath)
        
    def __TagBestPOS(self, OptimumPath):
        nodeList = OptimumPath.ChangeLinkToList
        nodeList[0].TagList[0].isBest = True
        currentIndex = 0
        for i in range(len(nodeList)-1, 0, -1):
            currentTagList = nodeList[i].TagList
            if currentIndex < len(currentTagList):
                tag = currentTagList[currentIndex]
                tag.isBest = True
                currentIndex = tag.PrevIndex
            else:
                bestTag = nodeList[i+1].BestTag
                pos = bestTag.POS
                tag = Tag(pos, 0, 0, True)
                nodeList[i].TagList.append(tag)
        
    def __PersonRecog(self, OptimumPath, OptimumNodes, OOVDict, Context):
        """
        BBCD:姓+姓+名1+名2;
        BBE: 姓+姓+单名;
        BBZ: 姓+姓+双名成词;
        BCD: 姓+名1+名2;
        BE:  姓+单名;
        BEE: 姓+单名+单名;韩磊磊
        BG:  姓+后缀
        BXD: 姓+姓双名首字成词+双名末字
        BZ:  姓+双名成词;
        B:   姓
        CD:  名1+名2;
        EE:  单名+单名;
        FB:  前缀+姓
        XD:  姓双名首字成词+双名末字
        Y:   姓单名成词
        """
        roleStr = OptimumPath.RoleString
        """
        print(roleStr)
        """
        nodes = OptimumPath.ChangeLinkToList
        start = 1
        while start < len(roleStr):
            isMatched = False
            for index in range(0,len(PATTERNS)):
                if roleStr[start:].startswith(PATTERNS[index]) and nodes[start-1].SrcContent != "・" and nodes[start+len(PATTERNS[index])].SrcContent != "・":
                    # FB : 前缀+姓。若后面还有 名1+名2(B)CD 或 单名+单名 (B)EE等，则FB规则失效
                    tmpStr = roleStr[start+2:start+3]
                    if PATTERNS[index] == "FB" and ( tmpStr == "E" or tmpStr == "C" or tmpStr == "G" ):
                        continue
                    
                    tmpIndex = start
                    personName = ""
                    while tmpIndex < start + len(PATTERNS[index]):
                        node = nodes[tmpIndex]
                        personName = personName + node.SrcContent
                        tmpIndex += 1
                    
                    if PATTERNS[index] == "CDCD":
                        if CheckForeignCharCount(personName) > 0:
                            start += len(PATTERNS[index]) # - 1不确定
                        continue
                    #print(PATTERNS[index],", ",personName)
                    
                    newNode = BiGramWordSegGraphNode()
                    newNode.AtomStart = nodes[start].AtomStart
                    newNode.AtomEnd = nodes[start + len(PATTERNS[index]) - 1].AtomEnd
                    newNode.Content = WORD_OOV_PERSON
                    newNode.SrcContent = personName
                    #print(newNode.SrcContent,", ",newNode.Content)
                    newNode.POS = - NOUN_PERSON
                    freq = - math.log( FACTORS[index] ) + self.__ComputePossibility(start, len(PATTERNS[index]), nodes, OOVDict, Context)
                    newNode.Frequency = freq
                    OptimumNodes.InsertNode(newNode)
                    start += len(PATTERNS[index])
                    isMatched = True
                    break
            
            if not isMatched:
                start = start + 1
    
    def __PlaceRecog(self, OptimumPath, OptimumNodes, OOVDict, Context):
        nodes = OptimumPath.ChangeLinkToList
        panelty = 1
        for index in range(1,len(nodes)):
            start = index
            end = index
            srcCont = nodes[end].SrcContent
            tag = nodes[end].BestTag
            if not tag is None:
                if tag.POS == 1:
                    end = end + 1
                    while end < len(nodes):
                        tmptag = nodes[end].BestTag
                        if tmptag is None:
                            break
                        tmppos = tmptag.POS
                        if tmppos == 1 or tmppos == 3:
                            if end > start + 1:
                                panelty += 1
                            srcCont = srcCont + nodes[end].SrcContent
                        elif tmppos == 2:
                            srcCont = srcCont + nodes[end].SrcContent
                        else:
                            break
                        end += 1
                elif tag.POS == 2:
                    panelty += 1
                    end = end + 1
                    while end < len(nodes):
                        tmptag = nodes[end].BestTag
                        if tmptag is None:
                            break
                        tmppos = tmptag.POS
                        if tmppos == 3:
                            if end > start + 1:
                                panelty += 1
                            srcCont = srcCont + nodes[end].SrcContent
                        elif tmppos ==2:
                            srcCont = srcCont + nodes[end].SrcContent
                        else:
                            break
                        end += 1
            if end > start:
                newNode = BiGramWordSegGraphNode()
                newNode.AtomStart = nodes[start].AtomStart
                newNode.AtomEnd = nodes[end - 1].AtomEnd
                newNode.Content = WORD_OOV_SPACE
                newNode.SrcContent = srcCont
                newNode.POS = - NOUN_SPACE
                freq = math.log(panelty) + self.__ComputePossibility(start, end-start, nodes, OOVDict, Context)
                newNode.Frequency = freq
                OptimumNodes.InsertNode(newNode)
    
    def __ForeignRecog(self, OptimumPath, OptimumNodes, OOVDict, Context):
        nodes = OptimumPath.ChangeLinkToList
        panelty = 1
        for index in range(1,len(nodes)):
            start = index
            end = index
            srcCont = nodes[end].SrcContent
            tag = nodes[end].BestTag
            if not tag is None:
                if tag.POS == 1:
                    end = end + 1
                    while end < len(nodes):
                        tmptag = nodes[end].BestTag
                        if tmptag is None:
                            break
                        tmppos = tmptag.POS
                        if tmppos == 1 or tmppos == 3:
                            if end > start + 1:
                                panelty += 1
                            srcCont = srcCont + nodes[end].SrcContent
                        elif tmppos == 2:
                            srcCont = srcCont + nodes[end].SrcContent
                        else:
                            break
                        end += 1
                elif tag.POS == 2:
                    panelty += 1
                    end = end + 1
                    while end < len(nodes):
                        tmptag = nodes[end].BestTag
                        if tmptag is None:
                            break
                        tmppos = tmptag.POS
                        if tmppos == 3:
                            if end > start + 1:
                                panelty += 1
                            srcCont = srcCont + nodes[end].SrcContent
                        elif tmppos ==2:
                            srcCont = srcCont + nodes[end].SrcContent
                        else:
                            break
                        end += 1
            if end > start:
                if len(srcCont) <= 2:
                    continue
                newNode = BiGramWordSegGraphNode()
                newNode.AtomStart = nodes[start].AtomStart
                newNode.AtomEnd = nodes[end - 1].AtomEnd
                newNode.Content = WORD_OOV_PERSON
                newNode.SrcContent = srcCont
                newNode.POS = - NOUN_PERSON
                freq = math.log(panelty) + self.__ComputePossibility(start, end-start, nodes, OOVDict, Context)
                newNode.Frequency = freq
                OptimumNodes.InsertNode(newNode)
    
    def __ComputePossibility(self, Start, Length, Nodes, OOVDict, Context):
        possibility = 0
        nodes = Nodes
        for index in range(Start, Start+Length):
            tmptag = nodes[index].BestTag
            if not tmptag is None:
                isMatched, word = OOVDict.MatchOnly(nodes[index].SrcContent, tmptag.POS)
                freq = 0
                if isMatched:
                    freq = word.Frequency
                possibility = possibility - ( math.log(freq + 1) - math.log(Context.GetPOSInitialFrequency(tmptag.POS) + 1) )
        return possibility
    
    def __OOVRecognition(self, TaggingType, OptimumPath, OptimumNodes, CoreDict, OOVDict, Context):
        self.__ClearTagList(OptimumPath)
        self.__RoleTagging(TaggingType, OptimumPath, CoreDict, OOVDict, Context)
        self.__GenerateBestPOSByViterbi(OptimumPath, Context)
        if TaggingType == TT_PERSON:
            self.__PersonRecog(OptimumPath, OptimumNodes, OOVDict, Context)
        elif TaggingType == TT_PLACE:
            self.__PlaceRecog(OptimumPath, OptimumNodes, OOVDict, Context)
        elif TaggingType == TT_FOREIGN:
            self.__ForeignRecog(OptimumPath, OptimumNodes, OOVDict, Context)
        
    def __POSTagging(self, OptimumPath, CoreDict, Context):
        
        currentNode = OptimumPath.Head
        while not currentNode is None:
            currentSrcContent = currentNode.SrcContent
            
            if currentNode.POS > 0:
                pos = currentNode.POS
                freq = -( math.log( currentNode.Frequency + 0.000001 ) - math.log( Context.GetPOSInitialFrequency(pos) + 1) )
                if freq < 0:
                    freq = 0
                tag = Tag(pos, freq)
                currentNode.TagList.append(tag)
            else:
                if currentNode.POS < 0:
                    currentNode.POS = - currentNode.POS
                    tag = Tag(currentNode.POS, currentNode.Frequency)
                    currentNode.TagList.append(tag)
                matchedAll = CoreDict.MatchAll(currentSrcContent)
                if len(matchedAll):
                    for item in matchedAll:
                        pos = item.POS
                        freq = - ( math.log( item.Frequency + 1 ) - math.log( Context.GetPOSInitialFrequency(pos) + len(matchedAll) ) )
                        tag = Tag(pos, freq)
                        currentNode.TagList.append(tag)
            currentNode = currentNode.Next

    
        
    def __POSTaggingAndGenerateResult(self, OptimumPath, CoreDict, Context):
        self.__POSTagging(OptimumPath, CoreDict, Context)
        self.__GenerateBestPOSByViterbi(OptimumPath, Context)
        result = []
        nodes = OptimumPath.ChangeLinkToList
        for index in range(1,len(nodes)-1):
            word = nodes[index].SrcContent
            tag = nodes[index].BestTag
            pos = tag.POS
            if pos == 204:
            	str = "cc"
            else:
                str = chr(pos>>8)
                if pos != ((pos>>8) << 8):
                    pos = pos - ((pos>>8)<<8)
                    str=str+chr(pos)
                #print(MAP_COLOR[str])
            result.append((word, MAP_POS[str], MAP_COLOR[str]))
        
        return result
        
    def __GuessTag(self, TaggingType, Node, Context):
        content = Node.Content;
        if TaggingType == TT_PERSON:
            if "××" in content:
                freq = 1 / (Context.GetPOSInitialFrequency(6) + 1)
                Node.TagList.append(Tag(6, freq))
            else:
                freq = 1 / (Context.GetPOSInitialFrequency(0) + 1)
                Node.TagList.append(Tag(0, freq))

                if Node.Length >= 4:
                    freq = 1 / (Context.GetPOSInitialFrequency(0) + 1)
                    Node.TagList.append(Tag(0, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(11) * 8)
                    Node.TagList.append(Tag(11, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(12) * 8)
                    Node.TagList.append(Tag(12, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(13) * 8)
                    Node.TagList.append(Tag(13, freq))
                elif Node.Length == 2:
                    freq = 1 / (Context.GetPOSInitialFrequency(0) + 1)
                    Node.TagList.append(Tag(0, freq))
                    charType = CheckCharType(content)
                    if charType == CT_UNCLEAR or charType == CT_CN_CHARACTER:
                        freq = 1 / (Context.GetPOSInitialFrequency(1) + 1)
                        Node.TagList.append(Tag(1, freq))
                        freq = 1 / (Context.GetPOSInitialFrequency(2) + 1)
                        Node.TagList.append(Tag(2, freq))
                        freq = 1 / (Context.GetPOSInitialFrequency(3) + 1)
                        Node.TagList.append(Tag(3, freq))
                        freq = 1 / (Context.GetPOSInitialFrequency(4) + 1)
                        Node.TagList.append(Tag(4, freq))
                        
                    freq = 1 / (Context.GetPOSInitialFrequency(11) * 8)
                    Node.TagList.append(Tag(11, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(12) * 8)
                    Node.TagList.append(Tag(12, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(13) * 8)
                    Node.TagList.append(Tag(13, freq))

        elif TaggingType == TT_PLACE:
            freq = 1 / (Context.GetPOSInitialFrequency(0) + 1)
            Node.TagList.append(Tag(0, freq))
            if Node.Length >= 4:
                freq = 1 / (Context.GetPOSInitialFrequency(11) * 8)
                Node.TagList.append(Tag(11, freq))
                freq = 1 / (Context.GetPOSInitialFrequency(12) * 8)
                Node.TagList.append(Tag(12, freq))
                freq = 1 / (Context.GetPOSInitialFrequency(13) * 8)
                Node.TagList.append(Tag(13, freq))
            elif Node.Length == 2:
                freq = 1 / (Context.GetPOSInitialFrequency(0) + 1)
                Node.TagList.append(Tag(0, freq))
                charType = CheckCharType(content)
                if charType == CT_UNCLEAR or charType == CT_CN_CHARACTER:
                    freq = 1 / (Context.GetPOSInitialFrequency(1) + 1)
                    Node.TagList.append(Tag(1, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(2) + 1)
                    Node.TagList.append(Tag(2, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(3) + 1)
                    Node.TagList.append(Tag(3, freq))
                    freq = 1 / (Context.GetPOSInitialFrequency(4) + 1)
                    Node.TagList.append(Tag(4, freq))
                    
                freq = 1 / (Context.GetPOSInitialFrequency(11) * 8)
                Node.TagList.append(Tag(11, freq))
                freq = 1 / (Context.GetPOSInitialFrequency(12) * 8)
                Node.TagList.append(Tag(12, freq))
                freq = 1 / (Context.GetPOSInitialFrequency(13) * 8)
                Node.TagList.append(Tag(13, freq))
        return