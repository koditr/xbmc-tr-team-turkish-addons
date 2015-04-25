# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
from xbmctools import z

fileName ="Yetiskin"

__settings__ = xbmcaddon.Addon(id='plugin.video.yetiskin')

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
        try:
                html = xbmctools.sifre3()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!-- XX-(.*?)-->').findall(html)
                for url in match:
                        link=xbmctools.get_url(url)
                        match=re.compile('<a href="(.*?)" title=".*?">\n\t\t\t\t\t\t<img src="/assets/images/cover_front_catalogs/(.*?).jpg"').findall(link)
                        for a,b in match:
                                url1=url.replace('/en/','')                                
                                url1=url1+a
                                name=b                                
                                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "Recent(url)",url1,"")

        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
def Recent(url1):
        link=xbmctools.get_url(url1)
        match=re.compile('<a href="(.*?)" title=".*?">\n\t\t\t<img src="(.*?)" alt="(.*?)">').findall(link)
        for url,thumbnail,name in match:
                thumbnail=z+thumbnail                
                url=z+url
                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "ayrisdirma(url)",url,thumbnail)
        page=re.compile('<span>.*?</span></li>\n<li><a href="(.*?)">(.*?)</a>').findall(link)
        for url,name in page:
                url=url1+url
                xbmctools.addDir(fileName,'[COLOR blue][B]NEXT Page >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "Recent(url)",url,"special://home/addons/plugin.video.magicTR/resources/images/sonrakisayfa.png")
def ayrisdirma(url):
        link=xbmctools.get_url(url)     
        match=re.compile('var films\= "http:\/\/(.*?).flv"').findall(link)
        for url in match:
                url='http://'+url+'.flv'
                name=' Now'
                xbmctools.addDir('[COLOR red]Watch '+name+'[/COLOR]',url,44,t)
        link=xbmctools.get_url(url)
        match1=re.compile("http:\/\/(.*?)part_(.*?).mp4").findall(link)
        for url,name in match1:
                url='http://'+url+'part_'+name+'.mp4'
                xbmctools.addDir(fileName,'[COLOR red]Part '+name+'[/COLOR]', "VideoLinks(url)",url,"")
        link=xbmctools.get_url(url)
        match2=re.compile("http:\/\/(.*?).mp4").findall(link)
        for url in match2:
                url='http://'+url+'.mp4'
                name=' Now'
                xbmctools.addDir(fileName,'[COLOR red]Watch'+name+'[/COLOR]',"VideoLinks(name,url)",url,"")               
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
def INFO(url):
  try:
        CATEGORIES()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR beige]SADECE VIP + Uyeler icindir[/COLOR],[COLOR yellow]Turkiyeden Izlenemeyebilir[/COLOR] ","[COLOR yellow]DNS Ayarlariyla girilebilir[/COLOR]")
  except:
        
        pass 
                                             

def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )








