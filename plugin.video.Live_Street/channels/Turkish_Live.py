# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
##from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
from xbmctools import pt
DA='LDE4OQlray8lK1osJ2JQXCUcPSo+KyJkOiM8dC0hcXsBdA=='
ZS='LDE4OQlraz87Mh0qLThSXyNWPj8mLWQpJWQZABAwPiIcEDE6JyxALxwaHUcwRw=='

fileName ="Turkish_Live"

__settings__ = xbmcaddon.Addon(id='plugin.video.Live_Street')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
#-------------------------------------------------#
import xbmctools

#-------------------------------------------------#
xbmcPlayer = xbmc.Player()

playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playList.clear()
#-------------------------------------------------#

addon_icon    = __settings__.getAddonInfo('icon')


def main():
        
#------------------------------------------------#
        try:
                html = xbmctools.sifre4()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools.angel(base64.b64decode(web))
                        tr=re.compile('<title>(.*?)</title>\n    <stream_url>(.*?)</stream_url>\n    <thumbnail>(.*?)</thumbnail>').findall(web)
                        for name,url,Thumbnail in tr:
                                url=url.replace('<![CDATA[','').replace(']]>','').replace('amp;','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                xbmctools.addDir(fileName,'[COLOR blue][B] >>[/B][/COLOR]'+ '[COLOR beige][B]'+name+'[/B][/COLOR]',"VideoLinks(name,url)",url,Thumbnail,Thumbnail)
##                HA=xbmctools.angel(base64.b64decode(ZS))
##                link=xbmctools.get_url(HA)
##                match11 = re.compile("-1,(.*?)\n(.*?)\n").findall(link)
##                for name,url in match11:
##                        if "Twi" in name:
##                                pass
##                        else:
##                                if "Sinem" in name:
##                                        pass
##                                else:
##                                        if "V Fi" in name:
##                                                pass
##                                        else:
##                                                xbmctools.addDir(fileName,'[COLOR orange][B] >>[/B][/COLOR]'+ '[COLOR blue][B]'+name+'[/B][/COLOR]',"VideoLinks3(name,url)",url,'','')
##                match9 = re.compile('<!--#BETA#(.*?)-->').findall(html)
##                for web in match9:
##                        url=xbmctools.angel(base64.b64decode(web))
##                        link=xbmctools.get_url(url)
##                        match1 = re.compile('href="(.*?)" title=".*?"> <span class=".*?">.*?</span> <span class=".*?"> <img src="(.*?)" alt="(.*?)"/>').findall(link)
##                        for url,Thumbnail,name in match1:
##                                xbmctools.addDir(fileName,'[COLOR blue][B] >>[/B][/COLOR]'+ '[COLOR pink][B] & SD > - '+name+'[/B][/COLOR]',"VideoLinks2(name,url)",url,Thumbnail,Thumbnail)
                match1 = re.compile('<!--#??#(.*?)-->').findall(html)
                for web in match1:
                        web=xbmctools.angel(base64.b64decode(web))
                        match=re.compile('<title>(.*?)</title>\n<link>(.*?)</link>').findall(web)
                        for name,url in match:
                                img=''
                                xbmctools.addDir(fileName,'[COLOR red][B] >>[/B][/COLOR]'+ '[COLOR orange][B]'+name+'[/B][/COLOR]',"de_get(name,url)",url,img,img)
                html = xbmctools.sifre2()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#li2#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools.angel(base64.b64decode(web))
                        tr=re.compile('<isim>(.*?)</isim>\n<link>(.*?)</link>\n<resim>(.*?)</resim>').findall(web)
                        for name,url2,Thumbnail in tr:
                                if "--" in name:
                                        pass
                                else:
                                        if "ugur" in name:
                                                pass
                                        else:
                                                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR purple]>>[/COLOR]  '+name+'[/B][/COLOR]',"VideoLinks9(name,url)",url2,Thumbnail,Thumbnail)
 
                        
                
                       
               
        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
def de_get(name,url):
        import requests as requests
        url1=xbmctools.angel(base64.b64decode(DA))
        link=xbmctools.get_url(url1)
        match=re.compile('.m3u8\?(.*?)"').findall(link)
        for cd in match:
                if "utna" in url:
                    VideoLinks3(name,url)
                else:
                    import requests as requests

                    if 'xxx&User' in url:
                        x = url.partition('xxx&User')
                        url = x[0] + 'xxx'
                    x = url.partition('---')
                    url = x[0]
                    id = x[2].replace('xxx','')
                    url=url+'?'+cd
                    VideoLinks3(name,url)

#-----------------------------------------#
def VideoLinks(name,url):
        link=xbmctools.get_url(url)
        match = re.compile('\{file\: "(.*?)"').findall(link)
        for url in match:
                url=url+xbmctools.angel(base64.b64decode(pt))
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                xbmctools.addLink('[COLOR red][B]RETURN List << [/B][/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
                listitem = xbmcgui.ListItem(name)
                playList.add(url, listitem)
                xbmcPlayer.play(playList)
                exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
                if exec_version < 14.0:
                        xbmctools.playlist()
                else:
                        xbmctools.playlist2()
def VideoLinks2(name,url):
        link=xbmctools.get_url(url)
        match=re.compile('file: \'(.*?)u8\',').findall(link)
        for url in match:
                url=url+'u8'
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                xbmctools.addLink('[COLOR red][B]RETURN List << [/B][/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
                listitem = xbmcgui.ListItem(name)
                playList.add(url, listitem)
                xbmcPlayer.play(playList)
                exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
                if exec_version < 14.0:
                        xbmctools.playlist()
                else:
                        xbmctools.playlist2()
                        
def VideoLinks3(name,url):
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        xbmctools.addLink('[COLOR red][B]RETURN List << [/B][/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        listitem = xbmcgui.ListItem(name)
        playList.add(url, listitem)
        xbmcPlayer.play(playList)
        exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
        if exec_version < 14.0:
                xbmctools.playlist()
        else:
                xbmctools.playlist2()
def VideoLinks9(name,url):
        
        link=xbmctools.get_url(url)
        match=re.compile('"mediaUrl":"(.*?)"').findall(link)
        for url in match:
                if match >1:
                        del match [1]
                        
                        url=url.replace('\\','')
                        xbmcPlayer = xbmc.Player()
                        
                        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                        
                        playList.clear()
                        xbmctools.addLink('[COLOR blue][B]'+'RETURN List <<'+' [/B][/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
                        
                        listitem = xbmcgui.ListItem(name)
                        playList.add(url, listitem)
                        xbmcPlayer.play(playList)
                        exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
                        if exec_version < 14.0:
                                xbmctools.playlist()
                        else:
                                xbmctools.playlist2()



def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )










