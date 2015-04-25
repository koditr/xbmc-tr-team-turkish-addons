# xbmctr MEDIA CENTER, is an XBMC add on that sorts and displays 
# video content from several websites to the XBMC user.
#
# Copyright (C) 2011, Emin Ayhan Colak
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# for more info please visit http://xbmctr.com
import base64
import cookielib,sys
import urllib2,urllib,re,os

from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

import xbmcplugin,xbmcgui,xbmc,xbmcaddon 
# -*- coding: iso-8859-9 -*-
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
import  tools,cozucu




def main(web):
    print "gelen url",web
    link=tools.get_url(web)
    folders=re.compile('<br>(.*?)</br>').findall(link)
##    print "folders",folders
    files=re.compile('<p>(.*?)</p>').findall(link)
##    print "files",files
    if folders:
        for folder in folders:
            a=base64.b64decode(folder)
            print "decode folder",a
            dosya=re.compile('<li><a href=".*?">\./(.*?)</a>').findall(a)
##            print 'dosya',dosya
            for videoTitle in dosya:
                url=str(web)+str(videoTitle)+"/"
                videoTitle=videoTitle.replace('.xml','').replace('_',' ')
##                print "gidecek url",url
                tools.addDir(videoTitle,url,"","smartx.main(url)")
    
    if files:
        first=re.compile('<p>(.*?)</p>').findall(link)
        first=base64.b64decode(first[0])
        second=re.compile('<li><a href=".*?">(.*?)</a>').findall(first)
        second=sorted(second, key=str.lower)
        for videoTitle in second:
            url=str(web)+str(videoTitle)
            videoTitle=videoTitle.replace('.xml','').replace('_',' ')
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
            thumbnail=channel('resim')[0].string
            tools.addDir(name,url,thumbnail,"smartx.get_part(name,url)")

def get_part(title,url):
    if xbmcPlayer.isPlaying():
            xbmcPlayer.stop()
            playList.clear()

    link=tools.get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    channels = soup('dizi')
    for channel in channels:
        name = channel('isim')[0].string
        if name == title:
            if xbmcPlayer.isPlaying():
                xbmcPlayer.stop()
            playList.clear()    
            items = channel.findAll("bilgi")
            for item in items:
                try:
                    videoTitle=item.server.string
                    videoTitle=videoTitle.replace('.xml','').replace('_',' ')
                    print "222",videoTitle

                except:
                    pass
                try:
                    url=cozucu.denetle(item.url.string)
                    url=url.replace('&amp','&')
                    print "333",url
                    
                except:
                    pass
                try:
                    thumbnail=item.thumbnail.string
                    
                except:
                    thumbnail="https://www.google.com.tr/logos/classicplus.png"
                listitem = xbmcgui.ListItem(videoTitle, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
                listitem.setInfo('video', {'videoTitle': videoTitle } )
                playList.add(url,listitem=listitem)
                tools.addLink(videoTitle,url,thumbnail,"")
            xbmcPlayer.play(playList)
        else:
            pass
               
        

