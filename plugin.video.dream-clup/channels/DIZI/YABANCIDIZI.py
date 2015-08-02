# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo



Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="YABANCIDIZI"


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
                        html = xbmctools1.yabancidizi()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Diziler [/B][/COLOR]', "soupfilm(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        #xbmctools1.addDir(fileName,'[COLOR beige][B]>>[/B][/COLOR] [COLOR orange][B]Alfabetik Siraya Gore Diziler [/B][/COLOR]', "alfabetik()",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        link=xbmctools1.get_url(sinema)
                                        soup = BeautifulSoup(link)
                                        panel = soup.findAll("ul", {"class": "category-list"})
                                        liste=BeautifulSoup(str(panel))
                                        for li in liste.findAll('li'):
                                                a=li.find('a')
                                                url= a['href']
                                                name=li.text.encode('utf-8', 'ignore')
                                                name=ifix.decode_fix(name)
                                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "diziicerik(url)",url,'','')

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()
        except Exception:
                buggalo.onExceptionRaised()


def alfabetik():
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.yabancidizi()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<site>(.*?)</site>').findall(web)
                        for sinema in tr:
                                link=xbmctools1.get_url(sinema)
                                soup = BeautifulSoup(link)
                                panel = soup.findAll("main", {"id": "main-wrapper"},smartQuotesTo=None)
                                panel = panel[0].findAll("ul", {"class": "alphabetical-category-index list-inline"})
                                liste=BeautifulSoup(str(panel))
                                for li in liste.findAll('li'):
                                        a=li.find('a')
                                        url= a['href']
                                        name=li.text.encode('utf-8', 'ignore')
                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "alfabetiksirala(url)",url,'','')

        except Exception:
                buggalo.onExceptionRaised()

       
def alfabetiksirala(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.yabancidizi()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<site>(.*?)</site>').findall(web)
                        for sinema in tr:
                                link=xbmctools1.get_url(sinema)
                                soup = BeautifulSoup(link)
                                panel = soup.findAll("main", {"id": "main-wrapper"},smartQuotesTo=None)
                                panel = panel[0].findAll("ul", {"data-index": url})
                                liste=BeautifulSoup(str(panel))
                                for li in liste.findAll('li'):
                                    a=li.find('a')
                                    url= a['href']
                                    name=li.text.encode('utf-8', 'ignore')
                                    xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "diziicerik(url)",url,'','')
        
        except Exception:
                buggalo.onExceptionRaised()        

def soupfilm(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("section", {"id": "recent-posts"},smartQuotesTo=None)
                panel = panel[0].findAll("article", {"class": "poster-article "})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        div1=panel[i].findAll("figure", {"class": "figure cover"},smartQuotesTo=None)
                        name=div1[0].find('img')['alt'].encode('utf-8', 'ignore')
                        thumbnail=div1[0].find('img')['src'].encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR lightblue][B]>> [/B][/COLOR]'+'[COLOR lightgreen][B]' + name+'[/B][/COLOR]',"ayrisdirma(url)",url,thumbnail)
                page=re.compile('<link rel=\'next\' href=\'(.*?)\'/>').findall(link)
                thumbnail="special://home/addons/plugin.video.dream-clup/resources/images/sonrakisayfa.png"
                for url in page:
                        name="Sonraki Sayfa"
                        url=str(url)
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>>'+name+'[/B][/COLOR]',"soupfilm(url)",url,thumbnail)
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
        


