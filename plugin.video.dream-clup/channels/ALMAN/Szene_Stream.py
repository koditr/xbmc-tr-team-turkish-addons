# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')

fileName ="Szene_Stream"


__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

denemesite = 'https://koditr.org/denemebugalo/submit.php'

buggalo.SUBMIT_URL = denemesite
try:
        html = xbmctools1.szenestreams()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        match = re.compile('<!--#(.*?)-->').findall(html)
        for web in match:
                web=xbmctools1.angel(base64.b64decode(web))
                tr=re.compile('<site>(.*?)</site>').findall(web)
                for sinema in tr:
                        sinema=sinema
except Exception:
        buggalo.onExceptionRaised()

def main():
        buggalo.SUBMIT_URL = denemesite
        try:        
                try:
                        html = xbmctools1.szenestreams()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
        ##                                xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Search()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Neue Filme [/B][/COLOR]', "Yeni2(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.szenestreams()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link>').findall(web)
                                                for name,url in tr:
                                                        name=ifix.decode_fix(name)
                                                        name=name.replace('&#8211','').replace('&','')
                                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yeni(url)",url,'','')

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()


        except Exception:
                buggalo.onExceptionRaised()              
def Yeni(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                
                link=xbmctools1.get_url(url)
                match=re.compile('<img src="(.*?)" class=".*?" style="" alt="(.*?)" width=".*?" height=".*?"></a></div>\n\n</div>\n</div>\n</div>\n</div> \n<div style=".*?" align=".*?">\n\n<span style=".*?">\n<img style=".*?" src=".*?" alt=".*?" title=".*?" border=".*?"> <b style=".*?">.*?</b>\n</span>\n\n<span style=".*?"></span>\n\n<span style=".*?">\n<img style=".*?" src=".*?" alt=".*?" title=".*?" border=".*?"> <b style=".*?">.*?</b>\n</span>\n</div>\n</td> \n\n\n<td style=".*?" valign=".*?">\n\n<div style=".*?" align=".*?"><b><a class=".*?" <a="" href="(.*?)">').findall(link)
                for thumbnail,name,url in match:
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]',"Linkler(url)",url,thumbnail,thumbnail)
                        
                url=url
                page=re.compile('<span>.*?</span></b> <a class="swchItem" href="(.*?)" onclick=".*?"><span>(.*?)</span>').findall(link)
                                 #<span>.*?</span></b> <a class="swchItem" href="(.*?)" onclick=".*?"><span>(.*?)</span>
                for url1,name in page:
                    if page >1:
                            del page[1]
                            url=url+url1
                            
                        
                            xbmctools1.addDir(fileName,'[COLOR purple][B]>>'+'Sayfa ' + name+'[/B][/COLOR]',"Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")
        except Exception:
                buggalo.onExceptionRaised()
def Yeni2(url):
        buggalo.SUBMIT_URL = denemesite
        try:        
    
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("div", {"style": "float:left; width:50%;"},smartQuotesTo=None)
                for i in range (len (panel)):
                        

                        div1=panel[i].findAll("div", {"class": "ImgWrapNews"},smartQuotesTo=None)
                        thumbnail=panel[i].find('a')['href'].encode('ISO-8859-1', 'ignore')
                        name=panel[i].find('img')['alt'].encode('ISO-8859-1', 'ignore')
                        div2=panel[i].findAll("a", {"class": "newstitl entryLink"},smartQuotesTo=None)
                        url= div2[0]['href']
                        url=url
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]',"Linkler(url)",url,thumbnail,thumbnail)
                        

                                 

                page=re.compile('<b class="swchItemA"><span>.*?</span></b>  <a class="swchItem" href="(.*?)" onclick=".*?"><span>(.*?)</span>').findall(link)       
                for url,name in page:
                    if page >1:
                            del page[1]
                            
                        
                            xbmctools1.addDir(fileName,'[COLOR purple][B]>>'+'Sayfa ' + name+'[/B][/COLOR]',"Yeni2(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")
        except Exception:
                buggalo.onExceptionRaised()

