# -*- coding: utf-8 -*-
import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import mechanize
import fix
from xml.dom.minidom import Document
import requests,json
import re, json,math
import urlresolver

Request = urllib2.Request
urlopen = urllib2.urlopen
openloadhdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}           
UserAgent = 'Mozilla%2F5.0+%28Windows%3B+U%3B+Windows+NT+6.1%3B+en-US%29+AppleWebKit%2F532.0+%28KHTML%2C+like+Gecko%29+Chrome%2F3.0.195.38+Safari%2F532.0'

__settings__ = xbmcaddon.Addon(id="plugin.video.dreAM")
tk="|User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')"


web1='LDE4OQlrazgvaEooPT5VQS1WPj1kKyUnZScjLC0rYjlbNA=='
web2='LDE4OQlrazgvaEooPT5VQS1WPj1kKyUnZSwpOSkkImdDLDR3PCRUIhclVw56'
web4='LDE4OQlrazgvaEooPT5VQS1WPj1kKyUnZTsgKj0gPmdDLDR3Ly1SKSYpXw4='

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
z='http://www.paradisehill.tv'
f="http://www.tekparthd.org/"
sinem="aHR0cDovL2ZpbG1pemxlODAuY29tLw=="
xbmcPlayer = xbmc.Player()
xbmcPlayer.stop()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playList.clear()


def get_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    link=fix.decode_fix(link)
    response.close()
    return link

def addLink(name, url, thumbnail=""):
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
    liz.setInfo(type="Video", infoLabels={"Title":name})
    liz.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
def addDir(name,url,mode,iconimage,fanart):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
bilinmeyen = ('lmth.tset/neyemnilib/retsam/maet-rt-cigam/rtidok/moc.tnetnocresubuhtig.war//:ptth')[::-1]
link=get_url(bilinmeyen)
match=re.compile('[D-L3]').findall(link)

key = match

def angel(input):
    output = []
    for i in range(len(input)):
        xor_num = ord(input[i]) ^ ord(key[i % len(key)])
        output.append(chr(xor_num))
    return ''.join(output)
def EXIT():
    xbmc.executebuiltin("XBMC.Container.Refresh(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
def sifre100():
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
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')]
    br.open('http://denesine.com/gizligiris/')
    br.title()
    br.select_form(nr=0)
    br.form['log']=__settings__.getSetting("Username")
    br.form['pwd']=__settings__.getSetting("password")
    br.submit()
    html=br.response().read()
    if "VIPuye" in html:
            print "DREAMTR"
    elif "ucretsizuye" in html:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('[COLOR red]DreamTR Uyelik Hatasi[/COLOR]','[COLOR yellow]V.I.P Uyeliginizin suresi dolmustur.[/COLOR]','[COLOR yellow]Detayli bilgi icin Nick isminizle > dreamtrdream@gmail.com a mail atiniz AYRINTILI TUM BILGILER http://dreamtr.club[/COLOR]')
            sys.exit()

    elif "Invalid username" in html:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('[COLOR red]DreamTR Uyelik Hatasi[/COLOR]','[COLOR yellow]V.I.P Uye Olmaniz Gerekiyor!!![/COLOR]','[COLOR yellow]Eger V.I.P Uye Iseniz ve Bu Mesaji GoruyorsanizYanlis Kullanici adi veya Sifre Girdiniz!!! Lutfen Tekrar Deneyiniz.[/COLOR]')
            sys.exit()

    return html

def playlist_yap(playList,name,url):
    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
    listitem.setInfo('video', {'name': name } )
    playList.add(url,listitem=listitem)
    return playList

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

def get_urlmobile(url):
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

#----#
def url_get(url, headers={}, computer=None, params=None):
    pc_headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'en-US,en;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    mobile_headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'}

    if computer == 'PC':
        if headers:
            pc_headers.update(headers)
        response = requests.get(url, headers=pc_headers, params=params, verify=False)
    else:
        if headers:
            mobile_headers.update(headers)
        response = requests.get(url, headers=mobile_headers, params=params, verify=False)
    if response.status_code == 200:
        return response.content, response.cookies.get_dict()
    else:
        pass
#--#
USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
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
def MailRu_Player(url):
    import re, urllib2
    def _regex(url):
        m1 = re.search('http://.+?mail\.ru.+?<param.+?value=\"movieSrc=(?P<url>[^\"]+)', url, re.IGNORECASE | re.DOTALL)
        m2 = re.search('://video.+?\.mail\.ru\/(?P<url>.+?)\.html', url, re.IGNORECASE | re.DOTALL)
        return m1 or m2
    m = _regex(url)
    vurl = ''
    items = []
    if m:
        vurl = m.group('url')
        vurl = re.sub('\&[^$]*','',vurl)
        vurl = re.sub('/embed','',vurl)
        vurl = 'http://videoapi.my.mail.ru/' + vurl + '.json'
    else:
        resp, cookie = url_get(url)
        match = re.compile('"metadataUrl":"(.*?)",').findall(resp)
        if 'http' not in match[0]:
            vurl = 'http:' + match[0]
        else:
            vurl = match[0]

    if vurl:
        resp, cookie = url_get(vurl)
        vkey = cookie['video_key']
        item = json.loads(resp)
        for v in item[u'videos']:
            quality = v['key']
            if 'http' not in v['url'][0:4]:
                    link = 'http:' + v['url'] + '|Cookie=' + urllib2.quote('video_key=' + vkey)# + '|Referer=' + url
                    url=link 
            else:
                    link = v['url'] + '|Cookie=' + urllib2.quote('video_key=' + vkey)# + '|Referer=' + url
                    url=link
            name=quality
            addLink(name,url,'')
#--#
def ok_ru(url):
    USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
    ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    sources = []
    if(re.search(r'ok.ru', url)):
            id = re.search('\d+', url).group(0)
            jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
            url=jsonUrl
            req = urllib2.Request(url)
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36")
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            match=re.compile('"name":"(.*?)","url":"(.*?)"').findall(link)
            for name,url in match:
                    if "profile" in name:
                            pass
                    else:
                            url=url.replace('\\u0026','&')
                            addLink(name,url,'')

#--
def playerdenetle(name, urlList):
    value=[]
    for url in urlList if not isinstance(urlList, basestring) else [urlList]:
            if "mail.ru" in url:
                    magix_player(name,url) 
    if  value:
            return value
#--
def name_fix(x):        
    x=x.replace('-',' ').replace('_',' ')
    return x[0].capitalize() + x[1:]


























































































































































#--
#24   
def dizividcal(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        yt3=re.compile('dailymotion.com\/embed\/video\/(.*?)\?').findall(link)
        for url in yt3:
            url='http://www.dailymotion.com/embed/video/'+url
            if url:
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile('"video\\\/mp4","url"\:"(.*?)\/H264\-(.*?)\\\/video(.*?)"').findall(link)
                for a,name2,c in match:
                    urlA=a+"/H264-"+name2+"/video"+c
                    urlA=urlA.replace('\/','/')
                    addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name2+'[/COLOR]'+'[/COLOR]',urlA,'')

    except:
        pass
    try:
        link=get_url(url)
        mp444=re.compile('ittir.in/v/(.*?)" width').findall(link)
        for url in mp444:
            url='http://uguryalcin.one/Kodi/Test/ornek.php?no='+url
            link=get_url(url)
            match=re.compile('file": ".*?\.googlevideo.com(.*?)",\n                "label": "(.*?)",\n                "type": "mp4"').findall(link)
            for urlA,name in match:
                urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]','https://redirector.googlevideo.com'+urlA,'')
    except:
        pass
    try:
        link=get_url(url)
        mp44=re.compile('src="http://www.canlidizi.*?/playerv4/oynat/(.*?)"').findall(link)
        for url in mp44:
            url='http://www.canlidizihd5.net/playerv4/oynat/'+url
            link=get_url(url)
            match4=re.compile('{"file":"(.*?)", "label":"(.*?)"').findall(link)
            for url,name in match4:
                addLink('[COLOR beige]'+name+'[/COLOR]',url,'')
    except:
        pass
    try:
        link=get_url(url)
        ply1=re.compile("videoseyredin.net/embed/(.*?)'").findall(link)
        for name in ply1:
            name='https://www.videoseyredin.net/embed/'+name
            link=get_url(name)
            match1=re.compile('file":"(.*?)","type":"mp4","label":"(.*?)"').findall(link)
            for url,name in match1:
                name="[COLOR orange]Kalite SEC > [/COLOR]"+name
                if "err" in name:
                    pass
                else:
                    addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
    except:
        pass
    try:
        match2=re.compile('/playlist/(.*?).json"').findall(link)
        for url in match2:
            url='https://www.videoseyredin.net/playlist/'+url+'.json'
            link=get_url(url)
            match=re.compile('file": ".*?\.googlevideo.com(.*?)",\n                "label": "(.*?)",\n                "type": "mp4"').findall(link)
            for urlA,name in match:
                urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]','https://redirector.googlevideo.com'+urlA,'')
    except:
        pass
    try:
        cldy=re.compile('cloudy.ec\/embed.php\?id\=(.*?)"').findall(link)
        for url in cldy:
            url='https://www.cloudy.ec/embed.php?id='+url
            magix_player(name,url)
    except:
        pass
    try:
        okru=re.compile('<iframe src="(.*?)" width=\'550\' height=\'400\'').findall(link)
        for url in okru:
            link=get_url(url)
            match4=re.compile('"file":"(.*?)"').findall(link)
            for url in match4:
                url=url.replace('\&','&')
                addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                listitem.setInfo('video', {'name': name } )
                playList.add(url,listitem=listitem)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                time.sleep(3)
                pDialog.close()
                if (pDialog.iscanceled()):
                        return False
    except:
        pass
    try:
        link=get_url(url)
        vk=re.compile('vk.com\/(.*?)"').findall(link)
        for url in vk:
            url='http://vk.com/'+url
            url=url.replace('&#038;','&')
            magix_player(name,url)
    except:
        pass
    try:
        link=get_url(url)
        vk2=re.compile('http://can(.*?)" width="550"').findall(link)
        for url in vk2:
            url='http://can'+url
            link=get_url(url)
            kod=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
            for oid,vidid,has in kod:
              url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
              link=get_url(url)
              if "480" in link:
                  match4=re.compile('"url480":"(.*?)"').findall(link)
              elif "360" in link:
                  match4=re.compile('"url360":"(.*?)"').findall(link)
              elif "240" in link:
                  match4=re.compile('"url240":"(.*?)"').findall(link)
              else:
                print "video yok"
                for url in match4:
                    url=url.replace("\/","/")                                                       
                    addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
                    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                    listitem.setInfo('video', {'name': name } )
                    playList.add(url,listitem=listitem)
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                    note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                    pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                    time.sleep(3)
                    pDialog.close()
                    if (pDialog.iscanceled()):
                            return False
    except:
        pass
    try:

        link=get_url(url)
        m3u8=re.compile('file: "http://(.*?)"').findall(link)
        for url in m3u8:
            url='http://'+url                                                
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass
    try:
        link=get_url(url)       
        yt=re.compile("encodeURIComponent\(\'(.*?)\'").findall(link)
        for url in yt:
            url=url.replace('http://www.youtube.com/watch?v=','')
            url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(url)
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                return False
    except:
        pass
    try:
        link=get_url(url)
        mr=re.compile('value="movieSrc=(.*?)&amp;mp4=1&').findall(link)#
        for url in mr:
            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
            if streams >0:
                del streams[0]
                for name2,url2 in streams:   
                    addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                    listitem.setInfo('video', {'name': name } )
                    playList.add(url2,listitem=listitem)
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                    note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                    pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                    if (pDialog.iscanceled()):
                            return False
    except:
        pass
    try:
        link=get_url(url)
        yt2=re.compile('http:\/\/www.youtube.com\/embed\/(.*?)feature=player_detailpage"').findall(link)
        for url in yt2:
            url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
            url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass
    try:
        
        link=get_url(url)
        yt3=re.compile('youtube.*?\/embed\/(.*?)\?').findall(link)
        for url in yt3:
            url='http://www.youtube.com/embed/'+url
            magix_player(name,url)
    except:
        pass
    try:
        link=get_url(url)
        yt4=re.compile('http://www.youtube.com/embed/(.*?)showinfo=0"').findall(link)
        for url in yt4:
            url=url.replace('?','').replace('iv_load_policy=3','').replace('iv_load_policy=3&#038;','')
            url='plugin://plugin.video.youtube/play/?video_id='+str(url)
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass
    try:
        link=get_url(url)
        yt5=re.compile('\'file\': \'(.*?)\'').findall(link)
        for url in yt5:
            url='plugin://plugin.video.youtube/?action=play_video&videoid='+str(url)
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass
    try:
        link=get_url(url)
        mr2=re.compile("src='http://videoapi.my.mail.ru/videos/embed/(.*?).html'").findall(link)
        for url in mr2:
            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
            if streams >0:
                del streams[0]
                for name2,url2 in streams: 
                    addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                    listitem.setInfo('video', {'name': name } )
                    playList.add(url2,listitem=listitem)
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                    note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                    pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                    if (pDialog.iscanceled()):
                            return False
    except:
        pass
    try:
        link=get_url(url)
        mr3=re.compile("src='http://api.video.mail.ru/videos/embed/(.*?).html'").findall(link)
        for url in mr3:
            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
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
            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
            if streams >0:
                del streams[0]
                for name2,url2 in streams:  
                    addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url2,'')
                    listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                    listitem.setInfo('video', {'name': name } )
                    playList.add(url2,listitem=listitem)
                    loadedLinks = loadedLinks + 1
                    percent = (loadedLinks * 100)/totalLinks
                    remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                    note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
                    pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
                    if (pDialog.iscanceled()):
                            return False
    except:
        pass
    try:
        link=get_url(url)
        okru2=re.compile('".*?\/player\/ok\/1.*?\.php\?v\=(.*?)"').findall(link)
        for url in okru2:
          url=(base64.b64decode(url))
          url=url.replace("http://ok.ru/video/","")
          url='http://ok.ru/videoembed/'+str(url)
          ok_ru(url)
        link=get_url(url)  
        okru3=re.compile('ok.ru\/videoembed\/(.*?)"').findall(link)
        for url in okru3:
          url='http://ok.ru/videoembed/'+str(url)
          ok_ru(url)
        link=get_url(url)  
        m3u82=re.compile('file:"(.*?)\?",width:').findall(link)
        for url in m3u82:                                            
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass
    try:
        link=get_url(url)  
        vidag=re.compile('http://vid.ag/(.*?)"').findall(link)
        for url in vidag:
            url='http://vid.ag/'+url
            link=get_url(url)
            match4=re.compile('\|static\|\|.*?\|\|.*?\|.*?\|.*?\|.*?\|(.*?)\|html\|').findall(link)
            for url in match4:
                url='http://vid.ag/'+url+'.m3u8'
            addLink(name+' '+'[COLOR beige]'+name2+'[/COLOR]',url,'')
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
            loadedLinks = loadedLinks + 1
            percent = (loadedLinks * 100)/totalLinks
            remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+'=    '+'' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+''+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
            note='[COLOR pink]'+'http://dreamtr.club'+'[/COLOR]'+'      '+'[COLOR beige]'+'DreamTR Team'+'[/COLOR]'
            pDialog.update(percent,'[COLOR red]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/COLOR]',remaining_display,note)
            if (pDialog.iscanceled()):
                    return False
    except:
        pass

xbmcPlayer.play(playList)
#--
#41 
def VIDEOLINKS1(name,url):
    xbmcPlayer = xbmc.Player()
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    urlList=[]
    playList.clear()
    link=get_url(url)
    matchOK=re.compile('\/live\/(.*?)"').findall(link)
    for url in matchOK:
        url=url.replace('#038;','')
        url='http://embedlive.flexmmp.com/live/'+url
        link=get_url(url)
        match2=re.compile('src: "(.*?)"').findall(link)
        for url in match2:
            url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
            xbmcPlayer = xbmc.Player()
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            listitem = xbmcgui.ListItem(name)
            playList.add(url, listitem)
            xbmcPlayer.play(playList)
            exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
            if exec_version < 14.0:
                playlist()
            else:
                playlist2()
    ply=re.compile('\/player\/url\/(.*?)"').findall(link)
    for name in ply:
        name=base64.b64decode(name)
        reverseName=""
        for x in range(len(name)-1,-1,-1):
            reverseName+=name[x]
            reverseName=base64.b64decode(reverseName)
            reverseName=reverseName.replace('ok/','')
            url=reverseName
            url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
            ok_ru(url)
    ply1=re.compile("videoseyredin.net/embed/(.*?)'").findall(link)
    for name in ply1:
        name='https://www.videoseyredin.net/embed/'+name
        link=get_url(name)
        match1=re.compile('https:\/\/cdn2.videoseyredin.net\/(.*?).mp4').findall(link)
        for url in match1:
            url='https://cdn2.videoseyredin.net/'+url+'.mp4'
            name=url
            name=name.replace('https://cdn2.videoseyredin.net/','').replace('/',' ').replace('.mp4','')
            name="[COLOR orange]Kalite SEC > [/COLOR]"+name
            if "err" in name:
                pass
            else:
                addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
        
    ply2=re.compile('src\="https://openload.co/embed/(.*?)"').findall(link)
    for name in ply2:
        name='https://openload.co/embed/'+name
        url=name
        magix_player(name,url)
    mega2=re.compile('http:\/\/videomega.tv\/view.php\?ref\=(.*?)\&.*?').findall(link)
    for url in mega2:
        url='http://videomega.tv/view.php?ref='+url
        magix_player(name,url)
    cldy=re.compile('cloudy.ec\/embed.php\?id\=(.*?)"').findall(link)
    for url in cldy:
        url='https://www.cloudy.ec/embed.php?id='+url
        magix_player(name,url)
    cldy1=re.compile('cloudy.ec\/embed.php\?id\=(.*?)&').findall(link)
    for url in cldy1:
        url='https://www.cloudy.ec/embed.php?id='+url
        magix_player(name,url)
    vidag=re.compile('vid.ag\/embed\-(.*?)\.html"').findall(link)
    for url in vidag:
        url='http://vid.ag/embed-'+url+'.html'
        magix_player(name,url)
    mega=re.compile('\videomega.tv\/(.*?)\&amp;width.*?"').findall(link)
    for url in mega:
        url='http://videomega.tv/'+str(url).encode('utf-8', 'ignore')
        magix_player(name,url)
    opn=re.compile('src="https://openload.co/embed/(.*?)/"').findall(link)
    for url in opn:
        url='https://openload.co/embed/'+url+'/'
        magix_player(name,url)
    mlr=re.compile('\/videos\/embed\/mail\/(.*?)\.html').findall(link)
    for url in mlr:
        url='http://videoapi.my.mail.ru/videos/embed/mail/'+url+'.html'
        magix_player(name,url)
    link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
    ok=re.compile('ok.ru\/videoembed\/(.*?)"').findall(link)
    for url in ok:
        url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
        ok_ru(url)
    ok_9=re.compile('ok.php\?vid\=(.*?)"').findall(link)
    for url in ok_9:
        url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
        ok_ru(url)
    vk_2=re.compile('vk.com\/(.*?)"').findall(link)
    for url in vk_2:
        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
        magix_player(name,url)
    vk_3=re.compile('rc="http://snnyk.com/(.*?)"').findall(link)
    for url1 in vk_3:
        url1=url1.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
        url1 = 'http://snnyk.com/'+str(url1).encode('utf-8', 'ignore')
        link=get_url(url1)
        vkvk=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
        for oid,vidid,has in vkvk:
            url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
            magix_player(name,url)
    youtube=re.compile('\youtube\.com\/embed\/(.*?)\"').findall(link)
    for url in youtube:
        url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
        magix_player(name,url)
    mailru2=re.compile('\/\/videoapi.my.mail.ru\/videos\/embed\/mail\/(.*?).html').findall(link)
    for mailrugelen in mailru2:
        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
        magix_player(name,url)
    mailru3=re.compile('http://api.video.mail.ru/videos/embed/mail/(.*?).html').findall(link)
    for mailrugelen in mailru3:
        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
        magix_player(name,url)
    dm=re.compile('www.dailymotion.com/embed/video/(.*?)\?').findall(link)
    for url in dm:
        url = 'http://www.dailymotion.com/embed/video/'+url
        magix_player(name,url)
    if not urlList:
        match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
        if match:
            for url in match:
                VIDEOLINKS1(name,url)
    if urlList:
        Sonuc=playerdenetle(name, urlList)
        for name,url in Sonuc:
            listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
            listitem.setInfo('video', {'name': name } )
            playList.add(url,listitem=listitem)
        xbmcPlayer.play(playList)
