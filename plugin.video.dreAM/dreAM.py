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
    xbmctools.addDir('[COLOR pink]! HdFilmCehennemi * New 2019 * ![/COLOR]',"Sinema2()",6,'http://dreamtr.club/resimler/Sinema2.png',fann)
    xbmc.executebuiltin('Container.SetViewMode(500)')
#3
def Dizi():
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR pink]'+'1-> Site - Dizikolik.Org'+'[/COLOR]','https://www.dizikolik.org/bolumler',19,'http://dreamtr.club/resimler/Dizi1.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR gold]'+'2-> Site - Canlidizihd7'+'[/COLOR]',url,1788,'http://dreamtr.club/resimler/Dizi2.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'3-> Site - Ddizim'+'[/COLOR]',url,1899,'http://dreamtr.club/resimler/Dizi3.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'4-> Site - Dizihd4'+'[/COLOR]',url,1898,'http://dreamtr.club/resimler/Dizi4.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR pink]'+'1.1-> Site - HdDiziIzle.Org'+'[/COLOR]','https://www.hddiziizle.org/',19,'https://www.hddiziizle.org/wp-content/uploads/2018/08/hdd.png',fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR pink]'+'1.2-> Site - DiziizleOnline.Net'+'[/COLOR]','https://www.diziizleonline.net/',19,'https://i.pinimg.com/originals/b9/a8/e7/b9a8e745dc7c86519b6c14a90e991430.png',fann)
    xbmctools.addDir('[COLOR orange]>>>[/COLOR] [COLOR beige]KANAL D Dizileri[/COLOR]',url,13,'https://vignette.wikia.nocookie.net/logopedia/images/a/a8/Kanal_D_Logo_%281994-2011%29.png',fann)
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Hint Dizileri Kanal 7[/COLOR]',"https://www.izle7.com/kanal7/hint-dizileri",28,'http://www.canlimobeseizle.com/wp-content/uploads/kanal7hd.png',fann)
    xbmc.executebuiltin('Container.SetViewMode(500)')
#4
def canliyayin():
    xbmctools.addDir('[COLOR pink]New* 2019 / Canli Tv 1*[/COLOR]',"Canli1()",11,'http://dreamtr.club/resimler/Canlitv1.png',fann)
    xbmctools.addDir('[COLOR pink]New* 2019 / Canli Tv 2*[/COLOR]',"Canli2()",12,'http://dreamtr.club/resimler/Canlitv2.png',fann)
    xbmctools.addDir('[COLOR yellow]New* 2019 / Canli Tv 3*[/COLOR]',"Canli3()",18,'http://dreamtr.club/resimler/Canlitv3.png',fann)
    xbmctools.addDir('[COLOR orange]# 2019 year * Canli Tv 4 * New *[/COLOR]',"Canli4()",27,'http://dreamtr.club/resimler/Canlitv4.png',fann)
    xbmctools.addDir('[COLOR yellow]# New * CanliTv.App 1.1* New *[/COLOR]',"Canli1b()",1198,'https://www.canlitv.app/images/logo.png',fann)
    xbmctools.addDir('[COLOR yellow]# New * CanliTv.Cafe 1.2 * New *[/COLOR]',"Canli1a()",1199,'https://www.canlitv.cafe/wp-content/uploads/2017/05/logo-1.png',fann)
    xbmctools.addDir('[COLOR yellow]# New * Web.CanliTvlivE.io 1.3 * New *[/COLOR]',"Canli1c()",1197,'https://pbs.twimg.com/profile_images/525770668541886464/OBCEWb5b.png',fann)
    xbmctools.addDir('[COLOR yellow]# New * Kesintisiz.TV 1.4 * New *[/COLOR]',"Canli1d()",1196,'https://www.kesintisiztv.com/images/kesintisiztv.png',fann)
    xbmctools.addDir('[COLOR yellow]# New * EcanliTVizle.Live 1.5 * New *[/COLOR]',"Canli1e()",1195,'https://www.ecanlitvizle.live/images/logo.png',fann)
    xbmc.executebuiltin('Container.SetViewMode(500)')

#--#
def get_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')
    response = urllib2.urlopen(req)
    link=response.read()
    link=link.replace('&#215;',"x").replace('&#231;',"c").replace('&#8217;',"-").replace('&#39;',"'").replace('&#252;',"u").replace('&#199;',"C").replace('&#246;',"o").replace('&#039;',"'")
    response.close()
    return link
#8
def Dizi1():
    url='http://www.canlihddiziler.net/'
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Arama/Search[/COLOR]',url,14,aramaa,fann)
    xbmctools.addDir('[COLOR orange]>>>[/COLOR] [COLOR beige]KANAL D Dizileri[/COLOR]',url,13,yeniek,fann)
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Hint Dizileri Kanal 7[/COLOR]',"http://www.izle7.com/kanal7/hint-dizileri",28,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,19,yeniek,fann)
    xbmctools.addDir('[COLOR pink]>>[/COLOR] [COLOR pink]New * Enson Eklenen Diziler * New [/COLOR]',"http://www.canlidizihd7.com/",19,yeniek,fann)
    
    link=get_url(url)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)"').findall(link)
    for url in match:
        name=url.replace('http://www.canlihddiziler.net/sonbolum/','').replace('izle','')
        xbmctools.addDir('[COLOR beige]>'+name+'[/COLOR]',url,28,'','')
#13
def Kanalddizi():
    url= 'https://www.kanald.com.tr/diziler'
    link=get_url(url)
    match=re.compile('<a href="(.*?)" title=".*?">\n    <img src="(.*?)" alt="(.*?)" title=".*?" class="img-responsive" itemprop="" />').findall(link)
    for url,thumbnail,name in match:
        thumbnail='http:'+thumbnail
        url='http://www.kanald.com.tr'+url+'/bolumler'
        #name=name.encode('utf-8', 'ignore')
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
    try: 
        link=get_url(url)
        match=re.compile('data.*?-id="(.*?)"').findall(link)
        url2='https://www.kanald.com.tr/actions/content/media/'+match[0]
        link2=get_url(url2)
        match2=re.compile('"ServiceUrl":"(.+?)","SecurePath":"(.+?)?key=.+?"').findall(link2)
        for url,code in match2:
            url=url+code+'key=93a08dbbdd93b00670860974d0f63a6d'+tk
            xbmctools.yenical4(name,url)
    except:
        pass
    try:
        link=get_url(url)
        ply22rr=re.compile('src="https://tubevs(.*?)"').findall(link)
        for url in ply22rr:
            url='https://tubevs'+url
            org_url=url
            import requests as req
            import requests
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': org_url
            }
            data = {
                'MIME Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'hash': url.split('/')[-1],
                'r': org_url
            }
            s = requests.Session()
            req = requests.Request('POST', url+'?do=getVideo', data=data, headers=headers)
            prepped = s.prepare_request(req)
            prepped.headers = headers
            resp = s.send(prepped)
            if resp.text:
                match=re.compile('file"\:"(.*?)","label"\:"(.*?)","type"').findall(resp.text)
                for url,name in match:
                    url=url.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('"','')
                    xbmctools.addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',url,'')
    except:
        xbmctools.frame(url)
        #"cikis"

        
         
#14
def Arama():
    dizi1='http://www.canlihddizi.com/'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (dizi1+'/?s='+query)
        Yeni(url)

#1788
def Ddizi12():
    xbmctools.addDir('[COLOR pink]>>[/COLOR] [COLOR pink]New * Enson Eklenen Diziler * New [/COLOR]',"http://www.canlidizihd7.com/",19,yeniek,fann)
    url="http://www.canlidizihd7.com/"
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
#27
def Canli4():
    urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
    name='Kanal D'
    xbmctools.addLink('[COLOR beige][COLOR orange]>>[/COLOR]  '+name+'[/COLOR]',urlD,'')
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
    import requests as requests
    url1='849=di?php.hctaw/moc.okinig.www//:ptth'[::-1]
    link=get_url(url1)
    match=re.compile('source:".*?\?wmsAuthSign\=(.*?)"').findall(link)
    for cd in match:
         "hosgeldin"
    url=url+'?wmsAuthSign='+cd
    xbmctools.yenical4(name,url)
