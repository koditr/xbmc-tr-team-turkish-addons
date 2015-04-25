# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json

fileName ="xman"

__settings__ = xbmcaddon.Addon(id='plugin.video.xman')

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
                match = re.compile('<!-- yy-(.*?)-->').findall(html)
                for homepage in match:
                        xbmctools.addDir(fileName,'[COLOR red][B][COLOR beige]>>[/COLOR]'+'NEW MOVIES'+'[/B][/COLOR]', "Recent(url)",homepage,"")
                html = xbmctools.sifre3()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!-- yy-(.*?)-->').findall(html)
                for url in match:
                        
        
                        link=xbmctools.get_url(url)
                        match=re.compile('<li><a target="_self" href="/tag/(.*?)" >(.*?)</a>').findall(link)
                        for a,b in match:                                
                                url1=homepage+'tag/'+a
                                name=b                
                                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "Recent(url)",url1,"")

        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
def GET_HTML(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:8.0) Gecko/20100101 Firefox/8.0')
  req.add_header('Referer', homepage)
  response = urllib2.urlopen(req)
  html=response.read()
  response.close()
  return html

def Recent(url1):
        html = xbmctools.sifre3()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        match = re.compile('<!-- yy-(.*?)-->').findall(html)
        for homepage in match:
                homepage=homepage
                link=xbmctools.get_url(url1)
                html = xbmctools.get_url(url1)
                ids = re.search('var tumbid  =(.+?);', html).group(1)
                descs = re.search('var tumbalt =(.+?)\];', html).group(1)

                ids = ids[1:-1]
                idlist = ids.split(',')
                descs = descs[2:-2]
                descs = descs.decode('string_escape')
                desclist =  descs.split("','")
                

                for id,desc in zip(idlist, desclist):
                        
                        vid_title = desc
                        vid_url = homepage+ id
                        vid_image = 'http://cdn.anythumb.com/236x177/' + id + '.jpg'
                        thumbnail=vid_image
                        url=vid_url
                        name=vid_title
                        xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "ayrisdirma(url)",url,thumbnail)
                page=re.compile('<a href="(.*?)" target="_self" id="paging_next">').findall(link)
                for url in page:
                        url=homepage+url
                        url=url.replace('/t','t').replace('//p','/p')
                        name=''
                        xbmctools.addDir(fileName,'[COLOR blue][B]NEXT Page >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "Recent(url)",url,"special://home/addons/plugin.video.magicTR/resources/images/sonrakisayfa.png")
def ayrisdirma(url):
        link=xbmctools.get_url(url)     
        match2=re.compile("'480p\': \'(.*?)\'").findall(link)
        for url in match2:
                #url='http://'+url+'.mp4'
                name=' Now'
                VideoLinks(name,url)              
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
        i = dialog.ok(url, "[COLOR beige]SADECE BRONZE / VIP + Uyeler icindir[/COLOR],[COLOR yellow]Turkiyeden Izlenemeyebilir[/COLOR] ","[COLOR yellow]DNS Ayarlariyla girilebilir[/COLOR]")
  except:
        
        pass 
                                             

def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )








