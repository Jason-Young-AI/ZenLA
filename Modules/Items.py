#!/usr/bin/env python

from Modules.Definitions import *

class Tag(object):
    def __init__(self, POS=UNSET_POS, Frequency=0, PrevIndex=0, isBest=False):
        if isinstance(POS, int) and isinstance(Frequency, (float, int)) and isinstance(PrevIndex, int) and isinstance(isBest, bool):
            self.__POS = POS
            self.__Frequency = Frequency
            self.__PrevIndex = PrevIndex
            self.__isBest = isBest
        else:
            raise ValueError("Tag.__init__ received wrong argument(s) type! ")
    
    @property
    def POS(self):
        return self.__POS
    
    @property
    def Frequency(self):
        return self.__Frequency
    
    @property
    def PrevIndex(self):
        return self.__PrevIndex
    
    @property
    def isBest(self):
        return self.__isBest
    
    @POS.setter
    def POS(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("Tag.POS must be an Integer! ")
        
        self.__Tag = SetValue
    
    @Frequency.setter
    def Frequency(self, SetValue):
        if not isinstance(SetValue, (float, int)):
            raise ValueError("Tag.Frequency must be an Integer or a Float! ")
        
        self.__Frequency = SetValue
    
    @PrevIndex.setter
    def PrevIndex(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("Tag.PrevIndex must be an Integer! ")
        
        self.__PrevIndex = SetValue
    
    @isBest.setter
    def isBest(self, SetValue):
        if not isinstance(SetValue, bool):
            raise ValueError("Tag.isBest must be a Boolean! ")
        
        self.__isBest = SetValue
    
class Word(object):
    
    def __init__(self, WContent="", WPOS=UNSET_POS, WFrequency=0):
        if isinstance(WContent, str) and isinstance(WPOS, int) and isinstance(WFrequency, int):
            self.__Content = WContent
            self.__POS = WPOS
            self.__Frequency = WFrequency
            self.__Length = len(self.__Content)
        else:
            raise ValueError("Word.__init__ received wrong argument(s) type! ")
    
    @property
    def Content(self):
        return self.__Content
    
    @property
    def POS(self):
        return self.__POS
    
    @property
    def Frequency(self):
        return self.__Frequency
        
    @property
    def Length(self):
        return self.__Length
    
    @Content.setter
    def Content(self, SetValue):
        if not isinstance(SetValue, str):
            raise ValueError("Word.Content must be a String! ")
        
        self.__Content = SetValue
        self.__Length = len(self.__Content)
    
    @POS.setter
    def POS(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("Word.POS must be an Integer! ")
        
        self.__POS = SetValue
    
    @Frequency.setter
    def Frequency(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("Word.Frequency must be an Integer! ")
        
        self.__Frequency = SetValue


class WordIndex(object):
    
    def __init__(self, WIWords=None):
        if WIWords is None :
                self.__Words = []
                self.__Number = len(self.__Words)
        elif isinstance(WIWords, list):
                self.__Words = WIWords
                self.__Number = len(self.__Words)
        else:
            raise ValueError("WordIndex.__init__ received wrong argument(s) type! ")
    
    @property
    def Words(self):
        return self.__Words
        
    @property
    def Number(self):
        self.__Number = len(self.__Words)
        return self.__Number
    
    @Words.setter
    def Words(self, SetValue):
        if not isinstance(SetValue, list):
            raise ValueError("WordIndex.Words must be a List! ")
        
        self.__Words = SetValue
        self.__Number = len(self.__Words)


class Sentence(object):

    def __init__(self, SSrcContent="", SisSegmentable=False):
        if isinstance(SSrcContent, str) and isinstance(SisSegmentable, bool):
            self.__SrcContent = SEN_BEGIN + SSrcContent + SEN_END
            self.__isSegmentable = SisSegmentable
            self.__SrcLength = len(self.__SrcContent)
        else:
            raise ValueError("Sentence.__init__ received wrong argument(s) type! ")
    
    @property
    def SrcContent(self):
        return self.__SrcContent
    
    @property
    def isSegmentable(self):
        return self.__isSegmentable

    @property
    def SrcLength(self):
        return self.__SrcLength
    

class Atom(object):
    
    def __init__(self, ASrcContent="", AType=CT_UNCLEAR):
        if isinstance(ASrcContent, str) and isinstance(AType, int):
            self.__SrcContent = ASrcContent
            self.__Type = AType
            self.__SrcLength = len(self.__SrcContent)
        else:
            raise ValueError("Atom.__init__ received wrong argument(s) type! ")
            
    @property
    def SrcContent(self):
        return self.__SrcContent
    
    @property
    def Type(self):
        return self.__Type
    
    @property
    def SrcLength(self):
        self.__SrcLength = len(self.__SrcContent)
        return self.__SrcLength

    @SrcContent.setter
    def SrcContent(self, SetValue):
        if not isinstance(SetValue, str):
            raise ValueError("Atom.SrcContent must be a String! ")
        
        self.__SrcContent = SetValue
        self.__SrcLength = len(self.__SrcContent)
    
    @Type.setter
    def Type(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("Atom.Type must be an Integer! ")
        
        self.__Type = SetValue


#二元切分词图的点
class BiGramWordSegGraphNode(object):
    
    #结点的内容为一个词，词取自原子序列的[AtomStart, AtomEnd)。
    def __init__(self, BGWSGNAtomStart=0, BGWSGNAtomEnd=0, BGWSGNContent="", BGWSGNSrcContent="", BGWSGNPOS=UNSET_POS, BGWSGNFrequency=0, BGWSGNTagList=None):
        if BGWSGNTagList is None :
            self.__TagList = []
        elif isinstance(BGWSGNTagList, list):
            self.__TagList = BGWSGNTagList
        else:
            raise ValueError("BiGramWordSegGraphNode.__init__ received wrong argument(s) type! ")
            
        if isinstance(BGWSGNAtomStart, int) and isinstance(BGWSGNAtomEnd, int) and isinstance(BGWSGNContent, str) and isinstance(BGWSGNSrcContent, str) and isinstance(BGWSGNPOS, int) and isinstance(BGWSGNFrequency, int):
            self.__Next = None
            self.__AtomStart = BGWSGNAtomStart
            self.__AtomEnd = BGWSGNAtomEnd
            self.__Content = BGWSGNContent
            self.__SrcContent = BGWSGNSrcContent
            self.__POS = BGWSGNPOS
            self.__Frequency = BGWSGNFrequency
            self.__Length = len(self.__Content)
            self.__SrcLength = len(self.__SrcContent)
        else:
            raise ValueError("BiGramWordSegGraphNode.__init__ received wrong argument(s) type! ")
    
    @property
    def Next(self):
        return self.__Next
            
    @property
    def TagList(self):
        return self.__TagList
    
    @property
    def AtomStart(self):
        return self.__AtomStart
        
    @property
    def AtomEnd(self):
        return self.__AtomEnd
        
    @property
    def Content(self):
        return self.__Content
        
    @property
    def SrcContent(self):
        return self.__SrcContent
        
    @property
    def POS(self):
        return self.__POS
        
    @property
    def Frequency(self):
        return self.__Frequency
        
    @property
    def Length(self):
        self.__Length = len(self.__Content)
        return self.__Length
        
    @property
    def SrcLength(self):
        self.__SrcLength = len(self.__SrcContent)
        return self.__SrcLength
        
    @Next.setter
    def Next(self, SetValue):
        if SetValue is None:
            self.__Next = None
        else:
            if not isinstance(SetValue, BiGramWordSegGraphNode):
                raise ValueError("BiGramWordSegGraphNode.Next must be a WordSegGraphNode! ")
            self.__Next = SetValue
        
    @TagList.setter
    def TagList(self, SetValue):
        if not isinstance(SetValue, list):
            raise ValueError("BiGramWordSegGraphNode.TagList must be a List! ")
        
        self.__TagList = SetValue

    @AtomStart.setter
    def AtomStart(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphNode.AtomStart must be an Integer! ")
        self.__AtomStart = SetValue
        
    @AtomEnd.setter
    def AtomEnd(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphNode.AtomEnd must be an Integer! ")
        self.__AtomEnd = SetValue
        
    @Content.setter
    def Content(self, SetValue):
        if not isinstance(SetValue, str):
            raise ValueError("BiGramWordSegGraphNode.Content must be a String! ")
        self.__Content = SetValue
        self.__Length = len(self.__Content)
        
    @SrcContent.setter
    def SrcContent(self, SetValue):
        if not isinstance(SetValue, str):
            raise ValueError("BiGramWordSegGraphNode.Content must be a String! ")
        self.__SrcContent = SetValue
        self.__SrcLength = len(self.__SrcContent)
        
    @POS.setter
    def POS(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphNode.POS must be an Integer! ")
        self.__POS = SetValue
        
    @Frequency.setter
    def Frequency(self, SetValue):
        if not isinstance(SetValue, (float, int)):
            raise ValueError("BiGramWordSegGraphNode.Frequency must be an Integer or a Float! ")
        self.__Frequency = SetValue
        
    @property
    def BestTag(self):
        for tag in self.__TagList:
            if tag.isBest:
                return tag
        return None
        
#二元切分词图的所有点构造的链表
class BiGramWordSegGraphNodeList(object):
    
    def __init__(self):
        self.__Head = None
        self.__Tail = None
        self.__Number = 0
        
    @property
    def Head(self):
        return self.__Head
    
    @property
    def Tail(self):
        return self.__Tail
    
    @property
    def Number(self):
        return self.__Number
        
    def ChangeValue(self, aValue, bValue):
        if not (isinstance(aValue, BiGramWordSegGraphNode) and isinstance(bValue, BiGramWordSegGraphNode)):
            raise ValueError("The arguments of the BiGramWordSegGraphNode.ChangeValue must be a WordSegGraphNode! ")
        aValue.AtomStart, bValue.AtomStart = bValue.AtomStart, aValue.AtomStart
        aValue.AtomEnd, bValue.AtomEnd = bValue.AtomEnd, aValue.AtomEnd
        aValue.Content, bValue.Content = bValue.Content, aValue.Content
        aValue.SrcContent, bValue.SrcContent = bValue.SrcContent, aValue.SrcContent
        aValue.POS, bValue.POS = bValue.POS, aValue.POS
        aValue.Frequency, bValue.Frequency = bValue.Frequency, aValue.Frequency
        aValue.TagList, bValue.TagList = bValue.TagList, aValue.TagList
                
    def FindEdgeEnd(self, Start):
        point = self.__Head
        
        while point != Start:
            point = point.Next
        
        point = point.Next
        
        step = 1
        while (not point is None) and Start.AtomEnd != point.AtomStart:
            step = step + 1
            point = point.Next
        
        return point, step
    
    def DeleteNextNode(self, Node):
        current = Node
        next = current.Next
        if next is None:
            return
        current.Next = next.Next
        self.__Number = self.__Number - 1
        return
        
    def InsertNextNode(self, Node, NextNode):
        NextNode.Next = Node.Next
        Node.Next = NextNode
        self.__Number = self.__Number + 1
        return
        
    def InsertNode(self, Node):
        if not isinstance(Node, BiGramWordSegGraphNode):
            raise ValueError("The argument of BiGramWordSegGraphNode.InsertNode must be a BiGramWordSegGraphNode! ")
            
        node = Node
        
        if self.__Head is None:
            self.__Head = node
            self.__Tail = node
            self.__Number = self.__Number + 1
        else:
            point = self.__Head
            nodeAS = node.AtomStart
            nodeAE = node.AtomEnd
            while not point is None:
                pointAS = point.AtomStart
                pointAE = point.AtomEnd
                if nodeAS > pointAS or (nodeAS == pointAS and nodeAE > pointAE):
                    point = point.Next
                else:
                    break
            
            if point is None:
                self.__Tail.Next = node
                self.__Tail = node
                self.__Number = self.__Number + 1
            else:
                if node.Content == WORD_OOV_SPACE and point.Content == WORD_OOV_PERSON:
                    return
                self.ChangeValue(point, node)
                if node.AtomStart > point.AtomStart or (node.AtomStart == point.AtomStart and node.AtomEnd > point.AtomEnd):
                    node.Next = point.Next
                    point.Next = node
                    self.__Tail = node
                    self.__Number = self.__Number + 1
                    
                    
    @property
    def ChangeLinkToList(self):
        ReturnList = []
        
        point = self.__Head
        
        while not point is None:
            node = BiGramWordSegGraphNode()
            node.AtomStart = point.AtomStart
            node.AtomEnd = point.AtomEnd
            node.Content = point.Content
            node.SrcContent = point.SrcContent
            node.POS = point.POS
            node.Frequency = point.Frequency
            node.TagList = point.TagList
            ReturnList.append(node)
            point = point.Next
        return ReturnList
    
    @property
    def RoleString(self):
        ReturnString = ""
        current = self.__Head
        while not current is None:
            """
            print("########## ", current.Content, " ##########")
            for i in current.TagList:
                print("########## ", i.POS, " , ", i.Frequency, " ##########")
                print("########## ", i.PrevIndex, " , ", i.Frequency, " ##########")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            """
            ReturnString = ReturnString + chr(current.BestTag.POS + ord("A"))
            current = current.Next
        return ReturnString
    
#二元切分词图的边
class BiGramWordSegGraphEdge(object):
    
    #边的内容为一个原子序列中相邻两个词的组合，起点为NodeStart, 终点NodeEnd。
    def __init__(self, BGWSGENodeStart=0, BGWSGENodeEnd=0, BGWSGEContent="", BGWSGEPOS=UNSET_POS, BGWSGEWeight=0):
        if isinstance(BGWSGENodeStart, int) and isinstance(BGWSGENodeEnd, int) and isinstance(BGWSGEContent, str) and isinstance(BGWSGEPOS, int) and isinstance(BGWSGEWeight, (float, int)):
            self.__Next = None
            self.__NodeStart = BGWSGENodeStart
            self.__NodeEnd = BGWSGENodeEnd
            self.__Content = BGWSGEContent
            self.__POS = BGWSGEPOS
            self.__Weight = BGWSGEWeight
            self.__Length = len(self.__Content)
        else:
            raise ValueError("BiGramWordSegGraphEdge.__init__ received wrong argument(s) type! ")
    
    @property
    def Next(self):
        return self.__Next
            
    @property
    def NodeStart(self):
        return self.__NodeStart
        
    @property
    def NodeEnd(self):
        return self.__NodeEnd
        
    @property
    def Content(self):
        return self.__Content
        
    @property
    def POS(self):
        return self.__POS
        
    @property
    def Weight(self):
        return self.__Weight
        
    @property
    def Length(self):
        self.__Length = len(self.__Content)
        return self.__Length
        
    @Next.setter
    def Next(self, SetValue):
        if SetValue is None:
            self.__Next = None
        else:
            if not isinstance(SetValue, BiGramWordSegGraphEdge):
                raise ValueError("BiGramWordSegGraphEdge.Next must be a BiGramWordSegGraphEdge! ")
            self.__Next = SetValue
        
    @NodeStart.setter
    def NodeStart(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphEdge.NodeStart must be an Integer! ")
        self.__NodeStart = SetValue
        
    @NodeEnd.setter
    def NodeEnd(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphEdge.NodeEnd must be an Integer! ")
        self.__NodeEnd = SetValue
        
    @Content.setter
    def Content(self, SetValue):
        if not isinstance(SetValue, str):
            raise ValueError("BiGramWordSegGraphEdge.Content must be a String! ")
        self.__Content = SetValue
        self.__Length = len(self.__Content)
        
    @POS.setter
    def POS(self, SetValue):
        if not isinstance(SetValue, int):
            raise ValueError("BiGramWordSegGraphEdge.POS must be an Integer! ")
        self.__POS = SetValue
        
    @Weight.setter
    def Weight(self, SetValue):
        if not isinstance(SetValue, (float, int)):
            raise ValueError("BiGramWordSegGraphEdge.Weight must be an Integer or a Float! ")
        self.__Weight = SetValue
        
    
#二元切分词图的所有边构造的链表
class BiGramWordSegGraphEdgeList(object):
    
    def __init__(self):
        self.__Head = None
        self.__Tail = None
        self.__Number = 0
        
    @property
    def Head(self):
        return self.__Head
    
    @property
    def Tail(self):
        return self.__Tail
    
    @property
    def Number(self):
        return self.__Number

    def ChangeValue(self, aValue, bValue):
        if not (isinstance(aValue, BiGramWordSegGraphEdge) and isinstance(bValue, BiGramWordSegGraphEdge)):
            raise ValueError("The arguments of the BiGramWordSegGraphEdge.ChangeValue must be a WordSegGraphEdge! ")
        aValue.NodeStart, bValue.NodeStart = bValue.NodeStart, aValue.NodeStart
        aValue.NodeEnd, bValue.NodeEnd = bValue.NodeEnd, aValue.NodeEnd
        aValue.Content, bValue.Content = bValue.Content, aValue.Content
        aValue.POS, bValue.POS = bValue.POS, aValue.POS
        aValue.Weight, bValue.Weight = bValue.Weight, aValue.Weight

    def FindFirstEdgeByEndNum(self, EdgeEndNum):
        edge = self.__Head
        while (not edge is None) and edge.NodeEnd != EdgeEndNum:
            edge = edge.Next
        return edge

    def InsertEdge(self, Edge):
        if not isinstance(Edge, BiGramWordSegGraphEdge):
            raise ValueError("The argument of BiGramWordSegGraphEdge.InsertEdge must be a BiGramWordSegGraphEdge! ")
            
        edge = Edge
        if self.__Head is None:
            self.__Head = edge
            self.__Tail = edge
            self.__Number = self.__Number + 1
        else:
            point = self.__Head
            edgeNS = edge.NodeStart
            edgeNE = edge.NodeEnd
            while not point is None:
                pointNS = point.NodeStart
                pointNE = point.NodeEnd
                if edgeNE > pointNE or (edgeNE == pointNE and edgeNS > pointNS):
                    point = point.Next
                else:
                    break
            
            if point is None:
                self.__Tail.Next = edge
                self.__Tail = edge
                self.__Number = self.__Number + 1
            else:
                self.ChangeValue(point, edge)
                if edge.NodeEnd > point.NodeEnd or (edge.NodeEnd == point.NodeEnd and edge.NodeStart > point.NodeStart):
                    edge.Next = point.Next
                    point.Next = edge
                    self.__Tail = edge
                    self.__Number = self.__Number + 1
                    
class BiGramWordSegGraph(object):
    
    def __init__(self, BGWSGNodeList, BGWSGEdgeList):
        if isinstance(BGWSGNodeList, BiGramWordSegGraphNodeList) and isinstance(BGWSGEdgeList, BiGramWordSegGraphEdgeList):
            self.__NodeList = BGWSGNodeList
            self.__EdgeList = BGWSGEdgeList
        else:
            raise ValueError("BiGramWordSegGraph.__init__ received wrong argument(s) type! ")
        
    @property
    def NodeList(self):
        return self.__NodeList
    
    @property
    def EdgeList(self):
        return self.__EdgeList
    
    @property
    def NodesNumber(self):
        return self.__NodeList.Number
    
    @property
    def EdgesNumber(self):
        return self.__EdgeList.Number
    
class NKindShortestNodeList(object):
    
    def __init__(self):
        self.__Distance = INFINITE_DIST
        self.__ParentNodesStack = []
        self.__Point = 0
    
    @property
    def Distance(self):
        return self.__Distance
        
    @property
    def ParentNodesStack(self):
        return self.__ParentNodesStack
        
    @property
    def Top(self):
        if len(self.__ParentNodesStack) == 0:
            return None
        self.__Point = 0
        return self.__ParentNodesStack[self.__Point]
        
    @property
    def Pop(self):
        if len(self.__ParentNodesStack) == 0:
            return None
        if self.__Point + 1 == len(self.__ParentNodesStack):
            return None
        self.__Point = self.__Point + 1
        return self.__ParentNodesStack[self.__Point]
        
    @property
    def TouchTheBottom(self):
        if len(self.__ParentNodesStack) == 0:
            return None
        if self.__Point == len(self.__ParentNodesStack) - 1:
            return True
        else:
            return False
        
    @Distance.setter
    def Distance(self, SetValue):
        if not isinstance(SetValue, (float, int)):
            raise ValueError("NKindShortestNodeList.Distance must be an Integer or a Float! ")
        self.__Distance = SetValue
        
    @ParentNodesStack.setter
    def ParentNodesStack(self, SetValue):
        if not isinstance(SetValue, list):
            raise ValueError("NKindShortestNodeList.ParentNodesStack must be a List! ")
        
        self.__ParentNodesStack = SetValue
        
