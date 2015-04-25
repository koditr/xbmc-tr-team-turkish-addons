# -*- coding: utf-8 -*-
# xbmctr MEDIA CENTER, is an XBMC add on that sorts and displays 
# video content from several websites to the XBMC user.
#
# Copyright (C) 2011, Dr Ayhan Colak
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# for more info please visit http://xbmctr.com

'''
Author: drascom
Date: 13/04/2012
'''

import urllib, urllib2, re, sys, cookielib
import xbmc, xbmcaddon, xbmcgui,xbmcplugin
import araclar
import mechanize
import urlresolver
import time,os,base64
import simplejson as json
#
# Eklenti bildirimleri --------------------------------------------------------
addon_id = 'script.module.xbmctr'
__ayarlar__ = xbmcaddon.Addon(id=addon_id)
path = __ayarlar__.getAddonInfo('path')
IMAGES_PATH = xbmc.translatePath(os.path.join(path, 'resoures','image'))
addon_icon    = __ayarlar__.getAddonInfo('icon')
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1)"
downloadFolder = __ayarlar__.getSetting('download-folder')
insidans=1
#--cozuculer--#
ktk='w4dhbMSxxZ9rYW4gw5x5ZQ=='
df='aHR0cDovL2ZvcnVtLnhibWN0ci5jb20vbWVtYmVyLnBocA=='
A='QWRtaW5pc3RyYXRvcg=='
f='JnBhc3N3b3JkPQ=='
k='dXNlcm5hbWU9'
b='JnN1Ym1pdD1Mb2dpbiZhY3Rpb249ZG9fbG9naW4mdXJsPWh0dHA6Ly9mb3J1bS54Ym1jdHIuY29tLw=='
r='aHR0cDovL2ZvcnVtLnhibWN0ci5jb20vdXllLQ=='
c='VklQ'
ss='TW9kZXJhdG9y'
tr='U3VwZXIgTW9kZXJhdG9y'
qq='Lmh0bWw='
yl='VXNlcm5hbWU='
kl='cGFzc3dvcmQ='
pl='TW9kIEFEQVlJ'
ttt='WWVuaSDDnHll'
#--cozuculer--#
    
__settings__ = xbmcaddon.Addon(id='script.module.xbmctr')
__language__ = __settings__.getLocalizedString


FILENAME = "cozucu"




'''Constants'''
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
vk=[]
value=[]




'''
listing,pagination function
for multipage web site
'''

def unique(l):
    s = set(); n = 0
    for x in l:
        if x not in s: s.add(x); l[n] = x; n += 1
    del l[n:]
def dacka(yol):
    files = os.listdir(yol)
    global imps
    imps = []

    for i in range(len(files)):
        py_name = files[i].split('.')
        if len(py_name) > 1:
            if py_name[1] == 'py' and py_name[0] != '__init__':
               py_name = py_name[0]
               imps.append(py_name)
    file = open(yol+'/__init__.py','w')
    toWrite = '__all__ = '+str(imps)
    file.write(toWrite)
    file.close()
    return imps
def addDir(fileName,name, mode, url="", thumbnail=""):
    u = sys.argv[0]+"?fileName="+urllib.quote_plus(fileName)+"&name="+urllib.quote_plus(name)+"&mode="+urllib.quote_plus(mode)+"&url="+urllib.quote_plus(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    
def fullfilm_gizli_player(url):
##        print 'GIZLI PLaYER url ',url
        link=araclar.get_url(url)
        link=link.replace('%3A',":").replace('%3F',"?").replace('%3D',"=")
        match=re.compile('v=(.*?)&').findall(link)
##        print 'GIZLI PLaYER',match
        url=match[0]
        return url

def liste_olustur(Url,match):
##        print 'Paging started'
        urlList=''
        for pageUrl in match:
                #web page list function
                urlList=urlList+pageUrl #add page to list
                urlList=urlList+':;'    #add seperator
                total=Url+':;'+urlList  #add first url
                match = total.split(':;') #split links
                del match [-1]            #delete first seperator
                #print match
        info='Film '+str(len(match)-1)+' part.'
        match = filter(bool,match)
        return match


def prepare_face_links(videoTitle,match):
        i=0
        for pageLink in match:
                link=araclar.get_url(pageLink)
                match=re.compile('<embed src=\'.*?file=(.*?)&a').findall(link)
                    
                for videoLink in match:
                        i+=1
                        araclar.addVideoLink(videoTitle+' Part '+str(i),videoLink,'')
                        playList.add(videoLink)

def Youtube_Player(url):
##        safe='aHR0cDovL3hibWN0ci50di8='
##        link=araclar.get_url(base64.b64decode(safe))
##        match1=re.compile('besir>>(.*?)<<besir').findall(link)
##        for kkk in match1:
##                print kkk    
        code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)

        print '[code]'+str(code)
        url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)
        return url

def uploadc_Player(url):
        uploadcurl=url
        link=araclar.get_url(uploadcurl)
        match=re.compile('\'file\',\'(.*?)Enter.*?.mp4\'').findall(link)
        for uploadcgelen in match:
            print str(uploadcgelen)
            url=str(uploadcgelen)+'Enter%20your%20zip%20code%20here.mp4'
            return url
			
##def mailru_Player(url):
##    referer='http://img.mail.ru/r/video2/uvpv3.swf?3'
##    cookie='VID=2SlVa309oFH4; mrcu=EE18510E964723319742F901060A; p=IxQAAMr+IQAA; video_key=203516; s='
##    UA='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
##    m = re.search('movieSrc=(?P<url>.+?)$', url, re.IGNORECASE | re.DOTALL)
##    if m:
##        items = []
##        headers = { "User-Agent":UA, "Referer":referer, "Cookie":cookie }
##        # header "Cookie" with parameters need to be set for your download/playback
##        quality = "???"
##        vurl = m.group('url')
##        vurl = re.sub('\&[^$]*','',vurl)
##        data = araclar.get_url_headers('http://api.video.mail.ru/videos/' + vurl + '.json', headers)
##        item = json.loads(data)
##        for qual in item[u'videos']:
##            if qual == 'sd':
##                quality = "480p"
##            elif qual == "hd":
##                quality = "720p"
##            else:
##                quality = "???"
##            link = item[u'videos'][qual]
##            items.append({'quality':quality, 'url':link+'|Cookie='+cookie+'|Referer='+referer})
##            
##        # best quality
##            videobul = sorted(items,key=lambda i:i['quality'])
##	#resolved.reverse()
##        return videobul[-1][u'url']

def Divxshare_Player(url):
        value=''
        xbmc.executebuiltin('Notification("Dream Clup",DIVXSTAGE Deneniyor.)')
        link=araclar.get_url(url)
        match=re.compile('domain="(.*?)";\n\t\t\tflashvars.file="(.*?)";\n\t\t\tflashvars\.filekey="(.*?)"').findall(link)
        if not match:
            xbmc.executebuiltin('Notification("Sitede HATA ",ilk Linki yok.)')
        for domain,dosya,key in match:
            transfer =domain+"/api/player.api.php?file="+dosya+"&codes=undefined&user=undefined&key="+key+"&pass=undefined"
            link=araclar.get_url(transfer)
            match=re.compile('url=(.*?)&').findall(link)
            if not match:
                xbmc.executebuiltin('Notification("Serverda HATA ",Ikinci Linki yok.)')
            for url in match:
                if url.endswith('flv'):
                        value=url
                else:
                    pass
        print value
        return value
def stagevu_player(code):
    xbmc.executebuiltin('Notification("Dream Clup",STAGEVU Deneniyor.)')
    link=araclar.get_url(url)
    sv1 = re.compile('src="(.+?)" border="0">').findall(link)
    link=araclar.get_url(sv1[0])
    sv3 = re.compile('src="(.+?)" border="0"').findall(link)
    link=araclar.get_url(sv3[0])
    StageVu=re.compile('<param name="src" value="(.+?)" />').findall(link)
    print "stagevu",StageVu
    return StageVu[0]
	
def wfih_player(code):
    return code
                        
def Yesload_Player(code):
    value=''
    xbmc.executebuiltin('Notification("Dream Clup",YESLOAD Deneniyor.)')
    link=araclar.get_url(code)
    yesloadurlbul1=re.compile('<a target="_blank" href="http://yesload.net/(.*?)">').findall(link)
    for x in yesloadurlbul1:
        code='http://yesload.net/player_api/info?token='+x
    link=araclar.get_url(code)
    yesloadurlbul2=re.compile('premium.token=(.*?)"').findall(link)
    for x in yesloadurlbul2:
        code='http://yesload.net/player_api/info?token='+x
    link=araclar.get_url(code)
    yesloadplayer=re.compile('url=(.*?).flv&').findall(link)
    for url in yesloadplayer:
        value=url
    return value

