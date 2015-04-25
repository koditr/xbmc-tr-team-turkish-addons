# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

fileName ="Film_PALAST"

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
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
                        html = xbmctools1.filmplast()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Search()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Filmler [/B][/COLOR]', "neuead(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.filmplast()
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
                                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "neuead2(url)",url,'','')

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()
        except Exception:
                buggalo.onExceptionRaised()
#-----------------#
def neuead(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match1=re.compile('<a href="http://www.filmpalast.to/(.*?)" title="(.*?)">\n\t\t       \t   <img src="/files/(.*?)"').findall(link)
                for url,name,thumbnail in match1:
                        thumbnail='http://www.filmpalast.to/files/'+thumbnail
                        url='http://www.filmpalast.to/'+url
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]', "ayrisdirma(name,url)",url,thumbnail,thumbnail)
                        
                        #----#
                page=re.compile('<a class="pageing button-small rb active"  >.*?</a> <a  class="pageing button-small rb"  href=(.*?)>(.*?)</a>').findall(link)
                for url,name in page:
                        url='http://www.filmpalast.to/'+url
                        xbmctools1.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "neuead(url)",url,'')
        except Exception:
                buggalo.onExceptionRaised()
#-----------------#
def neuead2(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match1=re.compile('<a href="(.*?)" title=".*?"> <img src="(.*?)" class="cover-opacity" alt="(.*?)"').findall(link)
                for url,thumbnail,name in match1:
                        thumbnail='http://www.filmpalast.to'+thumbnail
                        name=name.replace('stream','')
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]', "ayrisdirma(name,url)",url,thumbnail,thumbnail)
                        #------#
                page=re.compile('class="pageing button-small rb active"  >.*?</a> <a  class="pageing button-small rb"   href=\'http://(.*?)\'>(.*?)</a>').findall(link)
                for url,name in page:
                        url='http://'+url
                        xbmctools1.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "neuead2(url)",url,'')
                        #-----#
                page2=re.compile('<a class="pageing button-small rb active"  >.*?</a> <a  class="pageing button-small rb"  href=(.*?)>(.*?)</a>').findall(link)
                for url,name in page2:
                        xbmctools1.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "neuead2(url)",url,'')
        except Exception:
                buggalo.onExceptionRaised()
#-----------------#
def ayrisdirma(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match3=re.compile('target="_blank" href="http:\/\/(.*?)\/(.*?)" >').findall(link)
                for name,a in match3:
                        

                        url='http://'+name+'/'+a
                        xbmctools1.addDir(fileName,'[COLOR red][B]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,"")
        except Exception:
                buggalo.onExceptionRaised()
#-----------------#          
def Search():
        buggalo.SUBMIT_URL = denemesite
        try:
                keyboard = xbmc.Keyboard("", 'Search', False)
                keyboard.doModal()
                if keyboard.isConfirmed():
                    query = keyboard.getText()
                    url = ('http://www.filmpalast.to/search/title/'+query)
                    neuead2(url)
        except Exception:
                buggalo.onExceptionRaised()
#-----------@xbmctrTeam---------------------------------#



def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
