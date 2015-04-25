# -*- coding: utf-8 -*-




import urllib, urllib2, re, sys, cookielib
import xbmc, xbmcaddon, xbmcgui,xbmcplugin
import xbmctools1
import mechanize
import urlresolver
import time,os,base64
import simplejson as json
import buggalo
#
# Eklenti bildirimleri --------------------------------------------------------
addon_id = 'plugin.video.dream-clup'
__ayarlar__ = xbmcaddon.Addon(id=addon_id)
path = __ayarlar__.getAddonInfo('path')
IMAGES_PATH = xbmc.translatePath(os.path.join(path, 'resoures','image'))
addon_icon    = __ayarlar__.getAddonInfo('icon')
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1)"
downloadFolder = __ayarlar__.getSetting('download-folder')
insidans=1
#--cozuculer--#

t='http://www.tekparthd.org/?s='
    
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')
__language__ = __settings__.getLocalizedString

denemesite = 'https://koditr.org/denemebugalo/submit.php'
FILENAME = "cozuculer1"





xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
vk=[]
value=[]


def unique(l):
    s = set(); n = 0
    for x in l:
        if x not in s: s.add(x); l[n] = x; n += 1
    del l[n:]

def addDir(fileName,name, mode, url="", thumbnail=""):
    u = sys.argv[0]+"?fileName="+urllib.quote_plus(fileName)+"&name="+urllib.quote_plus(name)+"&mode="+urllib.quote_plus(mode)+"&url="+urllib.quote_plus(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

def magix_player(name,url):
    print url,'geldim'
    

    if "mail.ru" in url:
        MailRu_Player(url)
    if "ok.ru" in url:
        ok_ru(url)

            
    else:
        

        UrlResolverPlayer = url
        playList.clear()
        media = urlresolver.HostedMediaFile(UrlResolverPlayer)
        source = media
        if source:
                url = source.resolve()
                xbmctools1.addLink(name,url,'')
                xbmctools1.playlist_yap(playList,name,url)
                xbmcPlayer.play(playList)

def EXIT():
        xbmc.executebuiltin("XBMC.Container.Refresh(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")



###########################MAIL-RU-PLAYER######################################
def MailRu_Player(url):
    req = urllib2.Request(url)

    resp = urllib2.urlopen(req)
    html = resp.read()
    cookie_string = resp.headers.getheader('Set-Cookie').split(';')[0]

    print resp.headers.getheader('Set-Cookie')
    headers = {
        'Cookie': cookie_string
    }

    metadata_url_start = html.find('metadataUrl') + len('metadataUrl":"')
    metadata_url_end = html.find('"', metadata_url_start)
    metadata_url = html[metadata_url_start:metadata_url_end]

    metadata_response =  urllib2.urlopen(metadata_url)
    metadata = json.loads(metadata_response.read()) 

    #---------------------------------#
    xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
    streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
    for name,url in streams:
            xbmctools1.addLink('[COLOR lightblue][B]M_R >>  [/B][/COLOR]'+name,url,'')
    #---------------------------------#

USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
def ok_ru(url):



    fileName ="cozuculer1"


    sources = []

    if(re.search(r'ok.ru', url)):
        id = re.search('\d+', url).group(0)
        jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
        jsonSource = json.loads(http_req(jsonUrl))
        
        for source in jsonSource['videos']:
                name = '%s %s' % ('', source['name'])
                link = '%s|User-Agent=%s&Accept=%s&Referer=%s' % (source['url'], USER_AGENT, ACCEPT, urllib.quote_plus(url))
                url = link
                print url
                xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR blue]>>[/COLOR]'+name+'[/B][/COLOR]', "yeni4(name,url)",url,"")

def http_req(url, getCookie=False):

        
	req = urllib2.Request(url)
	req.add_header('User-Agent', USER_AGENT)
	req.add_header('Accept', ACCEPT)
	req.add_header('Cache-Control', 'no-transform')
	response = urllib2.urlopen(req)
	source = response.read()
	response.close()
	if getCookie:
		cookie = response.headers.get('Set-Cookie')
		return {'source': source, 'cookie': cookie}
	return source

def yeni4(name,url):

    xbmcPlayer = xbmc.Player() 
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
    playList.clear() 
    xbmctools1.addLink(name,url,'')
    listitem = xbmcgui.ListItem(name) 
    playList.add(url, listitem) 
    xbmcPlayer.play(playList)







