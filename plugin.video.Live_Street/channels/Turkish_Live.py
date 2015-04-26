# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
##from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
from xbmctools import pt

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
                print html
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        print web
                        web=xbmctools.angel(base64.b64decode(web))
                        tr=re.compile('<title>(.*?)</title>\n        <stream_url>(.*?)</stream_url>\n        <thumbnail>(.*?)</thumbnail>').findall(web)
                        for name,url,Thumbnail in tr:
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                name=name.replace('<![CDATA[','').replace(']]>','')
                                xbmctools.addDir(fileName,'[COLOR blue][B] >>[/B][/COLOR]'+ '[COLOR beige][B]'+name+'[/B][/COLOR]',"VideoLinks(name,url)",url,Thumbnail,Thumbnail)                     
        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
#-----------------------------------------#
def VideoLinks(name,url):
        link=xbmctools.get_url(url)
        match = re.compile('\{file: "(.*?)"').findall(link)
        for url in match:
                #pt=xbmctools.angel(base64.b64decode(pt))
                url=url+xbmctools.angel(base64.b64decode(pt))
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




def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )










