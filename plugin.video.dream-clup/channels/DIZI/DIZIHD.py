# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName ="DIZIHD"
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

denemesite = 'https://koditr.org/denemebugalo/submit.php'


def main():
        buggalo.SUBMIT_URL = denemesite
        try:
                
                
                try:
                        html = xbmctools1.dizihd()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR yellow][B]>>[/B][/COLOR] [COLOR red][B]>> - Arama/Search -<< [/B][/COLOR]', "Arama()",sinema,"https://koditr.org/changelog/search.png",'special://home/addons/plugin.video.dream-clup/fanart.jpg' )
                                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Diziler [/B][/COLOR]', "Recent(url)",sinema,"",'special://home/addons/plugin.video.dream-clup/fanart.jpg')
                                        html = xbmctools1.dizihd()
                                        name=__settings__.getSetting("Name")
                                        login=__settings__.getSetting("Username")
                                        password=__settings__.getSetting("password")
                                        match = re.compile('<!--#(.*?)-->').findall(html)
                                        for web in match:
                                                web=xbmctools1.angel(base64.b64decode(web))
                                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim>').findall(web)
                                                for url,name in tr:
                                                        name=ifix.decode_fix(name)
                                                        xbmctools1.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Recent(url)",url,'','')

                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()
        except Exception:
                buggalo.onExceptionRaised()
renk_code=0
###################################################################                
def renkler(renk):
    global renk_code
    liste=['[COLOR aliceblue]', '[COLOR antiquewhite]', '[COLOR aqua]', '[COLOR aquamarine]', '[COLOR azure]', '[COLOR beige]', '[COLOR bisque]', '[COLOR black]', '[COLOR blanchedalmond]', '[COLOR blue]', '[COLOR blueviolet]', '[COLOR brown]', '[COLOR burlywood]', '[COLOR cadetblue]', '[COLOR chartreuse]', '[COLOR chocolate]', '[COLOR coral]', '[COLOR cornflowerblue]', '[COLOR cornsilk]', '[COLOR crimson]', '[COLOR cyan]', '[COLOR darkblue]', '[COLOR darkcyan]', '[COLOR darkgoldenrod]', '[COLOR darkgray]', '[COLOR darkgreen]', '[COLOR darkkhaki]', '[COLOR darkmagenta]', '[COLOR darkolivegreen]', '[COLOR darkorange]', '[COLOR darkorchid]', '[COLOR darkred]', '[COLOR darksalmon]', '[COLOR darkseagreen]', '[COLOR darkslateblue]', '[COLOR darkslategray]', '[COLOR darkturquoise]', '[COLOR darkviolet]', '[COLOR deeppink]', '[COLOR deepskyblue]', '[COLOR dimgray]', '[COLOR dodgerblue]', '[COLOR firebrick]', '[COLOR floralwhite]', '[COLOR forestgreen]', '[COLOR fuchsia]', '[COLOR gainsboro]', '[COLOR ghostwhite]', '[COLOR gold]', '[COLOR goldenrod]', '[COLOR gray]', '[COLOR green]', '[COLOR greenyellow]', '[COLOR honeydew]', '[COLOR hotpink]', '[COLOR indianred ]', '[COLOR indigo  ]', '[COLOR ivory]', '[COLOR khaki]', '[COLOR lavender]', '[COLOR lavenderblush]', '[COLOR lawngreen]', '[COLOR lemonchiffon]', '[COLOR lightblue]', '[COLOR lightcoral]', '[COLOR lightcyan]', '[COLOR lightgoldenrodyellow]', '[COLOR lightgrey]', '[COLOR lightgreen]', '[COLOR lightpink]', '[COLOR lightsalmon]', '[COLOR lightseagreen]', '[COLOR lightskyblue]', '[COLOR lightslategray]', '[COLOR lightsteelblue]', '[COLOR lightyellow]', '[COLOR lime]', '[COLOR limegreen]', '[COLOR linen]', '[COLOR magenta]', '[COLOR maroon]', '[COLOR mediumaquamarine]', '[COLOR mediumblue]', '[COLOR mediumorchid]', '[COLOR mediumpurple]', '[COLOR mediumseagreen]', '[COLOR mediumslateblue]', '[COLOR mediumspringgreen]', '[COLOR mediumturquoise]', '[COLOR mediumvioletred]', '[COLOR midnightblue]', '[COLOR mintcream]', '[COLOR mistyrose]', '[COLOR moccasin]', '[COLOR navajowhite]', '[COLOR navy]', '[COLOR none]', '[COLOR oldlace]', '[COLOR olive]', '[COLOR olivedrab]', '[COLOR orange]', '[COLOR orangered]', '[COLOR orchid]', '[COLOR palegoldenrod]', '[COLOR palegreen]', '[COLOR paleturquoise]', '[COLOR palevioletred]', '[COLOR papayawhip]', '[COLOR peachpuff]', '[COLOR peru]', '[COLOR pink]', '[COLOR plum]', '[COLOR powderblue]', '[COLOR purple]', '[COLOR red]', '[COLOR rosybrown]', '[COLOR royalblue]', '[COLOR saddlebrown]', '[COLOR salmon]', '[COLOR sandybrown]', '[COLOR seagreen]', '[COLOR seashell]', '[COLOR sienna]', '[COLOR silver]', '[COLOR skyblue]', '[COLOR slateblue]', '[COLOR slategray]', '[COLOR snow]', '[COLOR springgreen]', '[COLOR steelblue]', '[COLOR tan]', '[COLOR teal]', '[COLOR thistle]', '[COLOR tomato]', '[COLOR turquoise]', '[COLOR violet]', '[COLOR wheat]', '[COLOR white]', '[COLOR whitesmoke]', '[COLOR yellow]', '[COLOR yellowgreen]']
    renk=liste[int(renk_code)]
    renk_kode=renk_code+1
    return renk
                                                
