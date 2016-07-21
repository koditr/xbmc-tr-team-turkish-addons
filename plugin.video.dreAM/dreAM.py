
#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
import urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
from xbmctools import z
from xbmctools import f
import member as mem
import requests

tk="|User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')"
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
pt='ODcpL1Y2ITpxLUczOHYcHD9EPWUpKSQmIz86Jy0zKWdQKylnODNDKyk1VkFmQD0t'
addon_id = 'plugin.video.dreAM'
__settings__ = xbmcaddon.Addon(id=addon_id)
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
addon_icon    = __settings__.getAddonInfo('icon')

import xbmctools,fix

xbmcPlayer = xbmc.Player()
xbmcPlayer.stop()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playList.clear()
addon_icon    = __settings__.getAddonInfo('icon')
adonversiyonu =   xbmcaddon.Addon().getAddonInfo("version")

def acilis():
    url = 'lmx.maerd/golegnahc/moc.enisened//:ptth'[::-1]
    link=get_url(url)
    r = re.findall(r'DUYURUPENCERESI ="ACIK"',link)
    if r:
        windows()
    else:
        pass
def CATEGORIES():
         acilis()
         threadName=[]
         delay=[]
         mem.baslamak(threadName, delay)
         mem.playlist3()
         gizlilik = __settings__.getSetting( "adult" )
         gizlilik2 = __settings__.getSetting( "code" )
         gizlilik3 = __settings__.getSetting( "code2" )
         gizlilik4 = __settings__.getSetting( "adult2" )
         addDir('[COLOR blue]SiNEMALAR[/COLOR]',"Sinema()",2,'http://dreamtr.club/resimler/Sinemalar.png','special://home/addons/plugin.video.dreAM/fanart.jpg')
         addDir('[COLOR pink]DiZiLER[/COLOR]',"Dizi()",3,'http://dreamtr.club/resimler/Diziler.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR yellow]CANLI YAYINLAR[/COLOR]',"canliyayin()",4,'http://dreamtr.club/resimler/CanliTVler.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR yellow]DreamTR Radyolar[/COLOR]',"radyo()",105,'http://dreamtr.club/resimler/Radyo.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR purple]BELGESEL iZLE[/COLOR]',"Belgesel()",1,'http://dreamtr.club/resimler/belgeselizle.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR grey]ALMAN [/COLOR]',"Alman()",61,'http://dreamtr.club/resimler/almanlar.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR orange]PORTAL [/COLOR]',"portal()",110,'http://dreamtr.club/resimler/portal.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR green]Yesilcam[/COLOR]',"yesilcam()",114,'http://dreamtr.club/resimler/yesilcam.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR grey]GENEL ARAMA [/COLOR]',"genelarama()",76,'http://dreamtr.club/resimler/genelarama.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         addDir('[COLOR grey]DREAM AYARLAR[/COLOR]',"Ayarlar()",2000,'http://dreamtr.club/resimler/ayarlar.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         if gizlilik == "false" or gizlilik2 != gizlilik3 or gizlilik4 == "false":
             pass
         else:
             addDir('[COLOR red]+18[/COLOR]',"yetiskin()",16,'http://dreamtr.club/resimler/adult1.png','special://home/addons/plugin.video.dreAM/fanart.jpg' )
         xbmc.executebuiltin('Container.SetViewMode(500)')
url = 'txt.2maerd/golegnahc/moc.enisened//:ptth'[::-1]
link=xbmctools.get_url(url)
konumuz=link
if xbmc.getInfoLabel( "System.BuildVersion" )[:2] == '14':
    xbmctools.playlist2()
else:
    pass
class windows():
    WINDOW = 10147
    CONTROL_LABEL = 1
    CONTROL_TEXTBOX = 5
    def __init__( self, *args, **kwargs ):
        xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
        self.window = xbmcgui.Window( self.WINDOW )
        xbmc.sleep( 100 )
        self.setControls()
    def setControls( self ):
        heading, text = self.getText()
        self.window.getControl( self.CONTROL_LABEL ).setLabel( "%s - %s" % ( heading, addon_id +"- Versiyon:"+adonversiyonu) )
        self.window.getControl( self.CONTROL_TEXTBOX ).setText( text )
    def getText( self ):
        txt = str(konumuz)
        return "DUYURU ",txt
#2
def Sinema():
        addDir('[COLOR beige]Sinema 1[/COLOR]',"Sinema1()",5,'http://dreamtr.club/resimler/Sinema1.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Sinema 2[/COLOR]',"Sinema2()",6,'http://dreamtr.club/resimler/Sinema2.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Sinema 3[/COLOR]',"Sinema3()",7,'http://dreamtr.club/resimler/Sinema3.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Sinema 4[/COLOR]',"Sinema4()",77,'http://dreamtr.club/resimler/Sinema4.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Sinema 5[/COLOR]',"Sinema5()",78,'http://dreamtr.club/resimler/Sinema5.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        xbmc.executebuiltin('Container.SetViewMode(500)')
#3
def Dizi():
        addDir('[COLOR beige]Dizi 1[/COLOR]',"Dizi1()",8,'http://dreamtr.club/resimler/Dizi1.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Dizi 2[/COLOR]',"Dizi2()",9,'http://dreamtr.club/resimler/Dizi2.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Dizi 3[/COLOR]',"Dizi3()",10,'http://dreamtr.club/resimler/Dizi3.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Dizi 4[/COLOR]',"Dizi4()",13,'http://dreamtr.club/resimler/Dizi4.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Televizyon Programlari[/COLOR]',"TVPROG()",119,'http://dreamtr.club/resimler/Dizi4.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        xbmc.executebuiltin('Container.SetViewMode(500)')
#4
def canliyayin():
        addDir('[COLOR beige]Canli Tv 1[/COLOR]',"Canli1()",11,'http://dreamtr.club/resimler/Canlitv1.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Canli Tv 2[/COLOR]',"Canli2()",12,'http://dreamtr.club/resimler/Canlitv2.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Canli Tv 3[/COLOR]',"Canli3()",18,'http://dreamtr.club/resimler/Canlitv3.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]Canli Tv 4[/COLOR]',"Canli4()",27,'http://dreamtr.club/resimler/Canlitv4.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        xbmc.executebuiltin('Container.SetViewMode(500)')
#61
def Alman():
        addDir('[COLOR beige]ALMAN SINEMA 1[/COLOR]',"AlmanS()",62,'http://dreamtr.club/resimler/almansinema.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        addDir('[COLOR beige]ALMAN CANLI TV[/COLOR]',"AlmanC()",63,'http://dreamtr.club/resimler/almantv.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
        xbmc.executebuiltin('Container.SetViewMode(500)')
def playlist_yap(playList,name,url):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        return playList
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; SmartTV) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def get_urlmobile(url):
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
#8
def Dizi1():
    url='moc.elziizidd.www//:ptth'[::-1]
    addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,14,'http://dreamtr.club/resimler/aramasearch.png',"special://home/addons/plugin.video.dreAM/fanart.jpg" )
    addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,19,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
    addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yerli Diziler[/COLOR]',url,15,"http://dreamtr.club/resimler/yenidizi.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )                   
    url1='http://www.canlidizihd4.com/'
    link=get_url(url1)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "kutu-resim"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,68,thumbnail,thumbnail)
    url2='http://www.canlidizihd4.com/page/2'
    link=get_url(url2)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "kutu-resim"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,68,thumbnail,thumbnail)
    url3='http://www.canlidizihd4.com/page/3'
    link=get_url(url3)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "kutu-resim"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,68,thumbnail,thumbnail)

#15
def Kategoriler():
        url='moc.elziizidd.www//:ptth'[::-1]
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "sidebar-right"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name=li.text
            name=fix.decode_fix(name)
            name=name.encode('utf8')
            thumbnail='special://home/addons/plugin.video.dreAM/fanart.jpg'
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,19,thumbnail,thumbnail)

        
#14
def Arama():
        dizi1='moc.elziizidd.www//:ptth'[::-1]
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (dizi1+'/?s='+query)
            Yeni(url)
#19
def Yeni(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "leftC"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "moviefilm"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
    page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
            addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")

#20
def dizivideolinks(url,name):
        urlList=''
        ok=True
        link=get_url(url)
        match2=re.compile('href="(.*?)"><span>.*?</span>').findall(link)
        for partUrl in match2:
                urlList=urlList+partUrl 
                urlList=urlList+':;'
        total=url+':;'+urlList
        pDialog = xbmcgui.DialogProgress()
        ret = pDialog.create('Loading playlist...')
        match = total.split(':;')
        del match[-1]
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
        pDialog.update(0,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
        i=0
        for url in match:
                i+=1
                name2=str(i)+'. Parca'
                
                link=get_url(url)
                try:
                        dm=re.compile('src="http://www.dailymotion.com/embed/video\/(.*?)\?syndication\=.*?"').findall(link)
                        for url in dm:
                                url = 'http://www.dailymotion.com/embed/video/'+url
                                addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,88,'','')
                except:
                        pass
                try:
                      vk=re.compile('vk.com\/(.*?)"').findall(link)
                      for url in vk:
                                url='http://vk.com/'+url
                                url=url.replace('&#038;','&')
                                link=get_url(url)
                                match4=re.compile('"url480":"(.*?)"').findall(link)
                                for url in match4:
                                        url=url.replace("\/","/")          
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                time.sleep(3)
                                pDialog.close()
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        
                        yt=re.compile("encodeURIComponent\(\'(.*?)\'").findall(link)
                        for url in yt:
                                url=url.replace('http://www.youtube.com/watch?v=','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        mr=re.compile('value="movieSrc=(.*?)&amp;mp4=1&').findall(link)#
                        for url in mr:
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:
                        ok=re.compile('http://ok.ru/videoembed/(.*?)"').findall(link)
                        for url in ok:
                                url='http://ok.ru/videoembed/'+str(url)
                                sources = []
                                if(re.search(r'ok.ru', url)):
                                        id = re.search('\d+', url).group(0)
                                        jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
                                        jsonSource = json.loads(http_req(jsonUrl))
                                        for source in jsonSource['videos']:
                                                        name = '%s %s' % ('', source['name'])
                                                        link = '%s|User-Agent=%s&Accept=%s&Referer=%s' % (source['url'], USER_AGENT, ACCEPT, urllib.quote_plus(url))
                                                        url4 = link
                                                        if "mob" in name: pass
                                                        elif "lowe" in name: pass
                                                        elif "sd" in name: pass
                                                        elif "h" in name: pass
                                                        else:
                                                                addLink(name+' '+'[COLOR beige]'+name+'[/COLOR]',url4,'')
                                                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                                                listitem.setInfo('video', {'name': name } )
                                                                playList.add(url4,listitem=listitem)
                                                                loadedLinks = loadedLinks + 1
                                                                percent = (loadedLinks * 100)/totalLinks
                                                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                                                if (pDialog.iscanceled()):
                                                                        return False
                except:
                        pass
                try:
                        ok2=re.compile('ok.php\?git\=(.*?)"').findall(link)
                        for url in ok2:  
                                url='http://ok.ru/videoembed/'+str(url)
                                addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,88,'','')
                except:
                        pass 
                try:
                    yeniodn=re.compile('<iframe src="/play/odnplay.(.*?)"').findall(link)
                    for url in yeniodn:
                        url='http://ddiziizle.org/play/odn.'+url
                        link=get_url(url)
                        match4=re.compile('"480p":"(.*?)"').findall(link)
                        for url in match4:
                                url=url.replace("\/","/")  
                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                        listitem.setInfo('video', {'name': name } )
                        playList.add(url,listitem=listitem)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                        if (pDialog.iscanceled()):
                                return False          
                except:
                    pass
                try:
                        ytb=re.compile('youtube.com\/embed\/(.*?)"').findall(link)
                        for url in ytb:
                                url='http://www.youtube.com/embed/' + str(url)
                                addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,99,'','')
                except:
                    pass
        xbmcPlayer.play(playList)
def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
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
#9
def Dizi2():
        url='moc.2dhizidilnac.www//:ptth'[::-1]
        addDir('[COLOR red]>>>>>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,25,"http://dreamtr.club/resimler/aramasearch.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR red]Yeni Yerli Diziler [/COLOR]',url,23,"http://dreamtr.club/resimler/yenidizi.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
#25
def Arama2():
        dizi2='moc.2dhizidilnac.www//:ptth'[::-1]
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (dizi2+'/?s='+query)
            Yeni2(url)
#23
def YeniDiziler2():
        url='moc.2dhizidilnac.www//:ptth'[::-1]
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "sol"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name=li.text
            name=fix.decode_fix(name)
            name=name.encode('utf8')
            thumbnail=""
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,21,thumbnail,thumbnail)




