# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="DIZIHD"
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')




def main(): 
                
##                try:
        html = xbmctools1.dizihd()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        match = re.compile('<!--Dizi(.*?)-->').findall(html)
        for web in match:
                web=xbmctools1.angel(base64.b64decode(web))
                tr=re.compile('<site>(.*?)</site>').findall(web)
                for sinema in tr:
                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Arama()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Diziler [/B][/COLOR]', "Recent(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
        match1 = re.compile('<!--Dizi(.*?)-->').findall(html)
        for web in match1:
                web=xbmctools1.angel(base64.b64decode(web))
                tr=re.compile('<kat>(.*?)</kat>').findall(web)
                for url in tr:
                        link=xbmctools1.get_url(url)
                        soup = BeautifulSoup(link)
                        panel = soup.findAll("div", {"class": "sidebar-right"})
                        liste=BeautifulSoup(str(panel))
                        for li in liste.findAll('li'):
                                a=li.find('a')
                                url= a['href']
                                name=li.text.encode('utf-8', 'ignore')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Recent(url)",url,'','')

                                
##                except:
##                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
##                        dialog = xbmcgui.DialogProgress()
##                        dialog1 = xbmcgui.Dialog()
##                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
##                        sys.exit()

###################################################################                
                                               
######                       
def Arama():

               
                html = xbmctools1.dizihd()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--Dizi(.*?)-->').findall(html)
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
                xbmctools1.addDir(fileName,'[COLOR yellow][B]YENI ARAMA YAP[/B][/COLOR]', "Arama()","","Arama")


def Recent(url):

                
        link=xbmctools1.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "leftC"})
        panel = panel[0].findAll("div", {"class": "moviefilm"})
        for i in range (len (panel)):
                url=panel[i].find("a")['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')        
                xbmctools1.addDir(fileName,'[COLOR beige][B]'+name+'[/B][/COLOR]',"Part(name,url)",url,thumbnail,thumbnail)


        #sayfalama basladi
        page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
        thumbnail="special://home/addons/plugin.video.dream-clup/resources/images/sonrakisayfa.png"
        for url,name in page:
                name="Sonraki Sayfa"
                url=str(url)
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>>'+name+'[/B][/COLOR]',"Recent(url)",url,thumbnail)
        xbmc.executebuiltin("Container.SetViewMode(500)")

def Part(name,url):
        url=url+"/9"
        link=xbmctools1.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "keremiya_part"})
        match=re.compile('<a href="(.*?)"><span>(.*?)</span></a>').findall(str(panel))
        for url,name in match:
                xbmctools1.addDir(fileName,'[COLOR beige][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,"","")
        

def VIDEOLINKS(name,url):
        
        #---------------------------#
        urlList=[]
        #---------------------------#
        playList.clear()
        link=xbmctools1.get_url(url)
        link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')

                #---------------------------------------------#
        vk_2=re.compile('\/vk.com\/(.*?)"').findall(link)
        for url in vk_2:
                url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                name='[COLOR beige][B][COLOR orange]>>>   [/COLOR] V Server [/B][/COLOR]'
                cozuculer1.magix_player(name,url)
                #---------------------------------------------#

        mp4=re.compile('"http://vid.ag/(.*?)"').findall(link)
        for url in mp4:
                url="http://vid.ag/"+url
                link=xbmctools1.get_url(url)
                match4=re.compile(',{file:"(.*?)",label:"SD"}').findall(link)
                for url in match4:
                    print url
                    zong=""
                    print zong
                    xbmctools1.addDir(fileName,'[COLOR blue][B]Daily Server  > '+name+'[/B][/COLOR]',"cozuculer1.yeni4(name,url)",url,'')
        ok=re.compile('http:\/\/ok.ru\/videoembed\/(.*?)" ').findall(link)
        for mailrugelen in ok:
            
            url = 'http://ok.ru/videoembed/'+str(mailrugelen)
            xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> OK.RU > '+name+'[/B][/COLOR]',"cozuculer1.ok_ru(url)",url,'')

        cloudy=re.compile('https://www.cloudy.ec/embed.php\?id\=(.*?)"').findall(link)
        for mailrugelen in cloudy:
            url = 'https://www.cloudy.ec/embed.php?id='+str(mailrugelen)
            xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> Cloudy '+name+'[/COLOR]',"cozuculer1.cloudy(url)",url,'')
        youtube=re.compile('www.youtube.com/embed/(.*?)"').findall(link)
        for url in youtube:
                url=url.replace('?showinfo=0','')
                url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> Y Server  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'')

##                #---------------------------------------------#
        mailru=re.compile("_myvideo/(.*?)'").findall(link)
        for mailrugelen in mailru:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/bi.siktir1/_myvideo/'+str(mailrugelen)+'.html'
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> Mail Ru  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'') 
        dm=re.compile(' src="//www.dailymotion.com/embed/video/(.*?)" ').findall(link)
        if "x2fy4px" in dm:
            pass
        else:
            if "x2fy4pe" in dm:
                pass
            else:
                if "x2fy4q9" in dm:
                    pass
                else:
                    
                    for url in dm:            
                           
                        url = 'http://www.dailymotion.com/embed/video/'+str(url).encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> DM Server  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'')
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

def date_fix(x):        
        x=x.replace('January', 'Ocak').replace('February', 'Subat').replace('March', 'Mart').replace('April', 'Nisan').replace('May', 'Mayis').replace('June', 'Haziran').replace('July', 'Temmuz').replace('August', 'Agustos').replace('September', 'Eylul').replace('October', 'Ekim').replace('November', 'Kasim').replace('December', 'Aralik')
        return x

def name_fix(x):        
        x=x.replace('&#038;', '-')
        return x