######                       
def Arama():
        buggalo.SUBMIT_URL = denemesite
        try:
                
                html = xbmctools1.dizihd()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<site>(.*?)</site>').findall(web)
                        for sinema in tr:
                                keyboard = xbmc.Keyboard("", 'Search', False)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        
                                        query = keyboard.getText()
                                        query=query.replace(' ','+')
                                        url = (sinema+'/?s='+query+'&x=0&y=0')
                                        Recent(url)
                xbmctools1.addDir(fileName,'[COLOR yellow][B]YENI ARAMA YAP[/B][/COLOR]', "Arama()","","Arama")

        except Exception:
                buggalo.onExceptionRaised()
def Recent(url):

                
        link=xbmctools1.get_url(url)
        match=re.compile('<div class="tarih">(.*?)</div>\r\n\t\t\t\t\t\t<a href="(.*?)"><img src="(.*?)" ></a>\r\n\t\t\t\t\t\t<h2><a href=".*?">(.*?)</a></h2>').findall(link)
        for date,url,thumbnail,name in match:
            date=date_fix(date)
            name=name_fix(name)
            name=name+' [COLOR blue]'+date+'[/COLOR]'         
            xbmctools1.addDir(fileName,'[COLOR beige][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail,thumbnail)


        #sayfalama basladi
        page=re.compile('<span class="current">.+?</span><a href="(.+?)" title="(.+?)">').findall(link)
        thumbnail="special://home/addons/plugin.video.dream-clup/resources/images/sonrakisayfa.png"
        for url,name in page:
                name="Sonraki Sayfa"
                url=str(url)
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>>'+name+'[/B][/COLOR]',"Recent(url)",url,thumbnail)
        xbmc.executebuiltin("Container.SetViewMode(500)")

##def yerli(url):
##        link=xbmctools1.get_url(url)
##        soup = BeautifulSoup(link)
##        panel=soup.find("div", {"id": "panel-1"})
##        for a in panel.findAll('a',href=True,title=True):
##                url=a['href']
##                name1=re.findall(r".*?dizihdtv.net/dizi-izle/(.*?)$", url)
##                name1=name1[0].replace('-izle',"").replace('-'," ")
##                thumbnail="http://dizihdtv.net/img/"+name1.replace(" ","")+".png"
##                # name=name.capitalize()
##                name = a.find(text=True)
##                xbmctools1.addDir(fileName,'[COLOR lightgreen][B]'+name.encode('utf-8')+'[/B][/COLOR]',"sezon(url)",url,thumbnail)
##
##        
##
##def yabanci(url):
##        link=xbmctools1.get_url(url)
##        soup = BeautifulSoup(link)
##        panel=soup.find("div", {"id": "panel-2"})
##        for a in panel.findAll('a',href=True,title=True):
##                url=a['href']
##                name=re.findall(r".*?dizihdtv.net/dizi-izle/(.*?)$", url)
##                name=name[0].replace('-izle',"").replace('-'," ")
##                thumbnail="http://dizihdtv.net/img/"+name.replace(" ","")+".png"
##                name=name.capitalize()
##                xbmctools1.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"sezonn(url)",url,thumbnail)
##
##def sezon(url):
##        link=xbmctools1.get_url(url)
##        match=re.compile('<div class="diziadi"></div>\r\n                                                <div class=".*?">.*?</div>\r\n\t\t\t\t\t\t<a href="(.*?)"><img src="(.*?)" ></a>\r\n\t\t\t\t\t\t<h2><a href=".*?">(.*?)</a>').findall(link)
##        for url,thumbnail,name in match:
##            #name1=re.findall(r".*?dizihdtv.net/(.*?)$", url)
##            name=name.replace('&#038;','')
##            xbmctools1.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')
##        page=re.compile('<span class="current">.+?</span><a href="http://dizihdtv.net/(.+?)" title="(.+?)">').findall(link)
##        thumbnail="image/sonrakisayfa.jpg"
##        for url,name in page:
##                name="Sonraki Sayfa"
##                url="http://dizihdtv.net/"+str(url)
##                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>>'+name+'[/B][/COLOR]',"sezon(url)",url,thumbnail)
##
##def sezonn(url):
##        link=xbmctools1.get_url(url)
##        match=re.compile('<div class="diziadi"></div>\r\n                                                <div class=".*?">.*?</div>\r\n\t\t\t\t\t\t<a href="(.*?)"><img src="(.*?)" ></a>\r\n\t\t\t\t\t\t<h2><a href=".*?">(.*?)</a>').findall(link)
##        for url,thumbnail,name in match:
##            #name1=re.findall(r".*?dizihdtv.net/(.*?)$", url)
##            xbmctools1.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')
##        page=re.compile('<span class="current">.+?</span><a href="http://dizihdtv.net/(.+?)" title="(.+?)">').findall(link)
##        thumbnail="image/sonrakisayfa.jpg"
##        for url,name in page:
##                name="Sonraki Sayfa"
##                url="http://dizihdtv.net/"+str(url)
##                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>>'+name+'[/B][/COLOR]',"sezonn(url)",url,thumbnail)
##    

def VIDEOLINKS(name,url):        
        #---------------------------#
        urlList=[]
        #---------------------------#
        playList.clear()
        link=xbmctools1.get_url(url)
        link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')

                #---------------------------------------------#
        vk_2=re.compile('\/vk.com\/(.*?)"').findall(link)
        for url in vk_2:
                url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                name='[COLOR beige][B][COLOR orange]>>>   [/COLOR] V Server [/B][/COLOR]'
                cozuculer1.magix_player(name,url)
                #---------------------------------------------#
        ok=re.compile('http:\/\/ok.ru\/videoembed\/(.*?)" ').findall(link)
        for mailrugelen in ok:
            
            url = 'http://ok.ru/videoembed/'+str(mailrugelen)
            xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> OK.RU > '+name+'[/B][/COLOR]',"cozuculer1.ok_ru(url)",url,'')
        youtube=re.compile('www.youtube.com/embed/(.*?)"').findall(link)
        for url in youtube:
                url=url.replace('?showinfo=0','')
                url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> Y Server  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'')