#19
def Yeni(url):
    if "http://www.canlidizihd7.com/" in url:
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
        if "dizikolik" in url:
            link=get_url(url)
            match1=re.compile('<a href="(.*?)" title=".*?" class="postifit">\n<img class="" src="(.*?)-50x50.jpg" width="50" height="50" alt="(.*?)" />').findall(link)
            for url,thumbnail,name in match1:
                xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail+'.jpg',thumbnail+'.jpg')
            page=re.compile('current\'>.*?</span></li><li><a href=\'(.*?)\' class=\'inactive\'>(.*?)</a></li>').findall(link)
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
                if "hddiziizle.org" in url:
                    urla=url
                    link=get_url(url)
                    soup = BeautifulSoup(link)
                    panel = soup.findAll("div", {"class": "fix-film_item fix_builder_recent clearfix list_items"},smartQuotesTo=None)
                    panel = panel[0].findAll("div", {"class": "movie-poster"})
                    for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                        name=name.replace('B&ouml;l&uuml;m','Bolum').replace('K&ouml;rd&uuml;\xc4\x9f&uuml;m','Kordugum')
                        thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
                    
                    page=re.compile('<a href=".*?page\/(.*?)\/" class="loadnavi noselect" data-paged=".*?" data-max="131">').findall(link)
                    for name in page:
                        Url='https://www.hddiziizle.org/page/'+name+'/'
                        xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,19,sonrakii,fann)
                else:
                    if "diziizleonline" in url:
                        urla=url
                        link=get_url(url)
                        soup = BeautifulSoup(link)
                        panel = soup.findAll("div", {"class": "fix-film-v2_item fix_home clearfix list_items"},smartQuotesTo=None)
                        panel = panel[0].findAll("div", {"class": "movie-poster"})
                        for i in range (len (panel)):
                            url=panel[i].find('a')['href']
                            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                            name=name.replace('B&ouml;l&uuml;m','Bolum').replace('K&ouml;rd&uuml;\xc4\x9f&uuml;m','Kordugum')
                            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                            xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,20,thumbnail,thumbnail)
                        
                        page=re.compile('<span class="current">.*?</span><a href="(.*?)" class="single_page" title=".*?">(.*?)</a>').findall(link)
                        for Url,name in page:
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
    if "canlihddiziler.net" in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "keremiya_part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('a href="(.*?)"><span>(.*?)</span></a>').findall(str(liste))
        for url,name2 in match2:
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name2+'[/COLOR]',url,22,fann,fann)
    if "dizikolik" in url:
        xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+"1."+name+'[/COLOR]',url,22,fann,fann)
        link=get_url(url)
        match=re.compile('<li class="btn btn-gray btn-noradius"><a href="(.*?)">(.*?)</a></li>').findall(link)
        for url,name in match:
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,22,fann,fann)
    if "hd7" in url:
        xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+"1. SeceneK"+'[/COLOR]',url,22,fann,fann)
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "part"})
        liste=BeautifulSoup(str(panel))
        match2=re.compile('<a href="(.*?)"><span>(.*?)</span>').findall(str(liste))
        for url,name2 in match2:
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name2+'[/COLOR]',url,22,fann,fann)
    if "hddiziizle.org" in url:
        xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+"1. SeceneK"+'[/COLOR]',url,22,fann,fann)
    if "diziizleonline.net" in url:
        xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+"1. SeCeneK"+'[/COLOR]',url,22,fann,fann)

