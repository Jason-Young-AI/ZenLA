#!/usr/bin/env python

import struct
import re

from Modules.Definitions import *

class Utilities(object):

    def ReadInteger(self, DictFile):
        
        ByteStr = DictFile.read(4)
        (Result, ) = struct.unpack("<I", ByteStr)
        
        return Result
    
    def ReadChineseWord(self, DictFile, ByteStrLength):
        
        ByteStr = DictFile.read(ByteStrLength)
        Result = ByteStr.decode("GBK")
        
        return Result
        
    def isSentenceSeperator(self, Char):
        
        if Char in CN_SEN_SEP:
            return True
        if Char in EN_SEN_SEP:
            return True
        if Char in CN_SUB_SEN_SEP:
            return True
        if Char in EN_SUB_SEN_SEP:
            return True
        if Char in BLANK_SEP:
            return True
        
        return False


    ##############################################################################
    ##############################################################################
    ##############################################################################、

    ###匹配中文的正则，一般用 [ \u4e00-\u9fa5 ]+ 即可搞定。
    ###不过这正则对一般的火星文鸟语就不太适用了，甚至全角的标点符号都不包含在内。
    ###其实，大部分网络上的鸟语都取自“中日韩统一表意文字（CJK Unified Ideographs）”，外加一些特殊的字符；
    ###所以，用 [ \u2E80-\uFE4F ]+ 基本上就可以都涵盖了。

    ###根据Unicode5.0整理如下：

    ###1）标准CJK文字

    ###http://www.unicode.org/Public/UNIDATA/Unihan.html

    ###2）全角ASCII、全角中英文标点、半宽片假名、半宽平假名、半宽韩文字母：FF00-FFEF

    ###http://www.unicode.org/charts/PDF/UFF00.pdf

    ###3）CJK部首补充：2E80-2EFF

    ###http://www.unicode.org/charts/PDF/U2E80.pdf

    ###4）CJK标点符号：3000-303F

    ###http://www.unicode.org/charts/PDF/U3000.pdf

    ###5）CJK笔划：31C0-31EF

    ###http://www.unicode.org/charts/PDF/U31C0.pdf

    ###6）康熙部首：2F00-2FDF

    ###http://www.unicode.org/charts/PDF/U2F00.pdf

    ###7）汉字结构描述字符：2FF0-2FFF

    ###http://www.unicode.org/charts/PDF/U2FF0.pdf

    ###8）注音符号：3100-312F

    ###http://www.unicode.org/charts/PDF/U3100.pdf

    ###9）注音符号（闽南语、客家语扩展）：31A0-31BF

    ###http://www.unicode.org/charts/PDF/U31A0.pdf

    ###10）日文平假名：3040-309F

    ###http://www.unicode.org/charts/PDF/U3040.pdf

    ###11）日文片假名：30A0-30FF

    ###http://www.unicode.org/charts/PDF/U30A0.pdf

    ###12）日文片假名拼音扩展：31F0-31FF

    ###http://www.unicode.org/charts/PDF/U31F0.pdf

    ###13）韩文拼音：AC00-D7AF

    ###http://www.unicode.org/charts/PDF/UAC00.pdf

    ###14）韩文字母：1100-11FF

    ###http://www.unicode.org/charts/PDF/U1100.pdf

    ###15）韩文兼容字母：3130-318F

    ###http://www.unicode.org/charts/PDF/U3130.pdf

    ###16）太玄经符号：1D300-1D35F

    ###http://www.unicode.org/charts/PDF/U1D300.pdf

    ###17）易经六十四卦象：4DC0-4DFF

    ###http://www.unicode.org/charts/PDF/U4DC0.pdf

    ###18）彝文音节：A000-A48F

    ###http://www.unicode.org/charts/PDF/UA000.pdf

    ###19）彝文部首：A490-A4CF

    ###http://www.unicode.org/charts/PDF/UA490.pdf

    ###20）盲文符号：2800-28FF

    ###http://www.unicode.org/charts/PDF/U2800.pdf

    ###21）CJK字母及月份：3200-32FF

    ###http://www.unicode.org/charts/PDF/U3200.pdf

    ###22）CJK特殊符号（日期合并）：3300-33FF

    ###http://www.unicode.org/charts/PDF/U3300.pdf

    ###23）装饰符号（非CJK专用）：2700-27BF

    ###http://www.unicode.org/charts/PDF/U2700.pdf

    ###24）杂项符号（非CJK专用）：2600-26FF

    ###http://www.unicode.org/charts/PDF/U2600.pdf

    ###25）中文竖排标点：FE10-FE1F

    ###http://www.unicode.org/charts/PDF/UFE10.pdf

    ###26）CJK兼容符号（竖排变体、下划线、顿号）：FE30-FE4F

    ###http://www.unicode.org/charts/PDF/UFE30.pdf

    ##############################################################################
    ##############################################################################
    ##############################################################################

    """
        Unicode 涵盖了GBK编码，而由于GBK以区位码记录，存储进计算机内存时会在原有区位码的基础上+0xA0A0，所以GBK为ASCII保留了编码空间。
        因此可以使用ord(ch)是否小于128来确定ch是否是ascii码
    """

    def CheckCharType(self, Char):
        if ord(Char) < 0x0080:
            return self.CheckEnglishCharType(Char)
        else:
            return self.CheckChineseCharType(Char)

    def CheckEnglishCharType(self, Char):
        EnglishDelimiters = " \"!,.?()[]{}+="
        if Char in EnglishDelimiters:
            return CT_EN_DELIMITER
        else:
            if self.isEnglishLetter(Char):
                return CT_SINGLE
            elif self.isEnglishNumber(Char):
                return CT_SINGLE
            else:
                return CT_SINGLE

    def CheckChineseCharType(self, Char):
        GBK_Byte = Char.encode("GBK")
        ( HighByte, LowByte ) = struct.unpack("BB",GBK_Byte)
        
        #########################################################################
        #CODE   +0  +1  +2  +3  +4  +5  +6  +7  +8  +9  +A  +B  +C  +D  +E  +F
        #A2A0       ⅰ   ⅱ   ⅲ   ⅳ   ⅴ  ⅵ  ⅶ   ⅷ   ⅸ   ⅹ                     
        #A2B0        ⒈   ⒉   ⒊   ⒋   ⒌  ⒍  ⒎   ⒏   ⒐   ⒑   ⒒  ⒓   ⒔   ⒕   ⒖
        #A2C0   ⒗   ⒘   ⒙   ⒚   ⒛   ⑴  ⑵  ⑶   ⑷   ⑸   ⑹   ⑺  ⑻   ⑼   ⑽   ⑾
        #A2D0   ⑿   ⒀   ⒁   ⒂   ⒃   ⒄  ⒅  ⒆   ⒇   ①   ②   ③  ④   ⑤   ⑥   ⑦
        #A2E0   ⑧   ⑨   ⑩   €         ㈠  ㈡ ㈢   ㈣   ㈤  ㈥   ㈦  ㈧  ㈨   ㈩     
        #A2F0        Ⅰ   Ⅱ   Ⅲ   Ⅳ   Ⅴ  Ⅵ  Ⅶ   Ⅷ   Ⅸ   Ⅹ   Ⅺ  Ⅻ        
        #########################################################################
        
        if HighByte == 0xA2:
            return CT_CN_INDEX
        
        if self.isChineseNumber(Char):
            return CT_SINGLE
        
        if self.isChineseLetter(Char):
            return CT_SINGLE

        #########################################################################
        #CODE   +0  +1  +2  +3  +4  +5  +6  +7  +8  +9  +A  +B  +C  +D  +E  +F
        #A1A0       　   、   。  ·   ˉ   ˇ   ¨  〃  々    —  ～   ‖   …   ‘   ’
        #A1B0   “    ”  〔    〕 〈   〉  《   》 「   」  『   』   〖   〗 【   】
        #A1C0   ±    ×   ÷   ∶   ∧   ∨   ∑   ∏   ∪   ∩   ∈   ∷   √    ⊥   ∥   ∠
        #A1D0   ⌒    ⊙   ∫   ∮    ≡   ≌   ≈   ∽   ∝   ≠   ≮   ≯   ≤   ≥   ∞   ∵
        #A1E0   ∴    ♂   ♀   °   ′   ″   ℃   ＄   ¤   ￠  ￡   ‰  §   №    ☆   ★
        #A1F0   ○    ●   ◎   ◇   ◆   □    ■   △   ▲   ※   →   ←   ↑  ↓   〓
        #.......................................................................
        #.......................................................................
        #A3A0       ！  ＂   ＃  ￥   ％  ＆  ＇  （   ）   ＊  ＋   ，  －  ．   ／
        #A3B0                                            ：  ；  ＜   ＝  ＞  ？
        #A3C0   ＠                                                             
        #A3D0                                               ［  ＼   ］  ＾  ＿
        #A3E0   ｀                                                             
        #A3F0                                               ｛   ｜   ｝  ￣
        #########################################################################
        
        if ( HighByte == 0xA1 or HighByte == 0xA3 ):
            return CT_CN_DELIMITER
        
        if 0xB0<=HighByte and HighByte<=0xF7:
            return CT_CN_CHARACTER
        
        return CT_UNCLEAR

    def isChineseNumber(self, Char):
    
        if ord(Char) < 0x0080:
            return False
        
        GBK_Byte = Char.encode("GBK")
        ( HighByte, LowByte ) = struct.unpack("BB",GBK_Byte)
                
        #########################################################################
        #CODE   +0  +1  +2  +3  +4  +5  +6  +7  +8  +9  +A  +B  +C  +D  +E  +F
        #A3A0   
        #A3B0   ０   １  ２  ３  ４   ５  ６   ７  ８   ９
        #A3C0   
        #A3D0   
        #A3E0   
        #A3F0   
        #########################################################################
        
        if HighByte == 0xA3 and 0xB0<=LowByte and LowByte<=0xB9:
            return True
        else:
            return False

    def isChineseLetter(self, Char):
    
        if ord(Char) < 0x0080:
            return False
        
        GBK_Byte = Char.encode("GBK")
        ( HighByte, LowByte ) = struct.unpack("BB",GBK_Byte)

        #########################################################################
        #CODE   +0  +1  +2  +3  +4  +5  +6  +7  +8  +9  +A  +B  +C  +D  +E  +F
        #A3A0
        #A3B0
        #A3C0        Ａ  Ｂ  Ｃ  Ｄ   Ｅ  Ｆ   Ｇ  Ｈ   Ｉ   Ｊ  Ｋ  Ｌ  Ｍ   Ｎ  Ｏ
        #A3D0   Ｐ   Ｑ  Ｒ  Ｓ  Ｔ   Ｕ  Ｖ   Ｗ  Ｘ   Ｙ   Ｚ
        #A3E0        ａ  ｂ  ｃ  ｄ   ｅ  ｆ   ｇ  ｈ   ｉ   ｊ  ｋ  ｌ   ｍ  ｎ  ｏ
        #A3F0   ｐ   ｑ  ｒ  ｓ  ｔ   ｕ  ｖ   ｗ  ｘ   ｙ   ｚ
        #########################################################################
        
        if HighByte == 0xA3 and (( 0xC1<=LowByte and LowByte<=0xDA) or (0xE1<=LowByte and LowByte<=0xFA)):
            return True
        else:
            return False

    def isEnglishNumber(self, Char):
    
        if ord(Char) < 0x0080:
            if ord("0")<=ord(Char) and ord(Char)<=ord("9"):
                return True
            else:
                return False
        else:
            return False

    def isEnglishLetter(self, Char):
    
        if ord(Char) < 0x0080:
            if (ord("a")<=ord(Char) and ord(Char)<=ord("z")) or (ord("A")<=ord(Char) and ord(Char)<=ord("Z")):
                return True
            else:
                return False
        else:
            return False

    def isLetter(self, Char):
        if self.isChineseLetter(Char) or self.isEnglishLetter(Char):
            return True
        return False

    def isNumber(self, Char):
        if self.isChineseNumber(Char) or self.isEnglishNumber(Char):
            return True
        return False

    def isAllChineseCharacter(self, Str):
        for char in Str:
            if CheckCharType(char) != CT_CN_CHARACTER:
                return False
        return True

    def isAllLetter(Str):
        for char in Str:
            if not isLetter(char):
                return False
        return True

    
    def isNumberStr(self, Str):
        PatternStr = r"^[±+－\-＋]?[０１２３４５６７８９\d]*[∶·．／./]?[０１２３４５６７８９\d]*[百千万亿佰仟％‰%]?$"
        if re.match(PatternStr, Str):
            return True
        return False
    
    def CountAppearTime(self, StrA, StrB):
        #StrB中的字符元素在StrA中出现的总次数
        Time = 0
        for char in StrB:
            if char in StrA:
                Time += 1
        return Time
    
    def isYearTime(self, Str):
        strLen = len(Str)
        if isNumberStr(Str):
            if strLen == 4 or (strLen==2 and Str[0] in "０１２３４５６７８９123456789"):
                return True
        if CountAppearTime("零○一二三四五六七八九壹贰叁肆伍陆柒捌玖", Str) == strLen and strLen >= 2:
            return True
        if strLen == 4 and CountAppearTime("千仟零○", Str) == 2:
            return True
        if strLen == 1 and CountAppearTime("千仟", Str) == 1:
            return True
        if strLen == 2 and re.match("^[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]$", Str):
            return True
        return False
                    
    def isChineseBigNumberStr(self, Str):
        PatternStr = r"^[几数第]?[零○一二两三四五六七八九十廿百千万亿壹贰叁肆伍陆柒捌玖拾佰仟∶·．／点]*[之]?[零○一二两三四五六七八九十廿百千万亿壹贰叁肆伍陆柒捌玖拾佰仟]*$"
        if re.match(PatternStr, Str):
            return True
        return False
        
    def isInGBKBlankSpace(self, ID):
        if 3755 <= ID and ID <= 3759:
            return True
        return False
        
    def ChineseCharID(self, Char):
        """
        print("###### ",len(Char)," ######")
        """
        GBK_Byte = Char.encode("GBK")
        ( HighByte, LowByte ) = struct.unpack("BB",GBK_Byte)
        ID = (HighByte - 0xB0)*94 + (LowByte - 0xA1)
        return ID
        
    def ChineseChar(self, ID):
        if ID < 0 or ID > WI_COUNT:
            return ""
        HighByte = (ID // 94) + 0xB0
        LowByte = ID - (ID // 94) * 94 + 0xA1
        GBK_Byte = struct.pack("BB", HighByte, LowByte)
        Char = GBK_Byte.decode("GBK")
        return Char
    
    def ChangeToDictWordFormat(self, Str):
        char = Str[0]
        charType = self.CheckCharType(char)
        """
        print("###### ",charType," ######")
        """
        if charType == CT_CN_CHARACTER:
            charIndex = self.ChineseCharID(char)
            Str = Str[1:]
            return True, charIndex, Str
        elif charType in (CT_CN_DELIMITER, CT_EN_DELIMITER):
            return True, DELIMITER_INDEX, Str
        else:
            return False, WI_COUNT, Str
            
    def CompareChineseStrID(self, StrA, StrB):
        #StrA < StrB -1
        #StrA = StrB 0
        #StrA > StrB 1
        minLength = min(len(StrA),len(StrB))
        for i in range(0, minLength):
            if ord(StrA[i]) < 0x0080 and ord(StrB[i]) < 0x0080:
                if ord(StrA[i]) < ord(StrB[i]):
                    return -1
                elif ord(StrA[i]) > ord(StrB[i]):
                    return 1
            elif ord(StrA[i]) < 0x0080:
                return -1
            elif ord(StrB[i]) < 0x0080:
                return 1
            else:
                """
                print(StrA[i]," - - ",StrB[i])
                """
                if self.ChineseCharID(StrA[i]) < self.ChineseCharID(StrB[i]):
                    return -1
                elif self.ChineseCharID(StrA[i]) > self.ChineseCharID(StrB[i]):
                    return 1
        
        if len(StrA) < len(StrB):
            return -1
        elif len(StrA) > len(StrB):
            return 1
        return 0
            
    def CheckForeignCharCount(self, Str):
        englishCC = CountAppearTime(TRANS_ENGLISH, Str)
        japaneseCC = CountAppearTime(TRANS_ENGLISH, Str)
        russianCC = CountAppearTime(TRANS_RUSSIAN, Str)
        
        returnValue = englishCC
        if returnValue <= japaneseCC:
            returnValue = japaneseCC
        if returnValue <= russianCC:
            returnValue = russianCC
        return returnValue
        
            
utilities = Utilities()



def ReadInteger(DictFile):
    return utilities.ReadInteger(DictFile)
    
def ReadChineseWord(DictFile, ByteStrLength):
    return utilities.ReadChineseWord(DictFile, ByteStrLength)

def isSentenceSeperator(Char):
    return utilities.isSentenceSeperator(Char)
    
def CheckCharType(Char):
    return utilities.CheckCharType(Char)

def isNumber(Char):
    return utilities.isNumber(Char)

def isLetter(Char):
    return utilities.isLetter(Char)
    
def isNumberStr(Str):
    return utilities.isNumberStr(Str)

def ChineseCharID(Char):
    return utilities.ChineseCharID(Char)

def ChineseChar(ID):
    return utilities.ChineseChar(ID)

def ChangeToDictWordFormat(Str):
    return utilities.ChangeToDictWordFormat(Str)

def CompareChineseStrID(StrA, StrB):
    return utilities.CompareChineseStrID(StrA, StrB)

def isInGBKBlankSpace(ID):
    return utilities.isInGBKBlankSpace(ID)

def isYearTime(Str):
    return utilities.isYearTime(Str)

def isChineseBigNumberStr(Str):
    return utilities.isChineseBigNumberStr(Str)

def isAllLetter(Str):
    return utilities.isAllLetter(Str)
    
def isAllChineseCharacter(Str):
    return utilities.isAllChineseCharacter(Str)

def CountAppearTime(StrA, StrB):
    return utilities.CountAppearTime(StrA, StrB)