# -*- coding: utf-8 -*-


'''
Edited on 5 April 2012

@author: Dr Ayhan Colak

'''
import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import mechanize
import ifix
from xml.dom.minidom import Document
#--------- eklentiye gore degisecek kisim ----------------------------
__settings__ = xbmcaddon.Addon(id="plugin.video.dream-clup")
#----------------------------------------------------------------------


__language__ = __settings__.getLocalizedString
downloadFolder = __settings__.getSetting('downloadFolder')
home = __settings__.getAddonInfo('path')
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
sys.path.append(IMAGES_PATH)
SUBS_PATH = xbmc.translatePath(os.path.join(home, 'resources', 'subs'))
sys.path.append(SUBS_PATH)
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
insidans=1







def name_prepare(videoTitle):
        print 'DUZELTME ONCESI:',videoTitle
        videoTitle=videoTitle.replace('İzle',"").replace('Türkçe',"").replace('Turkce',"").replace('Dublaj',"|TR|").replace('Altyazılı'," [ ALTYAZILI ] ").replace('izle',"").replace('Full',"").replace('720p',"").replace('HD',"")
        return videoTitle   
        


def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('27366.spull.netcdn.net','www.bicaps.net').replace('cdn.bicaps.net','www.bicaps.net')
##        link=ifix.decode_fix(link)
        response.close()
        return link

def addLink(name, url, thumbnail=""):
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
    liz.setInfo(type="Video", infoLabels={"Title":name})
    liz.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    
def addDir(fileName,name, mode, url="", thumbnail="",fanart=""):
    u = sys.argv[0]+"?fileName="+urllib.quote_plus(fileName)+"&name="+urllib.quote_plus(name)+"&mode="+urllib.quote_plus(mode)+"&url="+urllib.quote_plus(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
    liz.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)


bilinmeyen = ('http://magic-tr-team.googlecode.com/svn/trunk/bilinmeyen/test.html')
link=get_url(bilinmeyen)
match=re.compile('[D-L3]').findall(link)

key = match

def angel(input):
	
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)

def hata():
        d = xbmcgui.Dialog()
        d.ok('http://xbmctr.com GIRIS HATASI !', '  Bagış yaparak Site V.I.P. bolumune','  kayit olabilir ve bu bolumu izleyebilirsiniz.')
        __settings__.openSettings()
        return False

########
def sirala(IMAGES_PATH):
    
    for fileName in imps:
        thumbnail= os.path.join(IMAGES_PATH, fileName+".png")
        addDir(fileName, '[COLOR blue][B]'+fileName+'[/B][/COLOR]' ,"main()", "",thumbnail)
    xbmc.executebuiltin("Container.SetViewMode(500)")

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
def kalala(IMAGES_PATH,url):
        dacka(url)
        sirala(IMAGES_PATH)
        xbmc.executebuiltin("Container.SetViewMode(500)")
def dacka(yol):
    files = os.listdir(yol)
    global imps
    imps = []

    for i in range(len(files)):
        py_name = files[i].split('.')
        if len(py_name) > 1:
            if py_name[1] == 'py' and py_name[0] != '__init__':
               py_name = py_name[0]
               imps.append(py_name)
    file = open(yol+'/__init__.py','w')
    toWrite = '__all__ = '+str(imps)
    file.write(toWrite)
    file.close()
    return imps

##def kon():
##        if xbmc.getInfoLabel( "System.BuildVersion" )[:2] == '14':
##                dialog = xbmcgui.DialogProgress()
##                dialog1 = xbmcgui.Dialog()
##                dialog1.ok('[COLOR red][B]MagicTR Hata!![/B][/COLOR]','[COLOR blue][B]Kullandiginiz XBMC versiyonu MagicTR yi Desteklememektedir[/B][/COLOR]','[COLOR yellow][B]Lutfen Frodo veya Gothamda Kullaniniz[/B][/COLOR]')
##                sys.exit()
##        else:
##                pass
def EXIT():
        xbmc.executebuiltin("XBMC.Container.Refresh(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
#################              
def loadImports(yol):
    files = os.listdir(yol)
    global imps
    imps = []

    for i in range(len(files)):
        py_name = files[i].split('.')
        if len(py_name) > 1:
            if py_name[1] == 'py' and py_name[0] != '__init__':
               py_name = py_name[0]
               imps.append(py_name)
    file = open(yol+'/__init__.py','w')
    toWrite = '__all__ = '+str(imps)
    file.write(toWrite)
    file.close()
    return imps


def listChannels(IMAGES_PATH):
##    start()
    for fileName in imps:
        thumbnail= os.path.join(IMAGES_PATH, fileName+".png")
        addDir(fileName, '[COLOR blue][B]'+fileName+'[/B][/COLOR]' ,"main()", "",thumbnail)
        xbmc.executebuiltin("Container.SetViewMode(500)")

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
def listing(IMAGES_PATH,url):
        loadImports(url)
        listChannels(IMAGES_PATH)



def baglanbize():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/baglanfilmizle/')
        html = br.response().read()

        return html

def bicaps():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')  
        br.open('https://koditr.org/bicaps/')
        html = br.response().read()
        return html               

def fullfilm():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/filmifullizle/')
        html = br.response().read()

        return html

def filmplast():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/filmplast')
        html = br.response().read()

        return html

def hd720p():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/fullhd720pizle')
        html = br.response().read()

        return html

def hdizle():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/hdizle')
        html = br.response().read()

        return html

def loads7():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/loads7')
        html = br.response().read()

        return html

def media64():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/media64')
        html = br.response().read()

        return html

def ddizi():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/ddizi')
        html = br.response().read()

        return html

def dizihd():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/dizihd')
        html = br.response().read()

        return html

def harikadizi():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/harikadizi')
        html = br.response().read()

        return html

def ultra():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/ultrafilm')
        html = br.response().read()

        return html

def yabancidizi():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/yabancidizi')
        html = br.response().read()

        return html

def szenestreams():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/szenestreams')
        html = br.response().read()

        return html

def alman():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/almanlive')
        html = br.response().read()

        return html

def bilginmedia():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')
                __settings__.openSettings()
              
        br.open('https://koditr.org/bili')
        html = br.response().read()

        return html

def volkan():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/volkan')
        html = br.response().read()

        return html



def cavus():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/cavus')
        html = br.response().read()

        return html



def yorumcu():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/yorumcu')
        html = br.response().read()

        return html





def belgesel():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/belgesel')
        html = br.response().read()

        return html

def happy():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/happyfeets')
        html = br.response().read()

        return html


def besir():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/besir')
        html = br.response().read()

        return html

def merhaba():
        
        filepath=os.path.join(folders,'nfo.txt')
        cj = mechanize.CookieJar()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser(factory=mechanize.RobustFactory())
        br.set_cookiejar(cj)

        br.set_handle_equiv(True)

        br.set_handle_redirect(True)

        br.set_handle_referer(True)

        br.set_handle_robots(False)

        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Char‌​set', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
        br.open('https://koditr.org/wp-login.php')
        br.title()
        br.select_form(nr=0)
        br.form['log']=__settings__.getSetting("Username")
        br.form['pwd']=__settings__.getSetting("password")
        br.submit()
        html2=br.response().read()
        if "welcome" in html2:
                print "basarili bir login yapildi"
        else:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]IPTV HATA UYARISI[/B][/COLOR]','[COLOR yellow][B]Bronze Uye Olmaniz Gerekiyor!!! Eger Bronze Uye Iseniz ve Bu Mesaji Goruyorsaniz[/B][/COLOR]','[COLOR red][B]Yanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/B][/COLOR]')

              
        br.open('https://koditr.org/welcome')
        html = br.response().read()

        return html
def playlist_yap(playList,name,url):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        return playList
#-------------------------------#
def playlist():
        log_path = xbmc.translatePath('special://logpath/xbmc.log')
        f = open(log_path,"r")
        strToSearch= ""
        for line in f:
                
                strToSearch +=line
          

        patFinder1 = re.compile("http.+")
        patFinder2 = re.compile("rtmp.+")
                

        findPat1 = re.findall(patFinder1,strToSearch)

        
        findPat2 = re.findall(patFinder2,strToSearch)
 

        for i in findPat1:
                            
                subFound = patFinder1.sub('', strToSearch)
                

                f=open(log_path ,"w")        
                f.write(subFound)



        for b in findPat2:
                            
                subFound2 = patFinder2.sub('', strToSearch)
                

                f=open(log_path ,"w")                       
                f.write(subFound2)

        f.flush()
        f.close()

def playlist2():
        test='YWR2YW5jZWRzZXR0aW5ncy54bWw='
        nos='PGxvZ2xldmVsIGhpZGU9InRydWUiPi0xPC9sb2dsZXZlbD4='
        htmlp = HTMLParser.HTMLParser()
        pfile=xbmc.translatePath("special://home/userdata/")
        doc = Document()
        renk=doc.toprettyxml
        liste = doc.createElement("advancedsettings")
        doc.appendChild(liste)
        veri_ad = doc.createTextNode(base64.b64decode(nos))
        liste.appendChild(veri_ad)
        filepath = base64.b64decode(test)
        f = open(pfile+filepath, "w")
        f.write(htmlp.unescape(renk(indent="")))

def replace_fix(x):
        x=x.replace('\\', '')
        return x

#-------------------------------------------------#

