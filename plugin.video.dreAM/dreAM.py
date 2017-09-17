#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import BeautifulSoup as BS4
import xbmctools,fix
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

fann="special://home/addons/plugin.video.dreAM/fanart.jpg"
aramaa="http://dreamtr.club/resimler/aramasearch.png"
yeniek="http://dreamtr.club/resimler/yenieklenenler.png"
sonrakii="http://dreamtr.club/resimler/sonrakisayfa.png"

tk="|User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')"
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

addon_id = 'plugin.video.dreAM'
__settings__ = xbmcaddon.Addon(id=addon_id)
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
addon_icon    = __settings__.getAddonInfo('icon')

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
         xbmctools.addDir('[COLOR blue]SiNEMALAR[/COLOR]',"Sinema()",2,'http://dreamtr.club/resimler/Sinemalar.png',fann)
         xbmctools.addDir('[COLOR pink]DiZiLER[/COLOR]',"Dizi()",3,'http://dreamtr.club/resimler/Diziler.png',fann)
         xbmctools.addDir('[COLOR yellow]CANLI YAYINLAR[/COLOR]',"canliyayin()",4,'http://dreamtr.club/resimler/CanliTVler.png',fann)
         xbmctools.addDir('[COLOR yellow]DreamTR Radyolar[/COLOR]',"radyo()",105,'http://dreamtr.club/resimler/Radyo.png',fann)
         xbmctools.addDir('[COLOR purple]BELGESEL iZLE[/COLOR]',"Belgesel()",1,'http://dreamtr.club/resimler/belgeselizle.png',fann)
         xbmctools.addDir('[COLOR grey]ALMAN Sinema[/COLOR]',"Alman()",62,'http://dreamtr.club/resimler/almanlar.png',fann)
         xbmctools.addDir('[COLOR grey]DREAM AYARLAR[/COLOR]',"Ayarlar()",2000,'http://dreamtr.club/resimler/ayarlar.png',fann)
         xbmctools.addDir('[COLOR orange]*IPTV-Pro-Platinium* [/COLOR]',"iptvpro(name,url)",202,'http://dreamtr.club/resimler/iptvpro.png',fann)
         if gizlilik == "false" or gizlilik2 != gizlilik3 or gizlilik4 == "false":
             pass
         else:
             xbmctools.addDir('[COLOR red]+18[/COLOR]',"yetiskin()",16,'http://dreamtr.club/resimler/adult1.png',fann)
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
        xbmctools.addDir('[COLOR gold]! Sinema 1 * New * ![/COLOR]',"Sinema1()",5,'http://dreamtr.club/resimler/Sinema1.png',fann)
        xbmctools.addDir('[COLOR gold]! Yerlifilmiizle.Net * New * ![/COLOR]',"Sinema2()",6,'http://dreamtr.club/resimler/Sinema2.png',fann)
        xbmctools.addDir('[COLOR beige]Sinema 3[/COLOR]',"Sinema3()",7,'http://dreamtr.club/resimler/Sinema3.png',fann)
        xbmc.executebuiltin('Container.SetViewMode(500)')
#3
def Dizi():
    xbmctools.addDir('[COLOR orange]Dizi 1 * NEW Edition *[/COLOR]',"Dizi1()",8,'http://dreamtr.club/resimler/Dizi1.png',fann)
    xbmctools.addDir('[COLOR gold]Dizi 2 ## NEW ##[/COLOR]',"Dizi2()",9,'http://dreamtr.club/resimler/Dizi2.png',fann)
    xbmc.executebuiltin('Container.SetViewMode(500)')
#4
def canliyayin():
        xbmctools.addDir('[COLOR beige]Canli Tv 1[/COLOR]',"Canli1()",11,'http://dreamtr.club/resimler/Canlitv1.png',fann)
        xbmctools.addDir('[COLOR pink]Canli Tv 2* New *[/COLOR]',"Canli2()",12,'http://dreamtr.club/resimler/Canlitv2.png',fann)
        xbmctools.addDir('[COLOR beige]Canli Tv 3[/COLOR]',"Canli3()",18,'http://dreamtr.club/resimler/Canlitv3.png',fann)
        xbmctools.addDir('[COLOR orange]* Canli Tv 4 * New *[/COLOR]',"Canli4()",27,'http://dreamtr.club/resimler/Canlitv4.png',fann)
        xbmc.executebuiltin('Container.SetViewMode(500)')

#--#
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; SmartTV) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
#8
def Dizi1():
    url='http://www.canlihddizi.com/'
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,14,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,19,yeniek,fann)
    link=get_url(url)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)" >(.*?)</a>\n</li>').findall(link)
    for url,name in match:
            xbmctools.addDir('[COLOR beige]>'+name+'[/COLOR]',url,28,'','')
#14
def Arama():
        dizi1='http://www.canlihddizi.com/'
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (dizi1+'/?s='+query)
            Yeni(url)
#27
def Canli4():
    url='txt.nig/kabmaZa/bulc.rtmaerd//:ptth'[::-1]
    link=get_url(url)
    match=re.compile('<title>(.*?)--(.*?)</title>\n.*?<link>(.*?)\?.*?</link>').findall(link)
    for name,img,url2 in match:
        xbmctools.addDir('[COLOR beige][COLOR purple]>>[/COLOR]  '+name+'[/COLOR]',url2,91,img,img)
    match1=re.compile('<title>(.*?)--(.*?)</title>\n.*?<link>http://roku(.*?)</link>').findall(link)
    for name,img,url2 in match1:
        url2='http://roku'+url2
        xbmctools.addDir('[COLOR beige][COLOR orange]>>[/COLOR]  '+name+'[/COLOR]',url2,116,img,img)
#91
def de_get(name,url):
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.stop()
    import requests as requests#halktv
    url1='882=di?php.hctaw/moc.okinig.www//:ptth'[::-1]
    link=get_url(url1)
    match=re.compile('src=".*?\?wmsAuthSign\=(.*?)">').findall(link)
    for cd in match:
        print "hosgeldin"
    url=url+'?wmsAuthSign='+cd#+tk
    xbmctools.yenical4(name,url)
#19
def Yeni(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "fix-film-v2_item fix_home clearfix list_items"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "movie-poster"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
    page=re.compile('<span class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
    for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,sonrakii,fann)
#28
def Yeni222(url):
    link=get_url(url)
    match=re.compile('href="(.*?)">\n\n\t\t\t<span class=".*?"><span class=".*?" title=".*?"></span><span class=".*?" title=".*?">.*?</span></span><span class=".*?">(.*?)</span>\t\t\t<img src="(.*?)"').findall(link)
    for url,name,thumbnail in match:
        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
    page=re.compile('<span class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
    for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,sonrakii,fann)
#20
def dizivideolinks(url,name):
    xbmctools.addDir('[COLOR beige]>>[/COLOR]'+'[COLOR gold]'+'1 . Secenek '+'[/COLOR]',url,22,fann,fann)
    try:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "keremiya_part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('<a href="(.*?)"><span>(.*?)</span>').findall(str(liste))
        for url,name2 in match2:
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name2+'[/COLOR]',url,22,fann,fann)            
    
    except:
        pass

#9
def Dizi2():
        url='http://www.ddizi1.com'
        xbmctools.addDir('[COLOR red]>>>>>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,25,aramaa,fann)
        xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,yeniek,fann)
        url1='http://www.ddizi1.com'
        link=get_url(url1)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "blok-alt"},smartQuotesTo=None)
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('li'):
            a=li.find('a')
            url= a['href']
            name=li.text
            name=fix.decode_fix(name)
            name=name.encode('utf8')
            thumbnail=""
            xbmctools.addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,23,thumbnail,thumbnail)
