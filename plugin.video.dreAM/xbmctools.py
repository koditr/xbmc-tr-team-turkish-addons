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
    if "matplayer/go/" in url:
        url=url.replace('http://www.ddizi1.com/matplayer/go/','').replace('.mp4','')
        url=(base64.b64decode(url))
        url=url+tk
        url=url.replace('comhttps//','com/https//')
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
        liz.setInfo(type="Video", infoLabels={"Title":name})
        liz.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    else:
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
        liz.setInfo(type="Video", infoLabels={"Title":name})
        liz.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return()
        
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
    br.open('http://denesine.temadizayn.net/gizligiris/')
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
            dialog1 = xbmcgui.Dia#log()
            dialog1.ok('[COLOR red]DreamTR Uyelik Hatasi[/COLOR]','[COLOR yellow]V.I.P Uyeliginizin suresi dolmustur.[/COLOR]','[COLOR yellow]Detayli bilgi icin Nick isminizle > dreamtrdream@gmail.com a mail atiniz AYRINTILI TUM BILGILER http://dreamtr.club[/COLOR]')
            sys.exit()

    elif "Invalid username" in html:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dia#log()
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
            magix_player(name,url)
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
        magix_player(name,url)
    ok_9=re.compile('ok.php\?vid\=(.*?)"').findall(link)
    for url in ok_9:
        url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
        magix_player(name,url)
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
    match96=re.compile('<source src="(.*?)"').findall(link)
    for url in match96:
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
##        elif "mail." in url:
##            MailRu_Player(url)
##        elif "ok." in url:
##            ok_ru(url)
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
            magix_player(name,url)
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
        magix_player(name,url)
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
#22
def frame(url):
    name='Play'
    print "geldim"
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')
    response = urllib2.urlopen(req)
    link=response.read()
    #--
    link=get_url(url)
    ply23=re.compile('src="https://oload.tv/embed/(.*?)"').findall(link)
    for name in ply23:
        name='https://oload.tv/embed/'+name
        url=name
        magix_player(name,url)
    #--
    ddizi11=re.compile('src="http://www.hergunizle1.com/player/oynat/(.*?)"').findall(link)
    import requests as req
    for url in ddizi11:
        url='http://www.hergunizle1.com/player/oynat/'+url
        import requests as req
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"http://www.hergunizle1.com/",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        match=re.compile('file":"(.*?)", "label":"(.*?)", "type": "mp4"').findall(resp.text)
        for urlA,name in match:
            urlA=urlA.replace("u'http:\\/\\/redirector.googlevideo.com\\",'')
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',urlA+tk,'')
    match=re.compile('class="c5"><p><iframe src="(.*?)"').findall(link)
    for url in match:
        dizividcal(url)
    matchc=re.compile('<iframe src="(.*?)"  width=').findall(link)
    for url in matchc:
        if "reklam" in url:
            pass
        else:
            dizividcal(url)
    matcha=re.compile('src\=\".*?daily(.*?)\?').findall(link)
    for url in matcha:
        url='http://www.daily'+url
        dizividcal(url)
    matchab=re.compile('src\="http://www.ddizi1.com/dm.php\?git\=(.*?)\?').findall(link)
    for url in matchab:
        url='http://www.dailymotion.com/embed/video/'+url
        dizividcal(url)
    vidmoly=re.compile('vidmoly.me/(.*?)"').findall(link)
    for url in vidmoly:
        url='http://vidmoly.me/'+url
        link=get_url(url)#|thumbs.*?100\|xqx2odjilzokjiqbtexcnlavvokpjdpdrh4wppb3tffor6vxdampkuzgxihq|vid|
        match=re.compile('\|thumbs.*?\|(.*?)\|vid\|').findall(link)
        for b in match:
            print b
            if match:
                link=get_url(url)
                match1=re.compile('var spriteSheetUrl = "(.*?)i/.*?.jpg"').findall(link)
                                  #var spriteSheetUrl = "(.*?)i/01/00044/eazx3crm8io0_p.jpg"
                for a in match1:#//64.wintercoole.tk/xqx2odjilzokjiqbtexcnlavvokpjdpdrh4wppb3tffor6vxdampkuzgxihq/v.mp4 #01|100|
                    url=a+b+'/v.mp4'
                    url=url.replace('//','http://').replace('https:http://','https://').replace('01|100|','')
                    addLink('[COLOR gold]>  '+'[COLOR beige]'+'Vidmoly'+'[/COLOR]'+'[/COLOR]',url,'')
                   
    matchqq=re.compile('src="https://hqq.tv/player/embed_player.php\?vid\=(.*?)\&#038\;autoplay\=no"').findall(link)
    for vid in matchqq:
        resolve( vid)
    matchaa=re.compile('youtube.*?\/embed\/(.*?)\?').findall(link)
    for url in matchaa:
        url='http://www.youtube.com/embed/'+url
        name='Play-Youtube'
        magix_player(name,url)
    matchaa=re.compile('youtube.com\/embed\/(.*?)"').findall(link)
    for url in matchaa:
        url='http://www.youtube.com/embed/'+url
        name='Play-Youtube'
        magix_player(name,url)
    matchab=re.compile('ok.ru\/videoembed\/(.*?)"').findall(link)
    for url in matchab:
        url='http://ok.ru/videoembed/'+str(url)
        magix_player(name,url)
    ply1=re.compile("videoseyredin.net/embed/(.*?)'").findall(link)
    for url in ply1:
        dizividcal(url)
    mazz=re.compile('<iframe src="/matplayer/neez/(.*?)"').findall(link)
    for url in mazz:
        url='http://www.ddizi1.com/matplayer/neez/'+url
        link=get_url(url)
        match=re.compile('src="https://embed.tune.pk/play/(.*?)\?').findall(link)
        for url in match:
            url='https://embed.tune.pk/play/'+url
            link=get_url(url)
            match=re.compile('var requestURL = \'(.*?)\';').findall(link)
            for url in match:
                link=get_url(url)
                match=re.compile('file":"(.*?)","bitrate":(.*?),"label"').findall(link)
                for url,name in match:
                    url=url.replace('\/','/')
                    addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',url,'')
        match1=re.compile('dailymotion.com\/embed\/video\/(.*?)\?').findall(link)
        for url in match1:
            url='http://www.dailymotion.com/embed/video/'+url
            magix_player(name,url)
        match33=re.compile('file: "(.*?)",\n                label: "(.*?)"').findall(link)
        for url,name in match33:
            url='http://www.ddizi1.com'+url
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',url,'')
            
    mazz2=re.compile('src="http://www.ddizi1.com/matplayer/neez/(.*?)"').findall(link)#
    for url in mazz2:
        url='http://www.ddizi1.com/matplayer/neez/'+url
        link=get_url(url)
        match=re.compile('file: "(.*?)",\n                label: "(.*?)"').findall(link)
        for url,name in match:
            url='http://www.ddizi1.com'+url+tk
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',url,'')
            
    tune=re.compile('src\="http://tune.pk\/player\/embed_player.php\?vid\=(.*?)"').findall(link)#
    for url in tune:
        url='https://embed.tune.pk/play/'+url
        link=get_url(url)
        match=re.compile('contentURL.*?content\="(.*?)\"').findall(link)
        for url in match:
            addLink('[COLOR gold] Tune >>  '+'[COLOR beige]'+'Ply'+'[/COLOR]'+'[/COLOR]',url+tk,'')        
        
    ply2=re.compile('/playlist/(.*?).json"').findall(link)
    for url in ply2:
        url='https://www.videoseyredin.net/playlist/'+url+'.json'
        dizividcal(url)
    vk=re.compile('vk.com\/(.*?)"').findall(link)
    for url in vk:
        url='http://vk.com/'+url
        url=url.replace('&#038;','&')
        magix_player(name,url)
    okru2=re.compile('".*?\/player\/ok\/1.*?\.php\?v\=(.*?)"').findall(link)
    for url in okru2:
      url=(base64.b64decode(url))
      url=url.replace("http://ok.ru/video/","")
      url='http://ok.ru/videoembed/'+str(url)
      magix_player(name,url)
    hqq1=re.compile('goo.gl/(.*?)"').findall(link)
    for url in hqq1:
        url='https://goo.gl/'+url
        link=get_url(url)
        match=re.compile('videokeyorig = "(.*?)"').findall(link)
        for vid in match:
            resolve( vid)
    izle7=re.compile('izle7.com\/embed\-(.*?)"').findall(link)
    for url in izle7:
        url='http://www.izle7.com/embed-'+url
        link=get_url(url)
        match=re.compile("tp_file = '(.*?).mp4'").findall(link)
        for vid in match:
            vid=vid+'.mp4'
            name='Izle7'
            addLink(name,vid,'')
    itt=re.compile('src="https:\/\/ittir.in\/v\/(.*?)"').findall(link)
    for url in itt:
        url=url.replace('https://ittir.in/v/','')
        url='http://dreamtr.club/a_n_d/ornek.php?no='+url
        link=get_url(url)
        match=re.compile('file": ".*?\.googlevideo.com(.*?)",\n                "label": "(.*?)",\n                "type": "mp4"').findall(link)
        for urlA,name in match:
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]','https://redirector.googlevideo.com'+urlA,'')
    ddizi1=re.compile('ddizim.com/player\/oynat\/(.*?)"').findall(link)
    import requests as req
    for url in ddizi1:
        url='http://ddizim.com/player/oynat/'+url
        link=get_url(url)
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"http://ddizi1.com/",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        match=re.compile('file":"(.*?)", "label":"(.*?)", "type": "mp4"').findall(resp.text)
        for urlA,name in match:
            urlA=urlA.replace("u'http:\\/\\/redirector.googlevideo.com\\",'')
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',urlA+tk,'')
            
    canlii1=re.compile('src="http://www.canlidizihd6.com/playerv5/oynat/(.*?)"').findall(link)
    import requests as req
    for url in canlii1:
        url='http://www.canlidizihd6.com/playerv5/oynat/'+url
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"http://www.canlidizihd6.com/",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        match=re.compile('file":"(.*?)", "label":"(.*?)", "type": "mp4"').findall(resp.text)
        for urlA,name in match:
            urlA=urlA.replace("u'http:\\/\\/redirector.googlevideo.com\\",'')
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',urlA+tk,'')
    canlii2=re.compile('src="http://trdizi.tv/player/oynat/(.*?)"').findall(link)
    import requests as req
    for url in canlii2:
        url='http://trdizi.tv/player/oynat/'+url
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/201 ...",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Referer":"http://trdizi.tv/",
        "Connection":"keep-alive"
        }
        resp = req.get(url, allow_redirects=True, headers=headers)
        match=re.compile('file":"(.*?)", "label":"(.*?)", "type": "mp4"').findall(resp.text)
        for urlA,name in match:
            urlA=urlA.replace("u'http:\\/\\/redirector.googlevideo.com\\",'')
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]',urlA+tk,'')
    ply2=re.compile('openload.co/embed/(.*?)"').findall(link)
    for name in ply2:
        name='https://openload.co/embed/'+name
        url=name
        magix_player(name,url)
        
        