def Streamcloud_Player(url):
    print "streamcoud gelen url",url 
    value=''
    try:
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        cookie = response.info().getheader('Set-Cookie')  
        response.close()
   
        match=re.compile('<input type="hidden" name="op" value="(.*?)">\n\t\t\t\t\t\t<input type="hidden" name="usr_login" value="(.*?)">\n\t\t\t\t\t\t<input type="hidden" name="id" value="(.*?)">\n\t\t\t\t\t\t<input type="hidden" name="fname" value="(.*?)">\n\t\t\t\t\t\t<input type="hidden" name="referer" value="(.*?)">\n\t\t\t\t\t\t<input type="hidden" name="hash" value="(.*?)">\n\t\t\t\t\t\t<input type="submit" name="imhuman" .*? value="(.*?)">').findall(link)
        gelen_veri=re.compile('file: "(.+?)"').findall(link)
        if len(gelen_veri)>0:
            value=gelen_veri[0]
            return value
        else:
            
            for op,usr_login,id,fname,referer,hash,imhuman in match:
                import time
                time.sleep(11)

                gidecekveriler=urllib.urlencode({'op' : op, 'usr_login' : usr_login, 'id' : id, 'fname' : fname, 'referer' : referer, 'hash' : hash, 'imhuman' : imhuman.replace(" ","+")})
                req=urllib2.Request(url)
                req.add_header('Referer', url)
                req.add_data(gidecekveriler)
                req.add_header('Cookie',cookie)
                post = urllib2.urlopen(req)
                gelen_veri=post.read()
                #print gelen_veri

                gelen_veri=re.compile('file: "(.+?)"').findall(gelen_veri)
                
                for final in gelen_veri:
                    print final
                    value=final
        
    except:
        pass
    print "cozucu stream value",value
    return value

def stream2k_Player(code):
    value=''
    xbmc.executebuiltin('Notification("Dream Clup",STREAM2K Deneniyor.)')
    link=araclar.get_url(code)
    match=re.compile('<iframe.*?src="(.*?)"><\/iframe><BR><\/div>\W+<div id="underplayer">').findall(link)
    link=araclar.get_url(match[0])
    match1=re.compile("file: .(.*)'").findall(link)
    for url in match1:
        value=url
    return value


def VideoAz_Player(url):
     xbmc.executebuiltin('Notification("Dream Clup",VIDEOAZ Deneniyor.)')
     link=araclar.get_url(url)
     print url
     playerbul=re.compile('flashvars="(.*?)"').findall(link)
     print "playerbul",playerbul
     for a in playerbul:
         url1=('http://www.video.az/assets/player/player.swf?'+a)
         url=url1
         return url


def Dailymotion(code):
##        safe='aHR0cDovL3hibWN0ci50di8='
##        link=araclar.get_url(base64.b64decode(safe))
##        match1=re.compile('besir>>(.*?)<<besir').findall(link)
##        for kkk in match1:
##                print kkk
        value=[]
        count=[]
        url="http://www.dailymotion.com/embed/video/"+code
        xbmc.executebuiltin('Notification("Dream Clup",DAILYMOTION Deneniyor.)')
        link=araclar.get_url(url)
        link = urllib.unquote(link).decode('utf8').replace('\\/', '/')
        dm_high = re.compile('"stream_h264_url":"(.+?)"').findall(link)
        dm_low = re.compile('"stream_h264_ld_url":"(.+?)"').findall(link)
        if dm_high:
                count.append('Dailymotion 360kb/s HD')
        if dm_low:
                count.append('Dailymotion 180kb/s SD ')
        else:
                pass
        dialog = xbmcgui.Dialog()
        ret = dialog.select(__language__(30008),count)
        if ret == 0:
                
                value.append(('Dailymotion 384 p',dm_high[0]))
        if ret == 1:

                value.append(('Dailymotion 240 p',dm_low[0]))
        
        return value
		
def Flashx_Player(url):
##    safe='aHR0cDovL3hibWN0ci50di8='
##    link=araclar.get_url(base64.b64decode(safe))
##    match1=re.compile('besir>>(.*?)<<besir').findall(link)
##    for kkk in match1:
##            print kkk
    xbmc.executebuiltin('Notification("Dream Clup",FLASHX Deneniyor.)')
    link=araclar.get_url(url)
    print url
    playerbul=re.compile('href="http://flashx.tv/video\/(.*?)\/.*?">').findall(link)
    print "playerbul",playerbul
    for a in playerbul:
     url1=('http://play.flashx.tv/nuevo/player/cst.php?hash='+a)
     url=url1
     
     link=araclar.get_url(url)
     match=re.compile('<file>(.*?).flv</file>').findall(link)
     print "playerbul2",match
     for a in match:
         url=a+'.flv'
         print "playerbul3",url
         return url

def Putlocker_Player(url):
##    safe='aHR0cDovL3hibWN0ci50di8='
##    link=araclar.get_url(base64.b64decode(safe))
##    match1=re.compile('besir>>(.*?)<<besir').findall(link)
##    for kkk in match1:
##            print kkk
    value=''
    xbmc.executebuiltin('Notification("Dream Clup",PUTLOCKER Deneniyor.)')
    link=araclar.get_url(url)
    match=re.compile('<input type="hidden" value="(.*?)" name="(.*?)">').findall(link)
    print "ilk match",match
    for a,b in match:
        bilgiler=urllib.urlencode({b : a,'confirm': 'Close Ad and Watch as Free User'})
        adres=urllib.urlopen(url,bilgiler)
        #Gelen bilgiyi okuyalim
        adres=adres.read()
        #Gelen bilginin icinde URL adresini alalim
        adres=re.compile('playlist: \'(.*?)\'').findall(adres)
        for son_url in adres:
            url='http://www.putlocker.com'+son_url
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            link=link.replace('amp;',"").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g").replace('#038;',"")
            response.close()
            match=re.compile('content url="(.*?)"').findall(link)
            print "putlocker son",match
            if len(match) >1:
                del match[0]#burasi onemli kalmali ok
            for value in match:
                return value
            
    if not value:
        return false
    
def Sockshare_Player(url):
##    safe='aHR0cDovL3hibWN0ci50di8='
##    link=araclar.get_url(base64.b64decode(safe))
##    match1=re.compile('besir>>(.*?)<<besir').findall(link)
##    for kkk in match1:
##            print kkk    
    value=''
    xbmc.executebuiltin('Notification("Dream Clup",SOCKSHARE Deneniyor.)')
    link=araclar.get_url(url)
    match=re.compile('<input type="hidden" value="(.*?)" name="(.*?)">').findall(link)
    print "ilk match",match
    for a,b in match:
        bilgiler=urllib.urlencode({b : a,'confirm': 'Close Ad and Watch as Free User'})
        adres=urllib.urlopen(url,bilgiler)
        #Gelen bilgiyi okuyalim
        adres=adres.read()
        #Gelen bilginin icinde URL adresini alalim
        adres=re.compile('playlist: \'(.*?)\'').findall(adres)
        for son_url in adres:
            url='http://www.sockshare.com'+son_url
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            link=link.replace('amp;',"").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g").replace('#038;',"")
            response.close()
            match=re.compile('content url="(.*?)"').findall(link)
            print "sockshare son",match
            if len(match) >1:
                del match[0]#burasi onemli kalmali ok
            for value in match:
                return value
            
    if not value:
        return false
            
def vk_Player(vk_list):
##        safe='aHR0cDovL3hibWN0ci50di8='
##        link=araclar.get_url(base64.b64decode(safe))
##        match1=re.compile('besir>>(.*?)<<besir').findall(link)
##        for kkk in match1:
##                print kkk
        value=[]
        count=[]
        fixed=''
        gecis=0
        resolutions = ["240", "360", "480", "720", "1080"]
        
        for url in vk_list if not isinstance(vk_list, basestring) else [vk_list]:
                try:   
                    link=araclar.get_url(url)
                    host=re.compile("host=(.*?)&").findall(link)
                    uid=re.compile("uid=(.*?)&").findall(link)
                    vtag=re.compile("vtag=(.*?)&").findall(link)
                    hd = re.compile("hd_def=(.*?)&").findall(link)
                    if not hd or hd[0]=="-1":
                        hd = re.compile("max_hd = '(.*?)';").findall(link)
                    flv = re.compile("no_flv=(.*?)&").findall(link)
                    #http://cs514110.userapi.com/u175995076/video/ac8f196d08.xxx.mp4
                    start_url=host[0]+'u'+uid[0]+'/videos/' + vtag[0]
                    print "vk start url",start_url
                    print "hd:",hd
                    x=(int(hd[0])+1)
                    if hd >0 or flv == 1:
                            for i in range (x):
                                    i=resolutions[i]+' p'
                                    count.append(i) 
                            if gecis==0:
                                    dialog = xbmcgui.Dialog()
                                    ret = dialog.select(__language__(30014),count)
                                    for i in range (x):
                                            if ret == i:
                                                    url=start_url+'.'+str(resolutions[i])+'.mp4'
                                                    fixed=str(resolutions[i])
                                                    gecis+=1
                                                    
                                            else:
                                                    'VK SECIM YOK'
                            else:
                                    url=start_url+'.'+fixed+'.mp4'
                                    print ('SECIM :'+fixed)
                                    gecis+=1
                            value.append(url)
                    else:
                            print 'HD FLV YANLIS'
                except:
                        print 'LINK TARAMA FAILED'
                        pass
        return value

def xml_scanner(videoTitle,url):
        value=[]
        xmlScan=araclar.get_url(url)
        dizihd=re.compile('git=(.*?)"').findall(xmlScan)
        face_1=re.compile('http://dizihd.com/dizihdd.php(.+?)"').findall(xmlScan)#xml ici face link
        youtube_1=re.compile('v=(.*?)"').findall(xmlScan)#xml içi youtube link
        dizimag=re.compile('url="(.*?)"').findall(xmlScan) #xml ici dizimag                               
        music=re.compile('<file>(.*?)</file>').findall(xmlScan)
        if len(youtube_1)> 0  :
                for i, url in enumerate(youtube_1):
                        Url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(youtube_1[0])
                        value.append(Url)
        
        if len(face_1)> 0  :
                for i, url in enumerate(face_1):
                        Url='http://dizihd.com/dizihdd.php'+str(url)
                        value.append(Url)
                        
        if len(dizimag)> 0:
                for i, url in enumerate(dizimag):
                        value.append(url)
                       
        if len(music)> 0  :
                for i, url in enumerate(music):
                        value.append(url)
                       
        
        print 'XML DONUS DEGERI',value
        return value                      
                                
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)

def videobul(urlList):
    value=[]
    try:
        print "Bizim Sistem Deneniyor"
        value=denetle(urlList)
        print "Bizim sistem sonuc:",value
        if not value:
            print "urlresolver Sistem Deneniyor"
            value=UrlResolverPlayer(urlList)
            print "********* resolver sonuc ***********",value
    except:
        value=[('server bulunamadi','http://www.youtube.com/watch?v=tMqzgaKWJoQ')]
    finally:
        return value

def denetle(urlList):
        vk=[]
        value=[]
        print "URL listesi",urlList
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:
                print "cozulecek url",url
                if 'video.ak.fbcdn.net' in url:
                    value.append(("F Server",url))

                if 'vk.com' in url:
                    print 'VK BULUNDU'
                    vk.append(url)

                if "divxstage" in url:
                    value.append(("DivxStage",Divxshare_Player(url)))

                if "novamov" in url:
                    value.append(("NovaMov",Divxshare_Player(url)))

                if "flashx" in url:
                    value.append(("Flashx",Flashx_Player(url)))
                
                if 'youtube' in url:
                    print 'YOUTUBE BULUNDU'
                    value.append(("YT Server",Youtube_Player(url)))
					
                if 'uploadc' in url:
                    print 'UPLOADC BULUNDU'
                    value.append(("UPLOADC Server",uploadc_Player(url)))
					
                if 'mail.ru' in url:
                    print 'MAILRU BULUNDU'
                    value.append(("MR Server",mailru_Player(url)))
	
                if 'http://www.videoslasher.com' in url:
                    value.append(("VS Server",Videoslasher_Player(url)))

                if "movshare" in url:
                    value.append(("MovShare",Divxshare_Player(url)))

                if "vimple" in url:
                    xbmc.executebuiltin('Notification("Beklenen Hata",vimple henuz cozulmedi.)')

                if "stream2k.com" in url:
                    value.append(("Stream2k",stream2k_Player(url)))

                if "video.az" in url:
                    value.append(("VideoAz",VideoAz_Player(url)))
                
                if "stagevu" in url:
                    value.append(("StageVu",stagevu_Player(url)))

                if "streamcloud" in url:
                    code=Streamcloud_Player(url)
                    if code:
                        value.append(("Streamcloud",code))

                if "nowvideo" in url:
                    value.append(("NowVideo",Divxshare_Player(url)))

                if "yesload" in url:
                    value.append(("Yesload",Yesload_Player(url)))

                if "putlocker" in url:
                    value.append(("Putlocker",Putlocker_Player(url)))

                if "sockshare" in url:
                    value.append(("Sockshare",Sockshare_Player(url)))

        if vk:
                print 'VK ILK OKUMA:'
                vk_sonuc=vk_Player(vk)
                for url in vk_sonuc:
                        value.append(("VK Server",url))
                        
        if  value:
            return value
        else:
            return UrlResolverPlayer(urlList)
####
def magix_player(name,url):
    

        if "mail.ru" in url:
            MailRu_Player(url)
        if "ok.ru" in url:
            ok_ru(url)

                
        else:
            
                          
            
            UrlResolverPlayer = url
            playList.clear()
            media = urlresolver.HostedMediaFile(UrlResolverPlayer)
            source = media
            if source:
                    url = source.resolve()
                    araclar.addLink(name,url,'')
                    araclar.playlist_yap(playList,name,url)
                    xbmcPlayer.play(playList)
####

def UrlResolverPlayer(urlList):
        value=[]
        print "URL listesi",urlList
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:
                print "URLRESOLVER url",url
                if url in url:
                    print 'URLRESOLVER LINK BULUNDU'
                    UrlResolverPlayer = url
                    media = urlresolver.HostedMediaFile(UrlResolverPlayer)
                    source = media
                    if source:
                            xbmc.executebuiltin('Notification(Dream-Clup!,URLRESOLVER Deneniyor)')
                            url = source.resolve()
                            value.append(("URLRESOLVER LINK",url))

        if  value:
            return value
        else:
            return False
#
def skk():
        req = urllib2.Request((base64.b64decode(df)));
        req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/2013000101 Firefox/10.0.1")
        login= __ayarlar__.getSetting((base64.b64decode(yl)))
        password= __ayarlar__.getSetting((base64.b64decode(kl)))
        data=urllib2.urlopen(req,(base64.b64decode(k))+login+(base64.b64decode(f))+password+(base64.b64decode(b))).read()
        response = urllib2.urlopen((base64.b64decode(r))+login+(base64.b64decode(qq))).read()
        match=re.compile('\((.*?)\)<br').findall(response)
        if (base64.b64decode(A)) in match[0] or (base64.b64decode(pl)) in match[0] or (base64.b64decode(c)) in match[0] or (base64.b64decode(ktk)) in match[0] or (base64.b64decode(tr)) in match[0] or (base64.b64decode(ss)) in match[0] or (base64.b64decode(ttt)) in match[0]:
                __ayarlar__.setSetting('var',"True")
                return True
        else:
                d = xbmcgui.Dialog()
                d.ok(__ayarlar__.getLocalizedString(30001),__ayarlar__.getLocalizedString(30002),__ayarlar__.getLocalizedString(30003))
                d.ok(__ayarlar__.getLocalizedString(30004),__ayarlar__.getLocalizedString(30005),__ayarlar__.getLocalizedString(30006))
                __ayarlar__.setSetting('var',"False")
                return False
                EXIT()
def rebeka():
        d = xbmcgui.Dialog()
        login=__ayarlar__.getSetting("var")
        if not login or login=="False":
                global insidans
                if insidans==1:
                        cevap=d.yesno(__ayarlar__.getLocalizedString(30007),__ayarlar__.getLocalizedString(30008),__ayarlar__.getLocalizedString(30009),__ayarlar__.getLocalizedString(30010))
                        if cevap:
                                __ayarlar__.openSettings()
                                check=skk()
                        else:
                                __ayarlar__.setSetting('var',"False")
                                EXIT()
                        insidans+=1
                else:
                        pass
        if __ayarlar__.getSetting("var")=="True":
                pass
        else:
                __ayarlar__.setSetting('var',"False")
                EXIT()

def sirala(IMAGES_PATH):
   # rebeka()
    for fileName in imps:
        thumbnail= os.path.join(IMAGES_PATH, fileName+".png")
        addDir(fileName, '[COLOR lightgreen][B]'+fileName+'[/B][/COLOR]' ,"main()", "",thumbnail)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
def kalala(IMAGES_PATH,url):
        dacka(url)
        sirala(IMAGES_PATH)
def hata():
        d = xbmcgui.Dialog()
        d.ok(__ayarlar__.getLocalizedString(30011),__ayarlar__.getLocalizedString(30012),__ayarlar__.getLocalizedString(30013))
def EXIT():
        xbmc.executebuiltin("XBMC.Container.Refresh(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")


###########################MAIL-RU-PLAYER######################################
##referer='http://img.mail.ru/r/video2/uvpv3.swf?3'
##cookie='VID=2SlVa309oFH4; mrcu=EE18510E964723319742F901060A; p=IxQAAMr+IQAA; video_key=203516; s='
##UA='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
##
def MailRu_Player(url):
    req = urllib2.Request(url)

    resp = urllib2.urlopen(req)
    html = resp.read()
    cookie_string = resp.headers.getheader('Set-Cookie').split(';')[0]

    print resp.headers.getheader('Set-Cookie')
    headers = {
        'Cookie': cookie_string
    }

    metadata_url_start = html.find('metadataUrl') + len('metadataUrl":"')
    metadata_url_end = html.find('"', metadata_url_start)
    metadata_url = html[metadata_url_start:metadata_url_end]

    metadata_response =  urllib2.urlopen(metadata_url)
    metadata = json.loads(metadata_response.read()) 

    #---------------------------------#
    xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
    streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
    for name,url in streams:
            araclar.addLink('[COLOR lightblue][B]M_R >>  [/B][/COLOR]'+name,url,'')
    #---------------------------------#
####    safe='aHR0cDovL3hibWN0ci50di8='
####    link=araclar.get_url(base64.b64decode(safe))
####    match1=re.compile('besir>>(.*?)<<besir').findall(link)
####    for kkk in match1:
####            print kkk
##    
##    name='a'
##    m = _regex(url)
##    if m:
##        items = []
##        headers = { "User-Agent":UA, "Referer":referer, "Cookie":cookie }
##        quality = "???"
##        vurl = m.group('url')
##        vurl = re.sub('\&[^$]*','',vurl)
##        data = araclar.get_url_headers('http://videoapi.my.mail.ru/videos/' + vurl + '.json', headers)
##        item = json.loads(data)
##        for qual in item[u'videos']:
##            if qual == 'hd':
##                quality = "480p"
##            else:
##                quality = "???"
##            link = 'http://videoapi.my.mail.ru/file/video/v'+vurl
##            items.append({'quality':quality, 'url':link+'|Cookie='+cookie+'|Referer='+referer})
##        resolved = sorted(items,key=lambda i:i['quality'])
##        return resolved[-1][u'url']
##    
##    
##
##def _regex(url):
##    return re.search('movieSrc=(?P<url>.+?)$', url, re.IGNORECASE | re.DOTALL)
##    
##    
##
##def _regex(url):
##    return re.search('movieSrc=(?P<url>.+?)$', url, re.IGNORECASE | re.DOTALL)
####################################
    #---------------------------------#
USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

def ok_ru(url):
        fileName ="cozucu"


        sources = []

        if(re.search(r'ok.ru', url)):
            
               # try:
            id = re.search('\d+', url).group(0)
            jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
            jsonSource = json.loads(http_req(jsonUrl))
            
            for source in jsonSource['videos']:
                    name = '%s %s' % ('', source['name'])
                    link = '%s|User-Agent=%s&Accept=%s&Referer=%s' % (source['url'], USER_AGENT, ACCEPT, urllib.quote_plus(url))
                    #item = {'name': name, 'url': link}
                    #sources.append(item)
                    url = link
                    print url
                    araclar.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "yeni4(name,url)",url,"")
               # except: pass
        #return sources

def http_req(url, getCookie=False):
	req = urllib2.Request(url)
	req.add_header('User-Agent', USER_AGENT)
	req.add_header('Accept', ACCEPT)
	req.add_header('Cache-Control', 'no-transform')
	response = urllib2.urlopen(req)
	source = response.read()
	response.close()
	if getCookie:
		cookie = response.headers.get('Set-Cookie')
		return {'source': source, 'cookie': cookie}
	return source

def yeni4(name,url):
        xbmcPlayer = xbmc.Player() 
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
        playList.clear() 
        araclar.addLink(name,url,'')
        listitem = xbmcgui.ListItem(name) 
        playList.add(url, listitem) 
        xbmcPlayer.play(playList)




