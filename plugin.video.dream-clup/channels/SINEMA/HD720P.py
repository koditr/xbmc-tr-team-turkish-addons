# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import base64
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="HD720P"

__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

denemesite='https://koditr.org/denemebugalo/submit.php'


def main():
        buggalo.SUBMIT_URL = denemesite
        try:
        
                try:
                        html = xbmctools1.hd720p()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Arama()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Filmler [/B][/COLOR]', "Recent(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.hd720p()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link>').findall(web)
                                                for name,url in tr:
                                                        name=ifix.decode_fix(name)
                                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Recent(url)",url,'','')

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()

        except Exception:
                buggalo.onExceptionRaised()                                     
######                       
def Arama():
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.hd720p()
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
                                        query=query.replace(' ','+')
                                        url = (sinema+'/?s='+query)
                                        Recent(url)

        except Exception:
                buggalo.onExceptionRaised()
############
def Recent(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)  
                soup = BeautifulSoup(link)
                panel = soup.findAll("section", {"class": "film-kapla"},smartQuotesTo=None)
                panel = panel[0].findAll("div", {"class": "film-kutu-resim"})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('a').text
                        name=name.encode('utf-8', 'ignore')
                        name=name_fix(name)
                        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR orange]>>[COLOR beige][B]'+name+'[/B][/COLOR]',"ayrisdirma(url)",url,thumbnail,thumbnail)
                page=re.compile('<link rel=\'next\' href=\'(.*?)\' />\n\n').findall(link)
                for url in page:
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>> Sonraki SAYFA-> [/B][/COLOR]',"Yeni(url)",url,"https://koditr.org/changelog/sonrakisayfa.png")                     
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def ayrisdirma(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                url=url+'/8'

                listeler=[]
                urller=[]
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel=soup.find("div", {"class": "partlar"})
                for a in panel.findAll('a'):
                    url=a['href']
                    name= a.text
                    if "Fragman" in name:
                            pass
                    else:
                            
                            xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR][COLOR beige][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')

        except Exception:
                buggalo.onExceptionRaised()
def name_fix(x):        
        x=x.replace('&#8211;','-')
        return x[0].capitalize() + x[1:]

def replace_fix(x):        
        x=x.replace('–', '-').replace('&', '&').replace('&amp;', '&')
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
                vk_2=re.compile('video_ext.php(.*?)"').findall(link)
                for url in vk_2:
                        url = 'http://vk.com/video_ext.php'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
        ##        youtube=re.compile('\/embed\/(.*?)"').findall(link)
        ##        for url in youtube:
        ##                url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
        ##                cozuculer1.magix_player(name,url)
        ##		#---------------------------------------------#
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



def replace_fix(x):        
        x=x.replace('–', '-').replace('&', '&').replace('&amp;', '&')
        return x

