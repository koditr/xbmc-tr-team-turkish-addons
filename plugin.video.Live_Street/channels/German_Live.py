# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
##from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
from xbmctools import web1,web2,web4

fileName ="German_Live"

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
        html = xbmctools.sifre3()
        name=__settings__.getSetting("Name")
        bak = re.compile('<!--##(.*?)-->').findall(html)
        for bilgi in bak:
                dibilgi=xbmctools.angel(base64.b64decode(bilgi))
        coz = re.compile('<!--DK(.*?)-->').findall(html)
        for digerbilgi in coz:
                genebilgi=xbmctools.angel(base64.b64decode(digerbilgi))
                cj = mechanize.CookieJar()
                br = mechanize.Browser()
                br.set_cookiejar(cj)
                br = mechanize.Browser(factory=mechanize.RobustFactory())
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
                web=xbmctools.angel(base64.b64decode(web1))
                br.open(web)
                br.select_form(nr=0)
                br.form['user_name']=dibilgi
                br.form['user_pass']=genebilgi
                br.submit()
                web3=xbmctools.angel(base64.b64decode(web2))
                br.open(web3)
                html=br.response().read()
                match = re.compile('src="player.php\?channel\=(.*?)&page_id\=1"').findall(html)
                nameList=''
                ok=True
                pDialog = xbmcgui.DialogProgress()
                ret = pDialog.create('Kanal Yukleme...')
                for name in match:
                        if "visitx" in name:
                                pass
                        else:
                                if "babes" in name:
                                        pass
                                else:
                                        if "sexy" in name:
                                                pass
                                        else:
                                                if "star" in name:
                                                        pass
                                                else:
                                                        if "sportfer" in name:
                                                                pass
                                                        else:
                                                
                                                                nameList=nameList+name 
                                                                nameList=nameList+':;'
                                                                web5=xbmctools.angel(base64.b64decode(web4))
                                                                url1=web5+name+'&page_id=1'
                                                                url1=url1.replace(' ','%20')
                                                                br.open(url1)
                                                                html2=br.response().read()
                                                                match2 = re.compile('source src="(.*?)"').findall(html2)
                                                                total=':;'+nameList
                                                                match = total.split(':;')
                                                                del match[-1]
                                                                totalLinks = len(match)
                                                                percent = int( ( totalLinks / 67.0) * 100)
                                                                loadedLinks = 67
                                                                remaining_display ='Bulunan Kanal Sayisi '+'[COLOR yellow][B]'+str(totalLinks)+'[/B][/COLOR]'+' / '+'[COLOR green][B]'+str(loadedLinks)+'[/B][/COLOR]'
                                                                note='[COLOR pink]'+'https://www.koditr.org'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'Magic'+'[COLOR red]TR[/COLOR] Team'+'[/B][/COLOR]'
                                                                pDialog.update(percent,'[COLOR red][B]'+'Kanallar Olusturulurken Lutfen Bekleyiniz...'+'[/B][/COLOR]',remaining_display,note)
                                                                if pDialog.iscanceled():
                                                                        break
                                                                totalLinks=totalLinks+1                       
                                                                for kanal in match2:
                                                                    url2=kanal
                                                                    xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "VideoLinks(name,url)",url2,'')


def VideoLinks(name,url):
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








