# -*- coding: iso8859-9 -*-
# # xbmctr MEDIA CENTER, is an XBMC add on that sorts and displays 
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
Edited on 5 April 2012

@author: Dr Ayhan Colak

'''
import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time,datetime
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

__settings__ = xbmcaddon.Addon(id="plugin.video.mc")
__language__ = __settings__.getLocalizedString
downloadFolder = __settings__.getSetting('downloadFolder')
home = __settings__.getAddonInfo('path')
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
sys.path.append(IMAGES_PATH)
SUBS_PATH = xbmc.translatePath(os.path.join(home, 'resources', 'subs'))
sys.path.append(SUBS_PATH)
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
xbmcPlayer = xbmc.Player()



def name_prepare(videoTitle):
        print 'DUZELTME ONCESI:',videoTitle
        videoTitle=videoTitle.replace('İzle',"").replace('Türkçe',"").replace('Turkce',"").replace('Dublaj',"|TR|").replace('Altyazılı'," [ ALTYAZILI ] ").replace('izle',"").replace('Full',"").replace('720p',"").replace('HD',"")
        return videoTitle   
        
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('\xFD',"i").replace('&#39;&#39;',"\"").replace('&#39;',"\'").replace('\xf6',"o").replace('&amp;',"&").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g")
        link=link.replace('\xc5\x9f',"s").replace('&#038;',"&").replace('&#8217;',"'").replace('\xc3\xbc',"u").replace('\xc3\x87',"C").replace('\xc4\xb1',"ı").replace('&#8211;',"-").replace('\xc3\xa7',"c").replace('\xc3\x96',"O").replace('\xc5\x9e',"S").replace('\xc3\xb6',"o").replace('\xc4\x9f',"g").replace('\xc4\xb0',"I").replace('\xe2\x80\x93',"-")
        response.close()
        return link

def addLink(name,url,iconimage,subtitle):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmcPlayer.setSubtitles(subtitle)
        return ok



def addDir(name,url,thumbnail,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(thumbnail)
        if thumbnail != "":
                thumbnail = os.path.join(IMAGES_PATH, thumbnail+".jpg")
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addvideo(name,url,thumbnail,mode,filepath):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(thumbnail)+"&filepath="+urllib.quote_plus(filepath)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def hata():
        d = xbmcgui.Dialog()
        d.ok('http://xbmctr.com GIRIS HATASI !', '  Bagış yaparak Site V.I.P. bolumune','  kayit olabilir ve bu bolumu izleyebilirsiniz.')
        __settings__.openSettings()
        return False

def inside():
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

        login= __settings__.getSetting("login")
        if not login:
                __settings__.openSettings()
        else:
                pass
        login= __settings__.getSetting("login")
        password= __settings__.getSetting("password")
        req = urllib2.Request("http://forum.xbmctr.com/member.php"); #Login Page
        req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")

        vals = {'action' : 'do_login','url' : 'http://forum.xbmctr.com/','username' : login,'password' : password,'Submit' : 'login'}
        data = urllib.urlencode(vals)
        try:
                opener.open(req,data).read() #Source of Login Page
        except:
                d = xbmcgui.Dialog()
                d.ok('http://xbmctr.com GIRIS HATASI !', '  BAGIS yaparak Site V.I.P. bolumune','  kayit olabilir ve bu bolumu izleyebilirsiniz.')
                exit()
        resp = opener.open('http://forum.xbmctr.com/manager/')
        data=resp.read()
        if "  V.I.P" in data:
                print "Succesfully Loged in."
                return True
        else:
                print 'Login Hata'
                return False              
def better_yop():
        def gen(h):
                for c in h:
                    n = ord(c)-1
                    if n == 96:
                        yield 'z'
                    elif 96<n<122:
                        yield chr(n)
                    else:
                        yield c
        s='bHR0dDpwLaE3OC4zMTEvMahvNDIw'
        s= ''.join(gen(s))
        print s
        return base64.b64decode(s)
        
        
def Download_tool():        
        if downloadFolder is '':
                d = xbmcgui.Dialog()
                d.ok('Download Error','You have not set the download folder.\n Please set the addon settings and try again.','','')
                __settings__.openSettings(sys.argv[ 0 ])
        else:
                if not os.path.exists(downloadFolder):
                        print 'Download Folder Doesnt exist. Trying to create it.'
                        os.makedirs(downloadFolder)

def Download_subtitle(videoTitle,url):
        filepath = xbmc.translatePath(os.path.join(SUBS_PATH, str(videoTitle)+'.srt'))
        def download(url, dest):
##                    dialog = xbmcgui.DialogProgress()
##                    dialog.create('Downloading Movie','From Source', filename)
                    urllib.urlretrieve(url, dest, lambda nb, bs, fs, url = url: _pbhook(nb, bs, fs, url,''))
                    print dest
        def _pbhook(numblocks, blocksize, filesize, url = None,dialog = None):
                    try:
                        
                        percent = min((numblocks * blocksize * 100) / filesize, 100)
##                        dialog.update(percent)
                    except:
                        percent = 100
##                        dialog.update(percent)
##                    if dialog.iscanceled():
##                                    dialog.close()
        download(url, filepath)
        iscanceled = True
        xbmc.executebuiltin('Notification("Subtitle","Downloaded")')
        return filepath

def Download_xml(filepath,url):
##        videoTitle=videoTitle.replace(" ","_")
##        filepath = xbmc.translatePath(os.path.join(SUBS_PATH, str(videoTitle)+'.xml'))
        def download(url, dest):
##                    dialog = xbmcgui.DialogProgress()
##                    dialog.create('Downloading Movie','From Source', filename)
                    urllib.urlretrieve(url, dest, lambda nb, bs, fs, url = url: _pbhook(nb, bs, fs, url,''))
        def _pbhook(numblocks, blocksize, filesize, url = None,dialog = None):
                    try:
                        
                        percent = min((numblocks * blocksize * 100) / filesize, 100)
##                        dialog.update(percent)
                    except:
                        percent = 100
##                        dialog.update(percent)
##                    if dialog.iscanceled():
##                                    dialog.close()
        download(url, filepath)
        iscanceled = True
        return filepath

def check_time(xml):
        status=''
        if "TV" in xml:
                status="ESKI"
        else:
                if datetime.datetime.now()-datetime.datetime.fromtimestamp(os.path.getmtime(xml))> datetime.timedelta(minutes=300):
                        status="ESKI"
                else:
                        status="GUNCEL"
        return status
def check_xml_status(name,url):
        name=name.replace(" ","_")
        filepath = xbmc.translatePath(os.path.join(SUBS_PATH, str(name)+'.xml'))
        Sonuc=check_empty_xml(filepath)
        if Sonuc == 'YOK':
                print 'XML YOK'
                filepath=Download_xml(filepath,url)
                print 'XML OLUSTURULDU'
        else:
                print 'XML BULUNDU'
                pass

        status=check_time(filepath)
        print "XML DOSYA DURUMU : " +str(status)
        if status == "ESKI":
                print "xml dosya = ESKI / YENIDEN TARANIYOR."
                filepath=Download_xml(filepath,url)
                print 'XML YENILENDI'
                return filepath
        
        elif status == "GUNCEL":
                print "VAROLAN XML OKUNUYOR:"
                return filepath
        else:
                print 'RECENT SONUC :xml degerlendirilemedi'
        
        return filepath


def check_empty_xml(xml):
        if os.path.isfile(xml):
                Sonuc='VAR'
        else:
                Sonuc='YOK'
       
        return Sonuc