#21
def Yeni2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "kutu"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('a')['title'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
    page=re.compile('\'current\'>.*?</.*?="page larger" href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
            addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,21,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#26
def dizivideolinks2(url,name):
        urlList=''
        ok=True
        url=url+'/11'
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "video-alan"})
        panel = panel[0].findAll("div", {"id": "part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('href="(.*?)"><span>.*?</span>').findall(str(liste))
        for partUrl in match2:
                if "<" in partUrl:
                        pass
                else:
                        urlList=urlList+partUrl
                        urlList=urlList+':;'
        url=url.replace('/11','/')
        total=url+':;'+urlList
        pDialog = xbmcgui.DialogProgress()
        ret = pDialog.create('Loading playlist...')
        match = total.split(':;')
        del match[-1]
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
        pDialog.update(0,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
        i=0
        for url in match:
                i+=1
                name2=str(i)+'. Parca'
                link=get_url(url)
                try:
                        dm=re.compile('http:\/\/www.dailymotion.com\/embed\/video\/(.*?)\?').findall(link)
                        for url in dm:
                            url = 'http://www.dailymotion.com/embed/video/'+url
                            addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,88,'','')
                except:
                        pass
                try:
                      okru=re.compile('<iframe src="(.*?)" width=\'550\' height=\'400\'').findall(link)
                      for url in okru:
                                link=get_url(url)
                                match4=re.compile('"file":"(.*?)"').findall(link)
                                for url in match4:
                                        url=url.replace('\&','&')
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                time.sleep(3)
                                pDialog.close()
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                      vk=re.compile('vk.com\/(.*?)"').findall(link)
                      for url in vk:
                                url='http://vk.com/'+url
                                url=url.replace('&#038;','&')
                                addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,99,'','')
                except:
                        pass
                try:
                      vk2=re.compile('http://can(.*?)" width="550"').findall(link)
                      for url in vk2:
                                url='http://can'+url
                                link=get_url(url)
                                kod=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
                                for oid,vidid,has in kod:
                                        url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
                                        link=get_url(url)
                                        if "480" in link:
                                                match4=re.compile('"url480":"(.*?)"').findall(link)
                                        elif "360" in link:
                                                match4=re.compile('"url360":"(.*?)"').findall(link)
                                        elif "240" in link:
                                                match4=re.compile('"url240":"(.*?)"').findall(link)
                                        else:
                                                print "video yok"
                                        for url in match4:
                                                url=url.replace("\/","/")                                                       
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        time.sleep(3)
                                        pDialog.close()
                                        if (pDialog.iscanceled()):
                                                return False
                except:
                        pass
                try:
                      m3u8=re.compile('file: "http://(.*?)"').findall(link)
                      for url in m3u8:
                                url='http://'+url                                                
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        
                        yt=re.compile("encodeURIComponent\(\'(.*?)\'").findall(link)
                        for url in yt:
                                url=url.replace('http://www.youtube.com/watch?v=','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        mr=re.compile('value="movieSrc=(.*?)&amp;mp4=1&').findall(link)#
                        for url in mr:
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:   
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:   
                        yt2=re.compile('http:\/\/www.youtube.com\/embed\/(.*?)feature=player_detailpage"').findall(link)
                        for url in yt2:
                                url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:      
                        yt3=re.compile('www.youtube-nocookie.com/embed/(.*?)rel').findall(link)
                        for url in yt3:
                                url=url.replace('?','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt4=re.compile('http://www.youtube.com/embed/(.*?)showinfo=0"').findall(link)
                        for url in yt4:
                                url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
                                url='plugin://plugin.video.youtube/play/?video_id='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt5=re.compile('\'file\': \'(.*?)\'').findall(link)
                        for url in yt5:
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        mr2=re.compile("src='http://videoapi.my.mail.ru/videos/embed/(.*?).html'").findall(link)
                        for url in mr2:
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams: 
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:
                        mr3=re.compile("src='http://api.video.mail.ru/videos/embed/(.*?).html'").findall(link)
                        for url in mr3:
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:  
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:
                      okru2=re.compile('src=".*?.\/player\/ok\/1.*?.php\?v=(.*?)"').findall(link)
                      for url in okru2:
                            url=(base64.b64decode(url))
                            url=url.replace("http://ok.ru/video/","")
                            url='http://ok.ru/videoembed/'+str(url)
                            addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,88,'','')
                except:
                        pass
                try:
                      m3u82=re.compile('file:"(.*?)\?",width:').findall(link)
                      for url in m3u82:                                            
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                      vidag=re.compile('http://vid.ag/(.*?)"').findall(link)
                      for url in vidag:
                                url='http://vid.ag/'+url
                                link=get_url(url)
                                match4=re.compile('\|static\|\|.*?\|\|.*?\|.*?\|.*?\|.*?\|(.*?)\|html\|').findall(link)
                                for url in match4:
                                    url='http://vid.ag/'+url+'.m3u8'
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
        xbmcPlayer.play(playList)
def Dizi3():
        latte=''
        latte=['http://fox.com.tr/dizi-izle','https://www.kanald.com.tr/diziler','http://www.atv.com.tr/diziler','http://www.trt.tv/2/diziler','http://startv.com.tr/diziler','http://www.showtv.com.tr/dizi/tum_bolumler/aci-ask/1532','http://www.showtv.com.tr/dizi/tum_bolumler/iliski-durumu-karisik/1434','http://www.showtv.com.tr/dizi/tum_bolumler/kis-gunesi/1567','http://www.showtv.com.tr/dizi/tum_bolumler/asla-vazgecmem/1411']
        sitegit=latte[0]                                    
        link=get_url(sitegit)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "orta3"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "diziizle"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            thumbnail="http://fox.com.tr"+thumbnail
            name=name.replace('&#8211','').replace('&','')
            addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,120,thumbnail,thumbnail )
        sitegit4=latte[1]                                    
        link=get_url(sitegit4)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "kd-docs-news"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "col-sm-4"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            url='https://www.kanald.com.tr'+url+'/bolumler'
            thumbnail=panel[i].find('img')['data-src'].encode('utf-8', 'ignore')
            thumbnail=thumbnail.replace('//','https://')
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,126,thumbnail,thumbnail )
        sitegit6=latte[2]
        link=get_url(sitegit6)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "listC living"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "liste"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            url='http://www.atv.com.tr/'+url+'/bolum'
            url=url.replace('diziler','webtv')
            name=li.text.encode('utf-8', 'ignore')
            name=name.replace('&#220;','U').replace('&#214;','O').replace('&#199;','C').replace('&#246;','o').replace('&#252;','u').replace('&#231;','c').replace('20:00','  ')
            thumbnail=li.find('img')['data-original'].encode('utf-8', 'ignore')
            addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,130,thumbnail,thumbnail )
        sitegit2=latte[3]                                   
        link=get_url(sitegit2)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "container special_list_background"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "programs_item col-lg-3 col-md-3 col-sm-4 col-xs-4 col-xxs-6"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            url='http://www.trt.tv'+url
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            name=name.replace('&#8211','').replace('&','')
            addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,122,thumbnail,thumbnail )
        sitegit3=latte[4]                                    
        link=get_urlmobile(sitegit3)
        soup = BeautifulSoup(link)
        panel = soup.findAll("li", {"class": "multi"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            url='http://www.startv.com.tr'+url+"/bolumler"
            url=url.replace("   ","")
            name= li.text
            name=name.encode('utf-8', 'ignore')
            name=name.replace("&#246;","o").replace("&#252;","u").replace("&#231;","c")
            if "diziler" in url: pass
            elif "programlar" in url: pass
            elif "program" in url: pass
            else:
                addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,124,'','' )
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+'Aci Ask'+' [/COLOR]',latte[5],128,'http://mo.ciner.com.tr/showtv/iu/250x250/aci-ask.jpg?v=1456003224','http://mo.ciner.com.tr/showtv/iu/250x250/aci-ask.jpg?v=1456003224' )
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+'Iliski Durumu Karisik'+' [/COLOR]',latte[6],128,'http://mo.ciner.com.tr/showtv/iu/250x250/iliski-durumu-karisik.jpg?v=1456003429','http://mo.ciner.com.tr/showtv/iu/250x250/iliski-durumu-karisik.jpg?v=1456003429' )
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+'Kis Gunesi'+' [/COLOR]',latte[7],128,'http://mo.ciner.com.tr/showtv/iu/250x250/kis-gunesi.jpg?v=1455882498','http://mo.ciner.com.tr/showtv/iu/250x250/kis-gunesi.jpg?v=1455882498' )
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+'Asla Vazgecmem'+' [/COLOR]',latte[8],128,'http://mo.ciner.com.tr/showtv/iu/250x250/asla-vazgecmem.jpg?v=1455855428','http://mo.ciner.com.tr/showtv/iu/250x250/asla-vazgecmem.jpg?v=1455855428' )
#119
def TVPROG():
    latte=["http://fox.com.tr/program-izle","https://www.kanald.com.tr/programlar","http://www.atv.com.tr/programlar","http://www.trt.tv/20149/programlar","http://startv.com.tr/programlar"]
    sitegit=latte[0]                                    
    link=get_url(sitegit)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "orta3"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "diziizle"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        thumbnail="http://fox.com.tr"+thumbnail
        name=name.replace('&#8211','').replace('&','')
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,120,thumbnail,thumbnail )
    sitegit4=latte[1]                                    
    link=get_url(sitegit4)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "kd-docs-news"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "col-sm-4"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='https://www.kanald.com.tr'+url+'/bolumler'
        thumbnail=panel[i].find('img')['data-src'].encode('utf-8', 'ignore')
        thumbnail=thumbnail.replace('//','https://')
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,132,thumbnail,thumbnail )
    sitegit2=latte[3]                                   
    link=get_url(sitegit2)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "container special_list_background"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "programs_item col-lg-3 col-md-3 col-sm-4 col-xs-4 col-xxs-6"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='http://www.trt.tv'+url
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        name=name.replace('&#8211','').replace('&','')
        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,122,thumbnail,thumbnail )
    sitegit3=latte[4]                                    
    link=get_urlmobile(sitegit3)
    soup = BeautifulSoup(link)
    panel = soup.findAll("li", {"class": "multi"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('li'):
        a=li.find('a')
        url= a['href']
        url='http://www.startv.com.tr'+url+"/bolumler"
        name= li.text
        name=name.encode('utf-8', 'ignore')
        name=name.replace("&#252;","u").replace("&#39;","'").replace("&#199;","C").replace("&#246;","o")
        if "diziler" in url: pass
        elif "programlar" in url: pass
        elif "dizi" in url: pass
        else:
            addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,124,'','' )
##    sitegit5=latte[2]
##    link=get_url(sitegit5)
##    soup = BeautifulSoup(link)
##    panel = soup.findAll("div", {"class": "liste"},smartQuotesTo=None)
##    panel = panel[0].findAll("ul", {"id": "series-list"})
##    liste=BeautifulSoup(str(panel))
##    for li in liste.findAll('li'):
##        a=li.find('a')
##        url= a['href']
##        url='http://www.atv.com.tr'+url+'/bolum'
##        url=url.replace('programlar','webtv')
##        name=li.text.encode('utf-8', 'ignore')
##        name=name.replace('&#220;','U').replace('&#214;','O').replace('&#199;','C').replace('&#246;','o').replace('&#252;','u').replace('&#231;','c').replace('20:00','  ')
##        thumbnail=li.find('img')['data-original'].encode('utf-8', 'ignore')
##        addDir('[COLOR orange]>>[/COLOR] [COLOR beige]'+name+' [/COLOR]',url,133,thumbnail,thumbnail )


#120
def fox1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "altsayfaIcerik"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "videoBG"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url="http://fox.com.tr"+url+'/part/0'
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        name=name.replace('&#8211','').replace('&','')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,121,thumbnail,thumbnail )
    page=re.compile('<li class=\'nrm sayfaitemsAktive\' id=".*?"><a href=\'.*?\'>.*?</a></li>\r\n\t\t\t\t  \t\t\t\t\t\t\t<li class="nrm" id=".*?"><a href=\'(.*?)\'>(.*?)</a>').findall(link)
    for Url,name in page:
        Url="http://fox.com.tr"+Url
        addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,120,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#121
def fox2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    match=re.compile("mobile : { src : \'(.*?)\'").findall(str(soup))
    for url in match:
        yenical4(name,url)
#122
def trt1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "bolumlerContentGrid"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "item_height col-lg-2 col-md-2 col-sm-3 col-xs-4 col-xxs-6"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='http://www.trt.tv'+url
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        div1=panel[i].findAll("div", {"class": "video_name"},smartQuotesTo=None)
        name=div1[0].text.replace('&#220;','U').replace('&#214;','O').replace('&#199;','C').replace('&#246;','o').replace('&#252;','u').replace('&quot;','"')
        name=name.encode('utf-8', 'ignore')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,123,thumbnail,thumbnail )
#123
def trt2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "row"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"id": "player"})
    match=re.compile('url: "(.*?)Kalite').findall(str(panel[0]))
    for url in match:
        yenical4(name,url)
#124
def star1(url):
    link=get_urlmobile(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "data"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('h4'):
        a=li.find('a')
        url= a['href']
        name= li.text
        name=name.encode('utf-8', 'ignore')
        name=name.replace("&#246;","o").replace("&#252;","u")
        url='http://startv.com.tr'+url
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,125,'','' )

#125
def star2(url):
    link=get_urlmobile(url)
    soup = BeautifulSoup(link)
    match=re.compile('referenceId: "(.*?)"').findall(str(soup))
    for refid in match:
        url='http://dyg_video.rgbilisim.com/api/video_info?SecretKey=NtvApiSecret2014*&PublisherId=1&ReferenceId='+refid
        link=get_urlmobile(url)
        match=re.compile('"hls":"(.*?)"').findall(link)
        for url in match:
            url=url.replace('\/','/')
            yenical4(name,url)
#126
def kanald1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "kd-docs-section"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "caption clearfix"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='https://www.kanald.com.tr'+url
        name=panel[i].find('a').text.encode('utf-8', 'ignore')
        name=name.replace('&#246;','o').replace('&#252;','u')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,127,'','' )
    page=re.compile('kd-load-more><a href="(.*?)&.*?" data-url').findall(link)
    for Url in page:
        Url="https://www.kanald.com.tr"+Url
        addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+'[COLOR red]'+'>>'+'[/COLOR]',Url,126,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#127
def kanald2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "kd-docs-section"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "col-left"})
    match=re.compile('"VideoDetailCtrl" data-id="(.*?)">').findall(str(panel[0]))
    for kodlama in match:
        url='https://www.kanald.com.tr/actions/content/media/'+kodlama
        link=get_url(url)
        match=re.compile('"ServiceUrl":"(.*?)","SecurePath":"(.*?)"').findall(link)
        for calici,birlestirici in match:
            calici=calici.replace('https://',"http://")
            birlestirici=birlestirici.replace("\u0026","&")
            url=calici+birlestirici
            yenical4(name,url)
#128
def showtv1(url):
    link=get_url(url)
    match=re.compile('<a href="(.*?)">\r\n.*?<li>\r\n.*?<div class="video-play-icon"></div>\r\n.*?<img src="(.*?)" alt="" width="288" height="162"/>\r\n.*?<div class="baslik_spot">\r\n.*?<h3>(.*?)</h3>\r\n\r\n.*?</div>').findall(link)
    for url,thumbnail,name in match:
        url='http://www.showtv.com.tr'+url
        url=url.replace("\/","/")
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,129,thumbnail,thumbnail)
    page=re.compile('<div class="current">.*?</div>\n\t\t\t\t\t\t\t\t\t\t\t\t<a href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
        Url="http://www.showtv.com.tr"+Url
        addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,128,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#129
def showtv2(url):
    link=get_url(url)
    match=re.compile('url: "(.*?)",\n\tnextVideoUrl:').findall(link)
    for calgi in match:
        calgi=calgi.replace("\/","/")
        url=calgi
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+'          1.KISIM'+' [/COLOR]',url,42,'','')
    match2=re.compile('<a href="(.*?)">\r\n(.*?)</a>').findall(link)
    for url1,name in match2:
        url1='http://www.showtv.com.tr'+url1
        if '1. KISIM' in name: pass
        else:
            link=get_url(url1)
            match=re.compile('url: "(.*?)",\n\tnextVideoUrl').findall(link)
            for url in match:
                url=url.replace("\/","/")
                addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,42,'','')
#130
def atv1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "hListParts"},smartQuotesTo=None)
    panel = panel[0].findAll("ul", {"id": "series-video-list"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('li'):
        a=li.find('a')
        url= a['href']
        url='http://www.atv.com.tr'+url
        thumbnail=li.find('img')['data-original'].encode('utf-8', 'ignore')
        name=li.text.encode('utf-8', 'ignore')
        name=name.replace('&#220;','U').replace('&#214;','O').replace('&#199;','C').replace('&#246;','o').replace('&#252;','u').replace('&#231;','c').replace('20:00','  ').replace('&#39;',"'")
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,131,thumbnail,thumbnail)
#131
def atv2(url):
    link=get_url(url)
    match=re.compile('rel="canonical" href="http.*?/webtv/(.*?)/bolum/(.*?)\?id=.*?"').findall(link)
    for ff,num in match:
        sifreliurl='http://atv-vod.ercdn.net/'+ff+'/0'+num+'/'+ff+'_0'+num+'.smil/playlist.m3u8'
        altsifreli='http://atv-vod.ercdn.net/'+ff+'/0'+num+'/'+ff+'_0'+num+'_0400.mp4'
        altsifreli=altsifreli.replace('-','_').replace('atv_vod','atv-vod')
        sifreliurl=sifreliurl.replace('-','_').replace('atv_vod','atv-vod')
        url='http://videotoken.tmgrup.com.tr/webtv/secure?url='+sifreliurl+'&url2='+altsifreli
        link=get_url(url)
        match=re.compile('Url":"(.*?)"').findall(link)
        for url in match:
            url=url.replace("\u0026'","&")
            yenical4(name,url)
#132 
def kanaldprog(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "kd-docs-section"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "col-sm-3 col-xs-6"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='https://www.kanald.com.tr'+url
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        name=name.replace('&#246;','o').replace('&#252;','u')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,127,'','' )
    page=re.compile('kd-load-more><a href="(.*?)&.*?" data-url').findall(link)
    for Url in page:
        Url="https://www.kanald.com.tr"+Url
        addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+'[COLOR red]'+'>>'+'[/COLOR]',Url,132,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#133
def atvprog1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "hListParts"},smartQuotesTo=None)
    panel = panel[0].findAll("ul", {"id": "series-video-list"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('li'):
        a=li.find('a')
        url= a['href']
        url='http://www.atv.com.tr'+url
        name= li.text
        name=name.encode('utf-8', 'ignore')
        thumbnail=li.find('img')['src'].encode('utf-8', 'ignore')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,134,thumbnail,thumbnail)
#134
def atvprog2(url):
    link=get_url(url)
    match=re.compile('rel="canonical" href="http.*?/webtv/(.*?)/bolum/(.*?)\?id=.*?"').findall(link)
    for ff,num in match:
        sifreliurl='http://atv-vod.ercdn.net/'+ff+'/0'+num+'/'+ff+'_0'+num+'.smil/playlist.m3u8'
        altsifreli='http://atv-vod.ercdn.net/'+ff+'/0'+num+'/'+ff+'_0'+num+'_0400.mp4'
        altsifreli=altsifreli.replace('-','_').replace('atv_vod','atv-vod')
        sifreliurl=sifreliurl.replace('-','_').replace('atv_vod','atv-vod')
        url='http://videotoken.tmgrup.com.tr/webtv/secure?url='+sifreliurl+'&url2='+altsifreli
        link=get_url(url)
        match=re.compile('Url":"(.*?)"').findall(link)
        for url in match:
            url=url.replace("\u0026'","&")
            yenical4(name,url)
#135
def starprog(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "itemWrap clearfix"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "item"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        url='http://startv.com.tr'+url
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        addDir('[COLOR blue]>>[/COLOR] [COLOR blue]'+name+' [/COLOR]',url,125,thumbnail,thumbnail)
    page=re.compile('<span class="thisPage">.*?</span> / <span\r\n.*?class="allPages">.*?</span> </span><a href="(.*?)"').findall(link)
    for Url in page:
        Url="http://startv.com.tr"+Url
        addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+'[COLOR red]'+'[/COLOR]',Url,135,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
        
def name_fix1(x):        
        x=x
        return x[0].capitalize() + x[1:]
#13
def Dizi4():
        url='moc.1izidd.www//:ptth'[::-1]
        addDir('[COLOR red]>>>>>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,25,"http://dreamtr.club/resimler/aramasearch.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,34,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR red]Yerli Diziler [/COLOR]',url,33,"http://dreamtr.club/resimler/yenidizi.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
#33
def yerlidizi4():
        url='moc.1izidd.www//:ptth'[::-1]
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "blok-ust"})
        panel = panel[0].findAll("div", {"class": "blok-liste"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name=li.find('a')['title']
            name=name.encode('ISO-8859-1', 'ignore')
            name=fix.decode_fix(name)
            thumbnail=""
            name=name.replace('son bolum izle','').replace('&Yuml;','s').replace('&ndash;','o').replace('&Dagger;','C')
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,35,thumbnail,thumbnail)
#34    
def Yeni4(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "ortaicerik"})
        panel = panel[0].findAll("div", {"class": "dizi-box"})
        liste=BeautifulSoup(str(panel))
        for i in range (len(panel)):
            url=panel[i].find('a')['href']
            thumbnail=panel[i].find('img')['src']
            thumbnail="http://www.ddizi1.com/"+thumbnail
            name=panel[i].find('img')['alt'].encode('ISO-8859-1', 'ignore')
            name=fix.decode_fix(name)
            name=name.replace('son bolum izle','').replace('&Yuml;','s').replace('&ndash;','o').replace('&Dagger;','C')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,32,thumbnail,thumbnail)
        page=re.compile('class="active"><a href=".*?" rel=".*?">.*?</a></li>\r\n              <li ><a href=".*?" rel="(.*?)">(.*?)</a>').findall(link)
        for Url,name in page:
                Url="http://www.ddizi1.com/l.php?sayfa="+Url
                addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,34,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#35
def Hepsi4(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "orta-orta"})
        panel = panel[0].findAll("div", {"class": "four-box"})
        liste=BeautifulSoup(str(panel))
        for i in range (len(panel)):
            url=panel[i].find('a')['href']
            thumbnail=panel[i].find('img')['src']
            thumbnail="http://www.ddizi1.com/"+thumbnail
            name=panel[i].find('a')['title']
            name=fix.decode_fix(name)
            name=name.encode('ISO-8859-1', 'ignore')
            addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,32,thumbnail,thumbnail)
        page=re.compile('class="active"><a href=".*?">.*?</a></li>\r\n                <li ><a href="(.*?)">(.*?)</a>').findall(link)
        for Url,name in page:
                addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,35,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#32
def dizivideolinks4(url,name):
        urlList=''
        ok=True
        url=url+'/9'
        link=get_url(url)
        match2=re.compile('<li><a href="(.*?)">.*? Par\xc3\xa7a</a></li>').findall(link)
        for partUrl in match2:
                partUrl="http://www.ddizi1.com"+partUrl
                urlList=urlList+partUrl
                urlList=urlList+':;'
        url=url.replace('/9','/0')
        total=url+':;'+urlList
        pDialog = xbmcgui.DialogProgress()
        ret = pDialog.create('Loading playlist...')
        match = total.split(':;')
        del match[-1]
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
        pDialog.update(0,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
        i=0
        for url in match:
                i+=1
                name2=str(i)+'. Parca'
                link=get_url(url)
                try:
                        tekpart=re.compile('<div id="odnvideo" data-id="(.*?)"></div>').findall(link)
                        for url in tekpart:
                                url=url.replace("+","%2B")
                                url = 'http://www.ddizi1.com/js/odn.php?id='+url
                                link=get_url(url)
                                link=link.decode('string-escape')
                                if "360p" in link:                            
                                        match=re.compile('file":"(.*?)", "label":"360p"').findall(link)
                                elif "240p" in link:         
                                        match=re.compile('file":"(.*?)", "label":"240p"').findall(link)
                                else:
                                        print "video yok"
                                for url in match:
                                    print "calisiyor"
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        dm=re.compile('src="http://www.dailymotion.com/embed/video/(.*?)"').findall(link)
                        for url in dm:
                                url = 'http://www.dailymotion.com/embed/video/'+url
                                addDir('[COLOR lightyellow]'+name2+'[/COLOR]',url,88,'','')
                except:
                        pass
                try:
                      okru=re.compile('<iframe src="(.*?)" width=\'550\' height=\'400\'').findall(link)
                      for url in okru:
                                link=get_url(url)
                                match4=re.compile('"file":"(.*?)"').findall(link)
                                for url in match4:
                                        url=url.replace('\&','&')
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                time.sleep(3)
                                pDialog.close()
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                      vk=re.compile('vk.com\/(.*?)"').findall(link)
                      for url in vk:
                                url='http://vk.com/'+url
                                url=url.replace('&#038;','&')
                                link=get_url(url)
                                match4=re.compile('"url480":"(.*?)"').findall(link)
                                for url in match4:
                                        url=url.replace("\/","/")       
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                time.sleep(3)
                                pDialog.close()
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                      vk2=re.compile('http://can(.*?)" width="550"').findall(link)
                      for url in vk2:
                                url='http://can'+url
                                link=get_url(url)
                                kod=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
                                for oid,vidid,has in kod:
                                        url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
                                        link=get_url(url)
                                        if "480" in link:
                                                match4=re.compile('"url480":"(.*?)"').findall(link)
                                        elif "360" in link:
                                                match4=re.compile('"url360":"(.*?)"').findall(link)
                                        elif "240" in link:
                                                match4=re.compile('"url240":"(.*?)"').findall(link)
                                        else:
                                                print "video yok"
                                        for url in match4:
                                                url=url.replace("\/","/")                                                       
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        time.sleep(3)
                                        pDialog.close()
                                        if (pDialog.iscanceled()):
                                                return False
                except:
                        pass
                try:
                      m3u8=re.compile('file: "http://(.*?)"').findall(link)
                      for url in m3u8:
                                url='http://'+url                                                
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt=re.compile("encodeURIComponent\(\'(.*?)\'").findall(link)
                        for url in yt:
                                url=url.replace('http://www.youtube.com/watch?v=','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        mr=re.compile('value="movieSrc=(.*?)&amp;mp4=1&').findall(link)#
                        for url in mr:
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:  
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:
                        yt2=re.compile('http:\/\/www.youtube.com\/embed\/(.*?)feature=player_detailpage"').findall(link)
                        for url in yt2:
                                url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt3=re.compile('www.youtube-nocookie.com/embed/(.*?)rel').findall(link)
                        for url in yt3:
                                url=url.replace('?','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt4=re.compile('src="https:\/\/www.youtube.com\/embed\/(.*?)\?rel=.*?"').findall(link)
                        for url in yt4:
                                url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
                                url='plugin://plugin.video.youtube/play/?video_id='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        yt5=re.compile('\'file\': \'(.*?)\'').findall(link)
                        for url in yt5:
                                url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
                try:
                        mr2=re.compile("src='http://videoapi.my.mail.ru/videos/embed/(.*?).html'").findall(link)#
                        for url in mr2:  
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:
                        mr3=re.compile("src='http://api.video.mail.ru/videos/embed/(.*?).html'").findall(link)
                        for url in mr3: 
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                    for name2,url2 in streams:
                                        addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                        pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                            else:
                                    pass
                except:
                        pass
                try:  
                      okru2=re.compile('src="http://ok.ru/videoembed/(.*?)"').findall(link)
                      for url in okru2:
                                url=url.replace("http://ok.ru/video/","")
                                url='http://ok.ru/videoembed/'+str(url)
                                sources = []
                                if(re.search(r'ok.ru', url)):
                                        id = re.search('\d+', url).group(0)
                                        jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
                                        jsonSource = json.loads(http_req(jsonUrl))
                                        for source in jsonSource['videos']:
                                                        name = '%s %s' % ('', source['name'])
                                                        duzenleyici = re.search(r'sig.+', source['url']).group(0)
                                                        url='http://m.ok.ru/dk?st.cmd=moviePlaybackRedirect&st.'+duzenleyici
                                                        url4=url
                                                        if "mob" in name: pass
                                                        elif "lowe" in name: pass
                                                        elif "sd" in name: pass
                                                        elif "h" in name: pass
                                                        else:
                                                                addLink(name+' '+'[COLOR beige]'+name+'[/COLOR]',url4,'')
                                                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                                                listitem.setInfo('video', {'name': name } )
                                                                playList.add(url4,listitem=listitem)
                                                                loadedLinks = loadedLinks + 1
                                                                percent = (loadedLinks * 100)/totalLinks
                                                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                                                if (pDialog.iscanceled()):
                                                                        return False
                except:
                        pass
                try:
                      m3u82=re.compile('file:"(.*?)\?",width:').findall(link)
                      for url in m3u82:                                             
                                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                except:
                        pass
        xbmcPlayer.play(playList)
#5
def Sinema1():
    try:
        sinema='http://www.baglanfilmiizle.com/'
        addDir('[COLOR yellow]>>[/COLOR] [COLOR red]>> - Arama/Search -<< [/COLOR]',sinema,38,"http://dreamtr.club/resimler/aramasearch.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',sinema,39,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg')
        link=get_url(sinema)
        match=re.compile('</li><li><a href="http://www.baglanfilmiizle.com/film-izle/(.*?)">(.*?)</a></li>').findall(link)
        for url,name in match:
            if "Yeti" in name:
                pass
            else:
                url='http://www.baglanfilmiizle.com/film-izle/'+url
                addDir('[COLOR blue]>>[/COLOR] [COLOR orange]'+name+'[/COLOR]',url,39,"",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
    except:
        showMessage("[COLOR blue]dreAMTR[/COLOR]","[COLOR blue]IP Adresiniz Kitlendi[/COLOR]","[COLOR red]Lutfen Musteri Hizmetlerine Basvurun!! [/COLOR]")
        dialog = xbmcgui.DialogProgress()
        dialog1 = xbmcgui.Dialog()
        dialog1.ok('[COLOR red]Hesabiniz Kitlendi[/COLOR]','[COLOR yellow] Lutfen Musteri Hizmetlerine Basvurun!! [/COLOR]')
        sys.exit()

#38
def Aramasinema1():
    sinema='http://www.baglanfilmiizle.com'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+'/?s='+query)
        sinemaRecent1(url)                                                  
#39
def sinemaRecent1(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("article", {"id": "article"})
        panel = panel[0].findAll("div", {"class": "T-FilmResim"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                name=name.replace('&#8211;',' - ').replace('&#8217;',' ').replace('&#038;',' ')
                addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,40,thumbnail,thumbnail)
        page=re.compile('class="active_page"><a href=".*?">.*?</a></li>\n<li><a href="(.*?)">(.*?)</a>').findall(link)
        for url,name in page:
                addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,39,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#28
def sinemaRecen1(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "contentcontainer"})
        panel = panel[0].findAll("div", {"class": "postlistbox"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']               
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                div2=panel[i].findAll("h2", {"class": "postlisttitle"},smartQuotesTo=None)
                name=div2[0].text.encode('utf-8', 'ignore')
                name=name.replace("&#8211;"," - ")
                addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,29,thumbnail,thumbnail)
        page=re.compile('<span class=\'page current\'>.*?</span><a href=\'(.*?)\' class=\'page paginate\' >(.*?)</a>').findall(link)
        for url,name in page:
                addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,28,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#29
def ayrisdirm1(url):
    link=get_url(url)
    ply=re.compile('\/pusuk\/url\/(.*?)"').findall(link)
    for name in ply:
        name=base64.b64decode(name)
        reverseName=""
        for x in range(len(name)-1,-1,-1):
                reverseName+=name[x]
        reverseName=base64.b64decode(reverseName)
        reverseName=reverseName.replace('ok/','')
        url=reverseName
        url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
        ok_ru(url)
    ply1=re.compile('\/pusuk\/url\/(.*?)=').findall(link)
    for name in ply1:
        name=name+'='
        name=base64.b64decode(name)
        reverseName=""
        for x in range(len(name)-1,-1,-1):
                reverseName+=name[x]
        reverseName=base64.b64decode(reverseName)
        url=reverseName
        url=url.replace('/mail','')
        url = 'http://videoapi.my.mail.ru/videos/embed/'+url+'.html'
        magix_player(name,url)
    yt=re.compile('youtube.com/embed/(.*?)"').findall(link)
    for code in yt:
            url = 'http://www.youtube.com/embed/'+code
            name='Fragman'
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')         
    ok2=re.compile('src="//ok.ru/videoembed/(.*?)"').findall(link)
    for code in ok2:
            url = 'http://ok.ru/videoembed/'+str(code)
            name='OK RU  '
            addDir('[COLOR pink]'+name+'[/COLOR]',url,102,"",'')
    vk_2=re.compile('video_ext.php\?oid\=(.*?)"').findall(link) 
    for code in vk_2:
            url = 'http://vk.com/video_ext.php?oid='+str(code)
            url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
            name='Vk - Play'
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,1030,'',"")
    mailru2=re.compile('videos\/embed\/mail\/(.*?).html').findall(link)
    for code in mailru2:
            url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(code)+'.html'
            name='mail RU  '
            addDir('[COLOR blue]'+name+'[/COLOR]',url,99,"","")
    vidag=re.compile('http://vid.ag/(.*?)"').findall(link) 
    for url in vidag: 
            url = 'http://vid.ag/'+str(url).encode('utf-8', 'ignore')
            name='Play'
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    dd=re.compile('src="http://videomega.tv/view.php\?ref\=(.*?)\&width').findall(link) 
    for url in dd: 
            url = 'http://videomega.tv/view.php?ref='+str(url).encode('utf-8', 'ignore')
            name='Play'
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    ddo=re.compile('src="https://openload.co/embed/(.*?)"').findall(link) 
    for url in ddo: 
            url = 'https://openload.co/embed/'+str(url).encode('utf-8', 'ignore')
            name='Play'
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    vk_9=re.compile('video_ext.php\?oid\=(.*?)"').findall(link) 
    for url in vk_9: 
            url = 'http://vk.com/video_ext.php?oid='+str(url).encode('utf-8', 'ignore')
            name='Play'
            url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
            addDir('[COLOR yellow]'+name+'[/COLOR]',url,1030,"",'')
#40 -----------------------------yarisi ----------------------
def ayrisdirma1(url):
    addDir('[COLOR lightyellow]'+'Part 1'+'[/COLOR]',url,29,'','')
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("ul", {"class": "partlar"})
    match=re.compile('<a href="(.*?)">(.*?)</a>').findall(str(panel))
    for url,name in match:
            url=url.replace('" rel="nofollow',"")
            if "Fragman" in name: pass
            elif "FRAGMAN" in name: pass
            elif "PLUS" in name: pass
            elif "Yor" in name: pass
            elif "LOA" in name: pass
            elif "MEG" in name: pass
            elif "MA" in name: pass
            elif "VK" in name: pass
            else:
                addDir('[COLOR lightyellow]'+name+'[/COLOR]',url,29,'','')
#6
def Sinema2():
    url='http://www.tekparthdkeyfi.com/'
    addDir('[COLOR red]>>>>>>>>>>>>>>>>>[/COLOR][COLOR yellow] Film ARA - 2[/COLOR][COLOR red] <<<<<<<<<<<<<<<<<[/COLOR]',url,44,"http://dreamtr.club/resimler/aramasearch.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
    addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Yeni Eklenen Filmler [/COLOR]',url,43,"http://dreamtr.club/resimler/yenieklenenler.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "main"})
    panel = panel[0].findAll("ul", {"class": "ul-list"})
    liste=BeautifulSoup(str(panel))
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)".*?>(.*?)</a>').findall(str(liste))
    for url,name in match:
        if "Erotik" in name: pass
        else:
            addDir('[COLOR red]>>[/COLOR] [COLOR beige]'+name+'[/COLOR]',url,43,"","") 
#43
def Yenisinema2(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "film-container"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('article'):
                a=li.find('a')
                img=li.find('img')
                url= a['href']
                name=li.text.encode('utf-8', 'ignore')
                name=fix.decode_fix(name)
                thumbnail=img['src'].encode('utf-8', 'ignore')
                name=name.replace('&#8211','').replace('kez izlendiHemen Izle','').replace('izle',' ').replace('Izle',' ')
                addDir('[COLOR beige]'+name+'[/COLOR]',url,45,thumbnail,thumbnail)		
        page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
        for url,name in page:
                addDir('[COLOR blue]SAYFA >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',url,43,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#44
def Search2():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (f+'/?s='+query)
            url=url.replace(' ',"+")
            Yenisinema2(url)
#45
def ayrisdirma2(url):
    link=get_url(url)
    name=' Secenek 1 '
    addDir('[COLOR beige]'+name+'[/COLOR]',url,41,'','')
    match=re.compile('<a href="(.*?)"><span class=\'safirButton\'>(.*?)</span>').findall(link)
    for url,name in match:
        addDir('[COLOR beige]'+name+'[/COLOR]',url,41,'','')

#7
def Sinema3():
    sinema='http://www.bicaps.net'
    addDir('[COLOR yellow]>>[/COLOR] [COLOR red]>> - Arama/Search -<< [/COLOR]',sinema,48,"http://dreamtr.club/resimler/aramasearch.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
    sinema=sinema+"/?am_force_theme_layout=desktop"
    addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',sinema,47,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg')
    url=sinema
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "sidebar-right"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('li'):
        a=li.find('a')
        url= a['href']
        name= li.text
        name=name.encode('utf-8', 'ignore')
        name=fix.decode_fix(name)
        if name=="American Horror Story"or name=="Arrow"or name=="Breaking Bad"or name=="Da Vinci`s Demons"or name=="Dexter"or name=="Doctor Who"or name=="Fringe"or name=="Gotham"or name=="Lost"or name=="The 100"or name=="The Last Ship"or name=="The Originals"or name=="Hz. Omer"or name=="Masters of Horror"or name=="Mayday"or name=="Merlin"or name=="Person of Interest"or name=="Prison Break"or name=="Red Widow"or name=="Revolution"or name=="Sherlock"or name=="Sinbad"or name=="Slider"or name=="Star Wars: Klon Savaslari"or name=="Teen Wolf"or name=="Terminator: The Sarah Connor Chronicles"or name=="The Bible"or name=="The Following"or name=="The Killing"or name=="The Pacific"or name=="The Sopranos"or name=="The Vampire Diaries"or name=="The Walking Dead"or name=="Top of the Lake"or name=="Touch"or name=="Under The Dome"or name=="Vikings"or name=="Zero Hour"or name=="Hz. Omer" or name=="Yabanci DizilerAmerican Horror StoryArrowBreaking BadDa Vinci`s DemonsDexterDoctor WhoFringeGothamLostThe 100The Last ShipThe Originals"or name=="Filmler1080p Filmler2010 Filmleri2011 Filmleri2012 Filmleri2013 Filmleri2014 Filmleri2015 Filmleri3D FilmlerAamir Khan FilmleriAile FilmleriAksiyon FilmleriAltyazili FilmlerAnimasyon FilmleriAnimeBelgesellerBilim Kurgu FilmleriBiyografiCasuslukCizgi FilmlerCocuk FilmleriDansDram FilmleriEditor OnerisiFantastikGenclik FilmleriGerilim FilmleriGizemHint FilmleriIMDB 7.0+Kisa FilmKomediKore FilmleriKorku FilmleriMacera FilmleriMuzikalPolisiye FilmlerPolitikPsikolojikRomantik FilmlerSavas FilmleriSpor FilmleriSuc FilmleriTarih FilmleriTop 250WesternTurkce Dublaj FilmlerYabanci FilmlerZombi FilmleriYabanci DizilerAmerican Horror StoryArrowBreaking BadDa Vinci`s DemonsDexterDoctor WhoFringeGothamLostThe 100The Last ShipThe Originals":
            pass
        else:
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,47,'','')
#47
def Recent3(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "leftC"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "moviefilm"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            name=fix.decode_fix(name)
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            name=name.replace('HD','').replace('Izle','')
            addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,49,thumbnail,thumbnail)
        page=re.compile('current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
        for url,name in page:
                addDir('[COLOR blue]SAYFA >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',url,47,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
        page2=re.compile('</a><a href=\'(.*?)\' class=\'page smaller\'>.*?</a><span class=\'current\'>.*?</span>').findall(link)
        for url in page2:
                addDir('[COLOR red]Onceki Sayfa[/COLOR]',url,47,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#48
def Aramasinema3(): 
        sinema='http://www.bicaps.net'
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
                
                query = keyboard.getText()
                query=query.replace(' ','+')
                url = (sinema+'/?s='+query)
                Recent3(url)
        addDir('[COLOR yellow]YENI ARAMA YAP[/COLOR]',url,48,"","")
#49
def videolinks3(url,name):
        url=url+'15'
        listeler=[]
        urller=[]
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel=soup.find("div", {"class": "keremiya_part"})
        liste=BeautifulSoup(str(panel))
        match=re.compile('href="(.*?)"><span>(.*?)</span>').findall(str(liste))
        for url,name in match:
            if "netu" in name:
                pass
            else:
                listeler.append('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]')
                urller.append(url)
        dialog = xbmcgui.Dialog()
        secenek = dialog.select('Izleme Secenekleri...',listeler)
        for i in range(len(listeler)):
         if secenek == i:
           url=urller[i]
           VIDEOLINKS1(name,url)
           return url
         else:
           pass
#77
def Sinema4():
        sinema='http://www.evrenselfilm.net'
        addDir('[COLOR yellow]>>[/COLOR] [COLOR red]>> - Arama/Search -<< [/COLOR]',sinema,83,"http://dreamtr.club/resimler/aramasearch.png",'special://home/addons/plugin.video.dreAM/fanart.jpg' )
        addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',sinema,79,"",'special://home/addons/plugin.video.dreAM/fanart.jpg')
        link=get_url(sinema)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "sagBlok"})
        panel = panel[0].findAll("div", {"class": "menu-kat-container"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name= li.text.encode('utf-8', 'ignore')
            name=fix.decode_fix(name)
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,79,'','')               
#79
def Recentsinema4(url):
        link=xbmctools.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "solBlok"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "film"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                name=name.replace('&#8211','').replace('&#8217','').replace('&#038','')
                addDir('[COLOR gold]>>[COLOR beige]'+name+'[/COLOR]',url,29,thumbnail,thumbnail)
        page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">.*?</a>').findall(link)
        for url in page:
                name=' Sonraki Sayfa' 
                addDir('[COLOR blue]'+name+'[/COLOR]',url,79,"http://dreamtr.club/resimler/sonrakisayfa.png","")
#80
def tursinema4(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "sagBlok"})
        panel = panel[0].findAll("div", {"class": "menu-yan2-container"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name= li.text.encode('utf-8', 'ignore')
            name=fix.decode_fix(name)
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,29,'','')
#81
def tarihyabansinema4(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "sagBlok"})
        panel = panel[0].findAll("div", {"class": "menu-tarihegoreyabanci-container"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name= li.text.encode('utf-8', 'ignore')
            name=fix.decode_fix(name)
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,29,'','')
#82
def tarihyerlisinema4(url):
        link=xbmctools.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "sagBlok"})
        panel = panel[0].findAll("div", {"class": "menu-tarihegoreyerli-container"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name= li.text.encode('utf-8', 'ignore')
            name=fix.decode_fix(name)
            addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,29,'','')
#83
def Aramasinema4():     
        sinema='http://www.evrenselfilm.net'
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
                query = keyboard.getText()
                query=query.replace(' ','+')
                url = (sinema+'/?s='+query)
                Recentsinema4(url)
#78
def Sinema5():
    sinema='http://www.ultrafilmizle.com'
    addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',sinema,94,"",'special://home/addons/plugin.video.dreAM/fanart.jpg')
    link=get_url(sinema)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "sidebar"})
    panel = panel[0].findAll("div", {"class": "sidebar-right"})
    liste=BeautifulSoup(str(panel))
    for li in liste.findAll('li'):
        a=li.find('a')
        url= a['href']
        name= li.text
        name=name.encode('utf-8', 'ignore')
        name=name.replace('&#8211;','&').replace('&#8217;','')
        addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,90,'','')
#90
def ulkeleregoresinema5(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "leftC"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "ultra-movie"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        name=name.replace('&#8211','').replace('&','')
        name=name.replace('&#8211;','&').replace('&#8217;','')
        addDir('[COLOR beige][COLOR gold]>>  [/COLOR]'+name+'[/COLOR]',url,95,thumbnail,thumbnail)
    page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
    for url,name in page:
            name='[COLOR blue]'+'Sonraki Sayfa >>'+'[/COLOR]'+'  '+'[COLOR red]'+name+'[/COLOR]'
            addDir(name,url,90,"http://dreamtr.club/resimler/sonrakisayfa.png","")   
#94
def Recentsinema5(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "filmcontent"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "ultra-movie"})
    for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            name=name.replace('&#8211','').replace('&','')
            addDir('[COLOR beige][COLOR gold]>>  [/COLOR]'+name+'[/COLOR]',url,95,thumbnail,thumbnail)
    page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
    for url,name in page:
            name='[COLOR blue]'+'Sonraki Sayfa >>'+'[/COLOR]'+'  '+'[COLOR red]'+name+'[/COLOR]'
            addDir(name,url,94,"http://dreamtr.club/resimler/sonrakisayfa.png","")
#95
def ayrisdirmasinema5(name,url):
    urlA=url+'3'
    link=get_url(urlA)
    match=re.compile('<a href="http://www.ultrafilmizle.com/(.*?)"><span>(.*?)</span></a> ').findall(link)
    for url,name in match:
        if "Ok." in name:
            url='http://www.ultrafilmizle.com/'+url
            addDir('[COLOR beige]'+name+'[/COLOR]',url,41,"","")
        else:
            pass
#1
def Belgesel():
    sinema ='http://www.belgun.tv/'
    addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]YeniEklenen BElgeseller[/COLOR]',sinema,50,"http://dreamtr.club/resimler/yenieklenenler.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
    #name=fix.decode_fix(name)
    link=get_url(sinema)
    match=re.compile('category menu-item-.*?"><a href="(.*?)">(.*?)</a>').findall(link)
    for url,name in match:
            addDir('[COLOR beige][COLOR red]>[/COLOR]'+name+'[/COLOR]',url,50,"","")
#50
def BRecent(url):
        link=get_url(url)
        match=re.compile('<a href="(.*?)" title="(.*?)"><img width="202" height="289" src="(.*?)"').findall(link)
        for url,name,thumbnail in match:
                name=sembol_fix(name)
                addDir('[COLOR cyan]'+name+'[/COLOR]',url,51,thumbnail,thumbnail)
        page=re.compile('<span id="pagSonra"><a href="(.*?)"').findall(link)
        for url in page:
                addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]',url,50,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
def BELayrisdirma(url):
        link=get_url(url)
        match=re.compile('height="349" src="(.*?)"').findall(link)
        for url in match:
            addDir('[COLOR blue]Play >>[/COLOR]',url,88,"","special://home/addons/plugin.video.dreAM/fanart.jpg")
            
        

def sembol_fix(x):
    try:
        x=x.replace('\x93','"').replace('\x92',"'").replace('\x94','"').replace('/',"-").replace('-',"").replace('_'," ").replace("'","'").replace('&#8211;','&').replace('&#8217;','`').replace('&#038;','`').replace('\x85','...').replace('\xb4',"'")
    except:
        pass
    return x[0].capitalize() + x[1:]
#16
def yetiskin():
        url='http://en.paradisehill.cc/porn/'
        addDir('[COLOR red]>>[/COLOR][COLOR yellow]BILGI[/COLOR][COLOR red] <<[/COLOR]',"BILGILENDIRME",56,"","")               
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("section", {"class": "bc-list sect-catg"})
        panel = panel[0].findAll("div", {"class": "col-md-3 col-sm-4 col-xs-6 bc-item"})
        for i in range (len (panel)):
            url=panel[i].find("a", {"class": "bci-link"})['href']
            name=panel[i].find("a", {"class": "bci-link"})['title'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find("img", {"class": "bci-pic"})['src']
            url=z+url
            thumbnail=z+thumbnail
            addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,53,thumbnail,thumbnail)
#53
def Recentyet(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("section", {"class": "bc-list sect-catg"})
        panel = panel[0].findAll("div", {"class": "col-md-3 col-sm-4 col-xs-6 bc-item"})
        for i in range (len (panel)):
            url=panel[i].find("a", {"class": "bci-link"})['href']
            name=panel[i].find("a", {"class": "bci-link"})['title'].encode('utf-8', 'ignore')
            name=name.replace("Watch porno online","")
            thumbnail=panel[i].find("img", {"class": "item_img"})['src']
            thumbnail=z+thumbnail
            url=z+url
            addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,54,thumbnail,thumbnail)
        page=re.compile('<li class="page active"><a href=".*?">.*?</a></li>\n<li class="page"><a href="(.*?)">(.*?)</a></li>').findall(link)
        for url,name in page:
                url=z+url
                addDir('[COLOR blue]NEXT Page >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,53,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#54
def ayrisdirmayet(url):
        link=get_url(url)     
        match=re.compile('var films\= "http:\/\/(.*?).flv"').findall(link)
        for url in match:
                url='http://'+url+'.flv'
                name=' Now'
                addDir('[COLOR red]Watch '+name+'[/COLOR]',url,44,t,t)
        link=get_url(url)
        match1=re.compile("http:\/\/(.*?)part_(.*?).mp4").findall(link)
        for url,name in match1:
                url='http://'+url+'part_'+name+'.mp4'
                addDir('[COLOR red]Part '+name+'[/COLOR]',url,55,"","")
        link=get_url(url)
        match2=re.compile("http:\/\/(.*?).mp4").findall(link)
        for url in match2:
                url='http://'+url+'.mp4'
                name=' Now'
                addDir('[COLOR red]Watch'+name+'[/COLOR]',url,55,"","")               
#55
def VideoLinksyet(name,url):
        url=url+"|referer=http://www.paradisehill.tv/static/flowplayer/flowplayer.content-3.2.9.swf"  
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        xbmctools.addLink('RETURN List << ','','')
        listitem = xbmcgui.ListItem(name)
        playList.add(url, listitem)
        xbmcPlayer.play(playList)
        exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
        if exec_version < 14.0:
                xbmctools.playlist()
        else:
                xbmctools.playlist2()
#56
def INFOyet(url):
  try:
        yetiskin()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR beige]Uyeler icindir[/COLOR],[COLOR yellow]Turkiyeden Izlenemeyebilir[/COLOR] ","[COLOR yellow]DNS Ayarlariyla girilebilir[/COLOR]")
  except:
        pass

#62
def AlmanS():
    sinema='http://www.szene-streams.com'
    addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Neue Filme [/COLOR]',sinema,65,"http://dreamtr.club/resimler/yenieklenenler.png",'special://home/addons/plugin.video.dreAM/fanart.jpg')
    link=get_url(sinema)
    match=re.compile('<a class="CatInf" href="http://www.szene-streams.com/publ/(.*?)">  <div class=".*?">  <div class=".*?">.*?</div>  <div class="CatNameInf">(.*?)</div>').findall(link)
    for url,name in match:
        url='http://www.szene-streams.com/publ/'+url
        addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]'+name+'[/COLOR]',url,64,"",'special://home/addons/plugin.video.dreAM/fanart.jpg')                   
#64
def Yenialman1(url):
    urla=url
    link=get_url(url)
    match=re.compile('<img src="(.*?)" class=".*?" style="" alt="(.*?)" width=".*?" height=".*?"></a></div>\n\n</div>\n</div>\n</div>\n</div> \n<div style=".*?" align=".*?">\n\n<span style=".*?">\n<img style=".*?" src=".*?" alt=".*?" title=".*?" border=".*?"> <b style=".*?">.*?</b>\n</span>\n\n<span style=".*?"></span>\n\n<span style=".*?">\n<img style=".*?" src=".*?" alt=".*?" title=".*?" border=".*?"> <b style=".*?">.*?</b>\n</span>\n</div>\n</td> \n\n\n<td style=".*?" valign=".*?">\n\n<div style=".*?" align=".*?"><b><a class=".*?" <a="" href="(.*?)">').findall(link)
    for thumbnail,name,url in match:
        url='http://www.szene-streams.com/'+url
        addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,66,thumbnail,thumbnail)
    link=get_url(urla)
    page=re.compile('<span>.*?</span></b> <a class="swchItem" href="(.*?)" onclick=".*?"><span>(.*?)</span>').findall(link)
    for url1,name in page:
        if page >1:
                del page[1]
                url=urla+url1
                addDir('[COLOR purple]>>'+'Sayfa ' + name+'[/COLOR]',url,64,"http://dreamtr.club/resimler/sonrakisayfa.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
#65
def Yeni2alman1(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"style": "float:left; width:50%;"},smartQuotesTo=None)
        for i in range (len (panel)):
                div1=panel[i].findAll("div", {"class": "ImgWrapNews"},smartQuotesTo=None)
                thumbnail=panel[i].find('a')['href'].encode('ISO-8859-1', 'ignore')
                name=panel[i].find('img')['alt'].encode('ISO-8859-1', 'ignore')
                div2=panel[i].findAll("a", {"class": "newstitl entryLink"},smartQuotesTo=None)
                url= div2[0]['href']
                url=url
                addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,66,thumbnail,thumbnail)
#66
def Linkleralman1(url):
        link=get_url(url)   
        match1=re.compile('href="\n\nhttp://vidstream.in/(.*?)\n\n">').findall(link)
        for url in match1:
                url='http://vidstream.in/'+url                
                addDir('VidStream    >>',url,99,"","")
        match2=re.compile('href="\n\nhttp://www.divxstage.eu/video/(.*?)\n\n">').findall(link)
        for url in match2:
                url='http://www.divxstage.eu/video/'+url                
                addDir('DivxStage    >>',url,99,"","")
        match3=re.compile('href="\n\nhttp://primeshare.tv/download/(.*?)\n\n">').findall(link)
        for url in match3:
                url='http://primeshare.tv/download/'+url                
                addDir('PrimeShare    >>',url,99,"","")
        match4=re.compile('href="\n\nhttp://www.movshare.net/video/(.*?)\n\n">').findall(link)
        for code in match4:
                code=''                
                addDir('MovShare    >>',"NowVideo(name,url)",url,'')
        match9=re.compile('href="\n\nhttp://www.nowvideo.sx/video/(.*?)\n\n">').findall(link)
        for url in match9:
                url='http://www.nowvideo.sx/video/'+url
                addDir('NowVideo    >>',url,99,"","")
        match8=re.compile(' href="\n\nhttp://streamcloud.eu/(.*?)\n\n"><img alt="" src=".*?" ').findall(link)
        for url in match8:
                url='http://streamcloud.eu/'+url
                addDir('Stream Cloud   >>',url,99,"","")
        match5=re.compile('href="http://played.to/(.*?)">').findall(link)
        for url in match5:
                url='http://played.to/'+url                
                addDir('Played   >>',url,99,"","")
        match6=re.compile('<a target="_blank" href="\n\nhttp://xvidstage.com/(.*?)\n\n">').findall(link)
        for url in match6:
                url='http://xvidstage.com/'+url                
                addDir('XvidStage   >>',url,99,"","")
        match7=re.compile('href="http://faststream.in/(.*?)">').findall(link)
        for url in match7:
                url='http://faststream.in/'+url                
                addDir('FastStream   >>',url,99,"","")
        match10=re.compile('href="http://youwatch.org/(.*?)">').findall(link)
        for url in match10:
                url='http://youwatch.org/'+url
                addDir('YouWATCH   >>',url,99,"","")
        match11=re.compile('<a target="_blank" href="\n\nhttp://www.flashx.tv/(.*?)\n\n">').findall(link)
        for url in match11:
                url='http://www.flashx.tv/'+url                
                addDir('FlashX   >>',url,99,"","")
        match12=re.compile('<a target="_blank" href="\n\nhttp://www.cloudtime.to/video/(.*?)\n\n">').findall(link)
        for url in match12:
                url='http://www.cloudtime.to/video/'+url                
                addDir('CloudTime  >>',url,99,"","")
