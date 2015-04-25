# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName="Live_German"


__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')
a='rtmp://server101-yt.stream-company.org/live/'
b=' swfUrl=http://www.yourtv.to/js/jwplayer.flash.swf pageUrl=http://www.yourtv.to/online/live/fernsehen/stream/'
c='.html'
d='http://www.yourtv.to/img/data/channels/'
e='.gif'
f=' live=1'
k=''
t='rtmp://server101-yt.stream-company.org/live/ playpath='

yenit='http://1.bp.blogspot.com/-P1ykZvW7YQs/Tcg_hZHZ-xI/AAAAAAAAAt8/jB8Cx2KQfv8/s1600/Wallpaper+Flag+of+Romania.jpg'

denemesite = 'https://koditr.org/denemebugalo/submit.php'

def main():
        buggalo.SUBMIT_URL = denemesite
        try:
        
                try:
                        html = xbmctools1.alman()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#WW#(.*?)-->').findall(html)
                        for web in match:
                                print match
                                web=xbmctools1.angel(base64.b64decode(web))
                                #link=xbmctools1.get_url(web)
                                match=re.compile('<name>(.*?)</name>\n\n\t<link>(.*?)</link>').findall(web)
                                for name,url in match:
                                        xbmctools1.addDir(fileName,'[COLOR lightgreen][B]>> [/B][/COLOR]'+'[COLOR lightblue][B]' + name+'[/B][/COLOR]',"VIDEOLINKS2(name,url)",url,'') 
                                                        
     
                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()

        except Exception:
                buggalo.onExceptionRaised()       
def Livee(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match=re.compile('<a href="/online/live/fernsehen/stream/(.*?).html" title=".*?Online Live Stream">').findall(link)
                for x in match:
                        name=x
                        name=Liveeename_fix(name)
                        url=a+x+b+x+c+f
                        url=t+x+b+x+c+f
                        thumbnail=d+x+e
                        xbmctools1.addLink('[COLOR beige][B]>> '+name+' [/B][/COLOR]',url,thumbnail)
        except Exception:
                buggalo.onExceptionRaised()
def Liveeename_fix(x):        
        x=x.replace('aaa','bbb').replace("-",' ')
        return x[0].capitalize() + x[1:]


def yeni(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                match=re.compile(' src=&quot;http://embed.live-stream.tv/(.*?)&quot;').findall(link)
                for url2 in match:
                        idi=url2
                        url2='http://embed.live-stream.tv/'+url2
                        link=xbmctools1.get_url(url2)
                        match=re.compile('streamer\|(.*?)\|').findall(link)
                        for server in match:
                                url='rtmp://'+server+'.stream-server.org:1935/live playpath='+idi+'.stream swfUrl=http://static.live-stream.tv/player/player.swf'+url2+' live=1'
                                playList.clear()
                                xbmctools1.addLink(name,url,yenit)
                                listitem = xbmcgui.ListItem(name)
                                playList.add(url, listitem)
                                xbmcPlayer.play(playList)
        except Exception:
                buggalo.onExceptionRaised()
def hasbah(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                link=xbmctools1.get_url(url)
                link=link.replace('rtmp://$OPT:rtmp-raw=',"")
                match=re.compile('#EXTINF:-1,(.*?)\r\n(.*?)\r\n').findall(link)
                if match >0:
                        del match[0]

                        for name,url in match:
                                xbmctools1.addDir(fileName,'[COLOR beige][B]' + name+'[/B][/COLOR]',"VIDEOLINKS2(name,url)",url,'http://us.cdn1.123rf.com/168nwm/kaarsten/kaarsten1101/kaarsten110100156/8588091-cheering-blonde-woman-with-german-flag-all-on-white-background.jpg')
        except Exception:
                buggalo.onExceptionRaised()

def VIDEOLINKS2(name,url):
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
##################

def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
