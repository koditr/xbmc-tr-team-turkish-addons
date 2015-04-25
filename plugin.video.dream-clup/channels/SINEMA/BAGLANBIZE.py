# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import base64
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import time
import json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')

fileName ="BAGLANBIZE"


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
                        html = xbmctools1.baglanbize()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Arama()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Filmler [/B][/COLOR]', "baglanfilmizleRecent(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.baglanbize()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link>').findall(web)
                                                for name,url in tr:
                                                        name=ifix.decode_fix(name)
                                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "baglanfilmizleRecent(url)",url,'','')

                                

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()
        except Exception:
                buggalo.onExceptionRaised()
def Kategoriler():
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.baglanbize()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link>').findall(web)
                        for name,url in tr:
                                name=ifix.decode_fix(name)
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "baglanfilmizleRecent(url)",url,'','')



        except Exception:
                buggalo.onExceptionRaised()
def baglanfilmizleRecent(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("article", {"id": "article"},smartQuotesTo=None)
                panel = panel[0].findAll("div", {"class": "T-FilmResim"})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('a').text.encode('utf-8', 'ignore')
                        name=ifix.decode_fix(name)
                        name=name.replace('&#8211;','').replace('&#8217;','').replace('&#038;','')
                        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]', "ayrisdirma(name,url)",url,thumbnail,thumbnail)
                page=re.compile('<li class="active_page"><a href=".*?">.*?</a></li>\n<li><a href="(.*?)">(.*?)</a>').findall(link)
                for Url,name in page:
                        xbmctools1.addDir(fileName,'[COLOR blue][B]Sayfa>>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "baglanfilmizleRecent(url)",Url,"https://koditr.org/changelog/sonrakisayfa.png")
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def Arama():
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.baglanbize()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<site>(.*?)</site>').findall(web)
                        for sinema in tr:
                                keyboard = xbmc.Keyboard("", 'Search', False)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                    query = keyboard.getText()
                                    url = (sinema+'/?s='+query)
                                    baglanfilmizleRecent(url)

        except Exception:
                buggalo.onExceptionRaised()


def ayrisdirma(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
               # xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]'+'Part 1'+'[/B][/COLOR]', "VIDEOLINKS(name,url)",url,"")
                url=url+'/6'
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("ul", {"class": "partlar"})
                match=re.compile('<a href="(.*?)">(.*?)</a>').findall(str(panel[0]))
                for url,name in match:
                        if "Fragman" in name:
                                pass
                        else:                        
                                if "FRAGMAN" in name:
                                        pass
                                else:
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,"")	
        except Exception:
                buggalo.onExceptionRaised()
##def baglanfilmizleRecent2(Url):
##        link=xbmctools1.get_url(Url)
##        soup = BeautifulSoup(link)
##        panel = soup.findAll("span", {"class": "filmm sol"})
##        for i in range (len (panel)):
##                gelenurl=panel[i].find("div", {"class": "bt"})
##                url=gelenurl.find('a')['href'].encode('utf-8', 'ignore')
##                name=panel[i].find("div", {"class": "bs"}).text.encode('utf-8', 'ignore')
##                name=name.replace('&#8211','').replace('&#8217','')
##                img=re.compile('src="(.*?)"').findall(str(panel[i]))
##                for a in img:
##                    if not "bt" in a:
##                            thumbnail =a
##                xbmctools1.addDir(fileName,'[COLOR cyan][B]'+name+'[/B][/COLOR]', "ayrisdirma(name,url)",url+'/30',thumbnail)
##        page=re.compile('<a class=\'aktif\'>.*?</a><a href=\'(.*?)\' class=\'inaktif\' >(.*?)</a>').findall(link)
##        for Url,name in page:
##                xbmctools1.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "baglanfilmizleRecent2(url)",Url,"https://koditr.org/changelog/sonrakisayfa.png")
##        page2=re.compile('<link rel=\'prev\' href=\'(.*?)\' />').findall(link)
##        for Url in page2:
##                xbmctools1.addDir(fileName,'[COLOR red][B]Onceki Sayfa[/B][/COLOR]', "baglanfilmizleRecent2(url)",Url,"onceki")

def name_fix(x):        
        x=x.replace('-',' ')
        return x[0].capitalize() + x[1:]

def replace_fix(x):        
        x=x.replace('&#8211;', '-').replace('&#038;', '&').replace('&amp;', '&')
        return x

def VIDEOLINKS(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                urlList=[]
                #---------------------------#
                playList.clear()
                link=xbmctools1.get_url(url)
                link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')

                        #---------------------------------------------#
                vk_2=re.compile('vk.com\/(.*?)"').findall(link)
                for url in vk_2:
                        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                youtube=re.compile(' src\="\/\/www.youtube.com\/embed\/(.*?)"').findall(link)
                for url in youtube:
                        url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                youtube2=re.compile(' src="https://www.youtube.com\/embed\/(.*?)"').findall(link)
                for youurl in youtube2:
                        url = 'http://www.youtube.com/embed/'+str(youurl).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                mailru=re.compile('http:\/\/.*?\/mail\/(.*?).html').findall(link)
                for mailrugelen in mailru:
                        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(mailrugelen)+'.html'
                        
                        value=[]
                        value.append((name,cozuculer1.MailRu_Player(url)))
                ok=re.compile('http:\/\/ok.ru\/videoembed\/(.*?)"').findall(link)
                for mailrugelen in ok:
                        url = 'http://ok.ru/videoembed/'+str(mailrugelen)
                       
                        value=[]
                        value.append((name,cozuculer1.ok_ru(url)))
                        #---------------------------------------------#
                if not urlList:
                        match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                        print match
                        if match:
                                for url in match:
                                        VIDEOLINKS(name,url)
               
                if urlList:
                        Sonuc=playerdenetle(name, urlList)
                        for name,url in Sonuc:
                                xbmctools1.addLink(name,url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                        xbmcPlayer.play(playList)
        except Exception:
                buggalo.onExceptionRaised()     
def playerdenetle(name, urlList):
        value=[]
        import cozuculer1
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:


                if "mail.ru" in url:
                    value.append((name,cozuculer1.MailRu_Player(url)))
                    
        if  value:
            return value


def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
