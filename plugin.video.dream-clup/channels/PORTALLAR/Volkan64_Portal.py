# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re,base64
import urlresolver
import time
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="Volkan64_Portal"


__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

vtvt='https://koditr.org/livetv/Volkan64/Canli_TV/Volkan64_Canli_TV.png'
vrdt='https://koditr.org/livetv/Volkan64/Canli_Radyo/Radyo_Sefasi.png'
bundest='http://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Faux_drapeau_germano-turc.svg/800px-Faux_drapeau_germano-turc.svg.png'
bel='https://koditr.org/livetv/Volkan64/Belgesel_Keyfi.png'
almancanli='https://koditr.org/livetv/Volkan64/AlmanCanli/Alman_Kanallari.png'
almanspor='https://koditr.org/livetv/Volkan64/AlmanCanli/Alman_Spor_Kanallari.png'
trt='https://koditr.org/livetv/Volkan64/Trt_Kanallari.png'
yaban='https://koditr.org/livetv/Volkan64/Yabanci_Filmler.png'
turk='https://koditr.org/livetv/Volkan64/Turk_Sinemasi.png'
haba='https://koditr.org/livetv/Volkan64/Hababam_Sinifi_Filimleri.png'
muc='https://koditr.org/livetv/Volkan64/Kuran_Mucizeleri.png'
yer='https://koditr.org/livetv/Volkan64/Turk_Sinemasi.png'
anime='https://koditr.org/livetv/Volkan64/Animasyon_Filimler.png'
acikla='https://koditr.org/livetv/Volkan64/Aciklama_ve_Bilgilendirme.png'

denemesite = 'https://koditr.org/denemebugalo/submit.php'

def main():
        buggalo.SUBMIT_URL = denemesite
        try:
        
                try:
                        html = xbmctools1.volkan()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                

                                xbmctools1.addDir(fileName,'[COLOR orange][B]>>> Volkan Canli TV ~~[/B][/COLOR][COLOR red] [B]>>>>[/B][/COLOR][COLOR green]OTO GUNCEL [/COLOR][COLOR red]<<<<[/COLOR]', "vtv(name,url)",'',vtvt,vtvt)
                                xbmctools1.addDir(fileName,'[COLOR lightyellow][B]>>> Volkan Canli Radyo ~~[/B][/COLOR][COLOR red] [B]>>>>[/B][/COLOR][COLOR green]OTO GUNCEL [/COLOR][COLOR red]<<<<[/COLOR]', "radyo(name,url)",'',vrdt,vrdt)
                                xbmctools1.addDir(fileName,'[COLOR lightblue][B]>>>[COLOR red] Volkan Bundes Republic ~~[/B][/COLOR][COLOR lightyellow] [B]>>>>[/B][/COLOR][COLOR orange]OTO GUNCEL [/COLOR][COLOR lightyellow]<<<<[/COLOR]', "bundesler()",'',bundest,bundest)
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>> Aciklama ve Bilgilendirme[/B][/COLOR]', "aciklama(name,url)",'',str(acikla),str(acikla))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Animasyon Filimler[/B][/COLOR]', "animasyon(name,url)",'',str(anime),str(anime))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Belgesel Keyfi[/B][/COLOR]', "belgesel(name,url)",'',str(bel),str(bel))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Hababam Sinifi Filimleri[/B][/COLOR]', "hababam(name,url)",'',str(haba),str(haba))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Kuran Mucizeleri[/B][/COLOR]', "kuran(name,url)",'',str(muc),str(muc))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>TRT Kanallari[/B][/COLOR]', "trttv(name,url)",'',str(trt),str(trt))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Turk Sinemasi[/B][/COLOR]', "turksinemasi(name,url)",'',str(turk),str(turk))
                                xbmctools1.addDir(fileName,'[COLOR pink][B]>>>Yabanci Filimler[/B][/COLOR]', "yabanci(name,url)",'',str(yaban),str(yaban))
                               # xbmctools1.addDir(fileName,'[COLOR pink][B]>>>En Yeni Turk Filimleri[/B][/COLOR]', "yerli(name,url)",'',str(yer),str(yer))

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()

        except Exception:
                buggalo.onExceptionRaised()