##                #---------------------------------------------#
        mailru=re.compile("_myvideo/(.*?)'").findall(link)
        for mailrugelen in mailru:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/bi.siktir1/_myvideo/'+str(mailrugelen)+'.html'
                xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> Mail Ru  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'') 
        dm=re.compile(' src="//www.dailymotion.com/embed/video/(.*?)" ').findall(link)
        if "x2fy4px" in dm:
            pass
        else:
            if "x2fy4pe" in dm:
                pass
            else:
                if "x2fy4q9" in dm:
                    pass
                else:
                    
                    for url in dm:            
                           
                        url = 'http://www.dailymotion.com/embed/video/'+str(url).encode('utf-8', 'ignore')
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>>>>> DM Server  > '+name+'[/B][/COLOR]',"cozuculer1.magix_player(name,url)",url,'')
        if not urlList:
                match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                print match
                if match:
                        for url in match:
                                VIDEOLINKS(name,url)
       
        if urlList:
                Sonuc=playerdenetle(name, urlList)
                for name,url in Sonuc:
                        xbmctools1.addLink(name,url,'')
                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                        listitem.setInfo('video', {'name': name } )
                        playList.add(url,listitem=listitem)
                xbmcPlayer.play(playList)

     
def playerdenetle(name, urlList):
        value=[]
        import cozuculer1
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:


                if "mail.ru" in url:
                    value.append((name,cozuculer1.MailRu_Player(url)))
                    
        if  value:
            return value

def showMessage(heading='DreamClup', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )

def date_fix(x):        
        x=x.replace('January', 'Ocak').replace('February', 'Subat').replace('March', 'Mart').replace('April', 'Nisan').replace('May', 'Mayis').replace('June', 'Haziran').replace('July', 'Temmuz').replace('August', 'Agustos').replace('September', 'Eylul').replace('October', 'Ekim').replace('November', 'Kasim').replace('December', 'Aralik')
        return x

def name_fix(x):        
        x=x.replace('&#038;', '-')
        return x
