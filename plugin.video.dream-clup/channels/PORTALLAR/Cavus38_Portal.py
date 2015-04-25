# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re,base64
import urlresolver
import time
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="Cavus38_Portal"


__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

cvs='http://blog.questionpro.com/wp-content/uploads/2014/09/new-143095_640.jpg'

denemesite = 'https://koditr.org/denemebugalo/submit.php'

def main():
        buggalo.SUBMIT_URL = denemesite
        try:
        
                try:
                        html = xbmctools1.cavus()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                

                                xbmctools1.addDir(fileName,'[COLOR orange][B]>>> Ulusal Kanallar ~~[/B][/COLOR][COLOR red] [B]>>>>[/B][/COLOR][COLOR green]GUNCEL [/COLOR][COLOR red]<<<<[/COLOR]', "vtv(name,url)",'',cvs,'')

                                xbmctools1.addDir(fileName,'[COLOR orange][B]>>> TRT Kanallari ~~[/B][/COLOR][COLOR red] [B]>>>>[/B][/COLOR][COLOR green][/COLOR][COLOR red]<<<<[/COLOR]', "vtv1(name,url)",'',cvs,"")
                                xbmctools1.addDir(fileName,'[COLOR orange][B]>>> Cocuk Kanallari ~~[/B][/COLOR][COLOR red] [B]>>>>[/B][/COLOR][COLOR green] [/COLOR][COLOR red]<<<<[/COLOR]', "vtv2(name,url)",'',cvs,"")

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()

        except Exception:
                buggalo.onExceptionRaised()
def vtv(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.cavus()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<ulusalkanallarname>(.*?)</ulusalkanallarname>\n  <ulusalkanallarthumbnail>(.*?)</ulusalkanallarthumbnail>\n  <ulusalkanallarlink>(.*?)</ulusalkanallarlink>\n').findall(web)
                        for videoTitle,Thumbnail,Url in tr:
                                name=ifix.decode_fix(name)
                                Url=Url.replace('<![CDATA[','').replace(']]>','')
                                videoTitle=videoTitle.replace('<![CDATA[','').replace(']]>','')
                                Thumbnail=Thumbnail.replace('<![CDATA[','').replace(']]>','')
                                addVideoLink(videoTitle,Url,Thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def vtv1(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.cavus()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<trtkanallariname>(.*?)</trtkanallariname>\n  <trtkanallarithumbnail>(.*?)</trtkanallarithumbnail>\n  <trtkanallarilink>(.*?)</trtkanallarilink>').findall(web)
                        for videoTitle,Thumbnail,Url in tr:
                                name=ifix.decode_fix(name)
                                Url=Url.replace('<![CDATA[','').replace(']]>','')
                                videoTitle=videoTitle.replace('<![CDATA[','').replace(']]>','')
                                Thumbnail=Thumbnail.replace('<![CDATA[','').replace(']]>','')
                                addVideoLink(videoTitle,Url,Thumbnail)
                        xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def vtv2(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                html = xbmctools1.cavus()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('cocukkanallariname>(.*?)</cocukkanallariname>\n  <cocukkanallarithumbnail>(.*?)</cocukkanallarithumbnail>\n  <cocukkanallarilink>(.*?)</cocukkanallarilink>').findall(web)
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
