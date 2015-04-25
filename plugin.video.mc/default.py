# -*- coding: utf-8 -*-
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
'''
Created on 21 sempember 2012

@author: drascom
@version: 0.2.0

'''

import os,re,base64
import sys
import urllib,urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP


addon_id = 'plugin.video.mc'
__settings__ = xbmcaddon.Addon(id=addon_id)
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')

fanart = xbmc.translatePath( os.path.join( home, 'fanart.png' ) )
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
SUBS_PATH = xbmc.translatePath(os.path.join(home, 'resources', 'subs'))
sys.path.append(folders)
sys.path.append(IMAGES_PATH)
sys.path.append(SUBS_PATH)

import tools,forumtv,eTV,smartx,cozerim



def listele(name,url):
    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png")
    listitem.setInfo('video', {'name': name } )
    playList.add(url,listitem=listitem)
    return playList

##def check(Url,link):
##    folder=re.compile('<br>(.+?)</br>').findall(link)
##    xml=re.compile('<p>(.+?)</p>').findall(link)
##    try:#xml dosyalari bolumu
##        match=re.compile(u'<li><a href="(.*?)">').findall(base64.b64decode(xml[0]))
##        
##        for x in sorted(match):
##            if x =="radyo.xml":
##                name=x.replace(".xml","").replace("_"," ")
##                url=Url+"/"+x
##                thumbnail=name
##                tools.addDir(name,url,thumbnail,"radyo(name,url)","")
##            else:#yeniler kismini al temizle listele
##                name=x.replace("_dizihd","").replace("_fullfilm","").replace("_yabanci","").replace("_ddizi","").replace("_unutulmaz","").replace(".xml","").replace("_"," ")
##                url=Url+"/"+x
##                thumbnail=Url+'/'+str(x).replace(" ","_").replace(".xml","")+".jpg"
##                filepath=x.replace(".xml","").replace("_"," ")
##                tools.addvideo(name,url,thumbnail,"listing(name,url,filepath)",filepath)
##    except:
##        pass
##    xbmc.executebuiltin("Container.SetViewMode(50)")
##    try:#folder kismi bolumu
##        match=re.compile(u'<li><a href="./(.*?)">').findall(base64.b64decode(folder[0]))
##        print "folder bulundu"
##        for x in match:
##            name=x.replace("_"," ")
##            url=Url+'/'+str(x)
##            thumbnail=Url+'/'+str(x)+".jpg"
##            tools.addvideo(name,url,thumbnail,"main(url)","")
##            xbmc.executebuiltin("Container.SetViewMode(500)")
##    except:
##        pass
##    


webD='http://xbmctr.com/mc3/xml/Diziler/'    
webS='http://xbmctr.com/mc3/xml/Sinemalar/' 
turl="http://media5.yabancidiziizle1.com/live.mp4?ticket=X2VCRAneWdhrZIMJ3gxY"
##surl=cozerim.denetle(turl)[0]
##print surl
def mains(url):
##    tools.addLink('deneme',turl,"","")
    tools.addDir('Dizi Siteleri',"http://drascom.dyndns.org/xml/","Diziler","smartx.main(webD)")
    tools.addDir('Sinema Siteleri',"http://drascom.dyndns.org/xml/","Sinemalar","smartx.main(webS)")
    tools.addDir('Forum TV',"http://xbmctr.com/xml/","forumtv","forumtv.main()")
    url=base64.b64decode('aHR0cDovL3hibWN0ci5jb20vZVRWL3VzZXJmaWxlcy8=')
    tools.addDir('E-Televizyon',url,"forumtv","eTV.main()")    

 

