# -*- coding: utf-8 -*-
import urllib,urllib2,re,base64,os,sys,time
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName="BESIR_EURO_TV"
#------------------eklenecek kısım------------------
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')
#---------------------------------------------------

denemesite = 'https://koditr.org/denemebugalo/submit.php'


        
def main():
        buggalo.SUBMIT_URL = denemesite
        try:
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Turkce Ulusual Kanallar[/B][/COLOR]', "BuildPage(code='tr',dil='TR.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-U.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Deutsche Sender[/B][/COLOR]', "BuildPage(code='de',dil='DE.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-A.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Besir Filmler[/B][/COLOR]', "BuildPage(code='sn',dil='Sinema.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-F.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Kemal Sunal Filmleri[/B][/COLOR] ', "BuildPage(code='kemal',dil='kemal.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-K.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Yabanci Kanallar[/B][/COLOR]', "BuildPage(code='yaban',dil='yabanci.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-Y.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Turkce Radyolar[/B][/COLOR]', "BuildPage(code='rdy',dil='Radyo.xml')",'','https://koditr.org/dreamyenisistem/Portallarsifreli/B-R.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Turkce Spor Kanallari[/B][/COLOR]', "BuildPage(code='spr',dil='SPOR.xml')",'','http://www.tav-sanpark.com/images/spor_all.png')
                #xbmctools1.addDir(fileName,__language__(30052), "BuildPage(code='dini',dil='ULUSAL.xml')",web,'special://home/addons/plugin.video.dream-clup/resources/images/XBMCTRSPOR.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Cocuk Kanallari[/B][/COLOR]', "BuildPage(code='cocuk',dil='cocuk.xml')",'','http://evdonaucity.wdfiles.com/local--files/news-2008-2009/VBSLogoKinder.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Muzik Kanallari[/B][/COLOR] ', "BuildPage(code='muz',dil='muz.xml')",'','http://www.heridan.com/butonlar/mp3-muzik.png')
                xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]Dini Kanallar[/B][/COLOR] ', "BuildPage(code='din',dil='dini.xml')",'','http://www.abload.de/img/pic69001zqp8h.png')
                xbmc.executebuiltin("Container.SetViewMode(500)")

        except Exception:
                buggalo.onExceptionRaised()