#--
#107
def radyocal(url):
    name=''
    link=get_url(url)
    match93=re.compile('"http\:\/\/(.*?)\.m3u8(.*?)"').findall(link)
    for a,b in match93:
        url='http://'+a+'.m3u8'+b+tk
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
        listitem = xbmcgui.ListItem(name)
        playList.add(url, listitem)
        xbmcPlayer.play(playList)
        exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
        if exec_version < 14.0:
            playlist()
        else:
            playlist2()
    match94=re.compile('style\="width.*?" src\="(.*?)">').findall(link)
    for url in match94:
        if ".gif" in url:
            pass
        else:
            xbmcPlayer = xbmc.Player()
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            addLink('[COLOR blue]'+'RETURN List <<'+' [/COLOR]','','http://png-4.findicons.com/files/icons/1714/dropline_neu/128/edit_undo.png')
            listitem = xbmcgui.ListItem(name)
            playList.add(url, listitem)
            xbmcPlayer.play(playList)
            exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
            if exec_version < 14.0:
                    playlist()
            else:
                    playlist2()
    match95=re.compile('file: \'(.*?)\',\n\t\t\t\twidth').findall(link)
    for url in match95:
        yenical4(name,url)
#--
#42
def yenical4(name,url):
    xbmcPlayer = xbmc.Player() 
    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) 
    playList.clear() 
    addLink(name,url,'')
    listitem = xbmcgui.ListItem(name) 
    playList.add(url, listitem) 
    xbmcPlayer.play(playList)
#--
#99
def magix_player(name,url):
        if "www.dailymotion.com" in url:
            fix.daily_sec(name,url)
        elif "mail." in url:
            MailRu_Player(url)
        elif "ok." in url:
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
#--
#29
def ayrisdirm1(url):
    link=get_url(url)
    try:
        ply=re.compile('\/pusuk\/url\/(.*?)"').findall(link)
        for name in ply:
            name=name.replace('?mode=flash','')
            name=base64.b64decode(name)
            reverseName=""
            for x in range(len(name)-1,-1,-1):
                    reverseName+=name[x]
            reverseName=base64.b64decode(reverseName)
            reverseName=reverseName.replace('ok/','')
            url=reverseName
            url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
            ok_ru(url)
        ply1=re.compile('\/pusuk\/url\/(.*?)=').findall(link)
        for name in ply1:
            name=name+'='
            name=base64.b64decode(name)
            reverseName=""
            for x in range(len(name)-1,-1,-1):
                    reverseName+=name[x]
            reverseName=base64.b64decode(reverseName)
            url=reverseName
            url=url.replace('/mail','')
            url = 'http://videoapi.my.mail.ru/videos/embed/'+url+'.html'
            magix_player(name,url)
    except:
        pass
    
    req = urllib2.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    hqq=re.compile('src="https://hqq.tv/(.*?)"').findall(link)
    for url in hqq:
        url = 'https://hqq.tv/'+url
        url=url.replace('#038;','')
        hqq(url)
    ply10=re.compile('src="http:\/\/www.ultrafilmizle.com\/player\/url\/(.*?)"').findall(link)
    for name in ply10:
        name=base64.b64decode(name)
        reverseName=""
        for x in range(len(name)-1,-1,-1):
                reverseName+=name[x]
        reverseName=base64.b64decode(reverseName)
        reverseName=reverseName.replace('ok/','')
        url=reverseName
        value=[]
        url = 'http://ok.ru/videoembed/'+str(url)
        magix_player(name,url)
    ytt=re.compile('TEK PLUS--><br />\n<iframe width=".*?" height=".*?" src="(.*?)"').findall(link)
    for url in ytt:
        link=get_url(url)
        match=re.compile('file":"(.*?)"').findall(link)
        name='TEK PLUS Sec'
        for url in match:
            addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
    yt=re.compile('youtube.com/embed/(.*?)"').findall(link)
    for code in yt:
        url = 'http://www.youtube.com/embed/'+code
        name='Fragman'
        magix_player(name,url)
    ok2=re.compile('ok.ru\/videoembed\/(.*?)"').findall(link)
    for code in ok2:
        url = 'http://ok.ru/videoembed/'+str(code)
        name='OK RU  '
        ok_ru(url)
    vk_2=re.compile('video_ext.php\?oid\=(.*?)"').findall(link) 
    for code in vk_2:
        url = 'http://vk.com/video_ext.php?oid='+str(code)
        url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
        name='Vk - Play'
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,1030,'',"")
    mailru2=re.compile('videos\/embed\/mail\/(.*?).html').findall(link)
    for code in mailru2:
        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(code)+'.html'
        name='mail RU  '
        addDir('[COLOR blue]'+name+'[/COLOR]',url,99,"","")
    mailru22=re.compile('https://my.mail.ru/(.*?)\' width=').findall(link)
    for url in mailru22:
        url = 'https://my.mail.ru/'+url
        link=get_url(url)
        match=re.compile('movieSrc":"mail/(.*?)","metadataUrl').findall(link)
        for url in match:
            url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(url)+'.html'
            name='mail RU  '
            magix_player(name,url)
    upto=re.compile('src="http://uptostream.com/iframe/(.*?)"').findall(link)
    for url in upto:
        url = 'http://uptostream.com/iframe/'+url
        name='play'
        magix_player(name,url)
    vidag=re.compile('http://vid.ag/(.*?)"').findall(link) 
    for url in vidag: 
        url = 'http://vid.ag/'+str(url).encode('utf-8', 'ignore')
        name='Play'
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    dd=re.compile('src="http://videomega.tv/view.php\?ref\=(.*?)\&width').findall(link) 
    for url in dd: 
        url = 'http://videomega.tv/view.php?ref='+str(url).encode('utf-8', 'ignore')
        name='Play'
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    ddo=re.compile('src="https://openload.co/embed/(.*?)"').findall(link) 
    for url in ddo: 
        url = 'https://openload.co/embed/'+str(url).encode('utf-8', 'ignore')
        name='Play'
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,99,"",'')
    vk_9=re.compile('video_ext.php\?oid\=(.*?)"').findall(link) 
    for url in vk_9: 
        url = 'http://vk.com/video_ext.php?oid='+str(url).encode('utf-8', 'ignore')
        name='Play'
        url=url.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/') 
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,1030,"",'')

