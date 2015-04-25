# -*- coding: utf-8 -*-

# for more info please visit http://xbmctr.com
'''
Created on 21 sempember 2012

@author: drascom
@version: 0.2.0

'''

import os
import sys
import urllib,re,base64
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import time

#--------------Sifre-----------#

#----------------
addon_id = 'plugin.video.yetiskin'

__settings__ = xbmcaddon.Addon(id=addon_id)
home = __settings__.getAddonInfo('path')
fanart = xbmc.translatePath( os.path.join( home, 'fanart.png' ) )
channels = xbmc.translatePath(os.path.join(home, 'channels'))
sys.path.append(channels)
folder = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folder)
import xbmctools

klasorler=os.walk(channels).next()[1]
for klasor in klasorler:
    dizim=xbmc.translatePath(os.path.join(channels, klasor))
    sys.path.append(dizim)
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
sys.path.append(IMAGES_PATH)
##if xbmc.getInfoLabel( "System.BuildVersion" )[:2] == '14':
##    dialog = xbmcgui.DialogProgress()
##    dialog1 = xbmcgui.Dialog()
##    dialog1.ok('[COLOR red][B]MagicTR Hata!![/B][/COLOR]','[COLOR blue][B]MagicTR Kullandiginiz Versiyon Xbmcyi desteklememektedir[/B][/COLOR]','[COLOR yellow][B]Lutfen Frodo veya Gothamda Kullaniniz[/B][/COLOR]')
##    sys.exit()
##else:
##    pass


def main():
    #############
    klasorler=os.walk(channels).next()[1]
    for klasor in klasorler:
        fileName=klasor.replace(" ","")
        name='[COLOR lightgreen][B]'+klasor+'[/B][/COLOR]'
        thumbnail= os.path.join(IMAGES_PATH,klasor+".png")
        url=xbmc.translatePath(os.path.join(channels, klasor))
        araclar.addDir("araclar", name,"listing(IMAGES_PATH,url)", url,thumbnail)
    xbmc.executebuiltin("Container.SetViewMode(500)")

maaac=(xbmc.getInfoLabel("Network.MacAddress"))

##yer = 'http://www.iplocation.net/'
##link=xbmctools.get_url(yer)
##alim=re.compile("<a href=\'/click/1\'>IP2Location</a>.*?</div><table width=\'655\' cellspacing=\'0\' cellpadding=\'0\' border=\'0\'><tr><td bgcolor=\'#336666\' colspan=\'5\' height=\'2\'>        <spacer type=\'block\' height=\'2\'></td></tr><tr bgcolor=\'#99CCCC\'><td width=\'17%\'>IP Address</td><td width=\'18%\'>Country</td><td width=\'15%\'>Region</td><td width=\'15%\'>City</td><td width=\'35%\'>ISP</td></tr><tr><td bgcolor=\'#336666\' colspan=\'5\' height=\'2\'>        <spacer type=\'block\' height=\'2\'></td></tr><tr><td width=\'80\'>(.*?)</td><td>(.*?)></td><td>(.*?)</td><td>.*?</td><td>(.*?)</td></tr>").findall(link)
##
##for ip, region, country, isp in alim:
##    ip=ip
##    country=country
##    isp=isp


bilinmeyen = ('https://koditr.org/bilinmeyen/test.html')
link=xbmctools.get_url(bilinmeyen)
match=re.compile('[D-L3]').findall(link)

key = match

def angel(input):
	
	output = []
	
	for i in range(len(input)):
		xor_num = ord(input[i]) ^ ord(key[i % len(key)])
		output.append(chr(xor_num))
	
	return ''.join(output)


url = 'https://koditr.org/changelog/yetiskin.xml'
link=xbmctools.get_url(url)
match5=re.compile('name="(.*?)"').findall(link)
name1=" \n".join(match5)
match1=re.compile('duyuru="(.*?)"').findall(link)
duyuru=" \n".join(match1)
#MESSAGE_TITLE = 101
if xbmc.getInfoLabel( "System.BuildVersion" )[:2] == '14':
    xbmctools.playlist2()
else:
    pass

class Anapencere( xbmcgui.WindowXMLDialog ):
    def __init__( self, *args, **kwargs ):
        self.shut = kwargs['close_time'] 
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        xbmc.executebuiltin( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
        pass

    def setTableText(self, tab):
        self.tabText = tab
        
    def getTableText(self):
        return self.tabText     
        
                                       
    def onInit( self ):
        #################DUYURU BASLIK######################
##        self.strActionInfo = xbmcgui.ControlLabel(850, 120, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR pink]'+ip+'[/COLOR]')
##
##        self.strActionInfo = xbmcgui.ControlLabel(620, 120, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR brown]'+"IP Adresiniz:"+'[/COLOR]')
##
##        self.strActionInfo = xbmcgui.ControlLabel(850, 90, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR pink]'+country+'[/COLOR]')
##
##        self.strActionInfo = xbmcgui.ControlLabel(620, 90, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR brown]'+"IP nizin Bulundugu Yer:"+'[/COLOR]')
##
##        self.strActionInfo = xbmcgui.ControlLabel(850, 60, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR pink]'+isp+'[/COLOR]')
##
##        self.strActionInfo = xbmcgui.ControlLabel(620, 60, 1000, 700, '', 'font25', '')
##        self.addControl(self.strActionInfo)
##        self.strActionInfo.setLabel('[COLOR brown]'+"Kulladigniz ISP Sirketi:"+'[/COLOR]')



        #################VERSIYON BASLIK###################f###

        self.strActionInfo = xbmcgui.ControlLabel(90, 150, 1000, 700, '', 'font25', '')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel("MAC Adresiniz:")

        self.strActionInfo = xbmcgui.ControlLabel(250, 150, 1000, 700, '', 'font11', '')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel(xbmc.getInfoLabel("Network.MacAddress"))

        #################DUYURU BILGI######################
        self.strActionInfo = xbmcgui.ControlLabel(200, 60, 1000, 700, '', 'font11', '')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('[COLOR turquoise]'+str(duyuru)+'[/COLOR]')
 
        ################# VERSIYON BILGI######################
        self.strActionInfo = xbmcgui.ControlLabel(110, 170, 1000, 1000, '', 'font11', '')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('[COLOR beige]'+str(name1)+'[/COLOR]')
        #self.getControl(MESSAGE_TITLE).setLabel(self.getTableText()['title'])
        #control = self.window.getControl(101)
 #       control.addItem(xbmcgui.ListItem(title=duyuru))
        while self.shut > 0:
            xbmc.sleep(200)
            self.shut -= 1
        xbmc.Player().stop()
        self._close_dialog()

    
    def getLabel(self):
        """Returns the listitem label."""
        #self.getControl(MESSAGE_TITLE).setLabel(self.getTableText()[''])

    def onFocus( self, controlID ): pass
    
    def onClick( self, controlID ): 
        if controlID == 12:
            xbmc.Player().stop()
            self._close_dialog()
        if controlID == 7:
            xbmc.Player().stop()
            self._close_dialog()

    def onAction( self, action ):
        if action in [ 5, 6, 7, 9, 10, 92, 117 ] or action.getButtonCode() in [ 275, 257, 261 ]:
            xbmc.Player().stop()
            self._close_dialog()

    def _close_dialog( self ):
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        time.sleep( .4 )
        self.close()
        

def pencere():
    if xbmc.getCondVisibility('system.platform.ios'):
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    elif xbmc.getCondVisibility("system.platform.atv"):           
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    elif xbmc.getCondVisibility("system.platform.linux"):
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    elif xbmc.getCondVisibility("system.platform.android"):
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    elif xbmc.getCondVisibility("system.platform.osx"):
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    elif xbmc.getCondVisibility("system.platform.windows"):
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    else:
        ac = Anapencere('xbmc.xml',__settings__.getAddonInfo('path'),'DefaultSkin',close_time=34,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%__settings__.getAddonInfo('path'))
    ac.doModal()
    del ac



            
#######################################################################################



        
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
    
    
params = get_params()
name = None
fileName = None
mode = None
url = None
thumbnail = None

#Try-catch blocks to see which parameters are available 
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    fileName = urllib.unquote_plus(params["fileName"])
except:
    pass
try:
    mode = urllib.unquote_plus(params["mode"])
except:
    pass
try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    thumbnail = urllib.unquote_plus(params["thumbnail"])
except:
    pass

print "Ad: "+str(name)
print "Dosya: "+str(fileName)
print "mode: "+str(mode)
print "Url: "+str(url)
print "Resim: "+str(thumbnail)


if fileName == None:
    main()
    pencere()
    xbmctools.kalala(IMAGES_PATH,channels)

else:
    exec "import "+fileName+" as channel"
    exec "channel."+str(mode)
xbmcplugin.endOfDirectory(int(sys.argv[1]))