#9
def Dizi2():
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'1-> Site - Ddizi'+'[/COLOR]',url,1899,fann,fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+'2-> Site - Dizihd3'+'[/COLOR]',url,1898,fann,fann)
#1898
def Dizi288():
    url='http://www.dizihd4.com/'
    xbmctools.addDir('[COLOR red]>> [/COLOR] [COLOR orange]Dizi ARA / Search[/COLOR]',url,255,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,yeniek,fann)
    url='http://www.dizihd4.com/'
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')
    response = urllib2.urlopen(req)
    link=response.read()
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
    #xbmctools.addDir('[COLOR red]>>>>>>>[/COLOR] [COLOR beige]Dizi Ara / Search[/COLOR]',url,25,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR yellow]Enson Eklenen Diziler [/COLOR]',url,21,yeniek,fann)
    url1='http://www.ddizim.com/'
    link=get_url(url1)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"class": "blok-liste"},smartQuotesTo=None)
    match1=re.compile('<a href="http://www.ddizim.com/diziler\/(.*?)\/(.*?)\-son-bolum-izle"').findall(str(panel))
    for url,name in match1:
        url='http://www.ddizim.com/diziler/'+url+"/"+name+'-son-bolum-izle'
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
    dizi2='http://www.dizihd3.org'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (dizi2+'/?s='+query)
        Yeni2(url)
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
        thumbnail='http://www.ddizim.com/'+thumbnail
        name=name.replace('&#8211','').replace('&','')
        xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
    page=re.compile('class="active"><a href=".*?">.*?</a></li><li ><a href="(.*?)">(.*?)</a>').findall(link)
    for Url,name in page:
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,23,sonrakii,fann)
#21
def Yeni2(url):
    if "ddizim" in url: 
        if "l.php?sayfa=" in url:
            link=get_url(url)
            match=re.compile('<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?" alt=".*?" /><span class="dizi-adi">(.*?)</span>').findall(link)
            for url,thumbnail,name in match:
                xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
            Url='http://www.ddizim.com/l.php?sayfa=3'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'3'+'[/COLOR]',Url,21,sonrakii,fann)
            Urla='http://www.ddizim.com/l.php?sayfa=4'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'4'+'[/COLOR]',Urla,21,sonrakii,fann)
            Urlb='http://www.ddizim.com/l.php?sayfa=5'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'5'+'[/COLOR]',Urlb,21,sonrakii,fann)
            Urlba='http://www.ddizim.com/l.php?sayfa=6'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'6'+'[/COLOR]',Urlba,21,sonrakii,fann)
            Urlb7='http://www.ddizim.com/l.php?sayfa=7'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'7'+'[/COLOR]',Urlb7,21,sonrakii,fann)
            Urlb8='http://www.ddizim.com/l.php?sayfa=8'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'8'+'[/COLOR]',Urlb8,21,sonrakii,fann)
            Urlb9='http://www.ddizim.com/l.php?sayfa=9'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'9'+'[/COLOR]',Urlb9,21,sonrakii,fann)
            Urlb10='http://www.ddizim.com/l.php?sayfa=10'
            xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+'10'+'[/COLOR]',Urlb10,21,sonrakii,fann)
        else:
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"id": "ortaicerik"},smartQuotesTo=None)
            panel = panel[0].findAll("div", {"class": "dizi-box"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('ascii', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                thumbnail='http://www.ddizim.com/'+thumbnail
                name=name.replace('&#8211','').replace('&','')
                xbmctools.addDir('[COLOR beige][COLOR blue]>[/COLOR]'+name+'[/COLOR]',url,26,thumbnail,thumbnail)
            page=re.compile('<li class="active"><a href="javascript.*?" rel=".*?">.*?</a></li>\r\n              <li ><a href="javascript.*?" rel=".*?">(.*?)</a></li>').findall(link)
            for name in page:
                Url='http://www.ddizim.com/l.php?sayfa='+name
                xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,21,sonrakii,fann)
            
    else:
        if "dizihd4" in url:
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
            page=re.compile('class=\'current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
            for Url,name in page:
                    xbmctools.addDir('[COLOR blue]Sayfa >>[/COLOR]'+'[COLOR red]'+name+'[/COLOR]',Url,21,sonrakii,fann)

        
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
            url='http://www.ddizim.com/'+url
            name=name.replace('\xe0\xb8\xa3\xe0\xb8\x87','c')
            xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+name+'[/COLOR]',url,22,fann,fann)
    else:
        if "dizihd4" in url:
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
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR gold]BollyWood Filmleri [/COLOR]',"http://evrenselfilmlerim.net/kategori/turler/hindistan-filmleri",203,yeniek,fann)
    link=get_url(urlY)
    soup = BeautifulSoup(link)
    panel = soup.findAll("ul", {"class": "children"})
    liste=BeautifulSoup(str(panel))
    match2=re.compile('<li class="cat-item cat-item-.*?"><a href="http://evrenselfilmlerim.net/kategori/turler/(.*?)">(.*?)</a>').findall(str(liste))
    for url,name in match2:
        if "hindistan" in url:
            pass
        else:
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
def sinemaRecent12(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("article", {"class": "films"},smartQuotesTo=None)
    panel = soup.findAll("div", {"class": "m-box"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        thumbnail=panel[i].find('img')['src']
        name=panel[i].find('img')['title'].encode('utf-8', 'ignore')
        name=name.replace('&#8211;','&').replace('&#8217;','')
        xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,200,thumbnail,thumbnail)
    page=re.compile('current\'>.*?</span><a href=\'(.*?)\' class=\'inactive\' >(.*?)</a>').findall(link)
    for url1,name in page:
        xbmctools.addDir('[COLOR blue]Sonraki Sayfa >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url1,67,sonrakii,fann)
#203       
def sinema1recent(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("article", {"class": "fix-film-v2_item fix_home clearfix list_items"},smartQuotesTo=None)
    panel = soup.findAll("div", {"class": "movie-poster"})
    panela = soup.findAll("span", {"class": "center-icons"})
    for i in range (len (panel)):
        name2=panela[i].find('span')['title'].encode('utf-8', 'ignore')
        url=panel[i].find('a')['href']
        thumbnail=panel[i].find('img')['src']
        name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
        name=name.replace('&#8211;','&').replace('&#8217;','').replace('izle','')
        if "evrenselfilm-sosyal" in url:
            pass
        else:
            xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]'+'[COLOR gold]'+ name2+'[/COLOR]',url,200,thumbnail,thumbnail)
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
                if "Evren" in name:
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
    url='http://www.hdfilmcehennemi2.org/'
    xbmctools.addDir('[COLOR yellow]## Film Ara / Search ##[/COLOR]',url,44,aramaa,fann)
    xbmctools.addDir('[COLOR gold]>>[/COLOR] [COLOR beige]BollyWood Filmleri [/COLOR]',"http://www.hdfilmcehennemi2.org/tag/hint-filmleri",43,yeniek,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR pink]Yerli Filmler [/COLOR]',"http://www.hdfilmcehennemi2.org/kategori/yerli-filmler",43,yeniek,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]Yeni Eklenen Filmler [/COLOR]',url,43,yeniek,fann)
    link=get_url(url)
    match=re.compile('<li class="cat-item cat-item-.*?"><a href="http://www.hdfilmcehennemi2.org/kategori/(.*?)" >(.*?)</a>\n</li>').findall(link)
    for url,name in match:
        if "20" in name:
            pass
        else:
            xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR orange]'+name+'[/COLOR]','http://www.hdfilmcehennemi2.org/kategori/'+url,43,"",fann)
#44
def Search2():
    sinema="http://www.hdfilmcehennemi2.org/?arama="
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (sinema+query)
        Yenisinema2(url)                                                  
#43
def Yenisinema2(url):
    if "/tag"  in url:
        link=get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "tabpanel"},smartQuotesTo=None)
        panel = soup.findAll("div", {"class": "moviefilm"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            thumbnail=panel[i].find('img')['src']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            name=name.replace('&#8211;','&').replace('&#8217;','').replace('izle','')
            name=fix.decode_fix(name)
            xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,45,thumbnail,thumbnail)       
        pages=re.compile('current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
        for url,name in pages:
            xbmctools.addDir('[COLOR blue]>> Sayfa - [/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,43,sonrakii,fann)

    else:
        if "?arama"  in url:
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"class": "tabpanel"},smartQuotesTo=None)
            panel = soup.findAll("div", {"class": "moviefilm"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                thumbnail=panel[i].find('img')['src']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                name=name.replace('&#8211;','&').replace('&#8217;','').replace('izle','')
                name=fix.decode_fix(name)
                xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]',url,45,thumbnail,thumbnail)       
            pages=re.compile('current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
            for url,name in pages:
                xbmctools.addDir('[COLOR blue]>> Sayfa - [/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,43,sonrakii,fann)
        else:
            
            link=get_url(url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"class": "tabpanel"},smartQuotesTo=None)
            panel = soup.findAll("div", {"class": "moviefilm"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name2=panel[i].find('span')['class'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                name=name.replace('&#8211;','&').replace('&#8217;','').replace('izle','')
                name=fix.decode_fix(name)
                xbmctools.addDir('[COLOR beige][COLOR red]>>[/COLOR]'+name+'[/COLOR]'+'[COLOR gold]'+ name2+'[/COLOR]',url,45,thumbnail,thumbnail)       
            pages=re.compile('current\'>.*?</span><a class="page larger" title=".*?" href="(.*?)">(.*?)</a>').findall(link)
            for url,name in pages:
                xbmctools.addDir('[COLOR blue]>> Sayfa - [/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,43,sonrakii,fann)


#45
def ayrisdirma2(url):
    link=get_url(url+'/')
    xbmctools.addDir('[COLOR gold]>>[/COLOR]'+'[COLOR beige]'+"1.Player"+'[/COLOR]',url,68,'','') 
    match=re.compile('href="(.*?)"><span>(.*?)</span>').findall(link)
    for url1,name in match:
        xbmctools.addDir('[COLOR lightyellow]'+name+'[/COLOR]',url1,68,'','')
#68
def framee(name,url):
    if "hdfilmcehennemi" in url:
        import re
        link=get_url(url)
        match1q=re.compile('src="https://www.720p-izle.org/(.*?)"').findall(link)
        for url in match1q:
            url='https://www.720p-izle.org/'+url
            link=get_url(url)
            match=re.compile('<iframe src="(.*?)"').findall(link)
            for urla in match:
                if urla: 
                    url=urla
                    magix_player(name,url)
                else:
                    print " yok"

                            
    else:
        if "izle7" in url:
            link=get_url(url)
            import re
            match=re.compile("var video = '(.*?)'").findall(link)
            for vid in match:
                vid=vid.replace('https://two.inxy.co','https://one.inxy.co/360p').replace('mb_files/','')
                vid=vid#+"|referer=https://www.izle7.com/kanal7/izle-29435-ikimizin-yerine-119-bolum-izle-4-ocak-2018.html"
                name='Izle7'
                xbmctools.addLink(name,vid+tk,'')
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
                                magix_player(name,url)
                            else:
                                magix_player(name,url)
            else:
                pass

def sembol_fix(x):
    try:
        x=x.replace('\x93','"').replace('\x92',"'").replace('\x94','"').replace('/',"-").replace('-',"").replace('_'," ").replace("'","'").replace('&#8211;','&').replace('&#8217;','`').replace('&#038;','`').replace('\x85','...').replace('\xb4',"'")
    except:
        pass
    return x[0].capitalize() + x[1:]
#16
def yetiskin():
    url1='http://lubetube.com/categories'
    xbmctools.addDir('[COLOR red]>>[/COLOR][COLOR yellow]Info[/COLOR][COLOR red] <<[/COLOR]',"BILGILENDIRME",56,"","")
    xbmctools.addDir('[COLOR blue]New Movie>>[/COLOR]',"http://lubetube.com/",53,"","")
    link=get_url(url1)
    match1=re.compile('</strong></span><a class="frame" href="(.*?)"><img src=".*?" alt="(.*?)" />').findall(link)
    for url,name in match1:
        xbmctools.addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,53,'','')
#78

#53
def Recentyet(url):
    link=get_url(url)
    soup = BeautifulSoup(link)
    panel = soup.findAll("div", {"id": "content"})
    panel = panel[0].findAll("span", {"class": "pic"})
    for i in range (len (panel)):
        url=panel[i].find('a')['href']
        thumbnail=panel[i].find('img')['src']
        name=panel[i].find('a')['title']
        xbmctools.addDir('[COLOR beige][COLOR blue]>>[/COLOR]'+name+'[/COLOR]',url,54,thumbnail,thumbnail)
    page=re.compile('<span class="onpage">.*?</span>  <a href="(.*?)">(.*?)</a>').findall(link)
    for url,name in page:
            url='http://lubetube.com'+url
            xbmctools.addDir('[COLOR blue]NEXT Page >>[/COLOR]'+ '[COLOR red]'+name+'[/COLOR]',url,53,sonrakii,fann)
#54

def ayrisdirmayet(url):
    link=get_url(url)
    match1=re.compile('id="video-high" href="(.*?)" data-conten').findall(link)
    for urla in match1:
        name="Watch Now"
        xbmctools.addLink(name,urla,'')
      
#55

#56
def INFOyet(url):
    try:
        yetiskin()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR beige]ViP Uyeler icindir[/COLOR],[COLOR yellow]Turkiyeden ve Bazi Ülkelerden izlenemeyebilir[/COLOR] ","[COLOR yellow]DNS Ayarlariyla girilebilir[/COLOR]")
    except:
        pass
#62
def AlmanS():
    sinema='https://filmpalast.to/movies/new'
    xbmctools.addDir('[COLOR red]>>>[/COLOR] [COLOR orange]Filme Suche/Search[/COLOR]',sinema,655,aramaa,fann)
    xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR gold] ! Neue Filme ![/COLOR]',sinema,65,yeniek,fann)
    link=get_url(sinema)
    match=re.compile('<li> <a href="https://filmpalast.to/search/genre/(.*?)">(.*?)</a></li>').findall(link)
    for url,name in match:
        url='https://filmpalast.to/search/genre/'+url
        xbmctools.addDir('[COLOR blue]>>[/COLOR] [COLOR lightblue]'+name+'[/COLOR]',url,65,"",fann)
#655
def Almanara():
    url='https://filmpalast.to/search/title/'
    keyboard = xbmc.Keyboard("", 'Search', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        url = (url+query)
        Yeni2alman1(url)
#65
def Yeni2alman1(url):
    link=get_url(url)
    match=re.compile('<a href="(.*?)" title=".*?"> <img width="236px" height="338px" src="(.*?)" class="cover-opacity" alt="(.*?)" /></a>\n</article>\n<article class="liste glowliste  rb">\n<cite>\n<h2 class="rb">').findall(link)
    for url,thumbnail,name in match:
        thumbnail='https://filmpalast.to'+thumbnail
        url='https:'+url
        name=name.replace('stream ',' ')
        xbmctools.addDir('[COLOR orange]>>[COLOR beige]'+name+'[/COLOR]',url,201,thumbnail,thumbnail)
    page=re.compile('active">.*?</a> <a class="pageing button-small rb" href=\'(.*?)\'>(.*?)</a>').findall(link)
    for url1,name in page:
        xbmctools.addDir('[COLOR purple]>>'+'NeXt PaGe -> [/COLOR]'+name,url1,65,sonrakii,fann)
#201
def a6666(url):
    link=get_url(url)
    match=re.compile('<p class="hostName">(.*?)</p></li>\n<li class=".*?">\n\n<a  class=".*?" target=".*?" href="(.*?)">').findall(link)
    for name,url in match:
        xbmctools.addDir('[COLOR lightyellow]'+name+'[/COLOR]',url,99,'','')
#1195
def Canli1e():
    url='https://www.ecanlitvizle.live/trt-1-izle/'
    link=get_url(url)
    match=re.compile('<li><a href="https://www.ecanlitvizle.live/(.*?)">(.*?)</a></li>').findall(link)
    for url,name in match:
        if ('category' in url) or ('kullanim' in url) or ('iletisim' in url) or ('sitene' in url) or ('Kanallar' in url):
            pass
        else:
            url='https://www.ecanlitvizle.live/'+url
            xbmctools.addDir('[COLOR pink][COLOR beige]>>[/COLOR]  '+name+'[/COLOR]',url,101,'',"")
#1196
def Canli1d():
    url='https://www.kesintisiztv.com/trt-1'
    link=get_url(url)
    match=re.compile('<li><a href="https://www.kesintisiztv.com/(.*?)" title=".*?">(.*?)</a></li>').findall(link)
    for url,name in match:
        if "kategori" in url:
            pass
        else:
            url='https://www.kesintisiztv.com/'+url
            xbmctools.addDir('[COLOR pink][COLOR beige]>>[/COLOR]  '+name+'[/COLOR]',url,101,'',"")
#1197
def Canli1c():
    url='http://web.canlitvlive.io/tv-tum-kanallar.html'
    link=get_url(url)
    match=re.compile('<a href="(.*?)" title=".*?"><div class="chn_lg"><img src="(.*?)" width="100" height="75" alt="(.*?)"><div>').findall(link)
    for url,thumbnail,name in match:
        if "radyo" in url:
            pass
        else:
            url='http://web.canlitvlive.io'+url
            xbmctools.addDir('[COLOR pink][COLOR beige]>>[/COLOR]  '+name+'[/COLOR]',url,101,thumbnail,"")
#1199
def Canli1a():
    url='https://www.canlitv.cafe/'
    link=get_url(url)
    match=re.compile('<div class="kanal"> <a href="(.*?)" title=".*?"> <strong>(.*?)</strong>').findall(link)
    for url,name in match:
        xbmctools.addDir('[COLOR pink][COLOR beige]>>[/COLOR]  '+name+'[/COLOR]',url,100,"","")
#1198
def Canli1b():
    url='https://www.canlitv.app/'
    link=get_url(url)
    match=re.compile('<a href="(.*?)" title=".*?">\n<div class="kanallarlogo"><img src="(.*?)" alt="(.*?)" width="192"').findall(link)
    for url,thumbnail,name in match:
        xbmctools.addDir('[COLOR gold][COLOR purple]>>[/COLOR]  '+name+'[/COLOR]',url,100,thumbnail,"")
#11
def Canli1():
    urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
    name='>> Kanal D'
    xbmctools.addLink(name,urlD,'')
    sitegit='http://www.canlitvfull.com/'
    link=get_url(sitegit)
    match1=re.compile('<div class="postthumb">\n\t\t\t\t\t\t\t<a href="http://www.canlitvfull.com/(.*?)"><img width="138" height="93" src="(.*?)" class').findall(link)
    for name,thumbnail in match1:
        url='http://www.canlitvfull.com/'+name
        xbmctools.addDir('[COLOR beige][COLOR purple]>>[/COLOR]  '+name+'[/COLOR]',url,101,thumbnail,"")
        

#100
def ctv1(name,url):#
    if "canlitv.app" in url:
        import requests as req
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"https://www.canlitv.app/",
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
            "Referer":"https://www.canlitv.app/",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            match=re.compile("file: '(.*?)'").findall(resp.text)
            for url in match:
                xbmctools.yenical4(name,url+tk)
    if "canlitv.cafe" in url:
        import requests as req
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"https://www.canlitv.cafe",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        import re
        match=re.compile('iframe src="(.*?)"').findall(resp.text)
        for url in match:
            url='https://www.canlitv.cafe'+url
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"https://www.canlitv.cafe/",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            match=re.compile("file: '(.*?)'").findall(resp.text)
            for url in match:
                xbmctools.yenical4(name,url+tk)
    else:
        url=url
        link=get_url(url)
        match = re.compile('file:"(.*?)"').findall(link)
        for url in match:
            if url:
                url=url.replace('//yayin','http://yayin').replace('http:http://','http://')
                url=url
                xbmcPlayer.play(url)
                return canli3() 
        link=get_url(url)   #file: "(.*?)"
        match3 = re.compile('file : "(.*?)"').findall(link)
        for url in match3:
            if url:
                xbmctools.yenical4(name,url+tk)
        link=get_url(url)
        match99 = re.compile("file: '(.*?)',type").findall(link)
        for url in match99:
            if url:
                xbmctools.yenical4(name,url+tk)
        link=get_url(url)
        match1= re.compile("file: \'http(.*?)m3u8\.'").findall(link)
        for url in match1:
            if url:
                url='http'+url+'m3u8'
                xbmctools.yenical4(name,url+tk)
        link=get_url(url)
        match2= re.compile('filexxx= "(.*?)"').findall(link)
        for url in match2:
            if url:
                xbmctools.yenical4(name,url+tk)
        link=get_url(url)
        match3a = re.compile('ile: "(.*?)"').findall(link)
        for url in match3a:
            if url:
                xbmctools.yenical4(name,url+tk)
    pass

#12
def Canli2():
    sitegit='http://www.livetvs.io/tum-kanallar.html'
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
            
#101
def ctv2(url):
    name='Play'
    import requests as req
    if "kesintisiztv" in url:
        try:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"https://www.kesintisiztv.com/",
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
                "Referer":"https://www.kesintisiztv.com/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                import re
                match=re.compile("file: \'(.*?)\'").findall(resp.text)
                for url in match:
                    xbmctools.yenical4(name,url+tk)
        except:
            pass
    if "ecanlitvizle" in url:
        try:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"https://www.ecanlitvizle.live/",
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
                "Referer":"https://www.ecanlitvizle.live/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                import re
                match=re.compile("file: \'(.*?)\'").findall(resp.text)
                for url in match:
                    xbmctools.yenical4(name,url+tk)
        except:
            pass
    if "canlitvfull" in url:
        try:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"http://www.canlitvfull.com/",
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
                "Referer":"http://www.canlitvfull.com/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                import re
                match=re.compile('source src="(.*?)"').findall(resp.text)
                for url in match:
                    xbmctools.yenical4(name,url+tk)
        except:
            pass
    if "canliyayin.im" in url:
        try:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"http://canliyayin.im",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            import re
            match=re.compile('src="//embedlive(.*?)"').findall(resp.text)
            for url in match:
                url='http://embedlive'+url
                headers = {
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
                "Accept":"*/*",
                "Accept-Language":"en-US,en;q=0.5",
                "Referer":"http://embedlive.flexmmp.com/",
                "Connection":"keep-alive"
                }
                resp = req.get(url, allow_redirects=True, headers=headers)
                import re
                match=re.compile("hls: '(.*?)'").findall(resp.text)
                for url in match:
                    url='http:'+url
                    xbmctools.yenical4(name,url+tk)
        except:
            pass
    if "web.canlitvlive.io" in url:
        try:
            import requests as req
            headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Referer":"http://web.canlitvlive.io/",
            "Connection":"keep-alive"
            }
            resp = req.get(url, allow_redirects=True, headers=headers)
            import re
            match=re.compile('file: "(.*?)"').findall(resp.text)
            for url in match:
               # url='http:'+url
                xbmctools.yenical4(name,url+tk)
        except:
            pass



    else:
        if "dinle" in url:
            link=get_url(url)
            match=re.compile("file: \'(.*?)\',type").findall(link)
            for url in match:
                url=url+tk
                yenical44(name,url)
        else:#
    
            if "ocanli" in url:
                link=get_url(url)
                import re
                match=re.compile("file: \'(.*?)\'").findall(link)
                for url in match:
                    yenical44(name,url+tk)

            if ".plus" in url:
                link=get_url(url)
                import re
                match=re.compile('src="(.*?)" frameborder=').findall(link)
                for url1 in match:
                    if url1:
                        link=get_url(url1)
                        match=re.compile("file: \'(.*?)\'").findall(link)
                        for url in match:
                            xbmctools.addLink(name,url,'')
             

#18
def Canli3():#
    urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'
    name='>> Kanal D'
    xbmctools.addLink(name,urlD,'')
    urla='http://canliyayin.im/'
    link=get_url(urla)
    match1=re.compile('<a href="(.*?)" title=".*?"><img src="(.*?)" alt=".*?" class=".*?" width="80" height="80"/>\n<span>(.*?)</span><').findall(link)      
    for url,thumbnail,name in match1:
        xbmctools.addDir('[COLOR blue] >>[/COLOR]'+ '[COLOR pink]'+name+'[/COLOR]',url,101,thumbnail,'')

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
    match=re.compile('<li><a href=\'(.*?)\'>(.*?)</a></li>').findall(link)
    for url,name in match:
        xbmctools.addDir('[COLOR beige]>>'+name+'[/COLOR]',url,107,'','')


        
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
    xbmctools.addDir('[COLOR beige]*** ONLY 100 € / Year ***[/COLOR]',"","","",fann)
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
    if "vidmol" in url:
        link=get_url(url)
        match=re.compile('mp4\|(.*?)\|sources\|').findall(link)        
        for b in match:
            if match:
                link=get_url(url)#https://user-content-hot-142.molyusercontentstage.me/xqx2osfolnokjiqbtfmcnisdxzftizef5aofciunixy2nngqbvc2q2pvh54a/v.mp4
                match1=re.compile('var spriteSheetUrl = "(.*?)i/.*?.jpg"').findall(link)
                for a in match1:
                    url=a+b+'/v.mp4'
                    url=url.replace('//','http://').replace('https:http://','https://').replace('01|100|','')
                    name='ViDmOlY'
                    xbmctools.yenical4(name,url)
    if "dailymotion" in url:
        urla=url
        urla=urla.replace('motion.com/embed/video/','')
        urla = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url='+urla
        addLink('Play-DM',urla,'')
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
elif mode==8: Dizi1()
elif mode==9: Dizi2()
elif mode==11: Canli1()
elif mode==1199: Canli1a()
elif mode==1198: Canli1b()
elif mode==1197: Canli1c()
elif mode==1196: Canli1d()
elif mode==1195: Canli1e()
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
##elif mode==55: VideoLinksyet(name,url)
elif mode==56: INFOyet(url)
elif mode==59: VideoLinksyet2(name,url)
elif mode==60: INFOyet2(url)
elif mode==62: AlmanS()
elif mode==65: Yeni2alman1(url)
##elif mode==66: Linkleralman1(url)
elif mode==67: sinemaRecent12(url)
elif mode==68: framee(name,url)
elif mode==76: genelarama()
##elif mode==78: RecentyetA(url)
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
elif mode==203: sinema1recent(url)
elif mode==255: Arama22()
elif mode==655: Almanara()
elif mode==1788: Ddizi12()
##elif mode==1789: Ddizi11()
elif mode==1898: Dizi288()
elif mode==1899: ddizi2()
elif mode==2000: __settings__.openSettings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