def BuildPage(code,dil):
        buggalo.SUBMIT_URL = denemesite
        try:
            a=0
            html = xbmctools1.besir()
            name=__settings__.getSetting("Name")
            login=__settings__.getSetting("Username")
            password=__settings__.getSetting("password")
            match = re.compile('<!--#(.*?)-->').findall(html)
            for web in match:
                web=xbmctools1.angel(base64.b64decode(web))
                tr=re.compile('<name><!\[CDATA\[(.*?)\]\]></name>\n  <link><!\[CDATA\[(.*?)\]\]></link>\n  <thumbnail><!\[CDATA\[(.*?)\]\]></thumbnail>').findall(web)
                de=re.compile('<dename><!\[CDATA\[(.*?)\]\]></dename>\n  <delink><!\[CDATA\[(.*?)\]\]></delink>\n  <dethumbnail><!\[CDATA\[(.*?)\]\]></dethumbnail>').findall(web)
                sn=re.compile('<sinemaname><!\[CDATA\[(.*?)\]\]></sinemaname>\n  <sinemalink><!\[CDATA\[(.*?)\]\]></sinemalink>\n  <sinemathumbnail><!\[CDATA\[(.*?)\]\]></sinemathumbnail>').findall(web)
                klp=re.compile('<kliplername><!\[CDATA\[(.*?)\]\]></kliplername>\n  <kliplerlink><!\[CDATA\[(.*?)\]\]></kliplerlink>\n  <kliplerthumbnail><!\[CDATA\[(.*?)\]\]></kliplerthumbnail>').findall(web)
                rdy=re.compile('<radyoname><!\[CDATA\[(.*?)\]\]></radyoname>\n  <radyolink><!\[CDATA\[(.*?)\]\]></radyolink>\n  <radyothumbnail><!\[CDATA\[(.*?)\]\]></radyothumbnail>').findall(web)
                spr=re.compile('<sporname><!\[CDATA\[(.*?)\]\]></sporname>\n  <sporlink><!\[CDATA\[(.*?)\]\]></sporlink>\n  <sporthumbnail><!\[CDATA\[(.*?)\]\]></sporthumbnail>').findall(web)
                ulus=re.compile('<name><!\[CDATA\[(.*?)\]\]></name>\n  <link><!\[CDATA\[(.*?)\]\]></link>\n  <thumbnail><!\[CDATA\[(.*?)\]\]></thumbnail>').findall(web)
                cocuk=re.compile('<cocukname><!\[CDATA\[(.*?)\]\]></cocukname>\n  <cocuklink><!\[CDATA\[(.*?)\]\]></cocuklink>\n  <cocukthumbnail><!\[CDATA\[(.*?)\]\]></cocukthumbnail>').findall(web)
                muz=re.compile('<muzikname><!\[CDATA\[(.*?)\]\]></muzikname>\n  <muziklink><!\[CDATA\[(.*?)\]\]></muziklink>\n  <muzikthumbnail><!\[CDATA\[(.*?)\]\]></muzikthumbnail>').findall(web)
                din=re.compile('<dininame><!\[CDATA\[(.*?)\]\]></dininame>\n  <dinilink><!\[CDATA\[(.*?)\]\]></dinilink>\n  <dinithumbnail><!\[CDATA\[(.*?)\]\]></dinithumbnail>').findall(web)
                yaban=re.compile('<yabanciname><!\[CDATA\[(.*?)\]\]></yabanciname>\n  <yabancilink><!\[CDATA\[(.*?)\]\]></yabancilink>\n  <yabancithumbnail><!\[CDATA\[(.*?)\]\]></yabancithumbnail>').findall(web)
                kemal=re.compile('<kemalsunalname><!\[CDATA\[(.*?)\]\]></kemalsunalname>\n  <kemalsunallink><!\[CDATA\[(.*?)\]\]></kemalsunallink>\n  <kemalsunalthumbnail><!\[CDATA\[(.*?)\]\]></kemalsunalthumbnail>').findall(web)
            if code is 'tr':
        #------------------------------------------------ 
                 for videoTitle,Url,Thumbnail in tr:
                         addVideoLink(videoTitle,Url,Thumbnail)
                 xbmc.executebuiltin("Container.SetViewMode(500)")
        #------------------------------------------------
                      ############
            else:
                pass
            if code is 'de':
                  for videoTitle,Url,Thumbnail in de:
                          addVideoLink(videoTitle,Url,Thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")
            else:
                pass
            if code is 'sn':
                  for name,url,thumbnail in sn:
                       xbmctools1.addDir(fileName,name, "yeni4(name,url)",url,thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")
            else:
                pass
            if code is 'klp':
                  for name,url,thumbnail in klp:
                       xbmctools1.addDir(fileName,name, "yeni4(name,url)",url,thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")
            else:
                pass
            if code is 'rdy':
                  for videoTitle,Url,Thumbnail in rdy:
                          addVideoLink(videoTitle,Url,Thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")
            else:
                pass

            if code is 'spr':
                  for videoTitle,Url,Thumbnail in spr:
                       addVideoLink(videoTitle,Url,Thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")
            else:
                pass

            if code is 'cocuk':
                  for videoTitle,Url,Thumbnail in cocuk:
                       addVideoLink(videoTitle,Url,Thumbnail)
                  xbmc.executebuiltin("Container.SetViewMode(500)")

            else:
                pass

            if code is 'muz':
                    for videoTitle,Url,Thumbnail in muz:
                       addVideoLink(videoTitle,Url,Thumbnail)
                    xbmc.executebuiltin("Container.SetViewMode(500)")

            else:
                pass

            if code is 'din':
                    for videoTitle,Url,Thumbnail in din:
                       addVideoLink(videoTitle,Url,Thumbnail)
                    xbmc.executebuiltin("Container.SetViewMode(500)")

            else:
                pass

            if code is 'yaban':
                    for videoTitle,Url,Thumbnail in yaban:
                       addVideoLink(videoTitle,Url,Thumbnail)
                    xbmc.executebuiltin("Container.SetViewMode(500)")

            else:
                pass

            if code is 'kemal':
                    for name,url,thumbnail in kemal:
                       xbmctools1.addDir(fileName,name, "yeni4(name,url)",url,thumbnail)
                    xbmc.executebuiltin("Container.SetViewMode(500)")

            else:
                pass

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




def INFO(url):
  try:
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "www.xmbctr.com TEAM katkilariyla","Iyi seyirler dileriz...","Hazirlayan @Besir")
  except:
        pass 






def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
