# -*- coding: iso-8859-9 -*-
import base64
import cookielib,sys
import urllib2,urllib,re,os

from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

import xbmcplugin,xbmcgui,xbmc,xbmcaddon 

Addon = xbmcaddon.Addon('plugin.video.xbmcTR')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
addonsettings = xbmcaddon.Addon(id='plugin.video.xbmcTR')


FILENAME = "smartx"

__language__ = addonsettings.getLocalizedString
home = addonsettings.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
import  tools,cozerim




def main(web):
##    print "gelen url",web
    link=tools.get_url(web)
##    print base64.b64decode(link)
    folders=re.compile('<br>(.*?)</br>').findall(link)
    print "folders",folders
    files=re.compile('<p>(.*?)</p>').findall(link)
    print "files",files
    if folders:
        for folder in folders:
            a=base64.b64decode(folder)
            dosya=re.compile('<li><a href=".*?">\./(.*?)</a>').findall(a)
            print 'dosya',dosya
            for videoTitle in dosya:
                url=str(web)+str(videoTitle)+"/"
                videoTitle=videoTitle.replace('.xml','').replace('_',' ').replace('-',' ')
                print "gidecek url",url
                tools.addDir(videoTitle,url,"","smartx.main(url)")
    
    if files:
        first=re.compile('<p>(.*?)</p>').findall(link)
        first=base64.b64decode(first[0])
        second=re.compile('<li><a href=".*?">(.*?)</a>').findall(first)
        second=sorted(second, key=str.lower)
        for videoTitle in second:
            if "yeni" in videoTitle:
                url=str(web)+str(videoTitle)
                videoTitle='[COLOR lightgreen][B]YENI BOLUMLER[/B][/COLOR]'
                tools.addDir(videoTitle,url,"", "smartx.getData(url)")
        for videoTitle in second:
            url=str(web)+str(videoTitle)
            videoTitle=videoTitle.replace('.xml','').replace('-',' ').replace('_',' ')
            videoTitle=name_fix(videoTitle)
##            print "gidecek url",url
            tools.addDir(videoTitle,url,"", "smartx.getData(url)")
    


def getData(url):        
    print "getdata url:",url
    bolumList=[]
    link=tools.get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    if len(soup('movies')) > 0 :
        channels = soup('dizi')
        for channel in channels:
            name = channel('isim')[0].string
            name = name.replace('.xml','').replace('_',' ')
            thumbnail=channel('resim')[0].string.encode('utf-8')
            tools.addDir(name,url,thumbnail,"smartx.get_part(name,url)")

def get_part(title,adres):
    if xbmcPlayer.isPlaying():
            xbmcPlayer.stop()
            playList.clear()

    link=tools.get_url(adres)
    soup = BeautifulSoup(link)
    channels = soup('dizi')
    for channel in channels:
        name = channel('isim')[0].string.replace('_',' ')
        thumbnail=channel('resim')[0].string
        if not thumbnail:
            thumbnail="http://forum.xbmctr.com/images/thecure/logo.jpg"
        if name == title:
            if xbmcPlayer.isPlaying():
                xbmcPlayer.stop()
            playList.clear()    
            items = channel.findAll("bilgi")
            videoTitle=title
            for item in items:
                    server=cozerim.denetle(item.url.string.replace(';',''))
                    for title,url in server:
                        title=title
                        url=url                    

                    if videoTitle is not None:
                        listitem = xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
                        listitem.setInfo('video', {'videoTitle': videoTitle } )
                        playList.add(url,listitem=listitem)
                        tools.addLink(videoTitle,url,thumbnail,"")
                    else:
                        tools.addLink("Video Yok",url,thumbnail,"")
            xbmcPlayer.play(playList)
        else:
            pass
def name_fix(x):
    return x[0].capitalize() + x[1:]
        