def read(url):
    subtitle=''
    urlList=''
    namelist=[]
    videolist=[]
    link=tools.get_url(url)
    video=re.compile(u'<a id="video" class="tile wide text" href="(.*?)"><div class="text">(.*?)</div>').findall(link)
    noimg=re.compile(u'<a class="tile wide text" href="\./(.*?)"><div class="text">(.*?)</div>').findall(link)
    img=re.compile(u'<a class="tile wide imagetext wideimage" href="\./(.*?)"><img src="(.*?)" alt="(.*?)">').findall(link)
    if img:
        for url,thumbnail,name in img:
            url="http://178.211.38.42/boot/"+url
            tools.addvideo(name,url,thumbnail,"read(url)","")
    if noimg :
        for url,name in noimg:
            url="http://178.211.38.42/boot/"+url
            tools.addvideo(name,url,"","read(url)","")
    if video:
        for url,name in video:
            url=url.strip(' \t\n\r').replace("&amp;","&").replace("?rel=0","").replace(";=","=")
            urlList=urlList+url#add page to list
            urlList=urlList+':;'
            namelist.append(name)
            videolist.append(url)
            
           
          
        if xbmcPlayer.isPlaying():
            xbmcPlayer.stop()
        playList.clear()
        result=solver.denetle(urlList)
        if result:
            for server,url in result if not isinstance(result, basestring) else [result]:
                listele(name+" - "+server,url)
                tools.addLink(name+" - "+server,url,"",subtitle)
        else:
            for i in range(len(namelist)):
                listele(namelist[i],videolist[i])
                tools.addLink(namelist[i],videolist[i],"",subtitle)
            
        xbmcPlayer.play(playList)
    
        
def etv(isim,adres):
    link=tools.get_url(adres)
    xml=re.compile('<p>(.+?)</p>').findall(link)
    match=re.compile(u'<li><a href="(.*?)">').findall(base64.b64decode(xml[0]))
    for x in sorted(match):
        url=base64.b64decode('aHR0cDovL3hibWN0ci5jb20vZVRWL3VzZXJmaWxlcy8=')+str(x)
        name=x.replace(".xml","").replace("_"," ").upper()
        tools.addDir(name,url,name,"tvlist(name,url)")

def tvlist(name,url):
    filepath=tools.check_xml_status(name,url)
    oku = open(filepath, "r")
    soup = BeautifulStoneSoup(oku)
    item = soup.findAll("item")
    for i in range(len(item)):
        try:
            name=str(item[i].title.string)
        except:
            pass
        try:
            url=str(item[i].link.string)
        except:
            pass
        try:
            thumbnail=str(item[i].thumbnail.string)
        except:
            thumbnail=var+"dizi/xml/icon.png"
##        playList.add(videoTitle,url)
        tools.addLink(name,url,thumbnail,"")

##    try:
##        xbmcPlayer.setSubtitles(subtitle)
##    except:
##        pass
##    if not xbmcPlayer.isPlayingVideo():
##            d = xbmcgui.Dialog()
##            d.ok('Sunucu Hatası', 'Otomatik Calamadim..','Manuel Deneyiniz.')


def radyo(r):
    print r
    link=tools.get_url(r)
    soup = BeautifulStoneSoup(link)
    item = soup.findAll("item")
    for i in range(len(item)):
        try:
            name=str(item[i].title.string)
        except:
            pass
        try:
            url=str(item[i].link.string)
        except:
            pass
        try:
            thumbnail=str(item[i].thumbnail.string)
        except:
            thumbnail="http://178.211.38.42/dizi/xml/icon.png"
##        playList.add(videoTitle,url)
        tools.addLink(name,url,thumbnail,"")








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

    
##l_check=tools.inside()
##if l_check:
##        mode=None
##else:
##        tools.hata()
##        sys.exit()
        
params = get_params()


    
name = None
mode = None
url = None
thumbnail = None
filepath=None

#Try-catch blocks to see which parameters are available 
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass

try:
    mode = urllib.unquote_plus(params["mode"])
except:
    pass
try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    thumbnail = urllib.unquote_plus(params["thumbnail"])
except:
    pass
try:
    filepath = urllib.unquote_plus(params["filepath"])
except:
    pass

##print "Ad: "+str(name)
##print "Method: "+str(mode)
##print "Url: "+str(url)
##print "Resim: "+str(thumbnail)
##print "filepath:"+str(filepath)

if mode == None:
    mains(webD)
else:
    exec mode


xbmcplugin.endOfDirectory(int(sys.argv[1]))



