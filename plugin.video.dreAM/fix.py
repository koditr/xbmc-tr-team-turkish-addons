# -*- coding: utf-8 -*-

import base64
import re,xbmctools,urllib2



def sembol_fix(x):
    try:
        x=x.replace('\x93','"').replace('\x92',"'").replace('\x94','"').replace('/',"-").replace('-',"").replace('_'," ").replace("'","'").replace('&#8211;','&').replace('&#8217;','`').replace('&#038;','`').replace('\x85','...').replace('\xb4',"'")
    except:
        pass
    return x[0].capitalize() + x[1:]


def decode_fix(x):
    try:
        x=x.replace('\xc2\xa0',' ').replace('\xc3\xa7','c').replace('\xe2\x80\x93',' - ').replace('\xc4\xb1','i').replace('\xc3\xb6','o').replace('xc3\xbc','u').replace('xc5\x9f','s').replace('\xc5\x9e','S').replace('xc4\x9f','g').replace('\xc3\x87','C').replace('\xc3\x96','O').replace('\xc3\x9c','U').replace('\xc2\xa1','¡').replace('\xc2\xa2','¢').replace('&#039;','`').replace('\xc2\xa3','£').replace('\xc2\xa4','¤').replace('\xc2\xa5','¥').replace('\xc2\xa6','¦').replace('\xc2\xa7','§').replace('\xc2\xa8','¨').replace('\xc2\xa9','©').replace('\xc2\xaa','ª').replace('\xc2\xab','«').replace('\xc2\xac','¬').replace('\xc2\xad','­').replace('\xc2\xae','®').replace('\xc2\xaf','¯').replace('\xc2\xb0','°').replace('\xc2\xb1','±').replace('\xc2\xb2','²').replace('\xc2\xb3','³').replace('\xc2\xb4','´').replace('\xc2\xb5','µ').replace('\xc2\xb6','¶').replace('\xc2\xb7','·').replace('\xc2\xb8','¸').replace('\xc2\xb9','¹').replace('\xc2\xba','º').replace('\xc2\xbb','»').replace('\xc2\xbc','¼').replace('\xc2\xbd','½').replace('\xc2\xbe','¾').replace('\xc2\xbf','¿').replace('\xc3\x80','À').replace('\xc3\x81','Á').replace('\xc3\x82','Â').replace('\xc3\x83','Ã').replace('\xc3\x84','Ä').replace('\xc3\x85','Å').replace('\xc3\x86','Æ').replace('\xc3\x87','Ç').replace('\xc3\x88','È').replace('\xc3\x89','É').replace('\xc3\x8a','Ê').replace('\xc3\x8b','Ë').replace('\xc3\x8c','Ì').replace('\xc3\x8d','Í').replace('\xc3\x8e','Î').replace('\xc3\x8f','Ï').replace('\xc3\x90','Ð').replace('\xc3\x91','Ñ').replace('\xc3\x92','Ò').replace('\xc3\x93','Ó').replace('\xc3\x94','Ô').replace('\xc3\x95','Õ').replace('\xc3\x96','Ö').replace('\xc3\x97','×').replace('\xc3\x98','Ø').replace('\xc3\x99','Ù').replace('\xc3\x9a','Ú').replace('\xc3\x9b','Û').replace('\xc3\x9c','Ü').replace('\xc3\x9d','Ý').replace('\xc3\x9e','Þ').replace('\xc3\x9f','ß').replace('\xc3\xa0','à').replace('\xc3\xa1','á').replace('\xc3\xa2','â').replace('\xc3\xa3','ã').replace('\xc3\xa4','ä').replace('\xc3\xa5','å').replace('\xc3\xa6','æ').replace('\xc3\xa7','ç').replace('\xc3\xa8','è').replace('\xc3\xa9','é').replace('\xc3\xaa','ê').replace('\xc3\xab','ë').replace('\xc3\xac','ì').replace('\xc3\xad','í').replace('\xc3\xae','î').replace('\xc3\xaf','ï').replace('\xc3\xb0','ð').replace('\xc3\xb1','ñ').replace('\xc3\xb2','ò').replace('\xc3\xb3','ó').replace('\xc3\xb4','ô').replace('\xc3\xb5','õ').replace('\xc3\xb6','ö').replace('\xc3\xb7','÷').replace('\xc3\xb8','ø').replace('\xc3\xb9','ù').replace('\xc3\xba','ú').replace('\xc3\xbb','û').replace('\xc3\xbc','u').replace('\xc3\xbd','ý').replace('\xc3\xbe','þ').replace('\xc3\xbf','ÿ').replace('\xc4\x80','Ā').replace('\xc4\x81','ā').replace('\xc4\x82','Ă').replace('\xc4\x83','ă').replace('\xc4\x84','Ą').replace('\xc4\x85','ą').replace('\xc4\x86','Ć').replace('\xc4\x87','ć').replace('\xc4\x88','Ĉ').replace('\xc4\x89','ĉ').replace('\xc4\x8a','Ċ').replace('\xc4\x8b','ċ').replace('\xc4\x8c','Č').replace('\xc4\x8d','č').replace('\xc4\x8e','Ď').replace('\xc4\x8f','ď').replace('\xc4\x90','Đ').replace('\xc4\x91','đ').replace('\xc4\x92','Ē').replace('\xc4\x93','ē').replace('\xc4\x94','Ĕ').replace('\xc4\x95','ĕ').replace('\xc4\x96','Ė').replace('\xc4\x97','ė').replace('\xc4\x98','Ę').replace('\xc4\x99','ę').replace('\xc4\x9a','Ě').replace('\xc4\x9b','ě').replace('\xc4\x9c','Ĝ').replace('\xc4\x9d','ĝ').replace('\xc4\x9e','Ğ').replace('\xc4\x9f','g').replace('\xc4\xa0','Ġ').replace('\xc4\xa1','ġ').replace('\xc4\xa2','Ģ').replace('\xc4\xa3','ģ').replace('\xc4\xa4','Ĥ').replace('\xc4\xa5','ĥ').replace('\xc4\xa6','Ħ').replace('\xc4\xa7','ħ').replace('\xc4\xa8','Ĩ').replace('\xc4\xa9','ĩ').replace('\xc4\xaa','Ī').replace('\xc4\xab','ī').replace('\xc4\xac','Ĭ').replace('\xc4\xad','ĭ').replace('\xc4\xae','Į').replace('\xc4\xaf','į').replace('\xc4\xb0','I').replace('\xc4\xb1','ı').replace('\xc4\xb2','Ĳ').replace('\xc4\xb3','ĳ').replace('\xc4\xb4','Ĵ').replace('\xc4\xb5','ĵ').replace('\xc4\xb6','Ķ').replace('\xc4\xb7','ķ').replace('\xc4\xb8','ĸ').replace('\xc4\xb9','Ĺ').replace('\xc4\xba','ĺ').replace('\xc4\xbb','Ļ').replace('\xc4\xbc','ļ').replace('\xc4\xbd','Ľ').replace('\xc4\xbe','ľ').replace('\xc4\xbf','Ŀ').replace('\xc5\x80','ŀ').replace('\xc5\x81','Ł').replace('\xc5\x82','ł').replace('\xc5\x83','Ń').replace('\xc5\x84','ń').replace('\xc5\x85','Ņ').replace('\xc5\x86','ņ').replace('\xc5\x87','Ň').replace('\xc5\x88','ň').replace('\xc5\x89','ŉ').replace('\xc5\x8a','Ŋ').replace('\xc5\x8b','ŋ').replace('\xc5\x8c','Ō').replace('\xc5\x8d','ō').replace('\xc5\x8e','Ŏ').replace('\xc5\x8f','ŏ').replace('\xc5\x90','Ő').replace('\xc5\x91','ő').replace('\xc5\x92','Œ').replace('\xc5\x93','œ').replace('\xc5\x94','Ŕ').replace('\xc5\x95','ŕ').replace('\xc5\x96','Ŗ').replace('\xc5\x97','ŗ').replace('\xc5\x98','Ř').replace('\xc5\x99','ř').replace('\xc5\x9a','Ś').replace('\xc5\x9b','ś').replace('\xc5\x9c','Ŝ').replace('\xc5\x9d','ŝ').replace('\xc5\x9e','Ş').replace('\xc5\x9f','s').replace('\xc5\xa0','Š').replace('\xc5\xa1','š').replace('\xc5\xa2','Ţ').replace('\xc5\xa3','ţ').replace('\xc5\xa4','Ť').replace('\xc5\xa5','ť').replace('\xc5\xa6','Ŧ').replace('\xc5\xa7','ŧ').replace('\xc5\xa8','Ũ').replace('\xc5\xa9','ũ').replace('\xc5\xaa','Ū').replace('\xc5\xab','ū').replace('\xc5\xac','Ŭ').replace('\xc5\xad','ŭ').replace('\xc5\xae','Ů').replace('\xc5\xaf','ů').replace('\xc5\xb0','Ű').replace('\xc5\xb1','ű').replace('\xc5\xb2','Ų').replace('\xc5\xb3','ų').replace('\xc5\xb4','Ŵ').replace('\xc5\xb5','ŵ').replace('\xc5\xb6','Ŷ').replace('\xc5\xb7','ŷ').replace('\xc5\xb8','Ÿ').replace('\xc5\xb9','Ź').replace('\xc5\xba','ź').replace('\xc5\xbb','Ż').replace('\xc5\xbc','ż').replace('\xc5\xbd','Ž').replace('\xc5\xbe','ž').replace('\xc5\xbf','ſ')
    except:
        pass
    try:
        x=x.replace('&#xA0;',' ').replace('&#xA1;','¡').replace('&#xA2;','¢').replace('&#xA3;','£').replace('&#xA4;','¤').replace('&#xA5;','¥').replace('&#xA6;','¦').replace('&#xA7;','§').replace('&#xA8;','¨').replace('&#xA9;','©').replace('&#xAA;','ª').replace('&#xAB;','«').replace('&#xAC;','¬').replace('&#xAD;','­').replace('&#xAE;','®').replace('&#xAF;','¯').replace('&#xB0;','°').replace('&#xB1;','±').replace('&#xB2;','²').replace('&#xB3;','³').replace('&#xB4;','´').replace('&#xB5;','µ').replace('&#xB6;','¶').replace('&#xB7;','·').replace('&#xB8;','¸').replace('&#xB9;','¹').replace('&#xBA;','º').replace('&#xBB;','»').replace('&#xBC;','¼').replace('&#xBD;','½').replace('&#xBE;','¾').replace('&#xBF;','¿').replace('&#xC0;','À').replace('&#xC1;','Á').replace('&#xC2;','Â').replace('&#xC3;','Ã').replace('&#xC4;','Ä').replace('&#xC5;','Å').replace('&#xC6;','Æ').replace('&#xC7;','Ç').replace('&#xC8;','È').replace('&#xC9;','É').replace('&#xCA;','Ê').replace('&#xCB;','Ë').replace('&#xCC;','Ì').replace('&#xCD;','Í').replace('&#xCE;','Î').replace('&#xCF;','Ï').replace('&#xD0;','Ð').replace('&#xD1;','Ñ').replace('&#xD2;','Ò').replace('&#xD3;','Ó').replace('&#xD4;','Ô').replace('&#xD5;','Õ').replace('&#xD6;','Ö').replace('&#xD7;','×').replace('&#xD8;','Ø').replace('&#xD9;','Ù').replace('&#xDA;','Ú').replace('&#xDB;','Û').replace('&#xDC;','Ü').replace('&#xDD;','Ý').replace('&#xDE;','Þ').replace('&#xDF;','ß').replace('&#xE0;','à').replace('&#xE1;','á').replace('&#xE2;','â').replace('&#xE3;','ã').replace('&#xE4;','ä').replace('&#xE5;','å').replace('&#xE6;','æ').replace('&#xE7;','ç').replace('&#xE8;','è').replace('&#xE9;','é').replace('&#xEA;','ê').replace('&#xEB;','ë').replace('&#xEC;','ì').replace('&#xED;','í').replace('&#xEE;','î').replace('&#xEF;','ï').replace('&#xF0;','ð').replace('&#xF1;','ñ').replace('&#xF2;','ò').replace('&#xF3;','ó').replace('&#xF4;','ô').replace('&#xF5;','õ').replace('&#xF6;','ö').replace('&#xF7;','÷').replace('&#xF8;','ø').replace('&#xF9;','ù').replace('&#xFA;','ú').replace('&#xFB;','û').replace('&#xFC;','ü').replace('&#xFD;','ý').replace('&#xFE;','þ').replace('&#xFF;','ÿ').replace('&#x100;','Ā').replace('&#x101;','ā').replace('&#x102;','Ă').replace('&#x103;','ă').replace('&#x104;','Ą').replace('&#x105;','ą').replace('&#x106;','Ć').replace('&#x107;','ć').replace('&#x108;','Ĉ').replace('&#x109;','ĉ').replace('&#x10A;','Ċ').replace('&#x10B;','ċ').replace('&#x10C;','Č').replace('&#x10D;','č').replace('&#x10E;','Ď').replace('&#x10F;','ď').replace('&#x110;','Đ').replace('&#x111;','đ').replace('&#x112;','Ē').replace('&#x113;','ē').replace('&#x114;','Ĕ').replace('&#x115;','ĕ').replace('&#x116;','Ė').replace('&#x117;','ė').replace('&#x118;','Ę').replace('&#x119;','ę').replace('&#x11A;','Ě').replace('&#x11B;','ě').replace('&#x11C;','Ĝ').replace('&#x11D;','ĝ').replace('&#x11E;','Ğ').replace('&#x11F;','ğ').replace('&#x120;','Ġ').replace('&#x121;','ġ').replace('&#x122;','Ģ').replace('&#x123;','ģ').replace('&#x124;','Ĥ').replace('&#x125;','ĥ').replace('&#x126;','Ħ').replace('&#x127;','ħ').replace('&#x128;','Ĩ').replace('&#x129;','ĩ').replace('&#x12A;','Ī').replace('&#x12B;','ī').replace('&#x12C;','Ĭ').replace('&#x12D;','ĭ').replace('&#x12E;','Į').replace('&#x12F;','į').replace('&#x130;','İ').replace('&#x131;','ı').replace('&#x132;','Ĳ').replace('&#x133;','ĳ').replace('&#x134;','Ĵ').replace('&#x135;','ĵ').replace('&#x136;','Ķ').replace('&#x137;','ķ').replace('&#x138;','ĸ').replace('&#x139;','Ĺ').replace('&#x13A;','ĺ').replace('&#x13B;','Ļ').replace('&#x13C;','ļ').replace('&#x13D;','Ľ').replace('&#x13E;','ľ').replace('&#x13F;','Ŀ').replace('&#x140;','ŀ').replace('&#x141;','Ł').replace('&#x142;','ł').replace('&#x143;','Ń').replace('&#x144;','ń').replace('&#x145;','Ņ').replace('&#x146;','ņ').replace('&#x147;','Ň').replace('&#x148;','ň').replace('&#x149;','ŉ').replace('&#x14A;','Ŋ').replace('&#x14B;','ŋ').replace('&#x14C;','Ō').replace('&#x14D;','ō').replace('&#x14E;','Ŏ').replace('&#x14F;','ŏ').replace('&#x150;','Ő').replace('&#x151;','ő').replace('&#x152;','Œ').replace('&#x153;','œ').replace('&#x154;','Ŕ').replace('&#x155;','ŕ').replace('&#x156;','Ŗ').replace('&#x157;','ŗ').replace('&#x158;','Ř').replace('&#x159;','ř').replace('&#x15A;','Ś').replace('&#x15B;','ś').replace('&#x15C;','Ŝ').replace('&#x15D;','ŝ').replace('&#x15E;','Ş').replace('&#x15F;','ş').replace('&#x160;','Š').replace('&#x161;','š').replace('&#x162;','Ţ').replace('&#x163;','ţ').replace('&#x164;','Ť').replace('&#x165;','ť').replace('&#x166;','Ŧ').replace('&#x167;','ŧ').replace('&#x168;','Ũ').replace('&#x169;','ũ').replace('&#x16A;','Ū').replace('&#x16B;','ū').replace('&#x16C;','Ŭ').replace('&#x16D;','ŭ').replace('&#x16E;','Ů').replace('&#x16F;','ů').replace('&#x170;','Ű').replace('&#x171;','ű').replace('&#x172;','Ų').replace('&#x173;','ų').replace('&#x174;','Ŵ').replace('&#x175;','ŵ').replace('&#x176;','Ŷ').replace('&#x177;','ŷ').replace('&#x178;','Ÿ').replace('&#x179;','Ź').replace('&#x17A;','ź').replace('&#x17B;','Ż').replace('&#x17C;','ż').replace('&#x17D;','Ž').replace('&#x17E;','ž').replace('&#x17F;','ſ')
    except:
        pass
    try:
        x=x.replace('\xf6',"ö").replace('\xf0',"ğ").replace('\xfc',"ü").replace('\xfd',"ı").replace('\xe7',"ç").replace('\xfe',"ş").replace('\xd6',"Ö").replace('\xc7',"Ç").replace('\xdd',"İ").replace('\xde',"Ş").replace('\xdc',"Ü").replace('&#304;',"İ").replace('&#305;',"ı").replace('&#214;',"Ö").replace('&#246;',"ö").replace('&#220;',"Ü").replace('&#252;',"ü").replace('&#199;',"Ç").replace('&#231;',"ç").replace('&#286;',"Ğ").replace('&#287;',"ğ").replace('&#350;',"Ş").replace('&#351;',"ş").replace('\xe2',"â").replace('\xe2',"â")
    except:
        pass
    return x[0].capitalize() + x[1:]


class AADecoder(object):
    def __init__(self, aa_encoded_data):
        #self.encoded_str = aa_encoded_data.replace('/*´∇｀*/','')

        self.b = ["(c^_^o)", "(ﾟΘﾟ)", "((o^_^o) - (ﾟΘﾟ))", "(o^_^o)",
                  "(ﾟｰﾟ)", "((ﾟｰﾟ) + (ﾟΘﾟ))", "((o^_^o) +(o^_^o))", "((ﾟｰﾟ) + (o^_^o))",
                  "((ﾟｰﾟ) + (ﾟｰﾟ))", "((ﾟｰﾟ) + (ﾟｰﾟ) + (ﾟΘﾟ))", "(ﾟДﾟ) .ﾟωﾟﾉ", "(ﾟДﾟ) .ﾟΘﾟﾉ",
                  "(ﾟДﾟ) ['c']", "(ﾟДﾟ) .ﾟｰﾟﾉ", "(ﾟДﾟ) .ﾟДﾟﾉ", "(ﾟДﾟ) [ﾟΘﾟ]"]

    def is_aaencoded(self):
        idx = self.encoded_str.find("ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); ")
        if idx == -1:
            return False

        if self.encoded_str.find("(ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');", idx) == -1:
            return False

        return True

    def base_repr(self, number, base=2, padding=0):
        digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if base > len(digits):
            base = len(digits)

        num = abs(number)
        res = []
        while num:
            res.append(digits[num % base])
            num //= base
        if padding:
            res.append('0' * padding)
        if number < 0:
            res.append('-')
        return ''.join(reversed(res or '0'))

    def decode_char(self, enc_char, radix):
        end_char = "+ "
        str_char = ""
        while enc_char != '':
            found = False

            if not found:
                for i in range(len(self.b)):             
                    enc_char=enc_char.replace(self.b[i], str(i))
                
                startpos=0
                findClose=True
                balance=1
                result=[]
                if enc_char.startswith('('):
                    l=0
                    
                    for t in enc_char[1:]:
                        l+=1
                        if findClose and t==')':
                            balance-=1;
                            if balance==0:
                                result+=[enc_char[startpos:l+1]]
                                findClose=False
                                continue
                        elif not findClose and t=='(':
                            startpos=l
                            findClose=True
                            balance=1
                            continue
                        elif t=='(':
                            balance+=1
                 

                if result is None or len(result)==0:
                    return ""
                else:
                    
                    for r in result:
                        value = self.decode_digit(r, radix)
                        if value == "":
                            return ""
                        else:
                            str_char += value
                            
                    return str_char

            enc_char = enc_char[len(end_char):]

        return str_char

        
              
    def decode_digit(self, enc_int, radix):

        rr = '(\(.+?\)\))\+'
        rerr=enc_int.split('))+')
        v = ''
        
        #new mode

        for c in rerr:
            
            if len(c)>0:
                if c.strip().endswith('+'):
                    c=c.strip()[:-1]

                startbrackets=len(c)-len(c.replace('(',''))
                endbrackets=len(c)-len(c.replace(')',''))
                    
                if startbrackets>endbrackets:
                    c+=')'*startbrackets-endbrackets
                    
                c = c.replace('!+[]','1')
                c = c.replace('-~','1+')
                c = c.replace('[]','0')
                    
                v+=str(eval(c))
                    
        return v
         
        mode = 0
        value = 0

        while enc_int != '':
            found = False
            for i in range(len(self.b)):
                if enc_int.find(self.b[i]) == 0:
                    if mode == 0:
                        value += i
                    else:
                        value -= i
                    enc_int = enc_int[len(self.b[i]):]
                    found = True
                    break

            if not found:
                return ""

            enc_int = re.sub('^\s+|\s+$', '', enc_int)
            if enc_int.find("+") == 0:
                mode = 0
            else:
                mode = 1

            enc_int = enc_int[1:]
            enc_int = re.sub('^\s+|\s+$', '', enc_int)

        return self.base_repr(value, radix)

    def decode(self):

        self.encoded_str = re.sub('^\s+|\s+$', '', self.encoded_str)

        # get data
        pattern = (r"\(ﾟДﾟ\)\[ﾟoﾟ\]\+ (.+?)\(ﾟДﾟ\)\[ﾟoﾟ\]\)")
        result = re.search(pattern, self.encoded_str, re.DOTALL)
        if result is None:
            print "AADecoder: data not found"
            return False

        data = result.group(1)

        # hex decode string
        begin_char = "(ﾟДﾟ)[ﾟεﾟ]+"
        alt_char = "(oﾟｰﾟo)+ "

        out = ''

        while data != '':
            # Check new char
            if data.find(begin_char) != 0:
                print "AADecoder: data not found"
                return False

            data = data[len(begin_char):]

            # Find encoded char
            enc_char = ""
            if data.find(begin_char) == -1:
                enc_char = data
                data = ""
            else:
                enc_char = data[:data.find(begin_char)]
                data = data[len(enc_char):]

            
            radix = 8
            # Detect radix 16 for utf8 char
            if enc_char.find(alt_char) == 0:
                enc_char = enc_char[len(alt_char):]
                radix = 16

            str_char = self.decode_char(enc_char, radix)
            
            if str_char == "":
                print "no match :  "
                print  data + "\nout = " + out + "\n"
                return False
            
            out += chr(int(str_char, radix))
            print out

        if out == "":
            print "no match : " + data
            return False

        return out
def daily_sec(name,url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('"video\\\/mp4","url"\:"(.*?)\/H264\-(.*?)\\\/video(.*?)"').findall(link)
    for a,name2,c in match:
        urlA=a+"/H264-"+name2+"/video"+c
        urlA=urlA.replace('\/','/')
        xbmctools.addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name2+'[/COLOR]'+'[/COLOR]',urlA,'')