#68            
def Yeniii(url):
    name='1.Parca'
    addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,200,'','')
    url=url
    link=get_url(url)
    match=re.compile('<a href="(.*?)"><span>(.*?)Par\xc3\xa7a</span></a>').findall(link)
    for url,name in match:
        name=name+'Parca'
        addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,200,'','')

#76
def genelarama():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            query=query.replace(' ','+')
            query=name_fix(query)
        try:
            sinema='http://www.baglanfilmiizle.com'
            addDir('[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[COLOR red]SINEMA 1[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[/COLOR]',sinema,38,"http://dreamtr.club/resimler/Sinema1.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
            sinema='http://www.baglanfilmiizle.com'
            url = (sinema+'/?s='+query)
            sinemaRecent1(url)
        except:
            xbmc.executebuiltin('Notification("[COLOR white]Dream[COLOR white]TR[/COLOR]","[COLOR yellow]Sinema 1 Acilamadi[/COLOR]")') 
        try:
            url='http://www.tekparthd.org/'
            addDir('[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[COLOR red]SINEMA 2[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[/COLOR]',url,44,"http://dreamtr.club/resimler/Sinema2.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
            url='http://www.tekparthd.org/'
            url = (url+'/?s='+query)
            Yenisinema2(url)
        except:
            xbmc.executebuiltin('Notification("[COLOR white]Dream[COLOR white]TR[/COLOR]","[COLOR yellow]Sinema 2 Acilamadi[/COLOR]")')
        try:
            sinema='http://www.bicaps.net'
            addDir('[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[COLOR red]SINEMA 3[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[/COLOR]',sinema,48,"http://dreamtr.club/resimler/Sinema3.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
            sinema='http://www.bicaps.net'
            url = (sinema+'/?s='+query)
            Recent3(url)
        except:
            xbmc.executebuiltin('Notification("[COLOR white]Dream[COLOR red]TR[/COLOR]","[COLOR yellow]Sinema 3 Acilamadi[/COLOR]")')
        try:
            sinema='http://www.evrenselfilm.net'
            addDir('[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[COLOR red]SINEMA 4[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[/COLOR]',sinema,83,"http://dreamtr.club/resimler/Sinema4.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
            sinema='http://www.evrenselfilm.net'
            url = (sinema+'/?s='+query)
            Recentsinema4(url)
        except:
            xbmc.executebuiltin('Notification("[COLOR white]Dream[COLOR red]TR[/COLOR]","[COLOR yellow]Sinema 4 Acilamadi[/COLOR]")')
        try:
            sinema='http://www.ultrafilmizle.com'
            addDir('[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[COLOR red]SINEMA 5[COLOR beige]vvvvvvvvvvvvvvvvvvvvvvvvvvvv[/COLOR]',sinema,96,"http://dreamtr.club/resimler/Sinema4.png","special://home/addons/plugin.video.dreAM/fanart.jpg")
            sinema='http://www.ultrafilmizle.com'
            url = (sinema+'/?s='+query)
            Recentsinema5(url)
        except:
            xbmc.executebuiltin('Notification("[COLOR white]Dream[COLOR red]TR[/COLOR]","[COLOR yellow]Sinema 5 Acilamadi[/COLOR]")')
#63
def AlmanC():
        from xbmctools import web1,web2,web4
        html = xbmctools.sifre100()
        match1 = re.compile('<!--ALCAN(.*?)-->').findall(html)
        for web in match1:
            web='http://wownet.ro/iptv/'
            if web:
                link=get_url(web)
                match = re.compile('#EXTINF:.*?tvg-id=".*?" group-title="DE.*?" tvg-logo=".*?\.png",(.*?)\r\n(.*?)\r').findall(link)
                for name,url in match:
                    if "Marce" in name: pass
                    elif "Sky" in name: pass
                    elif "SKY" in name: pass
                    elif "Down" in name: pass
                    elif "KODI" in name: pass
                    else:
                        addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
            else:
                pass
        name=__settings__.getSetting("Name")
        bak = re.compile('<!--GEL(.*?)-->').findall(html)
        for bilgi in bak:
                dibilgi=xbmctools.angel(base64.b64decode(bilgi))
        coz = re.compile('<!--GIT(.*?)-->').findall(html)
        for digerbilgi in coz:
                genebilgi=xbmctools.angel(base64.b64decode(digerbilgi))
                cj = mechanize.CookieJar()
                br = mechanize.Browser()
                br.set_cookiejar(cj)
                br = mechanize.Browser(factory=mechanize.RobustFactory())
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
                web=xbmctools.angel(base64.b64decode(web1))
                br.open(web)
                br.select_form(nr=0)
                br.form['user_name']=dibilgi
                br.form['user_pass']=genebilgi
                br.submit()
                web3=xbmctools.angel(base64.b64decode(web2))
                br.open(web3)
                html=br.response().read()
                match = re.compile('src="player.php\?channel\=(.*?)&page_id\=1"').findall(html)
                nameList=''
                ok=True
                pDialog = xbmcgui.DialogProgress()
                ret = pDialog.create('Kanal Yukleme...')
                for name in match:
                        if "visitx" in name: pass
                        elif "babes" in name: pass
                        elif "sexy" in name: pass
                        elif "star" in name: pass
                        elif "sportfer" in name: pass
                        else:
                
                                nameList=nameList+name 
                                nameList=nameList+':;'
                                web5=xbmctools.angel(base64.b64decode(web4))
                                url1=web5+name+'&page_id=1'
                                url1=url1.replace(' ','%20')
                                br.open(url1)
                                html2=br.response().read()
                                match2 = re.compile('source src="(.*?)"').findall(html2)
                                total=':;'+nameList
                                match = total.split(':;')
                                del match[-1]
                                totalLinks = len(match)
                                percent = int( ( totalLinks / 36.0) * 100)
                                loadedLinks = 36
                                remaining_display ='Bulunan Kanal Sayisi '+'[COLOR yellow]'+str(totalLinks)+'[/COLOR]'+' / '+'[COLOR green]'+str(loadedLinks)+'[/COLOR]'
                                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'dreAM'+'[COLOR red]TR[/COLOR] Team'+'[/COLOR]'
                                pDialog.update(percent,'[COLOR red]'+'Kanallar Olusturulurken Lutfen Bekleyiniz...'+'[/COLOR]',remaining_display,note)
                                if pDialog.iscanceled():
                                        break
                                totalLinks=totalLinks+1                       
                                for kanal in match2:
                                    url2=kanal
                                    addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url2,'')
#11
def Canli1():
    addDir('[COLOR yellow]~~ Bu Listede Bir Cok Kanalin 2 Farkli Alternatifi Vardir  ~~[/COLOR]','','','https://lh3.ggpht.com/OOXV4V9YyovafA10xZhq0QgWNwFwCEhMI9kWJ2FDkjMmLa7rDWJmSmnsgOtMWdDGg3A=w300','')
    urlK='https://www.kanald.com.tr/embed/542410a361361f36f4c3fcf1'
    link=get_url(urlK)
    match=re.compile('ontentURL" content\="(.*?).m3u8"').findall(link)
    for url in match:
        url=url+'.m3u8'
        thumbnail='https://lh3.ggpht.com/OOXV4V9YyovafA10xZhq0QgWNwFwCEhMI9kWJ2FDkjMmLa7rDWJmSmnsgOtMWdDGg3A=w300'
        name='>> KANAL D '
        addLink('[COLOR beige]'+name+'[/COLOR]',url,'https://lh3.ggpht.com/OOXV4V9YyovafA10xZhq0QgWNwFwCEhMI9kWJ2FDkjMmLa7rDWJmSmnsgOtMWdDGg3A=w300')
    urlO='http://www.onlinetvler.com/'
    link=get_url(urlO)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO2='http://www.onlinetvler.com/?page=1'
    link=get_url(urlO2)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO3='http://www.onlinetvler.com/?page=2'
    link=get_url(urlO3)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'') 
        #-------#   
    web='lmx.otf/b/moc.enisened//:ptth'[::-1]
    link=get_url(web)
    tr=re.compile('<name><!\[CDATA\[(.*?)\]\]></name>\n<link><!\[CDATA\[(.*?)\]\]></link>\n<thumbnail>(.*?)</thumbnail>').findall(link)
    for name,url,thumbnail in tr:
        if "daily" in url:
            addDir(name,url,99,'','')
        else:
            if "kanal-d" in url:
                addDir(name,url,100,'','')
            else:
                if "fox" in url:
                    addDir(name,url,100,thumbnail,'')
                else:
                    if "tv-8" in url:
                        addDir(name,url,100,thumbnail,'')
                    else:
                        if "yol-tv" in url:
                            addDir(name,url,100,'','')
                        else:
                            if "kral" in url:
                                addDir(name,url,107,'','')
                            else:
                                addLink(name,url,thumbnail)
    url="http://m.canlitv.com/"
    link=get_url(url)
    match=re.compile('<a href="(.*?)" title=".*?">\r\n<div class="kanal_list">\r\n<div class="kanal_resim"><img src="(.*?)" alt=".*?"/></div>\r\n<div class="kanal_ad">(.*?)</div>').findall(link)
    for url,thumbnail,name in match:
        if "STV" in name: pass
        elif "Saman" in name : pass
        elif "rm" in name: pass
        elif "Mc T" in name: pass
        elif "Meht" in name: pass
        elif "nya" in name : pass
        elif "al T" in name: pass
        elif "Yum" in name: pass
        elif "CNN" in name: pass
        elif "anal A" in name: pass
        elif "mc Tv" in name: pass
        elif "y Tv" in name: pass
        elif "nal D" in name: pass
        else:
            url=url.replace('./','')
            url='http://m.canlitv.com/'+url
            thumbnail='http://m.canlitv.com/'+thumbnail
            addDir(name,url,107,thumbnail,'')

#100
def ctv1(name,url):
    try:
        link=get_url(url)
        match = re.compile('file:"(.*?)"').findall(link)
        for url in match:
            if url:
                url=url+tk
                xbmcPlayer.play(url)
            addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        match1= re.compile("file: \'http(.*?)m3u8\'").findall(link)
        for url in match1:
            if url:
                url='http'+url+'m3u8'+tk
                xbmcPlayer.play(url)
            addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
    except:
        showMessage('[COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]','[COLOR red]Iyi Seyirler Diler!!![/COLOR]')
        addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png') 
#12
def Canli2():
    html = xbmctools.sifre100()
    name=__settings__.getSetting("Name")
    login=__settings__.getSetting("Username")
    password=__settings__.getSetting("password")
    match = re.compile('<!--#(.*?)-->').findall(html)
    for web in match:
        web=''
##    addDir('[COLOR orange]~~ Bu Listede Bir Cok Kanalin 2 Farkli Alternatifi Vardir  ~~[/COLOR]','','','https://lh3.ggpht.com/OOXV4V9YyovafA10xZhq0QgWNwFwCEhMI9kWJ2FDkjMmLa7rDWJmSmnsgOtMWdDGg3A=w300','')
##    urlOW='http://onlinetvcanli.com/'
##    link=get_url(urlOW)
##    match=re.compile('<a href="(.*?)" title=".*?"><img src="(.*?)" alt="(.*?)" class="aligncenter" width="80" height="80"').findall(link)
##    for url,Thumbnail,name in match:
##        addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR pink]'+name+'[/COLOR]',url,41,Thumbnail,Thumbnail)
    urlO='http://www.onlinetvler.com/'
    link=get_url(urlO)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO2='http://www.onlinetvler.com/?page=1'
    link=get_url(urlO2)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO3='http://www.onlinetvler.com/?page=2'
    link=get_url(urlO3)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'') 
#101
def ctv2(url):
    try:
        link=xbmctools.get_url(url)
        match=re.compile('http://(.*?).m3u8').findall(link)
        for url in match:
            if url:
                url='http://'+url+'.m3u8'+tk
                xbmcPlayer.play(url)
            addDir('[COLOR red]RETURN List << [/COLOR]','',12,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
    except:
        showMessage('[COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]','[COLOR red]Iyi Seyirler Diler!!![/COLOR]')
        addDir('[COLOR red]RETURN List << [/COLOR]','',12,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')   
#18
def Canli3():
    url='txt.3vtc/b/moc.enisened//:ptth'[::-1]
    link=get_url(url)
    match=re.compile('<name>(.*?)\n<thumbnail>(.*?)\n<link>(.*?)\n').findall(link)       
    for name,Thumbnail,url in match:
        name=fix.decode_fix(name)
        addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR beige]'+name+'[/COLOR]',url,100,Thumbnail,Thumbnail)
#27
def Canli4():
    addDir('[COLOR yellow]~~ Bu Listede Her Kanalin 2 Farkli Alternatifi Vardir  ~~[/COLOR]','','','','')
    url1='txt.24vtc/b/moc.enisened//:ptth'[::-1]
    link=get_url(url1)
    match=re.compile('NOTICE:(.*?)\n.*?NOTICE: (.*?)\n.*?NOTICE: (.*?)\n').findall(link)
    for url,img,name in match:
        addDir('[COLOR yellow][COLOR purple]>>[/COLOR]  '+name+'[/COLOR]',url,71,img,img)
    url='txt.nig/kabmaZa/moc.enisened//:ptth'[::-1]
    link=get_url(url)
    match=re.compile('<title>(.*?)</title>\nKanal Linki:  (.*?).m3u8').findall(link)
    for name,url2 in match:
        img=''
        url2=url2+'.m3u8'
        addDir('[COLOR beige][COLOR purple]>>[/COLOR]  '+name+'[/COLOR]',url2,91,img,img)       
#91
def de_get(name,url):
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.stop()
    import requests as requests
    url1='802=di?php.hctaw/moc.okinig.www//:ptth'[::-1]
    link=get_url(url1)
    match=re.compile('m3u8\?(.*?)"').findall(link)
    for cd in match:
        if "utna" in url:
            VideoLinks3(name,url)
        else:
            import requests as requests
            if 'xxx&User' in url:
                x = url.partition('xxx&User')
                url = x[0] + 'xxx'
            else:
                print "user yok"
            x = url.partition('---')
            url = x[0]
            id = x[2].replace('xxx','')
            url=url+'?'+cd
            if url:
                xbmcPlayer.play(url)
                try:
                    addDir('[COLOR red]RETURN List << [/COLOR]','',18,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
                except:
                    showMessage('[COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]','[COLOR red]Iyi Seyirler Diler!!![/COLOR]')
                    addDir('[COLOR red]RETURN List << [/COLOR]','',18,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')  
            else:
                print "DreamTR"
def showMessage(heading='DreamTR', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )    
#41 
def VIDEOLINKS1(name,url):
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        urlList=[]
        playList.clear()
        link=get_url(url)
        matchOK=re.compile('\/live\/(.*?)"').findall(link)
        for url in matchOK:
            url=url.replace('#038;','')
            url='http://embedlive.flexmmp.com/live/'+url
            link=get_url(url)
            match2=re.compile('src: "(.*?)"').findall(link)
            for url in match2:
                url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
                listitem = xbmcgui.ListItem(name)
                playList.add(url, listitem)
                xbmcPlayer.play(playList)
                exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
                if exec_version < 14.0:
                        xbmctools.playlist()
                else:
                        xbmctools.playlist2()
        ply=re.compile('\/player\/url\/(.*?)"').findall(link)
        for name in ply:
                name=base64.b64decode(name)
                reverseName=""
                for x in range(len(name)-1,-1,-1):
                        reverseName+=name[x]
                reverseName=base64.b64decode(reverseName)
                reverseName=reverseName.replace('ok/','')
                url=reverseName
                url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
                ok_ru(url)
        mega2=re.compile('http:\/\/videomega.tv\/view.php\?ref\=(.*?)\&.*?').findall(link)
        for url in mega2:
            url='http://videomega.tv/view.php?ref='+url
            magix_player(name,url)
        cldy=re.compile('cloudy.ec\/embed.php\?id\=(.*?)"').findall(link)
        for url in cldy:
            url='https://www.cloudy.ec/embed.php?id='+url
            magix_player(name,url)
        vidag=re.compile('vid.ag\/embed\-(.*?)\.html"').findall(link)
        for url in vidag:
            url='http://vid.ag/embed-'+url+'.html'
            magix_player(name,url)
        mega=re.compile('\videomega.tv\/(.*?)\&amp;width.*?"').findall(link)
        for url in mega:
            url='http://videomega.tv/'+str(url).encode('utf-8', 'ignore')
            magix_player(name,url)
        opn=re.compile('src="https://openload.co/embed/(.*?)/"').findall(link)
        for url in opn:
            url='https://openload.co/embed/'+url+'/'
            magix_player(name,url)
        mlr=re.compile('\/videos\/embed\/mail\/(.*?)\.html').findall(link)
        for url in mlr:
            url='http://videoapi.my.mail.ru/videos/embed/mail/'+url+'.html'
            magix_player(name,url)
        link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
        ok=re.compile('ok.ru\/videoembed\/(.*?)"').findall(link)
        for url in ok:
                url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
                ok_ru(url)
        ok_9=re.compile('ok.php\?vid\=(.*?)"').findall(link)
        for url in ok_9:
                url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
                ok_ru(url)
        vk_2=re.compile('src="http://vk.com/(.*?)"').findall(link)
        for url in vk_2:
                url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                magix_player(name,url)
        vk_3=re.compile('rc="http://snnyk.com/(.*?)"').findall(link)
        for url1 in vk_3:
                url1=url1.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                url1 = 'http://snnyk.com/'+str(url1).encode('utf-8', 'ignore')
                link=get_url(url1)
                vkvk=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
                for oid,vidid,has in vkvk:
                        url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
                        magix_player(name,url)
        youtube=re.compile('\youtube\.com\/embed\/(.*?)\"').findall(link)
        for url in youtube:
                url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                magix_player(name,url)
        mailru2=re.compile('\/\/videoapi.my.mail.ru\/videos\/embed\/mail\/(.*?).html').findall(link)
        for mailrugelen in mailru2:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
                magix_player(name,url)
        mailru3=re.compile('http://api.video.mail.ru/videos/embed/mail/(.*?).html').findall(link)
        for mailrugelen in mailru3:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
                magix_player(name,url)
        if not urlList:
                match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                if match:
                    for url in match:
                            VIDEOLINKS1(name,url)
        if urlList:
                Sonuc=playerdenetle(name, urlList)
                for name,url in Sonuc:
                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                        listitem.setInfo('video', {'name': name } )
                        playList.add(url,listitem=listitem)
                xbmcPlayer.play(playList) 
def playerdenetle(name, urlList):
        value=[]
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:
                if "mail.ru" in url:
                    magix_player(name,url) 
        if  value:
            return value
def name_fix(x):        
        x=x.replace('-',' ').replace('_',' ')
        return x[0].capitalize() + x[1:]

def replace_fix(x):        
        x=x.replace('&#8211;', '-').replace('&#8211;', '-').replace('&#038;', '&').replace('http://loads7.com/blog/', '').replace('http://loads7.com', '').replace(' ', '').replace('&#038;', '&').replace('&amp;', '&').replace('&#8217;', "'").replace("2000'ler"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]2000'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('2012201120102009200820072006200320012000','').replace('193919361931','').replace("1930'lar"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1930'lu Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('1948194619451944194219411940','').replace("1940'lar"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1940'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('19581957195619551954195319511950','').replace("1950'ler"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1950'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('19691968196719641963196219611960','').replace("1960'lar"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1960'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('1979197819771976197519741973197219711970','').replace("1970'ler"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1970'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('1989198819871986198519841983198219811980','').replace("1980'ler"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1980'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]").replace('1999199819971996199519941993199219911990','').replace("1990'lar"," [COLOR red]<<<<<<<<<<<<[/COLOR][COLOR beige]1990'li Yillar Asagidadir[/COLOR][COLOR red]>>>>>>>>>>>>[/COLOR]")
        return x
#99
def magix_player(name,url):
        UrlResolverPlayer = url
        playList.clear()
        media = urlresolver.HostedMediaFile(UrlResolverPlayer)
        source = media
        if source:
                url = source.resolve()
                addLink(name,url,'')
                playlist_yap(playList,name,url)
                xbmcPlayer.play(playList)
def playlist_yap(playList,name,url):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        return playList
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
    xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
    streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
    if streams >0:
        for name2,url2 in streams:          
            xbmcPlayer = xbmc.Player()
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            addLink(name2,url2,'')
            listitem = xbmcgui.ListItem(name2)
            playList.add(url2, listitem)
        xbmcPlayer.play(playList)

USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
def ok_ru(url):
        sources = []
        if(re.search(r'ok.ru', url)):
            id = re.search('\d+', url).group(0)
            jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
            jsonSource = json.loads(http_req(jsonUrl))
            for source in jsonSource['videos']:
                name = '%s %s' % ('', source['name'])
                duzenleyici = re.search(r'sig.+', source['url']).group(0)
                url='http://m.ok.ru/dk?st.cmd=moviePlaybackRedirect&st.'+duzenleyici
                addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,42,"","")
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
#199
def yenical44(name,url):
        if "mail." in url:
            MailRu_Player(url)
        elif "vk."in url:
            magix_player(name,url)
        elif "ok." in url:
            ok_ru(url)
        elif "vid."in  url:
            magix_player(name,url)
        else:
            xbmcPlayer = xbmc.Player() 
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
            playList.clear() 
            addLink(name,url,'')
            listitem = xbmcgui.ListItem(name) 
            playList.add(url, listitem) 
            xbmcPlayer.play(playList)
def oynat(url,name):       
        playList.clear()
        url = str(url).encode('utf-8', 'ignore')
        if "dailymotion" in url:
            url= dailyplayer(url)
        elif "ok.ru" in url:
                url= okru(url)
        elif "odnoklassniki.ru" in url:
                url= okru(url)
        else:
            url1=urlresolver.resolve(url)
            if url1:
                    url = url1
        if url:
            if ("vk.com" in url or "youtube.com" in url or "rutube" in url):
                    oynat(url, name)
            else:
                    addLink(name,url,'')
                    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
                    listitem.setInfo('video', {'name': name } )
                    playList.add(url,listitem=listitem)
                    xbmcPlayer.play(playList)
        else:
                showMessage("[COLOR red][B]DreamTR[/B][/COLOR]","[COLOR beige][B]Link Bulunamadi[/B][/COLOR]")
def okru(url):

    id = re.search('\d+', url).group(0)
    json_url = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id

    req = urllib2.Request(json_url)
    response = urllib2.urlopen(req)
    source = response.read()
    response.close()
    json_source = json.loads(source)
    videolist = []
    qualitylist = []
    sources = []
    for source in json_source['videos']:
        name = source['name']
        link = source['url']
        videolist.append(link.decode('unicode_escape').encode('utf-8'))
        qualitylist.append(name)
    dialog = xbmcgui.Dialog()
    ret = dialog.select('kalite secin...',qualitylist)
    return videolist[ret] 

def dailyplayer(url):
        qualitylist =[]
        videolist=[]
        url = url.replace('dailymotion.com/video/', 'dailymotion.com/embed/video/')
        page = get_url(url)
        array = re.findall('stream_h264_(?:hd1080_|ld_|hq_|hd_|)url":"(.*?H264-(.*?)\\\\/.*?)"', page)
        if array:
                for v, q in array:
                        url = v.replace('\\', '')
                        videolist.append(url)
                        qualitylist.append(q+"p")
        array1 = re.findall('"(\\d+)":\\[{"type":"video\\\\\\/mp4","url":"([^"]+)"}]', page)
        if array1:
                for v, q in array1:
                        url = q.replace('\\', '')
                        videolist.append(url)
                        qualitylist.append(v+"p")
        dialog = xbmcgui.Dialog()
        ret = dialog.select('kalite secin...',qualitylist)
        return videolist[ret]  
#42
def yenical4(name,url):
    xbmcPlayer = xbmc.Player() 
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
    playList.clear() 
    addLink(name,url,'')
    listitem = xbmcgui.ListItem(name) 
    playList.add(url, listitem) 
    xbmcPlayer.play(playList)
    
def vk_player(name,url):
        hd = re.search('.*?(hd=\d)$',url).group(1)
        url1 = url.replace(hd,"hd=3")
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        liste=[]
        fixed=''
        gecis=0
        link=get_url(url1)
        host=re.compile("host=([^\&]+)").findall(link)
        uid=re.compile("uid=([^\&]+)").findall(link)
        vtag=re.compile("vtag=([^\&]+)").findall(link)
        hd = re.compile("hd_def=([^\&]+)").findall(link)
        extra = re.compile('mp4?(.*?)",').findall(link)
        if not hd or hd[0]=="-1":
            hd = re.compile("hd=([^\&]+)").findall(link)
        flv = re.compile("no_flv=([^\&]+)").findall(link)
        vkstream='%su%s/videos/%s' % (host[0],uid[0],vtag[0])
        x=(int(hd[0])+1)
        if hd >0 or flv == 1:
                for i in range (x):
                        streamkalite = ["240", "360", "480", "720", "1080"] 
                        i=streamkalite[i]+' p'
                        liste.append(i) 
                if gecis==0:
                        dialog = xbmcgui.Dialog()
                        ret = dialog.select('kalite secin...',liste)
                        for i in range (x):
                                if ret == i:
                                        url=vkstream+'.'+str(streamkalite[i])+'.mp4'+extra[0]
                                        fixed=str(streamkalite[i])
                                else:
                                        pass
                else:
                        url=vkstream+'.'+fixed+'.mp4'+extra[0]       
        addLink(name,url,'')
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        xbmcPlayer.play(playList)

def vk2_player(name,url):
    link=get_url(url)
    name="[COLOR beige]Tek Part VK[/COLOR]"              
    if "480" in link:
            match4=re.compile('"url480":"(.*?)"').findall(link)
    elif "360" in link:
            match4=re.compile('"url360":"(.*?)"').findall(link)
    elif "240" in link:
            match4=re.compile('"url240":"(.*?)"').findall(link)
    else:
            print "video yok"
    for url in match4:
            url=url.replace("\/","/")  
    addLink(name,url,'')
    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
    listitem.setInfo('video', {'name': name } )
    playList.add(url,listitem=listitem)
    xbmcPlayer.play(playList)

#105
def radyo():
        url='http://canliradyodinle.web.tr/'
        link=get_url(url)
        match=re.compile('<a href="http://canliradyodinle.web.tr/Radyolar/(.*?)"> <span class="icon.*?">').findall(link)
        for name in match:
                url='http://canliradyodinle.web.tr/Radyolar/'+name
                name=fix.decode_fix(name)
                addDir('[COLOR orange]>>'+name+'[/COLOR]',url,106,'','')
#106
def radyorecent(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "content"})
    panel = panel[0].findAll("div", {"class": "radio-mini"})
    for i in range (len (panel)):
            url=panel[i].find("a")['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            addDir('[COLOR orange] >> '+name+'[/COLOR]',url,107,thumbnail,thumbnail)
            
            
    sayfalama=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
    for url,name in sayfalama:
            addDir('[COLOR orange] >>Next Page - ' +name+'[/COLOR]',url,106,'','')
#107
def radyocal(url):
        link=get_url(url)
        match93=re.compile('"http://(.*?).m3u8(.*?)"').findall(link)
        for a,b in match93:
            url='http://'+a+'.m3u8'+b+tk
            xbmcPlayer = xbmc.Player()
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            listitem = xbmcgui.ListItem(name)
            playList.add(url, listitem)
            xbmcPlayer.play(playList)
            exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
            if exec_version < 14.0:
                    xbmctools.playlist()
            else:
                    xbmctools.playlist2()
        match94=re.compile('php\?radyo\=(.*?)\&amp\;').findall(link)
        for url in match94:
            xbmcPlayer = xbmc.Player()
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            listitem = xbmcgui.ListItem(name)
            playList.add(url, listitem)
            xbmcPlayer.play(playList)
            exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
            if exec_version < 14.0:
                    xbmctools.playlist()
            else:
                    xbmctools.playlist2()

#109
def kemal(url):
    link=get_url(url)
    kemal=re.compile('<kemalsunalname><!\[CDATA\[(.*?)\]\]></kemalsunalname>\n  <kemalsunallink><!\[CDATA\[(.*?)\]\]></kemalsunallink>\n  <kemalsunalthumbnail><!\[CDATA\[(.*?)\]\]></kemalsunalthumbnail>').findall(link)
    for name,url,thumbnail in kemal:
        addDir('[COLOR orange][B]>>[/B][/COLOR]'+'[COLOR beige][B]'+name+'[/B][/COLOR]',url,42,thumbnail,"http://img.onedio.com/img/raw/53b54bbdd15fe8394633e6b9")
#110
def ulbes(url):
    url='lmx.riseb/lmxriseB/moc.tayahalmalsi//:ptth'[::-1]
    link=get_url(url)
    tr=re.compile('<name><!\[CDATA\[(.*?)\]\]></name>\n  <link><!\[CDATA\[(.*?)\]\]></link>\n  <thumbnail><!\[CDATA\[(.*?)\]\]></thumbnail>').findall(link)
    for name,url,thumbnail in tr:
        addDir('[COLOR orange]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,199,thumbnail,thumbnail)
#111        
def ulsin(url):
    link=get_url(url)
    tr=re.compile('<sinemaname><!\[CDATA\[(.*?)\]\]></sinemaname>\n  <sinemalink><!\[CDATA\[(.*?)\]\]></sinemalink>\n  <sinemathumbnail><!\[CDATA\[(.*?)\]\]></sinemathumbnail>').findall(link)
    for name,url,thumbnail in tr:
        addDir('[COLOR orange][B]>>[/B][/COLOR]'+'[COLOR beige][B]'+name+'[/B][/COLOR]',url,42,thumbnail,thumbnail)
#114
def yesilcam():
    url='txt.maclisey/b/moc.enisened//:ptth'[::-1]
    link=get_url(url)
    match=re.compile('>>(.*?)<<').findall(link)
    for url in match:
        url=str(url)
        link=get_url(url)
        match=re.compile('<a href="\/watch\?v\=(.*?)" class=".*?" data-sessionlink=".*?" title="(.*?)"').findall(link)
        for a,name in match:
            thumbnail='https://i.ytimg.com/vi_webp/'+a+'/default.webp'
            url='plugin://plugin.video.youtube/?action=play_video&videoid='+a
            addDir('[COLOR orange]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,42,thumbnail,'')

#116
def Calcanli6(name,url):
    xbmcPlayer = xbmc.Player()
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playList.clear()
    addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
    listitem = xbmcgui.ListItem(name)
    playList.add(url, listitem)
    xbmcPlayer.play(playList)
    exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
    if exec_version < 14.0:
            xbmctools.playlist()
    else:
            xbmctools.playlist2()

def addLink(name, url, thumbnail):
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
    liz.setInfo(type="Video", infoLabels={"Title":name})
    liz.setProperty("IsPlayable", "true")
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    
def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param
params=get_params()
url=None
name=None
mode=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

if mode==None or url==None or len(url)<1:

    CATEGORIES()
elif mode==1: Belgesel()        
elif mode==2: Sinema()
elif mode==3: Dizi()
elif mode==4: canliyayin()
elif mode==5: Sinema1()
elif mode==6: Sinema2()
elif mode==7: Sinema3()
elif mode==8: Dizi1()
elif mode==9: Dizi2()
elif mode==10: Dizi3()
elif mode==11: Canli1()
elif mode==12: Canli2()
elif mode==13: Dizi4()
elif mode==14: Arama()
elif mode==15: Kategoriler()
elif mode==16: yetiskin()
##elif mode==17: yetiskin2()
elif mode==18: Canli3()
elif mode==19: Yeni(url)
elif mode==20: dizivideolinks(url,name)
elif mode==21: Yeni2(url)
##elif mode==22: EskiDiziler2(url)
elif mode==23: YeniDiziler2()
##elif mode==24: Yarisma2(url)
elif mode==25: Arama2()
elif mode==26: dizivideolinks2(url,name)
elif mode==27: Canli4()
elif mode==28: sinemaRecen1(url)
elif mode==29: ayrisdirm1(url)
elif mode==30: yerlidizi3()
elif mode==31: Yeni3(url)
elif mode==32: dizivideolinks4(url,name)
elif mode==33: yerlidizi4()
elif mode==34: Yeni4(url)
elif mode==35: Hepsi4(url)
##elif mode==36: Kategoriler1()
##elif mode==37: Kategorileryil1()
elif mode==38: Aramasinema1()
elif mode==39: sinemaRecent1(url)
elif mode==40: ayrisdirma1(url)
elif mode==41: VIDEOLINKS1(name,url)
elif mode==42: yenical4(name,url)
elif mode==43: Yenisinema2(url)
elif mode==44: Search2()
elif mode==45: ayrisdirma2(url)
elif mode==46: Kategoriler2()
elif mode==47: Recent3(url)
elif mode==48: Aramasinema3()
elif mode==49: videolinks3(url,name)
elif mode==50: BRecent(url)
elif mode==51: BELayrisdirma(url)
##elif mode==52: BSearch()
elif mode==53: Recentyet(url)
elif mode==54: ayrisdirmayet(url)
elif mode==55: VideoLinksyet(name,url)
elif mode==56: INFOyet(url)
##elif mode==57: Recentyet2(url)
##elif mode==58: ayrisdirmayet2(url)
elif mode==59: VideoLinksyet2(name,url)
elif mode==60: INFOyet2(url)
elif mode==61: Alman()
elif mode==62: AlmanS()
elif mode==63: AlmanC()
elif mode==64: Yenialman1(url)
elif mode==65: Yeni2alman1(url)
elif mode==66: Linkleralman1(url)
##elif mode==67: AlmanS2()
elif mode==68: Yeniii(url)
##elif mode==69: neueadalmanS2(url)
##elif mode==70: neuead2almanS2(url)
##elif mode==71: ayrisdirmaalmanS2(name,url)
##elif mode==72: SearchalmanS2()
##elif mode==73: YenialmanS3(url)
##elif mode==74: SearchalmanS3()
##elif mode==75: LinkleralmanS3(url)
elif mode==76: genelarama()
elif mode==77: Sinema4()
elif mode==78: Sinema5()
elif mode==79: Recentsinema4(url)
elif mode==80: tursinema4(url)
elif mode==81: tarihyabansinema4(url)
elif mode==82: tarihyerlisinema4(url)
elif mode==83: Aramasinema4()
##elif mode==84: ayrissinema4(url)
##elif mode==85: VIDEOLINKSsinema4(name,url)
##elif mode==86: VIDEOLINKS2sinema4(name,url)
##elif mode==87: VIDEOLINKS3sinema4(name,url)
##elif mode==88: VIDEOLINKS4sinema4(name,url)
elif mode==88: oynat(url,name)
elif mode==89: yeniler3(url)
elif mode==90: ulkeleregoresinema5(url)
elif mode==91: de_get(name,url)
elif mode==94: Recentsinema5(url)
elif mode==95: ayrisdirmasinema5(name,url)
##elif mode==97: VideoLinkscanli(name,url)
elif mode==98: dailyplayer(url)
elif mode==99: magix_player(name,url)
elif mode==100: ctv1(name,url)
elif mode==101: ctv2(url)
elif mode==102: ok_ru(url)
elif mode==103: vk_player(name,url)
elif mode==1030: vk2_player(name,url)
elif mode==104: MailRu_Player(url)
elif mode==105: radyo()
elif mode==106: radyorecent(url)
elif mode==107: radyocal(url)
##elif mode==108: portal()
elif mode==109: kemal(url)
elif mode==110: ulbes(url)
elif mode==111: ulsin(url)
##elif mode==112: DreamTV()
##elif mode==113: acsana(name)
elif mode==114: yesilcam()
##elif mode==115: Canli6()
elif mode==116: Calcanli6(name,url)
elif mode==119: TVPROG()
elif mode==120: fox1(url)
elif mode==121: fox2(url)
elif mode==122: trt1(url)
elif mode==123: trt2(url)
elif mode==124: star1(url)
elif mode==125: star2(url)
elif mode==126: kanald1(url)
elif mode==127: kanald2(url)
elif mode==128: showtv1(url)
elif mode==129: showtv2(url)
elif mode==130: atv1(url)
elif mode==131: atv2(url)
elif mode==132: kanaldprog(url)
elif mode==133: atvprog1(url)
elif mode==134: atvprog2(url)
elif mode==135: starprog(url)
elif mode==140: Diziara()
elif mode==199: yenical44(name,url)
##elif mode==200: survivorvideo(url,name)
elif mode==2000: __settings__.openSettings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