#25
def Arama2():
        dizi2='moc.2dhizidilnac.www//:ptth'[::-1]
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (dizi2+'/?s='+query)
            Yeni2(url)

#21
def Yeni2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-alt"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "dizi-box"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        thumbnail='http://www.ddizi1.com/'+thumbnail
        name=name.replace('&#8211','').replace('&','')
        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
    page=re.compile('<li class="active"><a href=".*?">.*?</a></li><li><a href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,21,sonrakii,fann)
#23           
def Yeni2dizi(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "orta-orta"},smartQuotesTo=None)
    panel = panel[0].findAll("div", {"class": "four-box"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
        thumbnail='http://www.ddizi1.com/'+thumbnail
        name=name.replace('&#8211','').replace('&','')
        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
    page=re.compile('class="active"><a href=".*?">.*?</a></li><li ><a href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,23,sonrakii,fann)
#26
def dizivideolinks2(url,name):
        urlList=''
        ok=True
        url=url+'/11'
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "dizi-parts"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('<a href="(.*?)">(.*?)</a></li>').findall(str(liste))
        for url,name in match2:
            url='http://www.ddizi1.com/'+url
            name=name.replace('\xe0\xb8\xa3\xe0\xb8\x87','c')
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,22,fann,fann)       
          
#5
def Sinema1():
    urlY="http://www.dijifem.com/"
    xbmctools.addDir('[COLOR yellow]Arama/Search[/COLOR]',urlY,38,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR gold]** Yerli Filmler ** [/COLOR]','http://www.dijifem.com/category/turk-filmleri',67,yeniek,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',urlY,67,yeniek,fann)
    link=get_url(urlY)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="http://www.dijifem.com/category/(.*?)" title=".*?">(.*?)</a>').findall(link)
    for url,name in match:
        url='http://www.dijifem.com/category/'+url
        xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR orange]'+name+'[/COLOR]',url,67,"",fann)
#38
def Aramasinema1():
    sinema="http://www.dijifem.com/"
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+'/?s='+query)
        sinemaRecent12(url)
#67
def sinemaRecent12(url):
    urla=url
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "filmtabLo-resim koseoval"},smartQuotesTo=None)
    liste=BeautifulSoup(str(panel))
    for i in range (len(panel)):
        url=panel[i].find('a')['href']
        thumbnail=panel[i].find('img')['src']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        name=name.replace('&#8211;','&').replace('&#8217;','')
        xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,200,thumbnail,thumbnail)
    page=re.compile('<span class=\'page-numbers current\'>.*?</span>\n<a class=\'page-numbers\' href=\'(.*?)\'>(.*?)</a>').findall(link)
    for url1,name in page:
        url1=url1.replace('" data-wpel-link="internal','')
        xbmctools.addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url1,67,sonrakii,fann)
#200
def ayyris(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel=soup.find("ul", {"class": "partLarisiraLa"})
    liste=BeautifulSoup(str(panel))
    name="Secenek - 1"
    url=url
    xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,29,"","")
    match=re.compile('<a href="(.*?)">(.*?)</a>').findall(str(liste))
    for url,name in match:
        url=url.replace('" data-wpel-link="internal','')
        xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,29,"","")
#40
def ayrisdirma1(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("ul", {"class": "tab-baslik dropit"})
    match2=re.compile('</span>\n\t\t\t\t\t\n\t\t\t\t\t(.*?)<span id="g(.*?)"').findall(str(panel))
    for name,pid in match2:
        if "ragman" in name:
            pass
        else:
            Baglanvideo(url,name,pid)
#6
def Sinema2():
    url='http://www.yerlifilmiizle.net/'
    xbmctools.addDir('[COLOR yellow]Arama/Search[/COLOR]',url,44,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',url,43,yeniek,fann)
    link=get_url(url)
    match=re.compile('<a href="(.*?)" class="btn btn-outline term-button category"><i class=\'icon icon-hash\'></i><strong>(.*?)</strong> Fimleri</a>').findall(link)
    for url,name in match:
            xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR orange]'+name+'[/COLOR]',url,43,"",fann)
#44
def Search2():
    sinema="http://www.yerlifilmiizle.net/?s="
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+query)
        Yenisinema2(url)                                                  
