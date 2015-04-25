# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="HARIKADIZI"
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
                        html = xbmctools1.harikadizi()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Yerli Diziler [/B][/COLOR]', "Yeni(url)",sinema+'/category/yerli-diziler',"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yabanci Yeni Eklenen Diziler  [/B][/COLOR]', "Yeni(url)",sinema+'/category/yabanci-diziler',"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yabanci Dizi Kategorileri [/B][/COLOR]', "YabanciKat()",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.harikadizi()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim>').findall(web)
                                                for url,name in tr:
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

def YabanciKat():
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.harikadizi()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<yabanci>(.*?)</yabanci><ad>(.*?)</ad>').findall(web)
                        for url,name in tr:
                                name=ifix.decode_fix(name)
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yabanci2(url)",url,'','')

        except Exception:
                buggalo.onExceptionRaised()

def Yabanci2(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match=re.compile('<a href="(.*?)" rel="bookmark" title="(.*?)"><div class="d_bolum"><div style="height:40px;width:40px;background-image').findall(link)
                for url,name in match:
                    if "facebook" in url:
                        pass
                    else:
                        xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR][COLOR beige][B]'+name+'[/B][/COLOR]',"partlar(url,name,thumbnail)",url,'')
        
        except Exception:
                buggalo.onExceptionRaised()                                                

def Yeni(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                soup = BeautifulSoup(link)
                panel = soup.findAll("div", {"class": "art-content"},smartQuotesTo=None)
                panel = panel[0].findAll("div", {"style": "float:left;"})
                for i in range (len (panel)):
                        url=panel[i].find('a')['href']
                        name=panel[i].find('a').text.encode('utf-8', 'ignore')
                        thumbnail=panel[i].find("div", {"class": "alignleft"})['style'].encode('utf-8', 'ignore')
                        thumbnail=replace_fix(thumbnail)
                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR blue]>[/COLOR]'+name+'[/B][/COLOR]',"partlar(url,name,thumbnail)",url,thumbnail,thumbnail)
                 ####---------------Sonraki sayfa-------------------------------########
                page=re.compile('<span class=\'current\'>.*?</span><a href=\'(.*?)\' class=\'page larger\'><div>(.*?)</div></a>').findall(link)
                for url,name in page:
                        xbmctools1.addDir(fileName,'[COLOR blue][B]Sayfa >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "Yeni(url)",url,"https://koditr.org/changelog/sonrakisayfa.png")
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()                
        
def partlar(url,name,thumbnail):
        buggalo.SUBMIT_URL = denemesite
        try:
                thumbnail=str(thumbnail)
                xbmctools1.addDir(fileName,'[COLOR cyan][B]'+name+'[/COLOR]', "VIDEOLINKS(name,url)",url,thumbnail)
                try:
                    link=xbmctools1.get_url(url)
                    soup = BeautifulSoup(link)
                    panel = soup.findAll("ul", {"class": "sgr-npt-summary"})
                    liste=BeautifulSoup(str(panel))
                    for li in liste.findAll('li'):
                        a=li.find('a')
                        url= a['href']
                        name2= li.text
                        name2=name2.encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR orange][B] >> [COLOR blue]'+str(name2)+'[COLOR orange] >> [/COLOR][COLOR lightblue]'+str(name)+'[/COLOR]',"partlar2(url,name)",url,'')
                except:
                        pass
               
                try:
                    link=xbmctools1.get_url(url)
                    soup = BeautifulSoup(link)
                    panel = soup.findAll("div", {"class": "art-PostContent"},smartQuotesTo=None)
                    panel = panel[0].findAll("div", {"class": "postTabs_divs"})
                    for i in range (len (panel)):
                        url=panel[i].find('iframe')['src'].encode('utf-8', 'ignore')
                        name2=panel[i].find("span", {"class": "postTabs_titles"}).text.encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR orange][B] >> [COLOR blue]'+str(name2)+'[COLOR orange] >> [/COLOR][COLOR lightblue]'+str(name)+'[/COLOR]',"VIDEOLINKS(name,url)",url,'')
                except:
                        pass


        except Exception:
                buggalo.onExceptionRaised()
def partlar2(url,name):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match=re.compile('flashvars="file=(.*?)" />').findall(link)
                for url in match:
                        xbmctools1.addDir(fileName,'[COLOR beige][B]'+''+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')
                try:
                        VIDEOLINKS(name,url)
                except:
                        pass


        except Exception:
                buggalo.onExceptionRaised()
def replace_fix2(x):
        x=x.replace('-',' ')
        return x

def name_fix(x):        
        x=x.replace('DİZİ İZLE','Yeni Eklenen Yerli ve Yabanci Diziler').replace("-",' ')
        return x[0].capitalize() + x[1:]

def replace_fix(x):        
        x=x.replace('–', '-').replace('&', '&').replace('&amp;', '&').replace('background-image:url(', '').replace(');filter: progid:DXImageTransform.Microsoft.AlphaImageLoader', ' ').replace("(src='http://www.harikadizi1.com/yeni-resim/100x100/",'').replace(".jpg',sizingMethod='scale');-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoader(src='http://www.harikadizi1.com/yeni-resim/100x100/",'').replace(".jpg',sizingMethod='scale');",'').replace("kurttlar-vadisi-pusu-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkurttlar-vadisi-pusu",'').replace("kurttlar",'kurtlar').replace("kurtlar-vadisi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkurtlar-vadisi",'').replace("beyaz-show-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbeyaz-show",'').replace("ask-ekmek-hayaller-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderask-ekmek-hayaller",'').replace("aramizda-kalsin-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderaramizda-kalsin",'').replace("zengin-kiz-fakir-oglan-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderzengin-kiz-fakir-oglan",'').replace("kardes-payi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkardes-payi",'').replace("cocuklar-duymasin-yeni-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadercocuklar-duymasin-yeni",'').replace("umutsuz-ev-kadinlari-izle-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderumutsuz-ev-kadinlari-izle",'').replace("eski-hikaye-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadereski-hikaye",'').replace("kim-milyoner-olmak-ister-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkim-milyoner-olmak-ister",'').replace("kizilelma-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkizilelma",'').replace("zeytin-tepesi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderzeytin-tepesi",'').replace("sevdaluk-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadersevdaluk",'').replace("unutma-beni-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderunutma-beni",'').replace("benim-hala-umudum-var-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbenim-hala-umudum-var",'').replace("gurbette-ask-bir-yastikta-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadergurbette-ask-bir-yastikta",'').replace("seksenler-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderseksenler",'').replace("benim-icin-uzulme-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbenim-icin-uzulme",'').replace("kucuk-aga-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkucuk-aga",'').replace("calikusu-yerli-diziler-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadercalikusu-yerli-diziler",'').replace("beni-boyle-sev-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbeni-boyle-sev",'').replace("asayis-berkkemal-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderasayis-berkkemal",'').replace("karadayi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkaradayi",'').replace("her-sevda-bir-veda-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderher-sevda-bir-veda",'').replace("yetenek-sizsiniz-yerli-diziler-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderyetenek-sizsiniz-yerli-diziler",'').replace("dila-hanim-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderdila-hanim",'').replace("cinayet-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadercinayet",'').replace("gunesi-beklerken-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadergunesi-beklerken",'').replace("bir-yusuf-masali-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbir-yusuf-masali",'').replace("cesur-hemsire-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadercesur-hemsire",'').replace("arkadasim-hosgeldin-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderarkadasim-hosgeldin",'').replace("osmanli-tokadi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderosmanli-tokadi",'').replace("arka-sokaklar-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderarka-sokaklar",'').replace("lale-devri-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderlale-devri",'').replace("bugunun-saraylisi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderbugunun-saraylisi",'').replace("fatih-harbiye-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderfatih-harbiye",'').replace("sefkat-tepe-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadersefkat-tepe",'').replace("yalann-dunya-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderyalann-dunya",'').replace("medcezir-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadermedcezir",'').replace("guldur-guldur-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderguldur-guldur",'').replace("gonul-hirsizi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadergonul-hirsizi",'').replace("boyle-bitmesin-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderboyle-bitmesin",'').replace("huzur-sokagi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderhuzur-sokagi",'').replace("karagul-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkaragul",'').replace("pis-yedili-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderpis-yedili",'').replace("merhameet-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoadermerhameet",'').replace("kucuk-gelin-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkucuk-gelin",'').replace("deniz-yildizi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderdeniz-yildizi",'').replace("kacak-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderkacak",'').replace("deniz-yildizi-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderdeniz-yildizi",'').replace("ekip-1-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderekip-1",'').replace("doksanlar-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderdoksanlar",'').replace("ben-de-ozledim-ms-filter: progid:DXImageTransform.Microsoft.AlphaImageLoaderben-de-ozledim",'')
        return x


def VIDEOLINKS(name,url):

        buggalo.SUBMIT_URL = denemesite
        try:
##        web='aHR0cDovL3NpbmVtYS54Ym1jdHIudHYv'
##        link=xbmctools1.get_url(base64.b64decode(web))
##        match=re.compile('<li><a href="#" class="toplam">(.*?)</a></li>').findall(link)
##        for bul in match:
##                bul=''
##                print bul
        #---------------------------#
                urlList=[]
                #---------------------------#
                playList.clear()
                link=xbmctools1.get_url(url)
                link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')

                        #---------------------------------------------#
                vk_2=re.compile('<iframe src="http://vk.com/(.*?)"').findall(link)
                for url in vk_2:
                        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)

                
                        #---------------------------------------------#

                vk_3=re.compile('http:\/\/vk.com\/(.*?)"').findall(link)
                for url in vk_3:
                        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                veka=re.compile('value="http:\/\/.*?\/veka.swf\?file\=(.*?)\&otobaslat\=0"').findall(link)
                for url in veka:
                        url = 'http://'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                divxstage=re.compile('src=\'http://embed.divxstage.eu/(.*?)&').findall(link)
                for url in divxstage:
                        url = 'http://embed.divxstage.eu/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                ok=re.compile('http://www.ok.ru/videoembed/(.*?)"').findall(link)
                for okrugelen in ok:
                        url = 'http://ok.ru/videoembed/'+str(okrugelen)
                        value=[]
                        value.append((name,cozuculer1.ok_ru(url)))
                        #---------------------------------------------#
                youtube=re.compile('src="http\:\/\/www.youtube.com\/embed\/(.*?)\?').findall(link)
                for url in youtube:
                        url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                movshare=re.compile('src=\'http://embed.movshare.net/(.*?)&').findall(link)
                for url in movshare:
                        url = 'http://embed.movshare.net/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                uploadc=re.compile('src="(.*?)uploadc(.*?)"').findall(link)
                for url,uploadcgelen in uploadc:
                        url = str(url)+'uploadc'+str(uploadcgelen).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                mailru=re.compile('http:\/\/.*?\/mail\/(.*?).html').findall(link)
                for mailrugelen in mailru:
                        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(mailrugelen)+'.html'
                        value=[]
                        value.append((name,cozuculer1.MailRu_Player(url)))
                        #---------------------------------------------#
                dm=re.compile('src="http://www.dailymotion.com/embed/video/(.*?)"').findall(link)
                for url in dm:
                        url = 'http://www.dailymotion.com/embed/video/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                video=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                for videodgelen in video:
                        url =videogelen
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                divxstage=re.compile('src="(.*?)divxstage(.*?)"').findall(link)
                for url,divxstagegelen in divxstage:
                        url = str(url)+'divxstage'+str(divxstagegelen).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                        #---------------------------------------------#
                        #---------------------------------------------#
                if not urlList:
                        match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
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