def sezonicerik(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("div", {"id": "seasons-list"})
                match=re.compile('<a href="(.*?)" class="season-button ">(.*?)</a>').findall(str(panel))
                for url,name in match:
                        xbmctools1.addDir(fileName,'[COLOR lightblue][B]>> [/B][/COLOR]'+'[COLOR lightgreen][B]' + name+'[/B][/COLOR]',"ayrisdirma(url)",url,'')
        except Exception:
                buggalo.onExceptionRaised()


def diziicerik(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("section", {"id": "category-posts"},smartQuotesTo=None)
                panel = panel[0].findAll("div", {"class": "post-title"})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('a').text.encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR lightblue][B]>> [/B][/COLOR]'+'[COLOR lightgreen][B]' + name+'[/B][/COLOR]',"ayrisdirma(url)",url,'')
        except Exception:
                buggalo.onExceptionRaised()
def ayrisdirma(url):
        url=url+'/15'
        url=url.replace('//15','/15')
        link=xbmctools1.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "video-toolbar"})
        match=re.compile('<option value="(.*?)">(.*?)</option>').findall(str(panel))
        for url,name in match:
                if "My" in name:
                        pass
                else:
                        if "Met" in name:
                                pass
                        else:
                                if "Raj" in name:
                                        pass
                                else:
                                        if "Hut" in name:
                                                pass
                                        else:
                                                if "Cl" in name:
                                                        pass
                                                else:
                                                        if "Pl" in name:
                                                                pass
                                                        else:
                                                                if "Ve" in name:
                                                                        pass
                                                                else:
##                                                                        url='http://www.dizibox.com/'+url
                                                                        xbmctools1.addDir(fileName,'[COLOR lightblue][B]>> [/B][/COLOR]'+'[COLOR lightgreen][B]' + name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')
                
 
                
def VIDEOLINKS(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:        
                #---------------------------#
                urlList=[]
                #---------------------------#
                playList.clear()
                link=xbmctools1.get_url(url)
                link=link.replace('&amp;', '&').replace('&', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/').replace("&#038;","&")
                ok=re.compile('http:\/\/play.dizibox.net\/dbx.php\?.*?v\=aH(.*?)"').findall(link)
                
                for url in ok:
                      url='aH'+url
                      url=(base64.b64decode(url))
                      name='OK-Ply'
                      cozuculer1.ok_ru(url)

                ok5=re.compile('http:\/\/play.dizibox.net\/dbx.php\?.*?v\=aH(.*?)&sub=.*?.srt"').findall(link)
                
                for url in ok5:
                      url='aH'+url
                      url=(base64.b64decode(url))
                      name='OK-Ply'
                      cozuculer1.ok_ru(url)
                      
                ok1=re.compile('src="http:\/\/odnoklassniki.ru\/videoembed\/(.*?)"').findall(link)
                for url in ok1:
                        url='http://ok.ru/videoembed/'+url
                        name='OK-Ply'
                        cozuculer1.magix_player(name,url)
                ok2=re.compile('src="http://ok.ru\/videoembed\/(.*?)"').findall(link)
                for url in ok2:
                        url='http://ok.ru/videoembed/'+url
                        name='OK-Ply'
                        cozuculer1.magix_player(name,url)
                                                
                vk1=re.compile('src="http:\/\/www.dizibox.org\/Vkplayer\/(.*?)"').findall(link)
                for url in vk1:
                        url=url.replace('&#038;', '&').replace('&', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                        url='http://vk.com/'+url
                        name='Vk-Ply'
                        cozuculer1.magix_player(name,url)
                vk9=re.compile('http://vk.com/dbx.php\?v\=(.*?)"').findall(link)

                for url in vk9:
                        url=(base64.b64decode(url))

                        #url=url.replace('&#038;', '&').replace('&', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                        url='http://vk.com/'+url
                        name='Vk-Ply'
                        cozuculer1.magix_player(name,url)

                vk8=re.compile('http://play.dizibox.net/vk/?(.*?)"').findall(link)

                for url in vk8:
                

##                        url=url.replace('&#038;', '&').replace('&', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                        url='http://vk.com/video_ext.php'+url
                        name='Vk-Ply'
                        cozuculer1.magix_player(name,url)
                mailru=re.compile('http:\/\/.*?\/mail\/(.*?).html').findall(link)
                for mailrugelen in mailru:
                        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(mailrugelen)+'.html'
                        value=[]
                        value.append((name,cozuculer1.MailRu_Player(url)))
                        #---------------------------------------------#
                mailru2=re.compile('src=".*?mail.*?mail/(.*?).html"').findall(link)
                for mailrugelen in mailru2:
                        url = 'http://video.mail.ru/movieSrc=/mail/'+mailrugelen+'&autoplay=0'
                        urlList.append(url)
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