#43
def Yenisinema2(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"calss": "col1 pull-left"},smartQuotesTo=None)
        panel = soup.findAll("li", {"class": "yerlifilmlist film-filmleri"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                name=name.replace('&#8211;',' - ').replace('&#8217;',' ').replace('&#038;',' ')
                xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,45,thumbnail,thumbnail)
        pages=re.compile('page-numbers current\'>.*?</span>\n<a class=\'page-numbers\' href=\'(.*?)\'>(.*?)</a>').findall(link)
        for url,name in pages:
            xbmctools.addDir('[COLOR blue]>> Sayfa - [/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,43,sonrakii,fann)

#45
def ayrisdirma2(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel=soup.find("ul", {"name": "part-system"})
    liste=BeautifulSoup(str(panel))
    match=re.compile('<a href="(.*?)"> <i class="fa fa-film"></i>\n (.*?)</a>').findall(str(liste))#src="http://www.ok.ru/videoembed/352586500751"
    for url1,name in match:
        xbmctools.addDir('[COLOR lightyellow]'+name+'[/COLOR]',url1,68,'','')
#68
def framee(name,url):
    link=get_url(url)
    pages=re.compile('<iframe src="(.*?)"').findall(link)
    for url in pages:
        magix_player(name,url)
    pagesa=re.compile('src="(.*?)" frameborder').findall(link)
    for url in pagesa:
        magix_player(name,url)  
#7
def Sinema3():
    sinema='http://www.bicaps.net'
    xbmctools.addDir('[COLOR yellow]>>[/COLOR] [COLOR red]>> - Arama/Search -<< [/COLOR]',sinema,48,aramaa,fann)
    sinema=sinema+"/?am_force_theme_layout=desktop"
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',sinema,47,yeniek,fann)
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
            xbmctools.addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,47,'','')
             
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
            xbmctools.addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,49,thumbnail,thumbnail)
        page=re.compile('current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
        for url,name in page:
                xbmctools.addDir('[COLOR blue]SAYFA >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',url,47,sonrakii,fann)
        page2=re.compile('</a><a href=\'(.*?)\' class=\'page smaller\'>.*?</a><span class=\'current\'>.*?</span>').findall(link)
        for url in page2:
                xbmctools.addDir('[COLOR red]Onceki Sayfa[/COLOR]',url,47,sonrakii,fann)
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
        xbmctools.addDir('[COLOR yellow]YENI ARAMA YAP[/COLOR]',url,48,"","")
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
           xbmctools.VIDEOLINKS1(name,url)
           return url
         else:
             pass


#1
def Belgesel():
    sinema ='http://www.belgun.tv/'
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Belgeseller[/COLOR]',sinema,50,yeniek,fann)
    link=get_url(sinema)
    match=re.compile('category menu-item-.*?"><a href="(.*?)">(.*?)</a>').findall(link)
    for url,name in match:
            xbmctools.addDir('[COLOR beige][COLOR red]>[/COLOR]'+name+'[/COLOR]',url,50,"","")
#50
def BRecent(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "solBlok"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "film"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('a')['title'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                xbmctools.addDir('[COLOR cyan]'+name+'[/COLOR]',url,51,thumbnail,thumbnail)
        page=re.compile('current\'>.*?</span><a class="page larger" href="(.*?)">.*?</a>').findall(link)
        for url in page:
                xbmctools.addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]',url,50,sonrakii,fann)
#51
def BELayrisdirma(url):
    xbmctools.addDir('[COLOR blue]Play >>[/COLOR]',url,41,"",fann)
    link=get_url(url)
    match=re.compile(' <a href="(.*?)"><span>(.*?)</span></a>').findall(link)
    for url,name in match:
        xbmctools.addDir('[COLOR blue]'+name+'[/COLOR]',url,41,"",fann)
 
def sembol_fix(x):
    try:
        x=x.replace('\x93','"').replace('\x92',"'").replace('\x94','"').replace('/',"-").replace('-',"").replace('_'," ").replace("'","'").replace('&#8211;','&').replace('&#8217;','`').replace('&#038;','`').replace('\x85','...').replace('\xb4',"'")
    except:
        pass
    return x[0].capitalize() + x[1:]
#16
def yetiskin():
        url='http://en.paradisehill.cc/porn/'
        xbmctools.addDir('[COLOR red]>>[/COLOR][COLOR yellow]Info[/COLOR][COLOR red] <<[/COLOR]',"BILGILENDIRME",56,"","")
        xbmctools.addDir('[COLOR blue]New Movie>>[/COLOR]',url,78,"","")
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
            xbmctools.addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,53,thumbnail,thumbnail)
#78
def RecentyetA(url):
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "row new-collect"})
        panel = panel[0].findAll("div", {"class": "col-md-3 col-sm-4 col-xs-6 bc-item"})
        for i in range (len (panel)):
            url=panel[i].find("a", {"class": "bci-title-link"})['href']
            name=panel[i].find("a", {"class": "bci-title-link"})['title'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            thumbnail=z+thumbnail
            url=z+url
            name=name.replace("Watch porno online","")
            xbmctools.addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,54,thumbnail,thumbnail)
        page=re.compile('<li class="page active"><a href=".*?">.*?</a></li>\n<li class="page"><a href="(.*?)">(.*?)</a></li>').findall(link)
        for url,name in page:
                url=z+url
                xbmctools.addDir('[COLOR blue]NEXT Page >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,78,sonrakii,fann)

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
            xbmctools.addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,54,thumbnail,thumbnail)
        page=re.compile('<li class="page active"><a href=".*?">.*?</a></li>\n<li class="page"><a href="(.*?)">(.*?)</a></li>').findall(link)
        for url,name in page:
                url=z+url
                xbmctools.addDir('[COLOR blue]NEXT Page >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,53,sonrakii,fann)
#54

def ayrisdirmayet(url):
    link=get_url(url)
    match1=re.compile("http:(.*?).mp4").findall(link)
    for url in match1:
        url=url.replace('\\',"")
        name="Watch Now"
        url='http:'+url+'.mp4'
        xbmctools.addDir('[COLOR red]Part '+name+'[/COLOR]',url,55,"","")           
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
    sinema='http://view4u.co/'
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR gold] ! Neue Filme ![/COLOR]',sinema,65,yeniek,fann)
    link=get_url(sinema)
    match=re.compile('<li><a href="/load(.*?)">(.*?)</a></li>').findall(link)
    for url,name in match:
        url='http://view4u.co/load'+url
        xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]'+name+'[/COLOR]',url,65,"",fann)                   
#65
def Yeni2alman1(url):
    link=get_url(url)
    match=re.compile('<div class="s_poster">\n <a href=".*?"><img src="(.*?)" alt=""></a>\n </div>\n <div class="s_info">\n <h2><a href="(.*?)">(.*?)</a>').findall(link)
    for thumbnail,url,name in match:
        thumbnail='http://view4u.co'+thumbnail
        url='http://view4u.co'+url
        xbmctools.addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,201,thumbnail,thumbnail)
    page=re.compile('<b class="swchItemA1"><span>.*?</span></b> <a class="swchItem1" href="(.*?)" onclick').findall(link)
    for url1 in page:
        url='http://view4u.co/'+url1
        xbmctools.addDir('[COLOR purple]>>'+'NeXt PaGe -> [/COLOR]',url,65,sonrakii,fann)
#201
def a6666(url):
    link=get_url(url)
    match=re.compile('src="http://view4u.co/anbieter01/(.*?).png" height=".*?" width=".*?"></font></b></legend><br><div class=".*?">\n <input onclick=".*?" value=".*?" type="b.*?">\n <div class=".*?" style=".*?">\n\n<a target=".*?" href="\n\n(.*?)\n\n">').findall(link)
    for name,url in match:
        xbmctools.addDir('[COLOR lightyellow]'+name+'[/COLOR]',url,99,'','')

#66
def Linkleralman1(url):
        link=get_url(url)
        match0=re.compile('<img style="margin:0;padding:0;border:0;" src="(.*?)"').findall(link)
        for thumbnail in match0:
            xbmctools.addDir("INFO - Picture",url,99,'http://www.szene-streams.com'+thumbnail,'http://www.szene-streams.com'+thumbnail)   
        match1=re.compile('http\:\/\/(.*?).eu\/(.*?).html').findall(link)
        for name,url in match1:
            url='http://streamcloud.eu/'+url+'.html'
            xbmctools.addDir('Play - > '+name,url,99,"","")

#11
def Canli1():
    urlF='http://www.fox.com.tr/canli-yayin'
    link=get_url(urlF)
    match=re.compile('src \: \\\'(.*?)\\\'').findall(link)
    for urlS in match:
        xbmctools.addLink("[COLOR beige] >> FOX TR[/COLOR]",urlS,"")
    urlO='http://www.onlinetvler.com/'
    link=get_url(urlO)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        xbmctools.addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO2='http://www.onlinetvler.com/?page=1'
    link=get_url(urlO2)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        xbmctools.addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'')
    urlO3='http://www.onlinetvler.com/?page=2'
    link=get_url(urlO3)
    match=re.compile('<a href="(.*?)"><img typeof="foaf:Image" src="(.*?)" width="190" height="120"').findall(link)
    for url,thumbnail in match:
        name=url.replace('tag','').replace('-',' ').replace('/','').replace('canli','').replace('izle','').replace('yayin','')
        url='http://www.onlinetvler.com'+url
        xbmctools.addDir('[COLOR orange]> - '+name+'[/COLOR]',url,107,thumbnail,'') 
#100
def ctv1(name,url):
    if "mcanlitv" in url:
        link=get_url(url)
        match=re.compile('mcanlitv.flexmmp(.*?)" frameborder=').findall(link)
        for url in match:
            url='http://mcanlitv.flexmmp'+url
            link=get_url(url)
            match=re.compile('hls: \'(.*?)\'\n').findall(link)
            for url in match:
                url=url+tk
                yenical44(name,url)
    else:
        
        try:
            req = urllib2.Request(url)
            req.add_header("User-Agent","Dalvik/1.6.0 (Linux; U; Android 4.2.2; A850 Build/JDQ39) Configuration/CLDC-1.1; Opera Mini/att/4.2.")
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            match = re.compile('file:"(.*?)"').findall(link)
            for url in match:
                if url:
                    url=url.replace('//yayin','http://yayin')
                    url=url+tk
                    xbmcPlayer.play(url)
                xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            match3 = re.compile('file : "(.*?)"').findall(link)
            for url in match3:
                if url:
                    url=url+tk
                    xbmcPlayer.play(url)
                xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            match1= re.compile("file: \'http(.*?)m3u8\.'").findall(link)
            for url in match1:
                if url:
                    url='http'+url+'m3u8'+tk
                    xbmcPlayer.play(url)
                xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            match2= re.compile('filexxx= "(.*?)"').findall(link)
            for url in match2:
                if url:
                    url=url+tk
                    xbmcPlayer.play(url)
                xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        except:
            showMessage('[COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]','[COLOR red]Iyi Seyirler Diler!!![/COLOR]')
            xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png') 
