#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
from bs4 import BeautifulSoup as BS4
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
    url = 'lmx.maerd/golegnahc/ten.nyazidamet.enisened//:ptth'[::-1]
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
         xbmctools.addDir('[COLOR grey]ALMAN Sinema[/COLOR]',"Alman()",62,'http://dreamtr.club/resimler/almanlar.png',fann)
         xbmctools.addDir('[COLOR grey]DREAM AYARLAR[/COLOR]',"Ayarlar()",2000,'http://dreamtr.club/resimler/ayarlar.png',fann)
         if gizlilik == "false" or gizlilik2 != gizlilik3 or gizlilik4 == "false":
             pass
         else:
             xbmctools.addDir('[COLOR red]+18[/COLOR]',"yetiskin()",16,'http://dreamtr.club/resimler/adult1.png',fann)
         xbmc.executebuiltin('Container.SetViewMode(500)')
url = 'txt.2maerd/golegnahc/ten.nyazidamet.enisened//:ptth'[::-1]
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
        xbmctools.addDir('[COLOR gold]! EvrenselFilm * New * ![/COLOR]',"Sinema1()",5,'http://dreamtr.club/resimler/Sinema1.png',fann)
        xbmctools.addDir('[COLOR pink]! Yerlifilmiizle.Org * New 2018 * ![/COLOR]',"Sinema2()",6,'http://dreamtr.club/resimler/Sinema2.png',fann)
        xbmc.executebuiltin('Container.SetViewMode(500)')
#3
def Dizi():
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR gold]'+'1-> Site - Canlihddiziler'+'[/COLOR]',url,1789,'http://dreamtr.club/resimler/Dizi1.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR gold]'+'2-> Site - Canlidizihd6'+'[/COLOR]',url,1788,'http://dreamtr.club/resimler/Dizi2.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'3-> Site - Ddizi'+'[/COLOR]',url,1899,'http://dreamtr.club/resimler/Dizi3.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'4-> Site - Dizihd3'+'[/COLOR]',url,1898,'http://dreamtr.club/resimler/Dizi4.png',fann)
    xbmctools.addDir('[COLOR orange]>>>[/COLOR] [COLOR beige]KANAL D Dizileri[/COLOR]',url,13,'https://vignette.wikia.nocookie.net/logopedia/images/a/a8/Kanal_D_Logo_%281994-2011%29.png',fann)
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Hint Dizileri Kanal 7[/COLOR]',"http://www.izle7.com/kanal7/hint-dizileri",28,'http://www.canlimobeseizle.com/wp-content/uploads/kanal7hd.png',fann)
    xbmc.executebuiltin('Container.SetViewMode(500)')
#4
def canliyayin():
        xbmctools.addDir('[COLOR pink]New* 2018 / Canli Tv 1*[/COLOR]',"Canli1()",11,'http://dreamtr.club/resimler/Canlitv1.png',fann)
        xbmctools.addDir('[COLOR pink]New* 2018 / Canli Tv 2*[/COLOR]',"Canli2()",12,'http://dreamtr.club/resimler/Canlitv2.png',fann)
        xbmctools.addDir('[COLOR yellow]New* 2018 / Canli Tv 3*[/COLOR]',"Canli3()",18,'http://dreamtr.club/resimler/Canlitv3.png',fann)
        xbmctools.addDir('[COLOR orange]* Canli Tv 4 * New *[/COLOR]',"Canli4()",27,'http://dreamtr.club/resimler/Canlitv4.png',fann)
        xbmc.executebuiltin('Container.SetViewMode(500)')

#--#
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; SmartTV) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('&#215;',"x").replace('&#231;',"c").replace('&#8217;',"-").replace('&#39;',"'").replace('&#252;',"u").replace('&#199;',"C").replace('&#246;',"o").replace('&#039;',"'")
        response.close()
        return link
#8


#1789
def Ddizi11():    
    url='http://www.canlihddiziler.net/'
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,14,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,19,yeniek,fann)
    link=get_url(url)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)"').findall(link)
    for url in match:
        name=url.replace('http://www.canlihddiziler.net/sonbolum/','').replace('izle','')
        xbmctools.addDir('[COLOR beige]>'+name+'[/COLOR]',url,28,'','')
#1788
def Ddizi12():
    xbmctools.addDir('[COLOR pink]>>[/COLOR] [COLOR pink]New * Enson Eklenen Diziler * New [/COLOR]',"http://www.canlidizihd6.net/",19,yeniek,fann)
    url="http://www.canlidizihd6.net/"
    link=get_url(url)
    match1=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?">(.*?)</a> </li>').findall(link)
    for url,name in match1:
        if "eski-yeni" in url:
            pass
        else:
            
            if "show-programlar" in url:
                pass
            else:
                
                if ">Genel</a> " in url:
                    pass
                else:
                    xbmctools.addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,19,'','')
    
#13
def Kanalddizi():
    url= 'https://www.kanald.com.tr/diziler'
    link=get_url(url)
    soup = BS4(link, 'html5lib')
    panel = soup.findAll("div", attrs={"class": "kd-docs-news"},smartQuotesTo=None)
    panel = panel[0].findAll("div", attrs={"class": "col-sm-6"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        thumbnail=panel[i].find('img')['data-src'].encode('utf-8', 'ignore')
        thumbnail='http:'+thumbnail
        url='http://www.kanald.com.tr'+url+'/bolumler'
        xbmctools.addDir('[COLOR orange]>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,7,thumbnail,thumbnail)
#7            
def Kanalddiziicerik(url):
        link=get_url(url)
        soup = BS4(link, 'html5lib')
        panel = soup.findAll("div", attrs={"class": "kd-docs-section"},smartQuotesTo=None)
        panel = panel[0].findAll("div", attrs={"class": "col-sm-3 col-xs-6"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            url= 'http://www.kanald.com.tr'+url
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['data-src'].encode('utf-8', 'ignore')
            thumbnail='http:'+thumbnail
            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,17,thumbnail,thumbnail)
        page=re.compile('<li class="active"><a href=".*?">.*?</a></li><li class=""><a href="(.*?)">(.*?)</a></li>').findall(link)
        for Url,name in page:
            Url='https://www.kanald.com.tr/'+Url
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,7,sonrakii,fann)

#17
def Kanalddizivideo(url,name):
        link=get_url(url)
        match=re.compile('data.*?-id="(.*?)"').findall(link)
        url2='https://www.kanald.com.tr/actions/content/media/'+match[0]
        link2=get_url(url2)
        match2=re.compile('"ServiceUrl":"(.+?)","SecurePath":"(.+?)?key=.+?"').findall(link2)
        for url,code in match2:
            url=url+code+'key=93a08dbbdd93b00670860974d0f63a6d'
            xbmctools.yenical4(name,url+tk)
         
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
    urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
    name='>> Kanal D'
    xbmctools.addLink(name,urlD,'')
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
    url=url+'?wmsAuthSign='+cd
    xbmctools.yenical4(name,url)
#19
def Yeni(url):
    if "http://www.canlidizihd6.net/" in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "kutu-resim"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
        page=re.compile('class=\'current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
        for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,sonrakii,fann)
    
    else:  
        if "izle7" in url:
            urla=url
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"class": "videos"},smartQuotesTo=None)
            panel = panel[0].findAll("div", {"class": "col-md-3 col-sm-6"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                name=name.replace('B&ouml;l&uuml;m','Bolum').replace('K&ouml;rd&uuml;\xc4\x9f&uuml;m','Kordugum')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,68,thumbnail,thumbnail)
            
            page=re.compile('<li class=" active">\n                                    <a href=".*?" title=".*?">.*?</a>\n                                </li>\n                                                            <li class="">\n                                    <a href="(.*?)" title=".*?">(.*?)</a>').findall(link)
            for Url,name in page:
                Url=urla+Url
                xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,sonrakii,fann)
        else:
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"class": "fix-film_item fix_home clearfix list_items"},smartQuotesTo=None)
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
    if "izle7.com" in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "videos"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "col-md-3 col-sm-6"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            url='http://www.izle7.com'+url
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            name=name.replace('B&ouml;l&uuml;m','Bolum').replace('K&ouml;rd&uuml;\xc4\x9f&uuml;m','Kordugum')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,19,thumbnail,thumbnail)
    else:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "fix-film-v2_item fix_category clearfix list_items"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "movie-poster"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
        page=re.compile('<span class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
        for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,28,sonrakii,fann)
