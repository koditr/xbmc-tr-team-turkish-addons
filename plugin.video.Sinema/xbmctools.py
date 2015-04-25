# -*- coding: iso8859-9 -*-




import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver,json
#--------- eklentiye gore degisecek kisim ----------------------------
__settings__ = xbmcaddon.Addon(id="plugin.video.Sinema")
#----------------------------------------------------------------------
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)



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

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok



def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def magix_player(name,url):
    

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
                    addLink(name,url,'')
                    playlist_yap(playList,name,url)
                    xbmcPlayer.play(playList)
                    
def playlist_yap(playList,name,url):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        return playList
    #---------------------------------#
USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

def ok_ru(url):


        sources = []

        if(re.search(r'ok.ru', url)):
            
               # try:
            id = re.search('\d+', url).group(0)
            jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
            jsonSource = json.loads(http_req(jsonUrl))
            
            for source in jsonSource['videos']:
                    name = '%s %s' % ('', source['name'])
                    link = '%s|User-Agent=%s&Accept=%s&Referer=%s' % (source['url'], USER_AGENT, ACCEPT, urllib.quote_plus(url))
                    #item = {'name': name, 'url': link}
                    #sources.append(item)
                    url = link
                    addLink('[COLOR lightblue][B]>>  [/B][/COLOR]'+name,url,'')
               # except: pass
        #return sources

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
        addLink(name,url,'')
        listitem = xbmcgui.ListItem(name) 
        playList.add(url, listitem) 
        xbmcPlayer.play(playList)
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
            addLink('[COLOR lightblue][B]M_R >>  [/B][/COLOR]'+name,url,'')
    #---------------------------------#