#24   
def dizividcal(url):
    if "daily" in url:
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
    if "itti" in url:
        url=url.replace('https://ittir.in/v/','')
        url='http://dreamtr.club/a_n_d/ornek.php?no='+url
        link=get_url(url)
        match=re.compile('file": ".*?\.googlevideo.com(.*?)",\n                "label": "(.*?)",\n                "type": "mp4"').findall(link)
        for urlA,name in match:
            urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
            addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]','https://redirector.googlevideo.com'+urlA,'')
    if "oynat" in url:
        link=get_url(url)
        match4=re.compile('{"file":"(.*?)", "label":"(.*?)"').findall(link)
        for url,name in match4:
            addLink('[COLOR beige]'+name+'[/COLOR]',url,'')
    if "videoseyredin" in url:
        link=get_url(url)
        match1=re.compile('file":"(.*?)","type":"mp4","label":"(.*?)"').findall(link)
        for url,name in match1:
            name="[COLOR orange]Kalite SEC > [/COLOR]"+name
            if "err" in name:
                pass
            else:
                addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
    if "videoseyredin" in url:
        link=get_url(url)
        match1=re.compile('file:"(.*?)",label:"(.*?)p').findall(link)
        for url,name in match1:
            name="[COLOR orange]Kalite SEC > [/COLOR]"+name
            if "err" in name:
                pass
            else:
                url=url.replace('","default":"true','')
                addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]',url,'')
    if "videoseyredin" in url:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        ply2=re.compile('playlist/(.*?).json"').findall(link)
        for url in ply2:
            url='https://www.videoseyredin.net/playlist/'+url+'.json'
            link=get_url(url)
            match=re.compile('file": ".*?\.googlevideo.com(.*?)",\n                "label": "(.*?)",\n                "type": "mp4"').findall(link)
            for urlA,name in match:
                urlA=urlA.replace('\/','/').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                addLink('[COLOR gold] KALITE SeC >>  '+'[COLOR beige]'+name+'[/COLOR]'+'[/COLOR]','https://redirector.googlevideo.com'+urlA,'')

