# -*- coding: utf-8 -*-
import urllib,urllib2,re,base64,os,sys,time
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS


#------------------eklenecek kısım------------------
Addon = xbmcaddon.Addon('plugin.video.dream-clup')
fileName="zBAKIM"
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
import xbmctools1,cozuculer1,ifix

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

addon_icon    = __settings__.getAddonInfo('icon')





        
def main():

        xbmctools1.addDir(fileName,'[COLOR red][B]>>  INFOYU OKUYUNUZ  <<[/B][/COLOR] ', "INFO(name)",'','https://koditr.org/changelog/nl.png')
        xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]PACKAGES TEMIZLIGI - 1 -[/B][/COLOR] ', "MAINDEL(name)",'','https://koditr.org/changelog/nl.png')
        xbmctools1.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+ '[COLOR beige][B]CACHE TEMIZLIGI - 2 -[/B][/COLOR] ', "MAINDEL2(name)",'','https://koditr.org/changelog/nl.png')
        xbmctools1.addDir(fileName,'[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]! Apple TV & Android BOX Cache Temizligi ![/B][/COLOR] ', "MAINDEL3(name)",'','https://koditr.org/changelog/nl.png')
        xbmctools1.addDir(fileName,'[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]!Tum CIHAZLAR icin DREAM Sifre Silinmesi Bilmiyorsaniz YAPMAYIN![/B][/COLOR] ', "MAINDEL4(name)",'','https://koditr.org/changelog/nl.png')
        xbmctools1.addDir(fileName,'[COLOR yellow][B]>> [/B][/COLOR]'+ '[COLOR yellow][B]!Tum CIHAZLAR icin MagicTR Sifre Silinmesi Bilmiyorsaniz YAPMAYIN![/B][/COLOR] ', "MAINDEL5(name)",'','https://koditr.org/changelog/nl.png')
def MAINDEL(name):
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('Dream - Clup UYARI', 'PACKAGES temizliginden Eminmisiniz ! ','','','No', 'Yes')
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
        ret = dialog.yesno('Dream - Clup UYARI', 'CACHE temizliginden Eminmisiniz ! ','','','No', 'Yes')
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
        ret = dialog.yesno('Dream - Clup UYARI', 'Apple TV & Android Box - CACHE temizliginden Eminmisiniz ! ','','','No', 'Yes')
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



def findaddon(url,name):  
    print '############################################################       REMOVE ADDON             ###############################################################'
    pluginpath = xbmc.translatePath(os.path.join('special://home/addons',''))
    import glob
    for file in glob.glob(os.path.join(pluginpath, url+'*')):
        name=str(file).replace(pluginpath,'').replace('plugin.','').replace('audio.','').replace('video.','').replace('skin.','').replace('repository.','')
        iconimage=(os.path.join(file,'icon.png'))
        fanart=(os.path.join(file,'fanart.jpg'))
        addDir(name,file,26,iconimage,fanart,'')
        setView('movies', 'SUB') 

def INFO(name):
  try:
        dialog = xbmcgui.Dialog()
        i = dialog.ok(name, "[COLOR beige]XBMC yi kapatmadan once temizligi gerceklestirin.[/COLOR]","[COLOR pink]iyi kullanimlar.[/COLOR]")
  except:
        
        pass 