#12
def Canli2():
    url1='http://www.canlitvlive.co/izle/star-tv-izle.html'
    req = urllib2.Request(url1)
    req.add_header("User-Agent","Dalvik/1.6.0 (Linux; U; Android 4.2.2; A850 Build/JDQ39) Configuration/CLDC-1.1; Opera Mini/att/4.2.")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('<a href="http://mobile.canlitvlive.co/izle/(.*?)" title=".*?"><img class=".*?" data-src="(.*?)" width="100" height="75"').findall(link)
    for url,thumbnail in match:
        name=url
        name=name.replace('.html','').replace('-',' ').replace('canli','').replace('izle','')
        name=fix.decode_fix(name)
        url='http://mobile.canlitvlive.co/izle/'+url
        xbmctools.addDir('[COLOR gold]> - '+name+'[/COLOR]',url,100,thumbnail,'')
        #--
    urlM='http://www.mcanlitv.net/'
    link=get_url(urlM)
    match=re.compile('src="(.*?)" class=".*? alt="" /></a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t<div class="post-link">\r\n\t\t\t\t<a href="(.*?)">(.*?)</a>').findall(link)
    for thumbnail,url,name in match:
        xbmctools.addDir('[COLOR green]> - '+name+'[/COLOR]',url,100,thumbnail,'')
    #--
        
#101
def ctv2(url):
    url=url.replace('https','http')
    req = urllib2.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('src=https://streaming(.*?)\n').findall(link)
    for url in match:
        if url:
            url='https://streaming'+url+tk
            xbmctools.yenical4(name,url)

#18
def Canli3():
    url='txt.3vtc/b/moc.enisened//:ptth'[::-1]
    link=get_url(url)
    match=re.compile('<name>(.*?)\n<thumbnail>(.*?)\n<link>(.*?)\n').findall(link)       
    for name,Thumbnail,url in match:
        name=fix.decode_fix(name)
        if "Fox-tv" in name:
            url='http://www.fox.com.tr/canli-yayin'
            link=get_url(url)
            match=re.compile('src \: \\\'(.*?)\\\'').findall(link)
            for url in match:
                #del url[-1]
                xbmctools.addLink('[COLOR blue] >>[/COLOR]'+ '[COLOR beige]'+name+'[/COLOR]',url,'')
        else:
            xbmctools.addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR beige]'+name+'[/COLOR]',url,100,Thumbnail,Thumbnail)
               

#199
def yenical44(name,url):
        if "mail." in url:
            xbmctools.MailRu_Player(url)
        elif "vk."in url:
            magix_player(name,url)
        elif "ok." in url:
            xbmctools.ok_ru(url)
        elif "vid."in  url:
            magix_player(name,url)
        else:
            xbmcPlayer = xbmc.Player() 
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
            playList.clear() 
            xbmctools.addLink(name,url,'')
            listitem = xbmcgui.ListItem(name) 
            playList.add(url, listitem) 
            xbmcPlayer.play(playList)
 
  

#105
def radyo():
    url="http://dreamtr.club/aZambak/Rdy.txt"
    link=get_url(url)
    match=re.compile('<a href="(.*?)" target=".*?"><img alt="(.*?)" border=".*?" width=".*?" height=".*?" src="(.*?)" title=".*?"').findall(link)
    for url,name,thumbnail in match:
        xbmctools.addDir('[COLOR beige]>>'+name+'[/COLOR]',url,107,thumbnail,thumbnail)


        
def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )

#116
def Calcanli6(name,url):
    url=url.replace('//yayin','http://yayin')
    xbmcPlayer = xbmc.Player()
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playList.clear()
    xbmctools.addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
    listitem = xbmcgui.ListItem(name)
    playList.add(url, listitem)
    xbmcPlayer.play(playList)
    exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
    if exec_version < 14.0:
            xbmctools.playlist()
    else:
            xbmctools.playlist2()
