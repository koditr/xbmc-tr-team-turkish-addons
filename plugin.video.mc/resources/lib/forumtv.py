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


FILENAME = "forumtv"
web='http://xbmctr.com/xml/'
__language__ = addonsettings.getLocalizedString
home = addonsettings.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
import  tools  




def main():     
    link=tools.get_url(web)
    folders=re.compile('<br>(.*?)</br>').findall(link)
    for folder in folders:
        dosya=re.compile('<li><a href=".*?">\./(.*?)</a>').findall(base64.b64decode(folder))
        print 'dosya',dosya
        for videoTitle in dosya:
            url=str(web)+str(videoTitle)+"/"
            tools.addDir(videoTitle,url,"","forumtv.scan(url)")   
    
    try:
        scan(web)
    except:
        pass
        
    
def scan(Url):
    print 'gelen url',Url
    link=tools.get_url(Url)
    first=re.compile('<p>(.*?)</p>').findall(link)
    print first
    first=base64.b64decode(first[0])
    print first
    second=re.compile('<li><a href=".*?">(.*?)</a>').findall(first)
    print 'second',second
    for videoTitle in second:
        url=str(Url)+str(videoTitle)
        tools.addDir(videoTitle,url,"", "forumtv.getData(url)")

def getData(url):
    bolumList=[]
    link=tools.get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    if len(soup('channels')) > 0 :
        channels = soup('channel')
        for channel in channels:
            videoTitle = channel('name')[0].string
            bolumList.append(videoTitle)

        if xbmcPlayer.isPlaying():
                xbmcPlayer.stop()
        playList.clear()    
        
        dialog = xbmcgui.Dialog()
        ret = dialog.select(__language__(30008),bolumList)
        for i, name in enumerate(bolumList):
            if ret == i:
                channel = soup('channel',{'name':bolumList[i]})
                
                for bolum in channel:
                        items = bolum.findAll("item")
                        for item in items:
                            try:
                                videoTitle=item.title.string
                            except:
                                pass
                            try:
                                url=item.link.string
                                
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
                
            else:
                pass
    else:
        items = soup.findAll("item")
        for item in items:
            try:
                videoTitle=item.title.string
                
            except:
                pass
            try:
                url=item.link.string
                
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
    


##    item = soup.findAll("item")
##    for i in range(len(item)):
##        try:
##            videoTitle=item[i].title.string
##        except:
##            pass
##        try:
##            url=item[i].link.string
##        except:
##            pass
##        try:
##            thumbnail=item[i].thumbnail.string
##        except:
##            thumbnail="https://www.google.com.tr/logos/classicplus.png"
##        playList.add(videoTitle,url)
##        tools.addVideoLink(videoTitle,url,thumbnail)
    






##
##def getSoup(url):
##        print 'getSoup(): '+url
##        if url.startswith('http://'):
##            try:
##                req = urllib2.Request(url)
##                response = urllib2.urlopen(req)
##                data = response.read()
##                response.close()
##            except urllib2.URLError, e:
##                # errorStr = str(e.read())
##                if hasattr(e, 'code'):
##                    print 'We failed with error code - %s.' % e.code
##                    xbmc.executebuiltin("XBMC.Notification(error code - "+str(e.code)+",10000,"+icon+")")
##                elif hasattr(e, 'reason'):
##                    print 'We failed to reach a server.'
##                    print 'Reason: ', e.reason
##                    xbmc.executebuiltin("XBMC.Notification(failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")
##        else:
##            data = open(url, 'r').read()
##        soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
##        return soup
##
##
##def getData(url):
##        soup = getSoup(url)
##        getItems(soup('item'))
##
##
##def getSubChannelItems(name,url,fanart):
##        soup = getSoup(url)
##        channel_list = soup.find('subchannel', attrs={'name' : name})
##        items = channel_list('subitem')
##        getItems(items,fanart)
##
##
##def getItems(items):
##        for item in items:
##            try:
##                name = item('title')[0].string
##            except:
##                print '-----Name Error----'
##                name = ''
##            try:
##                if item('epg'):
##                    if item('epg')[0].string > 1:
##                        name += getepg(item('epg')[0].string)
##                else:
##                    pass
##            except:
##                print '----- EPG Error ----'
##
##            try:
##                if addonsettings.getSetting('mirror_link') == "true":
##                    try:
##                        url = item('link')[1].string	
##                    except:
##                        url = item('link')[0].string
##                if addonsettings.getSetting('mirror_link_low') == "true":
##                    try:
##                        url = item('link')[2].string	
##                    except:
##                        try:
##                            url = item('link')[1].string
##                        except:
##                            url = item('link')[0].string
##                else:
##                    url = item('link')[0].string
##            except:
##                print '---- URL Error Passing ----'+name
##                pass
##
##            try:
##                thumbnail = item('thumbnail')[0].string
##                if thumbnail == None:
##                    raise
##            except:
##                thumbnail = ''
##            try:    
##                if not item('fanart'):
##                    if addonsettings.getSetting('use_thumb') == "true":
##                        fanArt = thumbnail
##                    else:
##                        fanArt = fanart
##                else:
##                    fanArt = item('fanart')[0].string
##                if fanArt == None:
##                    raise
##            except:
##                fanArt = fanart
##            try:
##                desc = item('info')[0].string
##            except:
##                desc = ''
##
##            try:
##                genre = item('genre')[0].string
##            except:
##                genre = ''
##
##            try:
##                date = item('date')[0].string
##            except:
##                date = ''
##            try:
##                tools.addVideoLink(name.encode('utf-8', 'ignore'),url,thumbnail)
##            except:
##                print 'There was a problem adding link - '+name.encode('utf-8', 'ignore')
##                
##
##
##