#20
def dizivideolinks(url,name):
    if "izle7" in url:
        link=get_url(url)
        match=re.compile('<link rel="canonical" href="http://www.izle7.com/kanal7/izle-(.*?)-.*?">').findall(link)
        for url in match:
            url='http://www.izle7.com/embed-'+url
            xbmctools.addDir('[COLOR beige]>>[/COLOR]'+'[COLOR gold]'+'Play'+'[/COLOR]',url,68,'','')
    xbmctools.addDir('[COLOR beige]>>[/COLOR]'+'[COLOR gold]'+'1 . Secenek '+'[/COLOR]',url,22,fann,fann)
    if "http://www.canlihddiziler.net/" in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "keremiya_part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('a href="(.*?)"><span>(.*?)</span></a>').findall(str(liste))
        for url,name2 in match2:
            
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name2+'[/COLOR]',url,22,fann,fann)  
    try:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('<a href="(.*?)"><span>(.*?)</span>').findall(str(liste))
        for url,name2 in match2:
            name2=name2.replace('Par\xc3\xa7a','Secenek')
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name2+'[/COLOR]',url,22,fann,fann)            
    
    except:
        pass

#9

#1898
def Dizi288():
    url='http://www.dizihd3.com/'
    xbmctools.addDir('[COLOR red]>> [/COLOR] [COLOR orange]Dizi ARA / Search[/COLOR]',url,255,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,yeniek,fann)
    url='http://www.dizihd3.com/'
    link=get_url(url)
    match1=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)" >(.*?)</a>\n</li>').findall(link)
    for url,name in match1:
        if "eski-diziler" in url:
            pass
        else:
            
            if "yabanci-diziler" in url:
                pass
            else:
                
                if "tv-showlari" in url:
                    pass
                else:
                    xbmctools.addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,21,'','')

#1899
def ddizi2():
    url='http://www.ddizim.com/'
    xbmctools.addDir('[COLOR red]>>>>>>>[/COLOR] [COLOR beige]Dizi Ara / Search[/COLOR]',url,25,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,yeniek,fann)
    url1='http://www.ddizim.com/'
    link=get_url(url1)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "blok-liste"},smartQuotesTo=None)
    match1=re.compile('<a href="http://www.ddizim.com/diziler\/(.*?)\/(.*?)\-son-bolum-izle"').findall(str(panel))
    for url,name in match1:
        url='http://www.ddizi1.com/diziler/'+url+"/"+name+'-son-bolum-izle'
        name=fix.decode_fix(name)
        xbmctools.addDir('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,23,'','')
#25
def Arama2():
    dizi2='http://www.ddizim.com'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (dizi2+'/?s='+query)
        Yeni2(url)
#255
def Arama22():
    dizi2='http://www.dizihd3.com'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (dizi2+'/?s='+query)
        Yeni2(url)

#21
def Yeni2(url):
    if "www.ddizim.com" in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "orta-alt"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "dizi-box"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('ascii', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            thumbnail='http://www.ddizi1.com/'+thumbnail
            name=name.replace('&#8211','').replace('&','')
            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
        page=re.compile('class="active"><a href=".*?">.*?</a></li><li ><a href="(.*?)">(.*?)</a>').findall(link)
        for Url,name in page:
                xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,21,sonrakii,fann)
    else:
        if "dizihd3" in url:
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"class": "orta-ici"},smartQuotesTo=None)
            panel = panel[0].findAll("div", {"class": "kutu"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                name=name.replace('&#8211','').replace('&','')
                xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
            page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
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
    if "ddizim" in url:
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
    else:
        if "dizihd3" in url:
            urlList=''
            ok=True
            url=url
            name1='1.Secenek'
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name1+'[/COLOR]',url,22,fann,fann) 
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"id": "part"})
            liste=BeautifulSoup(str(panel))
            match2=re.compile('<a href="(.*?)"><span>(.*?)</span>').findall(str(liste))
            for url,name in match2:
                name=name.replace('Par\xc3\xa7a','Secenek')
                xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,22,fann,fann)       

            
          