#202   
def iptvpro(name,url):
    xbmctools.addDir('[COLOR beige]*** ONLY 80 € / Year ***[/COLOR]',"","","",fann)
    url='http://guek.ddns.net:1903/get.php?username=dreamtreklenti&password=760psDvBJI&type=m3u&output=ts'
    link=get_url(url)
    match=re.compile("#EXTINF:-1,(.*?)\r\nhttp://(.*?)\r").findall(link)
    for name,url in match:
        if "ilgilendirme" in name:
            pass
        else:
            name=name.replace('Bein','****').replace('Sky','***').replace('SKY','***').replace('TVBU','****').replace('BEIN','****')
            xbmctools.addDir('[COLOR gold]>'+name+' - Platinium User[/COLOR]',url,19,'','')
#99
def magix_player(name,url):
    if "www.dailymotion.com" in url:
        xbmctools.daily_sec(name,url)
##    elif "mail." in url:
##        xbmctools.MailRu_Player(url)
##    elif "ok." in url:
##        xbmctools.ok_ru(url)
    else:
        UrlResolverPlayer = url
        playList.clear()
        media = urlresolver.HostedMediaFile(UrlResolverPlayer)
        source = media
        if source:
                url = source.resolve()
                xbmctools.addLink(name,url,'')
                xbmctools.playlist_yap(playList,name,url)
                xbmcPlayer.play(playList)

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
elif mode==11: Canli1()
elif mode==12: Canli2()
elif mode==14: Arama()
elif mode==15: Kategoriler()
elif mode==16: yetiskin()
elif mode==18: Canli3()
elif mode==19: Yeni(url)
elif mode==20: dizivideolinks(url,name)
elif mode==21: Yeni2(url)
elif mode==22: xbmctools.frame(url)
elif mode==23: Yeni2dizi(url)
elif mode==24: xbmctools.dizividcal(url)
elif mode==25: Arama2()
elif mode==26: dizivideolinks2(url,name)
elif mode==27: Canli4()
elif mode==28: Yeni222(url)
elif mode==29: xbmctools.ayrisdirm1(url)
elif mode==30: yerlidizi3()
elif mode==31: Yeni3(url)
elif mode==38: Aramasinema1()
elif mode==40: ayrisdirma1(url)
elif mode==41: xbmctools.VIDEOLINKS1(name,url)
elif mode==42: xbmctools.yenical4(name,url)
elif mode==43: Yenisinema2(url)
elif mode==44: Search2()
elif mode==45: ayrisdirma2(url)
elif mode==46: Kategoriler2()
elif mode==47: Recent3(url)
elif mode==48: Aramasinema3()
elif mode==49: videolinks3(url,name)
elif mode==50: BRecent(url)
elif mode==51: BELayrisdirma(url)
elif mode==53: Recentyet(url)
elif mode==54: ayrisdirmayet(url)
elif mode==55: VideoLinksyet(name,url)
elif mode==56: INFOyet(url)
elif mode==59: VideoLinksyet2(name,url)
elif mode==60: INFOyet2(url)
elif mode==62: AlmanS()
elif mode==65: Yeni2alman1(url)
elif mode==66: Linkleralman1(url)
elif mode==67: sinemaRecent12(url)
elif mode==68: framee(name,url)
elif mode==76: genelarama()
elif mode==78: RecentyetA(url)
elif mode==89: yeniler3(url)
elif mode==90: ulkeleregoresinema5(url)
elif mode==91: de_get(name,url)
elif mode==94: Recentsinema5(url)
elif mode==95: ayrisdirmasinema5(name,url)
elif mode==99: magix_player(name,url)
elif mode==100: ctv1(name,url)
elif mode==101: ctv2(url)
elif mode==105: radyo()
elif mode==107: xbmctools.radyocal(url)
elif mode==5000: calinma(url)
elif mode==116: Calcanli6(name,url)
elif mode==140: Diziara()
elif mode==199: yenical44(name,url)
elif mode==200: ayyris(url)
elif mode==201: a6666(url)
elif mode==202: iptvpro(name,url)
elif mode==2000: __settings__.openSettings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
