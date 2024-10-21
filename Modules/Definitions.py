#!/usr/bin/env python

import os

class Canstants(object):
    
    @property
    def TT_PERSON(self):
        ReturnValue = "PERSON"
        return ReturnValue
        
    @property
    def TT_PLACE(self):
        ReturnValue = "PLACE"
        return ReturnValue
        
    @property
    def TT_FOREIGN(self):
        ReturnValue = "FOREIGN"
        return ReturnValue

    @property
    def TAGGING_TYPE(self):
        ReturnValue = {self.TT_PERSON, self.TT_PLACE, self.TT_FOREIGN}

    @property
    def DICT_PATH(self):
        ReturnValue = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data")
        return ReturnValue

    @property
    def WI_COUNT(self):
        ReturnValue = 6768
        return ReturnValue
        
    @property
    def DELIMITER_INDEX(self):
        ReturnValue = 3755
        return ReturnValue
        
    @property
    def SEN_BEGIN(self):
        ReturnValue = "始##始"#"[-!-BEGIN-!-]"
        return ReturnValue
        
    @property
    def SEN_END(self):
        ReturnValue = "末##末"#"[-!-END-!-]"
        return ReturnValue
        
    @property
    def WORD_OOV_PERSON(self):
        ReturnValue = "未##人"#"[-!-PERSON-!-]"
        return ReturnValue
        
    @property
    def WORD_OOV_SPACE(self):
        ReturnValue = "未##地"#"[-!-SPACE-!-]"
        return ReturnValue
        
    @property
    def WORD_OOV_NUM(self):
        ReturnValue = "未##数"#"[-!-NUM-!-]"
        return ReturnValue
        
    @property
    def WORD_OOV_TIME(self):
        ReturnValue = "未##时"#"[-!-TIME-!-]"
        return ReturnValue
        
    @property
    def WORD_OOV_LETTER(self):
        ReturnValue = "未##串"#"[-!-LETTER-!-]"
        return ReturnValue
                
    @property
    def WORD_CONNECTOR(self):
        ReturnValue = "@"#"[-!-]"
        return ReturnValue
        
    @property
    def CN_SEN_SEP(self):
        ReturnValue = "。！？：；…"
        return ReturnValue
        
    @property
    def EN_SEN_SEP(self):
        ReturnValue = "!?:;"
        return ReturnValue
        
    @property
    def CN_SUB_SEN_SEP(self):
        ReturnValue = "、，（）“”‘’"
        return ReturnValue
        
    @property
    def EN_SUB_SEN_SEP(self):
        ReturnValue = ",()\"'"
        return ReturnValue

    @property
    def BLANK_SEP(self):
        ReturnValue = "\n\r 　"
        return ReturnValue

    @property
    def MAX_FREQUENCY(self):
        ReturnValue = 2079997
        return ReturnValue

    @property
    def INFINITE_DIST(self):
        ReturnValue = 10000
        return ReturnValue

    @property
    def CT_CN_NUMBER(self):
        ReturnValue = 0xCB      #取 Chinese numBer 缩写 CB 作为十六进制值，因为 n, u 不再十六进制内
        return ReturnValue

    @property
    def CT_CN_CHARACTER(self):
        ReturnValue = 0xCC      #取 Chinese Character 缩写 CC 作为十六进制值
        return ReturnValue

    @property
    def CT_CN_DELIMITER(self):
        ReturnValue = 0xCD      #取 Chinese Delimiter 缩写 CD 作为十六进制值
        return ReturnValue

    @property
    def CT_CN_LETTER(self):
        ReturnValue = 0xCE      #取 Chinese lEtter 缩写 CE 作为十六进制值，因为 l 不再十六进制内
        return ReturnValue

    @property
    def CT_EN_NUMBER(self):
        ReturnValue = 0xEB      #取 English numBer 缩写 EB 作为十六进制值，因为 n, u 不再十六进制内
        return ReturnValue

    @property
    def CT_EN_DELIMITER(self):
        ReturnValue = 0xED      #取 English Delimiter 缩写 ED 作为十六进制值
        return ReturnValue

    @property
    def CT_EN_LETTER(self):
        ReturnValue = 0xEE      #取 English lEtter 缩写 EE 作为十六进制值，因为 l 不再十六进制内
        return ReturnValue

    @property
    def CT_SINGLE(self):
        ReturnValue = 0xE1      #取 singlE 的字母 E 和数字 1 作为十六进制值，数字 1 代表"独立"的含义
        return ReturnValue

    @property
    def CT_UNCLEAR(self):
        ReturnValue = 0x00      #取数字 00 作为十六进制值，代表内容没有确定的含义
        return ReturnValue

    @property
    def CT_CN_INDEX(self):
        ReturnValue = 0x0D      #取数字 0 和 inDex 的字母 D 作为十六进制值，数字 0 代表"数字索引"的含义
        return ReturnValue

    @property
    def CT_NUMBER(self):
        ReturnValue = 0xB0      #取 numBer 的字母 B 和数字 0 作为十六进制值，数字 0 代表"数字"的含义
        return ReturnValue

    @property
    def CT_LETTER(self):
        ReturnValue = 0xEA      #取 lEtter 的字母 E 和字母 A 作为十六进制值，字母 A 代表"字母"的含义
        return ReturnValue

    @property
    def CT_MIX(self):
        ReturnValue = 0xA0      #字母 A 和数字 0 作为十六进制值，代表数字和字母混合的含义
        return ReturnValue

canstants = Canstants()

TAGGING_TYPE = canstants.TAGGING_TYPE
TT_PERSON = canstants.TT_PERSON
TT_PLACE = canstants.TT_PLACE
TT_FOREIGN = canstants.TT_FOREIGN

MAX_FREQUENCY = canstants.MAX_FREQUENCY
INFINITE_DIST = canstants.INFINITE_DIST

DICT_PATH = canstants.DICT_PATH #Dictionary Path
WI_COUNT = canstants.WI_COUNT #Word Index Count
DELIMITER_INDEX = canstants.DELIMITER_INDEX #Index in the Dict lead the Delimiter

SEN_BEGIN = canstants.SEN_BEGIN #Sentence Begin
SEN_END = canstants.SEN_END #Sentence End
WORD_OOV_PERSON = canstants.WORD_OOV_PERSON #   OP  未登录人名  
WORD_OOV_SPACE = canstants.WORD_OOV_SPACE   #   OS  未登录地名
WORD_OOV_NUM = canstants.WORD_OOV_NUM       #   ON  未登录数词
WORD_OOV_TIME = canstants.WORD_OOV_TIME     #   OT  未登录时间
WORD_OOV_LETTER = canstants.WORD_OOV_LETTER #   OL  未登录字串
WORD_CONNECTOR = canstants.WORD_CONNECTOR    #   两个词的连接符

CN_SEN_SEP = canstants.CN_SEN_SEP #Chinese Sentence Seperator
EN_SEN_SEP = canstants.EN_SEN_SEP #English Sentence Seperator
CN_SUB_SEN_SEP = canstants.CN_SUB_SEN_SEP #Chinese Sub Sentence Seperator
EN_SUB_SEN_SEP = canstants.EN_SUB_SEN_SEP #English Sub Sentence Seperator
BLANK_SEP = canstants.BLANK_SEP #Seperator \n, \r, half-width space, full-width space

CT_SINGLE = canstants.CT_SINGLE
CT_UNCLEAR = canstants.CT_UNCLEAR
#CT_MIX = canstants.CT_MIX
#CT_NUMBER = canstants.CT_NUMBER
#CT_LETTER = canstants.CT_LETTER

#CT_CN_NUMBER = canstants.CT_CN_NUMBER
#CT_EN_NUMBER = canstants.CT_EN_NUMBER
#CT_CN_LETTER = canstants.CT_CN_LETTER
#CT_EN_LETTER = canstants.CT_EN_LETTER
CT_CN_DELIMITER = canstants.CT_CN_DELIMITER
CT_EN_DELIMITER = canstants.CT_EN_DELIMITER

CT_CN_INDEX = canstants.CT_CN_INDEX
CT_CN_CHARACTER = canstants.CT_CN_CHARACTER

class POSTags(object):

    @property
    def SEN_BEGIN_POS(self):
        ReturnValue = 1#( ord('S')<<8 ) + ord('B')    #SB     句子的开始标记[-!-BEGIN-!-]
        return ReturnValue
        
    @property
    def SEN_END_POS(self):
        ReturnValue = 4#( ord('S')<<8 ) + ord('E')    #SE     句子的结束标记[-!-END-!-]
        return ReturnValue
       
    @property
    def UNSET_POS(self):
        ReturnValue = 0#( ord('U')<<8 ) + ord('P')    #UP     词性尚未确定
        return ReturnValue        

    @property
    def OOV(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('V')    #OV     未登录词
        return ReturnValue
        
    @property
    def OOV_PERSON(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('P')    #OP     未登录人名
        return ReturnValue
        
    @property
    def OOV_SPACE(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('S')    #OS     未登录地名
        return ReturnValue
        
    @property
    def OOV_NUM(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('N')    #ON     未登录数词
        return ReturnValue
        
    @property
    def OOV_TIME(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('T')    #OT     未登录时间
        return ReturnValue
        
    @property
    def OOV_LETTER(self):
        ReturnValue = 2#( ord('O')<<8 ) + ord('L')    #OL     未登录字串
        return ReturnValue
        
    @property
    def BIGRAM_POS(self):
        ReturnValue = 3#( ord('B')<<8 ) + ord('P')    #BP     二元词语词性
        return ReturnValue
        
    @property
    def LETTER_BLOCK(self):
        ReturnValue = ( ord('n')<<8 ) + ord('x')    #nx     英文或英文数字字符串
        return ReturnValue
        
    @property
    def PUNC(self):
        ReturnValue = ( ord('w')<<8 )               #w      标点符号
        return ReturnValue
        
    @property
    def ADJ(self):
        ReturnValue = ( ord('a')<<8 )               #a      形容词
        return ReturnValue
        
    @property
    def ADV(self):
        ReturnValue = ( ord('d')<<8 )               #d      副词
        return ReturnValue
        
    @property
    def NOUN(self):
        ReturnValue = ( ord('n')<<8 )               #n      名词
        return ReturnValue
        
    @property
    def VERB(self):
        ReturnValue = ( ord('v')<<8 )               #v      动词
        return ReturnValue
        
    @property
    def TIME(self):
        ReturnValue = ( ord('t')<<8 )               #t      时间词
        return ReturnValue
        
    @property
    def GEN(self):
        ReturnValue = ( ord('g')<<8 )               #g      语素
        return ReturnValue
        
    @property
    def SPACE(self):
        ReturnValue = ( ord('s')<<8 )               #s      处所词
        return ReturnValue
        
    @property
    def CONJ(self):
        ReturnValue = ( ord('c')<<8 )               #c      连词
        return ReturnValue
        
    @property
    def EXC(self):
        ReturnValue = ( ord('e')<<8 )               #e      叹词
        return ReturnValue
        
    @property
    def NUM(self):
        ReturnValue = ( ord('m')<<8 )               #m      叹词
        return ReturnValue
        
    @property
    def ONOM(self):
        ReturnValue = ( ord('o')<<8 )               #o      拟声词
        return ReturnValue
        
    @property
    def PREP(self):
        ReturnValue = ( ord('p')<<8 )               #p      介词
        return ReturnValue
        
    @property
    def QUAN(self):
        ReturnValue = ( ord('q')<<8 )               #q      量词
        return ReturnValue
        
    @property
    def PRONOUN(self):
        ReturnValue = ( ord('r')<<8 )               #r      代词
        return ReturnValue
        
    @property
    def AUXI(self):
        ReturnValue = ( ord('u')<<8 )               #u      助词
        return ReturnValue
        
    @property
    def IDIOM(self):
        ReturnValue = ( ord('i')<<8 )               #i      成语
        return ReturnValue
        
    @property
    def HEAD(self):
        ReturnValue = ( ord('h')<<8 )               #h      前接成分
        return ReturnValue
        
    @property
    def TAIL(self):
        ReturnValue = ( ord('t')<<8 )               #t      后接成分
        return ReturnValue

    @property
    def YUQI(self):
        ReturnValue = ( ord('y')<<8 )               #y      语气词
        return ReturnValue

    @property
    def ZHUANG(self):
        ReturnValue = ( ord('z')<<8 )               #z      状态词
        return ReturnValue

    @property
    def BIE(self):
        ReturnValue = ( ord('b')<<8 )               #b      区别词
        return ReturnValue

    @property
    def FANG(self):
        ReturnValue = ( ord('f')<<8 )               #f      方位词
        return ReturnValue

    @property
    def JIAN(self):
        ReturnValue = ( ord('j')<<8 )               #j      简称略语
        return ReturnValue

    @property
    def TEMP(self):
        ReturnValue = ( ord('l')<<8 )               #l      习用语
        return ReturnValue

    @property
    def ADJ_ADV(self):
        ReturnValue = ( ord('a')<<8 ) + ord('d')    #ad     副形词
        return ReturnValue

    @property
    def ADJ_NOUN(self):
        ReturnValue = ( ord('a')<<8 ) + ord('n')    #an     名形词
        return ReturnValue

    @property
    def ADJ_GEN(self):
        ReturnValue = ( ord('a')<<8 ) + ord('g')    #ag     形语素
        return ReturnValue

    @property
    def ADV_GEN(self):
        ReturnValue = ( ord('d')<<8 ) + ord('g')    #dg     副语素
        return ReturnValue

    @property
    def NOUN_GEN(self):
        ReturnValue = ( ord('n')<<8 ) + ord('g')    #ng     名语素
        return ReturnValue

    @property
    def VERB_GEN(self):
        ReturnValue = ( ord('v')<<8 ) + ord('g')    #vg     动语素
        return ReturnValue

    @property
    def TIME_GEN(self):
        ReturnValue = ( ord('t')<<8 ) + ord('g')    #tg     时语素
        return ReturnValue

    @property
    def NOT_GEN(self):
        ReturnValue = ( ord('x')<<8 )               #x      非语素字
        return ReturnValue

    @property
    def NOUN_PERSON(self):#     UP      词性尚未确定    取英文 Unset POS 缩写 UP 两个字母 
        ReturnValue = ( ord('n')<<8 ) + ord('r')    #nr     人名
        return ReturnValue

    @property
    def NOUN_SPACE(self):
        ReturnValue = ( ord('n')<<8 ) + ord('s')    #ns     地名
        return ReturnValue

    @property
    def NOUN_ORG(self):
        ReturnValue = ( ord('n')<<8 ) + ord('t')    #nt     机构团体
        return ReturnValue

    @property
    def NOUN_ZHUAN(self):
        ReturnValue = ( ord('n')<<8 ) + ord('z')    #nz     其他专名
        return ReturnValue

    @property
    def VERB_ADV(self):
        ReturnValue = ( ord('v')<<8 ) + ord('d')    #vd     副动词
        return ReturnValue

    @property
    def VERB_NOUN(self):
        ReturnValue = ( ord('v')<<8 ) + ord('n')    #vn     名动词
        return ReturnValue        

    @property
    def YUQI_GEN(self):
        ReturnValue = ( ord('y')<<8 ) + ord('g')    #yg     语气语素
        return ReturnValue
        
    @property
    def AUXI_GEN(self):
        ReturnValue = ( ord('u')<<8 ) + ord('g')    #ug     助语素
        return ReturnValue

    @property
    def PRONOUN_GEN(self):
        ReturnValue = ( ord('r')<<8 ) + ord('g')    #rg     代语素
        return ReturnValue

    @property
    def QUAN_GEN(self):
        ReturnValue = ( ord('q')<<8 ) + ord('g')    #qg     量语素
        return ReturnValue
        
    @property
    def NUM_GEN(self):
        ReturnValue = ( ord('m')<<8 ) + ord('g')    #mg     数语素
        return ReturnValue
        
    @property
    def BIE_GEN(self):
        ReturnValue = ( ord('b')<<8 ) + ord('g')    #bg     区别语素
        return ReturnValue
        
    @property
    def NOUN_GEN(self):
        ReturnValue = ( ord('n')<<8 ) + ord('g')    #ng     名语素
        return ReturnValue
        
    @property
    def U_J(self):
        ReturnValue = ( ord('u')<<8 ) + ord('j')    #uj     结构助词的
        return ReturnValue
        
    @property
    def U_L(self):
        ReturnValue = ( ord('u')<<8 ) + ord('l')    #ul     时态助词了
        return ReturnValue
        
    @property
    def U_V(self):
        ReturnValue = ( ord('u')<<8 ) + ord('v')    #uv     结构助词地
        return ReturnValue
        
    @property
    def U_Z(self):
        ReturnValue = ( ord('u')<<8 ) + ord('z')    #uz     时态助词着
        return ReturnValue
        
    @property
    def U_G(self):
        ReturnValue = ( ord('u')<<8 ) + ord('g')    #ug     时态助词
        return ReturnValue
        
    @property
    def U_D(self):
        ReturnValue = ( ord('u')<<8 ) + ord('d')    #ud     结构助词
        return ReturnValue
        
    @property
    def HOUJIE(self):
        ReturnValue = ( ord('k')<<8 )               #k      后接成分
        return ReturnValue

    @property
    def MAP_POS(self):
        ReturnValue = dict(
            a="形容词",
            ad="副形词",
            an="名形词",
            ag="形语素",
            b="区别词",
            bg="区别语素",
            c="连词",
            cc="单字",
            d="副词",
            dg="副语素",
            e="叹词",
            f="方位词",
            g="语素",#无
            h="前接成分",
            i="成语",#无
            j="简称略语",
            k="后接成分",
            l="习用语",
            m="数词",
            mg="数语素",
            n="名词",
            ng="名语素",
            nr="人名",
            ns="地名",
            nt="机构团体",
            nx="外文字符串",
            nz="其他专名",
            o="拟声词",
            p="介词",
            q="量词",
            qg="量语素",#无
            r="代词",
            rg="代语素",
            s="处所词",
            t="时间词",
            tg="时语素",
            u="助词",
            ud="结构助词",
            ug="时态助词",
            #ug="助语素",
            uj="结构助词-\"的\"",
            ul="时态助词-\"了\"",
            uv="结构助词-\"地\"",
            uz="时态助词-\"着\"",
            v="动词",
            vd="副动词",
            vg="动语素",
            vn="名动词",
            w="标点符号",#无
            x="非语素字",
            y="语气词",
            yg="语气语素",
            z="状态词",
        )
        return ReturnValue
        
    @property
    def MAP_COLOR(self):
        ReturnValue = dict(
            a="Blue",
            ad="BlueViolet",
            an="BurlyWood",
            ag="Chocolate",
            b="CornflowerBlue",
            bg="DarkGoldenRod",
            c="DarkGreen",
            cc="Black",
            d="DarkOliveGreen",
            dg="DarkRed",
            e="DarkSalmon",
            f="DarkViolet",
            g="ForestGreen",#无
            h="GoldenRod",
            i="Indigo",#无
            j="HotPink",
            k="MediumVioletRed",
            l="OrangeRed",
            m="Purple",
            mg="Teal",
            n="Tomato",
            ng="Turquoise",
            nr="Crimson",
            ns="CornflowerBlue",
            nt="DarkKhaki",
            nx="DodgerBlue",
            nz="Black",
            o="DimGrey",
            p="DeepSkyBlue",
            q="Fuchsia",
            qg="GoldenRod",#无
            r="Gray",
            rg="IndianRed",
            s="Maroon",
            t="MidnightBlue",
            tg="Navy",
            u="Olive",
            ud="Purple",
            ug="SaddleBrown",
            #ug="助语素",
            uj="DarkCyan",
            ul="Teal",
            uv="SteelBlue",
            uz="SlateGray",
            v="YellowGreen",
            vd="Sienna",
            vg="OliveDrab",
            vn="MediumSlateBlue",
            w="MediumPurple",#无
            x="MediumOrchid",
            y="MediumBlue",
            yg="Magenta",
            z="LimeGreen",
        )
        return ReturnValue


postags = POSTags()
MAP_POS = postags.MAP_POS
MAP_COLOR = postags.MAP_COLOR
SEN_BEGIN_POS = postags.SEN_BEGIN_POS   #     SB      句子的开始标记[-!-BEGIN-!-]    取英文 Sentence Begin 缩写 SB 两个字母 
SEN_END_POS = postags.SEN_END_POS       #     SE      句子的开始标记[-!-END-!-]    取英文 Sentence End 缩写 SE 两个字母 

UNSET_POS = postags.UNSET_POS           #     UP      词性尚未确定    取英文 Unset POS 缩写 UP 两个字母 

OOV = postags.OOV               #   OV  未登录词    不可识别词及用户自定义词组。取英文 Out-of-Vocabulary 缩写OOV的后两个字母。
OOV_PERSON = postags.OOV_PERSON #   OP  未登录人名  
OOV_SPACE = postags.OOV_SPACE   #   OS  未登录地名
OOV_NUM = postags.OOV_NUM       #   ON  未登录数词
OOV_TIME = postags.OOV_TIME     #   OT  未登录时间
OOV_LETTER = postags.OOV_LETTER #   OL  未登录字串
BIGRAM_POS = postags.BIGRAM_POS #   BP  二元词语词性

PUNC = postags.PUNC             #   w   标点符号

ADJ = postags.ADJ               #   a   形容词     取英语形容词 adjective 的第 1 个字母。
ADV = postags.ADV               #   d   副词      取 adverb 的第 2 个字母，因其第 1 个字母已用于形容词。
NOUN = postags.NOUN             #   n   名词      取英语名词 noun 的第 1 个字母。
VERB = postags.VERB             #   v   动词      取英语动词 verb 的第 1 个字母。
TIME = postags.TIME             #   t   时间词     取英语 time 的第 1 个字母。
GEN = postags.GEN               #   g   语素      绝大多数语素都能作为合成词的"词根"，取汉字"根(gen)"的声母。

SPACE = postags.SPACE           #   s   处所词     取英语 space 的第 1 个字母。
CONJ = postags.CONJ             #   c   连词      取英语连词 conjunction 的第 1 个字母。
EXC = postags.EXC               #   e   叹词      取英语叹词 exclamation 的第 1 个字母。
NUM = postags.NUM               #   m   数词      取英语 numeral 的第 3 个字母, n, u 已有他用。
ONOM = postags.ONOM             #   o   拟声词     取英语拟声词 onomatopoeia 的第 1 个字母。
PREP = postags.PREP             #   p   介词      取英语介词 prepositional 的第 1 个字母。
QUAN = postags.QUAN             #   q   量词      取英语 quantity 的第 1 个字母。
PRONOUN = postags.PRONOUN       #   r   代词      取英语代词 pronoun 的第 2 个字母, 因 p 已用于介词。
AUXI = postags.AUXI             #   u   助词      取英语助词 auxiliary 的第 2 个字母,因 a 已用于形容词。

IDIOM = postags.IDIOM           #   i   成语      取英语成语 idiom 的第 1 个字母。
HEAD = postags.HEAD             #   h   前接成分    取英语 head 的第 1 个字母。
TAIL = postags.TAIL             #   k   后接成分

YUQI = postags.YUQI             #   y   语气词     取汉字"语(yu)"的声母的第 1 个字母。
ZHUANG = postags.ZHUANG         #   z   状态词     取汉字"状(zhuang)"的声母的第 1 个字母。
BIE = postags.BIE               #   b   区别词     取汉字"别(bie)"的声母的第 1 个字母。
FANG = postags.FANG             #   f   方位词     取汉字"方(fang)"的声母的第 1 个字母。
JIAN = postags.JIAN             #   j   简称略语    取汉字"简(jian)"的声母的第 1 个字母。
TEMP = postags.TEMP             #   l   习用语     习用语尚未成为成语，有点"临时性"，取"临(lin)"的声母第 1 个字母。

ADJ_ADV = postags.ADJ_ADV       #   ad  副形词     直接作状语的形容词。形容词代码 a 和副词代码 d 并在一起。
ADJ_NOUN = postags.ADJ_NOUN     #   an  名形词     具有名词功能的形容词。形容词代码 a 和名词代码 n 并在一起。

ADJ_GEN = postags.ADJ_GEN       #   ag  形语素     形容词性语素。形容词代码为 a，语素代码 g 前面置以 A。
ADV_GEN = postags.ADV_GEN       #   dg  副语素     副词性语素。副词代码为 d，语素代码 g 前面置以 D。
NOUN_GEN = postags.NOUN_GEN     #   ng  名语素     名词性语素。名词代码为 n，语素代码 g 前面置以 N。
VERB_GEN = postags.VERB_GEN     #   vg  动语素     动词性语素。动词代码为 v, 语素代码 g 前面置以 V。
TIME_GEN = postags.TIME_GEN     #   tg  时语素     时间词性语素。时间词代码为 t, 语素代码 g 前面置以 T。
YUQI_GEN = postags.YUQI_GEN     #   yg  语气语素
AUXI_GEN = postags.AUXI_GEN     #   ug  助语素
PRONOUN_GEN = postags.PRONOUN_GEN  #   rg  代语素
QUAN_GEN = postags.QUAN_GEN  #qg     量语素
NUM_GEN = postags.NUM_GEN  #mg     数语素
BIE_GEN = postags.BIE_GEN  #bg     区别语素
U_J = postags.U_J  #uj     结构助词的
U_L = postags.U_L  #ul     时态助词了
U_V = postags.U_V  #uv     结构助词地
U_Z = postags.U_Z  #uz     时态助词着
U_G = postags.U_G  #ug     时态助词
U_D = postags.U_D  #ud     结构助词
HOUJIE = postags.HOUJIE  #k      后接成分
LETTER_BLOCK = postags.LETTER_BLOCK     #     nx      英文或英文数字字符串 取英文 Letter Block 缩写 LB 两个字母。


NOT_GEN = postags.NOT_GEN       #   x   非语素字    非语素字只是一个符号，字母 x 通常用于代表未知数、符 号。

NOUN_PERSON = postags.NOUN_PERSON   #   nr  人名      名词代码 n 和"人(ren)"的声母 r 并在一起。
NOUN_SPACE = postags.NOUN_SPACE     #   ns  地名      名词代码 n 和处所词代码 s 并在一起。
NOUN_ORG = postags.NOUN_ORG         #   nt  机构团体   名词代码 n 和"团(tuan)"的声母 t 并在一起。
NOUN_ZHUAN = postags.NOUN_ZHUAN     #   nz  其他专名   名词代码 n 和"专(zhuan)"的声母的第 1 个字母 z 并在一起。

VERB_ADV = postags.VERB_ADV         #   vd  副动词     直接作状语的动词。动词和副词的代码并在一起。
VERB_NOUN = postags.VERB_NOUN       #   vn  名动词     具有名词功能的动词。动词和名词的代码并在一起。


class Person(object):
    
    @property
    def PATTERNS(self):
        ReturnValue = [ "BBCD", "BBC", "BBE", "BBZ", "BCD", "BEE", "BE", "BG", "BXD", "BZ", "CDCD", "CD", "EE", "FB", "Y", "XD" ]
        return ReturnValue
       
    @property
    def FACTORS(self):
        ReturnValue = [ 0.003606, 0.000021, 0.001314, 0.000315, 0.656624, 0.000021, 0.146116, 0.009136, 0.000042, 0.038971, 0, 0.090367, 0.000273, 0.009157, 0.034324, 0.009735, 0 ]
        return ReturnValue
        
    @property
    def LITTLE_FREQUENCY(self):
        ReturnValue = 6
        return ReturnValue
        
    @property
    def TRANS_ENGLISH(self):
        ReturnValue = "·—阿埃艾爱安昂敖奥澳笆芭巴白拜班邦保堡鲍北贝本比毕彼别波玻博勃伯泊卜布才采仓查差柴彻川茨慈次达大戴代丹旦但当道德得的登迪狄蒂帝丁东杜敦多额俄厄鄂恩尔伐法范菲芬费佛夫福弗甫噶盖干冈哥戈革葛格各根古瓜哈海罕翰汗汉豪合河赫亨侯呼胡华霍基吉及加贾坚简杰金京久居君喀卡凯坎康考柯科可克肯库奎拉喇莱来兰郎朗劳勒雷累楞黎理李里莉丽历利立力连廉良列烈林隆卢虏鲁路伦仑罗洛玛马买麦迈曼茅茂梅门蒙盟米蜜密敏明摩莫墨默姆木穆那娜纳乃奈南内尼年涅宁纽努诺欧帕潘畔庞培佩彭皮平泼普其契恰强乔切钦沁泉让热荣肉儒瑞若萨塞赛桑瑟森莎沙山善绍舍圣施诗石什史士守斯司丝苏素索塔泰坦汤唐陶特提汀图土吐托陀瓦万王旺威韦维魏温文翁沃乌吾武伍西锡希喜夏相香歇谢辛新牙雅亚彦尧叶依伊衣宜义因音英雍尤于约宰泽增詹珍治中仲朱诸卓孜祖佐伽娅尕腓滕济嘉津赖莲琳律略慕妮聂裴浦奇齐琴茹珊卫欣逊札哲智兹芙汶迦珀琪梵斐胥黛"
        return ReturnValue
        
    @property
    def TRANS_RUSSIAN(self):
        ReturnValue = "·阿安奥巴比彼波布察茨大德得丁杜尔法夫伏甫盖格哈基加坚捷金卡科可克库拉莱兰勒雷里历利连列卢鲁罗洛马梅蒙米姆娜涅宁诺帕泼普奇齐乔切日萨色山申什斯索塔坦特托娃维文乌西希谢亚耶叶依伊以扎佐柴达登蒂戈果海赫华霍吉季津柯理琳玛曼穆纳尼契钦丘桑沙舍泰图瓦万雅卓兹"
        return ReturnValue
        
    @property
    def TRANS_JAPANIESE(self):
        ReturnValue = "安奥八白百邦保北倍本比滨博步部彩菜仓昌长朝池赤川船淳次村大代岛稻道德地典渡尔繁饭风福冈高工宫古谷关广桂贵好浩和合河黑横恒宏后户荒绘吉纪佳加见健江介金今进井静敬靖久酒菊俊康可克口梨理里礼栗丽利立凉良林玲铃柳隆鹿麻玛美萌弥敏木纳南男内鸟宁朋片平崎齐千前浅桥琴青清庆秋丘曲泉仁忍日荣若三森纱杉山善上伸神圣石实矢世市室水顺司松泰桃藤天田土万望尾未文武五舞西细夏宪相小孝新星行雄秀雅亚岩杨洋阳遥野也叶一伊衣逸义益樱永由有佑宇羽郁渊元垣原远月悦早造则泽增扎宅章昭沼真政枝知之植智治中忠仲竹助椎子佐阪坂堀荻菅薰浜濑鸠筱"
        return ReturnValue
        
        
person = Person()
PATTERNS = person.PATTERNS
FACTORS = person.FACTORS
LITTLE_FREQUENCY = person.LITTLE_FREQUENCY
TRANS_ENGLISH = person.TRANS_ENGLISH
TRANS_RUSSIAN = person.TRANS_RUSSIAN
TRANS_JAPANIESE = person.TRANS_JAPANIESE