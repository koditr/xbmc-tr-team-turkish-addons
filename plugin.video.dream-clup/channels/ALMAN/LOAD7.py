# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="LOAD7"

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


def main():
        buggalo.SUBMIT_URL = denemesite
        try:        
                try:
                        html = xbmctools1.loads7()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Load7Search()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        html = xbmctools1.loads7()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link>').findall(web)
                                                for name,url in tr:
                                                        name=ifix.decode_fix(name)
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
                soup = BeautifulSoup(link)
                panel = soup.findAll("td", {"class": "archiveEntries"},smartQuotesTo=None)
                panel = panel[0].findAll("div", {"class": "eMessage"})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('a')['href']
                        name=replace_fix(name)
                        name=name_fix(name)
                        thumbnailgelen=panel[i].find('p')
                        thumbnail=thumbnailgelen.find('img')['src'].encode('utf-8', 'ignore')
                        thumbnail=replace_fix(thumbnail)
                        thumbnail='http://loads7.com/'+thumbnail
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]',"Linkler(url)",url,thumbnail,thumbnail)
                        

                                 
                url=url
                page=re.compile('<a class=".*?" href="(.*?)" onclick=".*?"><span>.*?</span').findall(link)
                #<a class=".*?" href="(.*?)" onclick=".*?"><span>.*?</span
                for url1 in page:
                        url=url+url1
                        xbmctools1.addDir(fileName,'[COLOR purple][B]>>'+'Sayfa [/B][/COLOR]',"Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")

        except Exception:
                buggalo.onExceptionRaised()
def Load7Search():
        buggalo.SUBMIT_URL = denemesite
        try:        
                keyboard = xbmc.Keyboard("", 'Search', False)
                keyboard.doModal()
                if keyboard.isConfirmed():
                    query = keyboard.getText()
                    query=query.replace(' ','+')
                    query=name_fix(query)
                                
                try:
                    xbmctools1.addDir(fileName,'[COLOR blue][B]-----LOADS7-----[/B][/COLOR]', "","","Search")
                    Url = ('http://loads7.com/search/?q='+query)
                    link=xbmctools1.get_url(Url)
                    soup = BeautifulSoup(link)
                    panel = soup.findAll("td", {"valign": "top", "style": "padding:0px 10px 0px 10px;", },smartQuotesTo=None)
                    panel = panel[0].findAll("div", {"class": "eTitle"})
                    for i in range (len (panel)):
                            url=panel[i].find('a')['href']
                            name=panel[i].find('a').text
                            xbmctools1.addDir(fileName,'[COLOR lightgreen][B]>> -'+name+'[/B][/COLOR]', "Linkler(url)",url,'')
                except:
                    xbmc.executebuiltin('Notification("[COLOR yellow][B]xbmcTR[/B][/COLOR]","[COLOR yellow][B]Loads7 Acilamadi[/B][/COLOR]")')
        except Exception:
                buggalo.onExceptionRaised()
def Linkler(url):
        buggalo.SUBMIT_URL = denemesite
        try:
        ##        web='aHR0cDovL3NpbmVtYS54Ym1jdHIudHYv'
        ##        link=xbmctools1.get_url(base64.b64decode(web))
        ##        match=re.compile('<li><a href="#" class="toplam">(.*?)</a></li>').findall(link)
        ##        for bul in match:
        ##                bul=''
        ##                print bul
                link=xbmctools1.get_url(url)
                match=re.compile('http:\/\/streamcloud.eu\/(.*?)"').findall(link)
                for url in match:
                        url='http://streamcloud.eu/'+url
                        print url
                        xbmctools1.addDir(fileName,'Streamcloud >>',"cozuculer1.magix_player(name,url)",url,'')
                match1=re.compile('http://www.nowvideo.sx/video/(.*?)"').findall(link)
                for url in match1:
                        url='http://www.nowvideo.sx/video/'+url
                        xbmctools1.addDir(fileName,'NowVideo >>',"cozuculer1.magix_player(name,url)",url,'')
                match3=re.compile('http:\/\/www.movshare.net\/video\/(.*?)"').findall(link)
                for url in match3:
                        url='http://www.movshare.net/video/'+url
                        xbmctools1.addDir(fileName,'MoVShr >>',"cozuculer1.magix_player(name,url)",url,'')
                match4=re.compile('"http:\/\/www.youtube.com\/embed\/(.*?)\?').findall(link)
                for url in match4:
                        url='http://www.youtube.com/embed/'+url
                        xbmctools1.addDir(fileName,'YouTube >>',"cozuculer1.magix_player(name,url)",url,'')
        except Exception:
                buggalo.onExceptionRaised()              
##def streamcloud(name,url):
##        playList.clear()
##        link=xbmctools1.get_url(url)  
##        match=re.compile('http:\/\/streamcloud.eu\/(.*?).avi.html').findall(link)
##        print match
##        for url in match:
##                url='http://streamcloud.eu/'+url+'.avi.html'
##                print url
##                Sonuc=cozuculer1.videobul(url)
##                print "donen sonuc",Sonuc
##                if Sonuc=="False":
##                        dialog = xbmcgui.Dialog()
##                        i = dialog.ok(name,"Site uyarisi","     Film Siteye henuz yuklenmedi   ","  Yayinlandiktan sonra yüklenecektir.  ")
##                        return False 
##                else:                                
##                        for name,url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
##                                        xbmctools1.addLink(name,url,'')
##                                        xbmctools1.playlist_yap(playList,name,url) 
##                        xbmcPlayer.play(playList)
##def NowVideo(name,url):
##        playList.clear()
##        link=xbmctools1.get_url(url)  
##        match=re.compile('http://www.nowvideo.eu/video/(.*?)"').findall(link)
##        print match
##        for url in match:
##                url='http://www.nowvideo.eu/video/'+url
##                print url
##                Sonuc=cozuculer1.videobul(url)
##                print "donen sonuc",Sonuc
##                if Sonuc=="False":
##                        dialog = xbmcgui.Dialog()
##                        i = dialog.ok(name,"Site uyarisi","     Film Siteye henuz yuklenmedi   ","  Yayinlandiktan sonra yüklenecektir.  ")
##                        return False 
##                else:                                
##                        for name,url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
##                                        xbmctools1.addLink(name,url,'')
##                                        xbmctools1.playlist_yap(playList,name,url) 
##                        xbmcPlayer.play(playList)
       


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