#5
def Sinema1():
    urlY="http://evrenselfilmlerim.net/"
    xbmctools.addDir('[COLOR pink]# Film Ara / Search NEW #[/COLOR]',urlY,38,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',urlY,203,yeniek,fann)
    link=get_url(urlY)
    soup = BeautifulSoup(link)
    panel = soup.findAll("ul", {"class": "children"})
    liste=BeautifulSoup(str(panel))
    match2=re.compile('<li class="cat-item cat-item-.*?"><a href="http://evrenselfilmlerim.net/kategori/turler/(.*?)">(.*?)</a>').findall(str(liste))
    for url,name in match2:
        xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',"http://evrenselfilmlerim.net/kategori/turler/"+url,203,'','')  
#38
def Aramasinema1():#
    sinema="http://evrenselfilmlerim.net"
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+'/?s='+query)
        sinema1recent(url)
#67
##def sinemaRecent12(url):
##    link=get_url(url)
##    soup = BeautifulSoup(link)
##    panel = soup.findAll("article", {"class": "films"},smartQuotesTo=None)
##    panel = soup.findAll("div", {"class": "m-box"})
##    for i in range (len (panel)):
##        url=panel[i].find('a')['href']
##        thumbnail=panel[i].find('img')['src']
##        name=panel[i].find('img')['title'].encode('utf-8', 'ignore')
##        name=name.replace('&#8211;','&').replace('&#8217;','')
##        xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,200,thumbnail,thumbnail)
##    page=re.compile('current\'>.*?</span><a href=\'(.*?)\' class=\'inactive\' >(.*?)</a>').findall(link)
##    for url1,name in page:
##        xbmctools.addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url1,67,sonrakii,fann)
#203       
def sinema1recent(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("article", {"class": "fix-film-v2_item fix_home clearfix list_items"},smartQuotesTo=None)
    panel = soup.findAll("div", {"class": "movie-poster"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        thumbnail=panel[i].find('img')['src']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        name=name.replace('&#8211;','&').replace('&#8217;','').replace('izle','')
        if "evrenselfilm-sosyal" in url:
            pass
        else:
            xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,200,thumbnail,thumbnail)
    page=re.compile('class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
    for url1,name in page:
        xbmctools.addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url1,203,sonrakii,fann)
        
#200
def ayyris(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel=soup.find("div", {"class": "keremiya_part"})
    liste=BeautifulSoup(str(panel))
    name="Secenek - 1"
    url=url
    xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,68,"","")
    match=re.compile('<a href="(.*?)"><span>(.*?)</span>').findall(str(liste))
    for url,name in match:
        if "javascript" in url:
            pass
        else:
            if "vV" in name:
                pass
            else:
                xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,68,"","")
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
    url='https://www.yerlifilmiizle.org/'
    xbmctools.addDir('[COLOR yellow]Arama/Search[/COLOR]',url,44,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',url,43,yeniek,fann)
    link=get_url(url)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?">(.*?)</a>\n</li>').findall(link)
    for url,name in match:
            xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR orange]'+name+'[/COLOR]',url,43,"",fann)
#44
def Search2():
    sinema="http://www.yerlifilmiizle.org/?s="
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+query)
        Yenisinema2(url)                                                  