def bundesler():
        buggalo.SUBMIT_URL = denemesite
        try:
                xbmctools1.addDir(fileName,'[COLOR lightblue][B]>>>[COLOR red] Volkan Bundes Republic ~~[/B][/COLOR][COLOR lightyellow] [B]>>>>[/B][/COLOR][COLOR orange]OTO GUNCEL [/COLOR][COLOR lightyellow]<<<<[/COLOR]', "bundestv(name,url)",'',almancanli,almancanli)
                xbmctools1.addDir(fileName,'[COLOR lightblue][B]>>>[COLOR red] Volkan Bundes Republic Spor ~~[/B][/COLOR][COLOR lightyellow] [B]>>>>[/B][/COLOR][COLOR orange]OTO GUNCEL [/COLOR][COLOR lightyellow]<<<<[/COLOR]', "bundesspor(name,url)",'',almanspor,almanspor)
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def vtv(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<name>(.*?)</name>\n  <thumbnail>(.*?)</thumbnail>\n  <link>(.*?)</link>\n').findall(web)
                        for videoTitle,Thumbnail,Url in tr:
                                Url=Url.replace('<![CDATA[','').replace(']]>','')
                                videoTitle=videoTitle.replace('<![CDATA[','').replace(']]>','')
                                Thumbnail=Thumbnail.replace('<![CDATA[','').replace(']]>','')
                                name=ifix.decode_fix(name)
                                addVideoLink(videoTitle,Url,Thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def radyo(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        match1=re.compile('<radyotitle>(.*?)</radyotitle>\n  <radyothumbnail>(.*?)</radyothumbnail>\n  <radyolink>(.*?)</radyolink>\n').findall(web)
                        for name,thumbnail,url in match1:
                                name=ifix.decode_fix(name)
                                name=name.replace('&gt;','>')
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR red]''>> ''[/COLOR]'+ name,"yeni4(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def bundestv(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<almancanliname>(.*?)</almancanliname>\n  <almancanlithumbnail>(.*?)</almancanlithumbnail>\n  <almancanlilink>(.*?)</almancanlilink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR red]''>> ''[/COLOR]'+ name,"yeni4(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def bundesspor(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<almansporname>(.*?)</almansporname>\n  <almansporthumbnail>(.*?)</almansporthumbnail>\n  <almansporlink>(.*?)</almansporlink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR red]''>> ''[/COLOR]'+ name,"yeni4(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def animasyon(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<animasyontitle>(.*?)</animasyontitle>\n  <animasyonthumbnail>(.*?)</animasyonthumbnail>\n  <animasyonlink>(.*?)</animasyonlink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def belgesel(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<belgeseltitle>(.*?)</belgeseltitle>\n  <belgeselthumbnail>(.*?)</belgeselthumbnail>\n  <belgesellink>(.*?)</belgesellink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def hababam(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<hababamtitle>(.*?)</hababamtitle>\n  <hababamthumbnail>(.*?)</hababamthumbnail>\n  <hababamlink>(.*?)</hababamlink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def kuran(name,url):

        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<mucizetitle>(.*?)</mucizetitle>\n  <mucizethumbnail>(.*?)</mucizethumbnail>\n  <mucizelink>(.*?)</mucizelink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def turksinemasi(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<turksinemasititle>(.*?)</turksinemasititle>\n  <turksinemasithumbnail>(.*?)</turksinemasithumbnail>\n  <turksinemasilink>(.*?)</turksinemasilink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def yabanci(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<yabancifilmtitle>(.*?)</yabancifilmtitle>\n  <yabancifilmthumbnail>(.*?)</yabancifilmthumbnail>\n  <yabancifilmlink>(.*?)</yabancifilmlink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def aciklama(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<aciklamatitle>(.*?)</aciklamatitle>\n  <aciklamathumbnail>(.*?)</aciklamathumbnail>\n  <aciklamalink>(.*?)</aciklamalink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR red]''>> ''[/COLOR]'+ name,"yeni4(name,url)",url,thumbnail)
        except Exception:
                buggalo.onExceptionRaised()
def yerli(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<yerlititle>(.*?)</yerlititle>\n  <yerlithumbnail>(.*?)</yerlithumbnail>\n  <yerlilink>(.*?)</yerlilink>\n').findall(web)
                        for name,thumbnail,url in tr:
                                name=ifix.decode_fix(name)
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                thumbnail=thumbnail.replace('<![CDATA[','').replace(']]>','')
                                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]> [/COLOR]'+name+'[/B][/COLOR]', "cozuculer1.magix_player(name,url)",url,thumbnail,thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()        
def trttv(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.volkan()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<trtname>(.*?)</trtname>\n  <trtthumbnail>(.*?)</trtthumbnail>\n  <trtlink>(.*?)</trtlink>\n').findall(web)
                        for videoTitle,Thumbnail,Url in tr:
                                name=ifix.decode_fix(name)
                                Url=Url.replace('<![CDATA[','').replace(']]>','')
                                videoTitle=videoTitle.replace('<![CDATA[','').replace(']]>','')
                                Thumbnail=Thumbnail.replace('<![CDATA[','').replace(']]>','')
                                addVideoLink(videoTitle,Url,Thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
                
        except Exception:
                buggalo.onExceptionRaised()
def yeni4(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                xbmctools1.addLink(name,url,'')
                listitem = xbmcgui.ListItem(name)
                playList.add(url, listitem)
                xbmcPlayer.play(playList)
        except Exception:
                buggalo.onExceptionRaised()        
def UrlResolver_Player(name,url):
        UrlResolverPlayer = url
        playList.clear()
        media = urlresolver.HostedMediaFile(UrlResolverPlayer)
        source = media
        if source:
                url = source.resolve()
                xbmctools1.addLink(name,url,'')
                xbmctools1.playlist_yap(playList,name,url)
                xbmcPlayer.play(playList)

def get_url(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                link=link.replace('\xf6',"o").replace('&amp;',"&").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g")
                link=link.replace('\xc5\x9f',"s").replace('&#038;',"&").replace('&#8217;',"'").replace('\xc3\xbc',"u").replace('\xc3\x87',"C").replace('\xc4\xb1',"?").replace('&#8211;',"-").replace('\xc3\xa7',"c").replace('\xc3\x96',"O").replace('\xc5\x9e',"S").replace('\xc3\xb6',"o").replace('\xc4\x9f',"g").replace('\xc4\xb0',"I").replace('\xe2\x80\x93',"-")
                response.close()
                return link
        except Exception:
                buggalo.onExceptionRaised()
def addFolder(FILENAME, videoTitle, method, url="", thumbnail="",fanart=""):
        u = sys.argv[0]+"?fileName="+urllib.quote_plus(FILENAME)+"&videoTitle="+urllib.quote_plus(videoTitle)+"&method="+urllib.quote_plus(method)+"&url="+urllib.quote_plus(url)+"&fanart="+urllib.quote_plus(fanart)
        if thumbnail != "":
                thumbnail = os.path.join(IMAGES_PATH, thumbnail+".png")
        liz = xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz=xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setProperty( "Fanart_Image", fanart )
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    

def addVideoLink(linkTitle, url, thumbnail=""):
    liz = xbmcgui.ListItem(linkTitle, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
    liz.setInfo(type="Video", infoLabels={"Title":linkTitle})
    liz.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)


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


def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
