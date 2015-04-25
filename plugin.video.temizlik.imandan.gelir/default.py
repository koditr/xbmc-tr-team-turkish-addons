import urllib,urllib2,re,xbmcplugin,xbmcgui

#!/usr/bin/python
# -*- coding: utf-8 -*-


XbmcTRteam='http://XbcmTR.com'

def CATEGORIES():
        addDir('[COLOR red][B]>>  INFOYU OKUYUNUZ  <<[/B][/COLOR] ', "INFO(name)",'7','http://koditr.org/changelog/nl.png')
        addDir('[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]PACKAGES TEMIZLIGI - 1 -[/B][/COLOR] ', "MAINDEL(name)",'1','http://koditr.org/changelog/nl.png')
        addDir('[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]CACHE TEMIZLIGI - 2 -[ Sadece PC ][/B][/COLOR] ', "MAINDEL2(name)",'2','http://koditr.org/changelog/nl.png')
        addDir('[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]! Apple TV & Android BOX Cache Temizligi ![/B][/COLOR] ', "MAINDEL3(name)",'11','http://koditr.org/changelog/nl.png')
        addDir('[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]!Tum CIHAZLAR icin DREAM Sifre Silinmesi Bilmiyorsaniz YAPMAYIN![/B][/COLOR] ', "MAINDEL4(name)",'12','http://koditr.org/changelog/nl.png')
        addDir('[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]!Tum CIHAZLAR icin MagicTR Sifre Silinmesi Bilmiyorsaniz YAPMAYIN![/B][/COLOR] ', "MAINDEL5(name)",'13','http://koditr.org/changelog/nl.png')

def MAINDEL(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('KodiTR Team UYARI', 'PACKAGES temizliginden Eminmisiniz ! ','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/addons/packages/', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    dialog = xbmcgui.Dialog(e)
                    i = dialog.ok('!!! Packages !!!', "[COLOR beige]Packages Temizliginiz Bitmistir[/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")
def MAINDEL2(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('KodiTR Team UYARI', 'CACHE temizliginden Eminmisiniz ! ','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/cache', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    dialog = xbmcgui.Dialog(e)
                    i = dialog.ok('Temizlendi Uyarisi !!!', "[COLOR beige]Temizliginiz basariyla bitmistir[/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")
def MAINDEL3(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('KodiTR Team UYARI', 'Apple TV & Android Box - CACHE temizliginden Eminmisiniz ! ','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/temp', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    dialog = xbmcgui.Dialog(e)
                    i = dialog.ok('Temizlendi Uyarisi !!!', "[COLOR beige]Temizliginiz basariyla bitmistir[/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")
def MAINDEL4(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('!!Dream Sifrenizi Silmek icin Eminmisiniz  !!', '! Dream Sifrelerinizi Silmek istediginizden Eminmisiniz !! ','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.dream-clup', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    dialog = xbmcgui.Dialog(e)
                    i = dialog.ok('!Dream Sifreniz Silindi!', "[COLOR beige]Dream Sifreler Silindi ![/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")


def MAINDEL5(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('!!MagicTR Sifrenizi Silmek icin Eminmisiniz  !!', '! MagicTR Sifrelerinizi Silmek istediginizden Eminmisiniz !! ','','','No', 'Yes')
        if ret:
            import os 
            folder = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.magicTR', ''))
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    dialog = xbmcgui.Dialog(e)
                    i = dialog.ok('!MagicTR Sifreniz Silindi!', "[COLOR beige]MagicTR Sifreler Silindi ![/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")




                        				
def INFO(url):
  try:
        CATEGORIES()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR beige]XBMC daha hizli ve sorunsuz kullanmaniz icindir.[/COLOR]","[COLOR yellow]Bu Islemleri SIK SIK YAPINIZ !![/COLOR]")
  except:

        pass 
                
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
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==1:
        print ""+url
        MAINDEL(name)

elif mode==2:
        print ""+url
        MAINDEL2(name)

elif mode==11:
        print ""+url
        MAINDEL3(name)
elif mode==12:
        print ""+url
        MAINDEL4(name)
elif mode==13:
        print ""+url
        MAINDEL5(name)

elif mode==7:
        print ""+url
        INFO(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