#43
def Yenisinema2(url):
    link=get_url(url)
    match1=re.compile('<img src="(.*?)" alt="(.*?)" /></a>\r\n</div>\r\n\r\n<div class="movie-details existing-details">\r\n<span class="movie-title">\r\n<a href="(.*?)"').findall(link)
    for thumbnail,name,url in match1:
        xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,45,thumbnail,thumbnail)
    pages=re.compile('<span class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
    for url,name in pages:
        xbmctools.addDir('[COLOR blue]>> Sayfa - [/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,43,sonrakii,fann)

#45
def ayrisdirma2(url):
    urla=url
    urla=urla.replace('-2/','/')
    xbmctools.addDir('[COLOR lightyellow]'+'Tek Parca'+'[/COLOR]',urla,68,'','')
    link=get_url(url)
    match=re.compile('<a href="(.*?)"><div class="part ">\r\n.*?<div class=".*?">(.*?)</div>').findall(link)
    for url1,name in match:
        xbmctools.addDir('[COLOR lightyellow]'+name+'[/COLOR]',url1,68,'','')
#68
def framee(name,url):
    if "izle7" in url:
        link=get_url(url)
        import re
        match=re.compile("var video = '(.*?)'").findall(link)
        for vid in match:
            vid=vid.replace('http://two.inxy.co','http://one.inxy.co/360p').replace('mb_files/','')
            vid=vid+"|referer=http://www.izle7.com/kanal7/izle-20967-ah-kalbim-24bolum.html"
            name='Izle7'
            xbmctools.addLink(name,vid,'')
    else:
        
        if "evrensel" in url:
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel=soup.find("div", {"class": "autosize-container"})
            liste=BeautifulSoup(str(panel))
            import re
            match1=re.compile('\="(.*?)"').findall(str(panel))
            for url in match1:
                if "javascript" in url:
                    pass
                else:
                    if "evrensel" in url:
                        pass
                    else:
                        if "vidmoly" in url:
                            url=url.replace('//','http://')
                            link=get_url(url)
                            match1=re.compile('var player \= new Clappr.Player\(\{\n  sources\: \["(.*?)"\,').findall(link)
                            for url in match1:
                                url=url.replace('//','http://')
                                xbmctools.addLink('[COLOR gold]>  '+'[COLOR beige]'+'Vidmoly'+'[/COLOR]'+'[/COLOR]',url,'')
                        else:
                            magix_player(name,url)
        else:
            if "yerlifilmiizle" in url:
                link=get_url(url)
                import re
                pages=re.compile('iframe src="(.*?)" width').findall(link)
                for url in pages:
                    magix_player(name,url)
                pagesa=re.compile('src="(.*?)" frameborder').findall(link)
                for url in pagesa:
                    magix_player(name,url) 


 
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
        name=name.replace("Watch porn online","")
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
        name=name.replace("Watch porn online","")
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
        url=url.replace('//','/').replace(':/','://')
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
    try:
        urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
        name='>> Kanal D'
        xbmctools.addLink(name,urlD,'')
        url='http://www.ocanlitv.net/'
        link=get_url(url)
        match=re.compile('<div class="item">\n\t<a href="(.*?)">\n\t<img src="(.*?)" alt="(.*?)" width="100" height="93">').findall(link)
        for url,thumbnail,name in match:
            if "Kanal D" in name:
                pass
            else:
                xbmctools.addDir(name,url,101,thumbnail,'')
    except:
        print"kanald yok"
    try:
        sitegit='https://www.kumanda.tv/show-tv-canli/'
        link=get_url(sitegit)
        soup = BeautifulSoup(link)
        panel=soup.findAll("ol", {"class": "tvlistesi"})
        match1=re.compile('<li><a href="(.*?)" title=".*?">(.*?)</a></li>').findall(str(panel))
        for url,name in match1:
            xbmctools.addDir('[COLOR pink] >>'+name+'[/COLOR]',url,101,"",'')
    except:
        print"kesintisiz yok"
    try:
        
        url='https://canlitv.co/tum-kanallar'
        req = urllib2.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<li>\n<a href="(.*?)">\n<img src="(.*?)" alt=".*?" />\n<strong>(.*?)</strong>\n</a>\n</li>').findall(link)
        for url,thumbnail,name in match:
            a='https://canlitv.co/'
            url=a+url
            thumbnail=a+thumbnail
            xbmctools.addDir('[COLOR orange] >>'+name+'[/COLOR]',url,101,thumbnail,'')
    except:
        print"canli.co yok"
        

#100
def ctv1(name,url):#
    try:
        url=url
        link=get_url(url)
        match = re.compile('file:"(.*?)"').findall(link)
        for url in match:
            if url:
                url=url.replace('//yayin','http://yayin').replace('http:http://','http://')
                url=url
                yenical44(name,url)
                return canli3() 
        link=get_url(url)
        match3 = re.compile('file : "(.*?)"').findall(link)
        for url in match3:
            if url:
                url=url+tk
                xbmcPlayer.play(url)
            xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        link=get_url(url)
        match99 = re.compile("file: '(.*?)',type").findall(link)
        for url in match99:
            if url:
                url=url+tk
                xbmcPlayer.play(url)
            xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        link=get_url(url)
        match1= re.compile("file: \'http(.*?)m3u8\.'").findall(link)
        for url in match1:
            if url:
                url='http'+url+'m3u8'+tk
                xbmcPlayer.play(url)
            xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        link=get_url(url)
        match2= re.compile('filexxx= "(.*?)"').findall(link)
        for url in match2:
            if url:
                url=url+tk
                xbmcPlayer.play(url)
            xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
    except:
        pass
        showMessage('[COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]','[COLOR red]Iyi Seyirler Diler!!![/COLOR]')
        xbmctools.addDir('[COLOR red]RETURN List << [/COLOR]','',11,'http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
#12
def Canli2():
    sitegit='http://www.canlitvlive.io/tum-kanallar.html'
    link=get_url(sitegit)
    soup = BeautifulSoup(link)
    panel=soup.findAll("div", {"class": "tv-body"})
    match1=re.compile('<a href="(.*?)" title="(.*?)">').findall(str(panel))
    for url,name in match1:
        url=url.replace('/izle/','http://www.canlitvlive.io/izle/')
        name=fix.decode_fix(name)
        name=name.replace('Izle','')
        if "Canl" in name:
            pass
        elif "Tum" in name:
            pass
        elif "Alfabe" in name:
            pass
        elif "Kanal  D" in name:
            pass
        elif "CNN" in name:
            pass
        elif "Teve" in name:
            pass
        else:
            xbmctools.addDir('[COLOR pink]> - '+name+'[/COLOR]',url,100,'','')
            
        #--
##    urlM='http://www.mcanlitv.net/'
##    link=get_url(urlM)
##    match=re.compile('src="(.*?)" class=".*? alt="" /></a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t<div class="post-link">\r\n\t\t\t\t<a href="(.*?)">(.*?)</a>').findall(link)
##    for thumbnail,url,name in match:
##        name=name.replace('&#8211;','')
##        xbmctools.addDir('[COLOR orange]> - '+name+'[/COLOR]',url,101,thumbnail,'')
    #--
        
#101
def ctv2(url):
    name='Play'
    import requests as req
    if "https://www.kumanda.tv/" in url:
        import requests as req
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"https://www.kumanda.tv/",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        import re
        match=re.compile('src="(.*?)" frameborder').findall(resp.text)
        for url in match:
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"https://www.kumanda.tv/",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            import re
            match=re.compile("file: \'(.*?)\'").findall(resp.text)
            for url in match:
                xbmctools.yenical4(name,url+tk)
    else:
        
        if "canlitv.co/" in url:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"https://canlitv.co/",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            import re
            match=re.compile('src="(.*?)" frameborder').findall(resp.text)
            for url in match:
                url='https://canlitv.co/'+url
                headers = {
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
                "Accept":"*/*",
                "Accept-Language":"en-US,en;q=0.5",
                "Referer":"https://canlitv.co/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                match=re.compile("file: \'(.*?)\'").findall(resp.text)
                for url in match:
                    xbmctools.yenical4(name,url+tk)

        else:
            
            if "ecanlitvizle" in url:
                import requests as req
                import re
                headers = {
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
                "Accept":"*/*",
                "Accept-Language":"en-US,en;q=0.5",
                "Referer":"https://www.ecanlitvizle.live/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                import re
                match=re.compile("file: '(.*?)'").findall(resp.text)
                for url in match:
                    url=url+tk
                    yenical44(name,url)
            else:
                

                if "dinle" in url:
                    link=get_url(url)
                    match=re.compile("file: \'(.*?)\',type").findall(link)
                    for url in match:
                        url=url+tk
                        yenical44(name,url)
                else:
                    if "mcanlitv" in url:
                        import re
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
                        if "ocanli" in url:
                            link=get_url(url)
                            import re
                            match=re.compile("file: \'(.*?)\'").findall(link)
                            for url in match:
                                xbmctools.yenical4(name,url+tk)
                        else:
                            if ".plus" in url:
                                link=get_url(url)
                                import re
                                match=re.compile('src="(.*?)" frameborder=').findall(link)
                                for url1 in match:
                                    if url1:
                                        link=get_url(url1)
                                        match=re.compile("file: \'(.*?)\'").findall(link)
                                        for url in match:
                                            xbmctools.yenical4(name,url)
                            else:
                                import re
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
                                url=url.replace('https','http')
                                req = urllib2.Request(url)
                                req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36")
                                response = urllib2.urlopen(req)
                                link=response.read()
                                response.close()
                                match=re.compile("hls: '(.*?)'").findall(link)
                                for url in match:
                                    if url:
                                        url=url+tk
                                        xbmctools.yenical4(name,url)

#18
def Canli3():#
    urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
    name='>> Kanal D'
    xbmctools.addLink(name,urlD,'')
##    url='http://www.canlitvlive.site/tum-kanallar.html'
##    link=get_url(url)
##    match=re.compile('<a href="(.*?)" title=".*?"><div class="chn_lg"><img src="(.*?)" width="100" height="75" alt=".*?"><div><h2>(.*?)</h2></div></div>').findall(link)       
##    for url,Thumbnail,name in match:
##        Thumbnail='http:'+Thumbnail
##        url='httppppp://www.canlitvlive.site'+url
##        print url
##        name=fix.decode_fix(name)
##        xbmctools.addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR beige]'+name+'[/COLOR]',url,100,Thumbnail,Thumbnail)
    urla='https://www.ecanlitvizle.live/kanal-7-izle/'
    link=get_url(urla)
    match1=re.compile('<a href="https://www.ecanlitvizle.live/(.*?)/">(.*?)</a></li>').findall(link)      
    for url,name in match1:
        url='https://www.ecanlitvizle.live/embed.php?kanal='+url
        if "<i" in name:
            pass
        else:
            
            if "ullan" in name:
                pass
            else:
                
                if "leti" in name:
                    pass
                else:
                    xbmctools.addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR pink]'+name+'[/COLOR]',url,101,'','')

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

#99
def magix_player(name,url):
    if "www.dailymotion.com" in url:
        xbmctools.daily_sec(name,url)
    elif "hqq" in url:
        url=url.replace('&amp;autoplay=no','').replace('https://hqq.tv/player/embed_player.php?vid=','')
        vid=url
        xbmctools.resolve( vid)
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
elif mode==2: Sinema()
elif mode==3: Dizi()
elif mode==4: canliyayin()
elif mode==5: Sinema1()
elif mode==6: Sinema2()
elif mode==7: Kanalddiziicerik(url)
elif mode==11: Canli1()
elif mode==12: Canli2()
elif mode==13: Kanalddizi()
elif mode==14: Arama()
elif mode==15: Kategoriler()
elif mode==16: yetiskin()
elif mode==17: Kanalddizivideo(url,name)
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
elif mode==53: Recentyet(url)
elif mode==54: ayrisdirmayet(url)
elif mode==55: VideoLinksyet(name,url)
elif mode==56: INFOyet(url)
elif mode==59: VideoLinksyet2(name,url)
elif mode==60: INFOyet2(url)
elif mode==62: AlmanS()
elif mode==65: Yeni2alman1(url)
elif mode==66: Linkleralman1(url)
##elif mode==67: sinemaRecent12(url)
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
elif mode==203: sinema1recent(url)
elif mode==255: Arama22()
elif mode==1788: Ddizi12()
elif mode==1789: Ddizi11()
elif mode==1898: Dizi288()
elif mode==1899: ddizi2()
elif mode==2000: __settings__.openSettings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