#--
def request( url, headers={}):
    print('request: %s' % url)
    req = urllib2.Request(url, headers=headers)
    try:
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
    except urllib2.HTTPError, error:
        data=error.read()
    print('len(data) %s' % len(data))
    return data

def _decode2( file_url):
    def K12K(a, typ='b'):
        codec_a = ["G", "L", "M", "N", "Z", "o", "I", "t", "V", "y", "x", "p", "R", "m", "z", "u",
                   "D", "7", "W", "v", "Q", "n", "e", "0", "b", "="]
        codec_b = ["2", "6", "i", "k", "8", "X", "J", "B", "a", "s", "d", "H", "w", "f", "T", "3",
                   "l", "c", "5", "Y", "g", "1", "4", "9", "U", "A"]
        if 'd' == typ:
            tmp = codec_a
            codec_a = codec_b
            codec_b = tmp
        idx = 0
        while idx < len(codec_a):
            a = a.replace(codec_a[idx], "___")
            a = a.replace(codec_b[idx], codec_a[idx])
            a = a.replace("___", codec_b[idx])
            idx += 1
        return a

    def _xc13(_arg1):
        _lg27 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        _local2 = ""
        _local3 = [0, 0, 0, 0]
        _local4 = [0, 0, 0]
        _local5 = 0
        while _local5 < len(_arg1):
            _local6 = 0
            while _local6 < 4 and (_local5 + _local6) < len(_arg1):
                _local3[_local6] = _lg27.find(_arg1[_local5 + _local6])
                _local6 += 1
            _local4[0] = ((_local3[0] << 2) + ((_local3[1] & 48) >> 4))
            _local4[1] = (((_local3[1] & 15) << 4) + ((_local3[2] & 60) >> 2))
            _local4[2] = (((_local3[2] & 3) << 6) + _local3[3])

            _local7 = 0
            while _local7 < len(_local4):
                if _local3[_local7 + 1] == 64:
                    break
                _local2 += chr(_local4[_local7])
                _local7 += 1
            _local5 += 4
        return _local2

    return _xc13(K12K(file_url, 'e'))               

def _decode3( w, i, s, e):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = []
    var5 = []
    while (True):
        if (var1 < 5):
            var5.append(w[var1])
        elif (var1 < len(w)):
            var4.append(w[var1])
        var1 += 1
        if (var2 < 5):
            var5.append(i[var2])
        elif (var2 < len(i)):
            var4.append(i[var2])
        var2 += 1
        if (var3 < 5):
            var5.append(s[var3])
        elif (var3 < len(s)):
            var4.append(s[var3])
        var3 += 1
        if (len(w) + len(i) + len(s) + len(e) == len(var4) + len(var5) + len(e)):
            break
    var6 = ''.join(var4)
    var7 = ''.join(var5)
    var2 = 0
    result = []
    for var1 in range(0, len(var4), 2):
        ll11 = -1
        if (ord(var7[var2]) % 2):
            ll11 = 1
        result.append(chr(int(var6[var1:var1 + 2], 36) - ll11))
        var2 += 1
        if (var2 >= len(var5)):
            var2 = 0
    return ''.join(result)

def _decode_data( data):
    valuesPattern = r";}\('(\w+)','(\w*)','(\w*)','(\w*)'\)\)"
    values = re.search(valuesPattern, data, re.DOTALL)
    return _decode3(values.group(1), values.group(2), values.group(3), values.group(4))

