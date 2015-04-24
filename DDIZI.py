# -*- coding: utf-8 -*-
import urllib,urllib2,re,base64,os,sys
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import buggalo

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName="DDIZI"
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')

denemesite = 'http://koditr.org/denemebugalo/submit.php'


def main():
        buggalo.SUBMIT_URL = denemesite
        try:
                
        
                try:
                        html = xbmctools1.ddizi()
                        name=__settings__.getSetting("Name")
                        login=__settings__.getSetting("Username")
                        password=__settings__.getSetting("password")
                        match = re.compile('<!--#(.*?)-->').findall(html)
                        for web in match:
                                web=xbmctools1.angel(base64.b64decode(web))
                                tr=re.compile('<site>(.*?)</site>').findall(web)
                                for sinema in tr:
                                        xbmctools1.addDir(fileName,'[COLOR gold][B]>> [/B][/COLOR][COLOR beige][B]Yeniler[/B][/COLOR]','yeni(url)',sinema,"")
                                        div_list=["[COLOR blue][B]>>[/B][/COLOR][COLOR lightblue][B] Yerli Diziler[/B][/COLOR]","[COLOR brown][B]>>[/B][/COLOR][COLOR beige][B] Eski Diziler[/B][/COLOR]","[COLOR green][B]>>[/B][/COLOR][COLOR lightgreen][B] Tv Showlar[/B][/COLOR]","[COLOR red][B]>>[/B][/COLOR][COLOR pink][B] Yabanci Diziler[/B][/COLOR]"]
                                        for x in range(0,4):
                                                name=div_list[x]
                                                url=str(x)
                                                if "Eski" in name:
                                                        pass
                                                else:
                                                        if "Tv" in name:
                                                                pass
                                                        else:
                                                                if "Yab" in name:
                                                                        pass
                                                                else:
                                                                        xbmctools1.addDir(fileName,name,"panel(url)",url,"YOK")


                                
                except:
                        showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                        dialog = xbmcgui.DialogProgress()
                        dialog1 = xbmcgui.Dialog()
                        dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                        sys.exit()
                        
        except Exception:
                buggalo.onExceptionRaised()        


def yeni(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                
                link=xbmctools1.get_url(url)
                match=re.compile('<div class="dizi-box"><a href="(.*?)"><img src="(.*?)" width="120" height="90" alt="(.*?)"').findall(link)
                for url,thumbnail,name in match:
                        thumbnail='http://ddizi.tv'+thumbnail
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR]'+'[COLOR lightblue][B] '+name+'[/B][/COLOR]',"parts(url)",url,thumbnail,thumbnail)
                xbmc.executebuiltin("Container.SetViewMode(500)")
        except Exception:
                buggalo.onExceptionRaised()
def panel(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                        
                html = xbmctools1.ddizi()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!--#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools1.angel(base64.b64decode(web))
                        tr=re.compile('<site>(.*?)</site>').findall(web)
                        for sinema in tr:
                                link=xbmctools1.get_url(sinema)
                                soup=BS(link.decode('utf-8','ignore'))
                                div = soup.findAll("div",{"class":"blok-liste"})
                                for li in div[int(url)].findAll('li'):#-------------dizi anasayfalari bulur
                                        url= li.a['href']
                                        name = li.a.text
                                        name=name.encode("utf-8")
                                        xbmctools1.addDir(fileName,'[COLOR red][B]>>[/B][/COLOR][COLOR pink][B] '+name+'[/B][/COLOR]',"kategoriler(url)",url,"YOK")

        except Exception:
                buggalo.onExceptionRaised()
def kategoriler(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                
                data=xbmctools1.get_url(url)
                match=re.compile('<div class="dizi-box2"><a title="(.*?)" href="(.*?)"><img src="(.*?)"').findall(data)#-----dizi bolumleri bulur
                for name,url,thumbnail in match:
                        print url
                        

                        if not thumbnail:
                             thumbnail="yok"
                        else:
                                thumbnail='http://www.ddizi.tv'+thumbnail
                                
                                xbmctools1.addDir(fileName,'[COLOR green][B]>>[/B][/COLOR][COLOR lightgreen][B] '+name+'[/B][/COLOR]',"parts(url)",url,thumbnail)
                        
                veri=data.strip(' \t\n\r').replace(" ","")
                page=re.compile('class="active"><ahref=".*?">.*?</a></li>\r\n<li><ahref="(.*?)"').findall(veri)# ----- sonraki sayfa
                if page:
                        try:
                                url=page[0]
                                xbmctools1.addDir(fileName,'Sonraki Sayfa',kategoriler(url),url,"http://koditr.org/changelog/sonrakisayfa.png")
                        except:
                                pass

        except Exception:
                buggalo.onExceptionRaised()
def parts(url):
        buggalo.SUBMIT_URL = denemesite
        try:
                
                link=xbmctools1.get_url(url)
                match=re.compile('<a href="(.*?)" rel="nofollow">(.*?)</a></li>').findall(link)
                for url,name in match:
                        url='http://www.ddizi.tv'+url
                        xbmctools1.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR]'+'[COLOR lightblue][B] '+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')

        except Exception:
                buggalo.onExceptionRaised()
def VIDEOLINKS(name,url):
        buggalo.SUBMIT_URL = denemesite
        try:
                

                urlList=[]
                #---------------------------#
                playList.clear()
                link=xbmctools1.get_url(url)
                print url+'geldim'
                link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                        #---------------------------------------------#
                vk_2=re.compile('<iframe src="http://vk.com/(.*?)"').findall(link)
                for url in vk_2:
                        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                vk_1=re.compile(' src="https://vk.com/(.*?)"').findall(link)
                for url in vk_1:
                        url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                ok=re.compile('"odnvideo" data-id="(.*?)"').findall(link)
                for url in ok:
                        url = 'http://ok.ru/videoembed/'+url
                        print url
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                youtube=re.compile('encodeURIComponent\(\'(.*?)\'').findall(link)
                for url in youtube:
                        url=url.replace('http://www.youtube.com/watch?v=','')
                        url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                dm2=re.compile('http:\/\/www.dailymotion.com\/embed\/video\/(.*?)\?"').findall(link)
                                   #http://www.dailymotion.com/embed/video/x2er4g6?syndication=234148
                for url in dm2:
                        url = 'http://www.dailymotion.com/embed/video/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        ######################
                dm=re.compile('http:\/\/www.dailymotion.com\/embed\/video\/(.*?)"').findall(link)
                                   #http://www.dailymotion.com/embed/video/x2er4g6?syndication=234148
                for url in dm:
                        url = 'http://www.dailymotion.com/embed/video/'+str(url).encode('utf-8', 'ignore')
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
                mailru=re.compile('http:\/\/.*?\/mail\/(.*?).html').findall(link)
                for mailrugelen in mailru:
                        url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+str(mailrugelen)+'.html'
                        value=[]
                        value.append((name,cozuculer1.MailRu_Player(url)))
                        #---------------------------------------------#
                video=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                for videodgelen in video:
                        url =videogelen
                        cozuculer1.magix_player(name,url)
                        #---------------------------------------------#
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

        except Exception:
                buggalo.onExceptionRaised()     
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