def Linkler(url):
        link=xbmctools1.get_url(url)
##        match=re.compile('src="http://www.youtube.com/embed/(.*?)"').findall(link)
##        for url in match:
##                url='http://www.youtube.com/embed/'+url                
##                xbmctools1.addDir(fileName,'Trailer >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match1=re.compile('href="\n\nhttp://vidstream.in/(.*?)\n\n">').findall(link)
        for url in match1:
                url='http://vidstream.in/'+url                
                xbmctools1.addDir(fileName,'VidStream    >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match2=re.compile('href="\n\nhttp://www.divxstage.eu/video/(.*?)\n\n">').findall(link)
        for url in match2:
                url='http://www.divxstage.eu/video/'+url                
                xbmctools1.addDir(fileName,'DivxStage    >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match3=re.compile('href="\n\nhttp://primeshare.tv/download/(.*?)\n\n">').findall(link)
        for url in match3:
                url='http://primeshare.tv/download/'+url                
                xbmctools1.addDir(fileName,'PrimeShare    >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match4=re.compile('href="\n\nhttp://www.movshare.net/video/(.*?)\n\n">').findall(link)
        for code in match4:
                code=''                
                xbmctools1.addDir(fileName,'MovShare    >>',"NowVideo(name,url)",url,'')
                
        match9=re.compile('href="\n\nhttp://www.nowvideo.sx/video/(.*?)\n\n">').findall(link)
        for url in match9:
                url='http://www.nowvideo.sx/video/'+url
                xbmctools1.addDir(fileName,'NowVideo    >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match8=re.compile(' href="\n\nhttp://streamcloud.eu/(.*?)\n\n"><img alt="" src=".*?" ').findall(link)
        for url in match8:
                url='http://streamcloud.eu/'+url
                xbmctools1.addDir(fileName,'Stream Cloud   >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match5=re.compile('href="http://played.to/(.*?)">').findall(link)
        for url in match5:
                url='http://played.to/'+url                
                xbmctools1.addDir(fileName,'Played   >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match6=re.compile('<a target="_blank" href="\n\nhttp://xvidstage.com/(.*?)\n\n">').findall(link)
        for url in match6:
                url='http://xvidstage.com/'+url                
                xbmctools1.addDir(fileName,'XvidStage   >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match7=re.compile('href="http://faststream.in/(.*?)">').findall(link)
        for url in match7:
                url='http://faststream.in/'+url                
                xbmctools1.addDir(fileName,'FastStream   >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match10=re.compile('href="http://youwatch.org/(.*?)">').findall(link)
        for url in match10:
                url='http://youwatch.org/'+url
                xbmctools1.addDir(fileName,'YouWATCH   >>',"cozuculer1.magix_player(name,url)",url,'')
                
        match11=re.compile('<a target="_blank" href="\n\nhttp://www.flashx.tv/(.*?)\n\n">').findall(link)
        for url in match11:
                url='http://www.flashx.tv/'+url                
                xbmctools1.addDir(fileName,'FlashX   >>',"cozuculer1.magix_player(name,url)",url,'')
        match12=re.compile('<a target="_blank" href="\n\nhttp://www.cloudtime.to/video/(.*?)\n\n">').findall(link)
        for url in match12:
                url='http://www.cloudtime.to/video/'+url                
                xbmctools1.addDir(fileName,'CloudTime  >>',"cozuculer1.magix_player(name,url)",url,'')

       


def name_fix(x):        
        x=x.replace('-',' ').replace('_',' ')
        return x[0].capitalize() + x[1:]
        
def replace_fix(x):        
        x=x.replace('&#8211;', '-').replace('&#038;', '&').replace('http://loads7.com/blog/', '').replace('http://loads7.com', '').replace(' ', '')
        return x
       

def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