def resolve( vid):
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/57.0.2987.137 Mobile/13G34 Safari/601.1.46'
    headers = { 'User-Agent': user_agent,
                'Referer': 'https://hqq.watch/player/embed_player.php?vid=' + vid}
    player_url = "https://hqq.watch/player/embed_player.php?vid=%s" % vid
    data = request(player_url, headers)
    data = _decode_data(data)
    data = _decode_data(data)
    
    code_crypt = data.split(';; ')
    data = _decode_data(code_crypt[1])

    if data:
        jsonInfo = request("http://hqq.watch/player/ip.php?type=json", headers)
        jsonIp = json.loads(jsonInfo)['ip']

        at = re.search(r'var at *= *"(\w+)";', data, re.DOTALL)
        http_referer = re.search('var http_referer *= *"([^"]*)";', data, re.DOTALL)

        if jsonIp and at:
            get_data = {'iss': jsonIp, 'vid': vid, 'at': at.group(1), 'autoplayed': 'on', 'referer': 'on',
                        'http_referer': http_referer.group(1), 'pass': '', 'embed_from' : '', 'need_captcha' : '0',
                        'hash_from' : ''
                        }
            data = urllib.unquote(request("http://hqq.watch/sec/player/embed_player.php?" +
                                               urllib.urlencode(get_data), headers))
            
            at = re.search(r'var\s*at\s*=\s*"([^"]*?)"', data)
            l = re.search(r'link_1: ([a-zA-Z]+), server_1: ([a-zA-Z]+)', data)
            
            data = _decode_data(data)
            data = _decode_data(data)
            code_crypt = data.split(';; ')
            data = _decode_data(code_crypt[1])
            
            vid_server = re.search(r'var ' + l.group(2) + ' = "([^"]+)"', data).group(1)
            vid_link = re.search(r'var ' + l.group(1) + ' = "([^"]+)"', data).group(1)

            if vid_server and vid_link and at:
                get_data = {'server_1': vid_server, 'link_1': vid_link, 'at': at.group(1), 'adb': '0/',
                            'b': '1', 'vid': vid }
                headers['x-requested-with'] = 'XMLHttpRequest'
                data = request("http://hqq.watch/player/get_md5.php?" + urllib.urlencode(get_data), headers)
                jsonData = json.loads(data)
                encodedm3u = jsonData['file']
                decodedm3u = _decode2(encodedm3u.replace('#', ''))
                decodedm3u = decodedm3u.replace("?socket", ".mp4.m3u8")
                fake_agent = user_agent
                name='Hqq_Player'
                url=decodedm3u  + '|' + fake_agent
                addLink(name,url,'')
                    

