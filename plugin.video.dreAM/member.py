### -*- coding: utf-8 -*-

import mechanize
import urllib,urllib2,re,cookielib
import base64
import os,sys,xbmc, xbmcgui, xbmcaddon, xbmcplugin
import xbmctools
import time,HTMLParser
from xml.dom.minidom import Document

__settings__ = xbmcaddon.Addon(id='plugin.video.dreAM')
addon_icon    = __settings__.getAddonInfo('icon')

def baslamak(threadName, delay):
    try:
        
    
        threadName=[]
        delay=[]
        html = xbmctools.sifre100()
        match = re.compile('Uyeliginiz: <strong>(.*?)</strong></p>').findall(html)
        for membership in match:
             membership=membership
        match2 = re.compile('Kullanici isminiz: <strong>(.*?)</strong></p>').findall(html)
        for uye in match2:
            uye=uye
        match3 = re.compile('Email adresiniz: <strong>(.*?)</strong></p>').findall(html)
        for email in match3:
            email=email
        match4 = re.compile('Giris yapmis oldugunuz sayi: <strong>(.*?)</strong>.*?</p>').findall(html)
        for girissayisi in match4:
            girissayisi=girissayisi
        match5 = re.compile('IP adresiniz: <strong>(.*?)</strong></p>').findall(html)
        for ipadd in match5:
            ipadd=ipadd
        match6 = re.compile('Uyelik Bitis: <strong>(.*?)</strong>.*?</td>').findall(html)
        for tarih in match6:
            if tarih == "":
                tarih="Sonsuz"
            else:            
                tarih=tarih

        EN ='English/'
            
        test='c3RyaW5ncy5wbw=='
        htmlp = HTMLParser.HTMLParser()
        pfile1=xbmc.translatePath('special://home/addons/plugin.video.dreAM/resources/language/'+EN)
        filepath = base64.b64decode(test)
        f1 = open(pfile1+filepath, "w")
      
        
        f1.write('msgid ""\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350000"\n')
        f1.write('msgid "[COLOR yellow][B]Membership Name:[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350001"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+uye+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350002"\n')
        f1.write('msgid "[COLOR brown][B]Membership Type:[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350003"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+membership+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350004"\n')
        f1.write('msgid "[COLOR green][B]Your IP Address:[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350005"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+ipadd+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350006"\n')
        f1.write('msgid "[COLOR red][B]Your Email:[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350007"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+email+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350008"\n')
        f1.write('msgid "[COLOR orange][B]Membership End Date:[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#350009"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+tarih+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#3500010"\n')
        f1.write('msgid "[COLOR purple][B]Number of Enter :[/B][/COLOR]"\n')
        f1.write('msgstr ""\n\n')
        f1.write('msgctxt "#3500011"\n')
        f1.write('msgid "'+'[COLOR beige][B]'+girissayisi+'[/B][/COLOR]'+'"\n')
        f1.write('msgstr ""\n')
        f1.flush()
        f1.close()

    except:
        showMessage('           [COLOR red]V.I.P Uye Olmaniz Gerekli[/COLOR]','                          [COLOR beige]Dream[/COLOR][COLOR red]TR[/COLOR]')
        sys.exit()

    


def playlist3():
        rss='UnNzRmVlZHMueG1s'
        nos='ICA8c2V0IGlkPSIxIj4NCiAgICA8ZmVlZCB1cGRhdGVpbnRlcnZhbD0iMjAiPmh0dHA6Ly9kcmVhbXRyLmNsdWIvYmlsaW5tZXllbi9mZWVkLnhtbDwvZmVlZD4NCiAgICA8ZmVlZCB1cGRhdGVpbnRlcnZhbD0iMTAiPmh0dHA6Ly9kcmVhbXRyLmNsdWIvYmlsaW5tZXllbi9jYW5saS54bWw8L2ZlZWQ+DQogICAgPGZlZWQgdXBkYXRlaW50ZXJ2YWw9IjEwIj5odHRwOi8vZHJlYW10ci5jbHViL2JpbGlubWV5ZW4vZGl6aS54bWw8L2ZlZWQ+DQogICAgPGZlZWQgdXBkYXRlaW50ZXJ2YWw9IjEwIj5odHRwOi8vZHJlYW10ci5jbHViL2JpbGlubWV5ZW4vc2luZW1hLnhtbDwvZmVlZD4NCiAgPC9zZXQ+'
        htmlp = HTMLParser.HTMLParser()
        pfile=xbmc.translatePath("special://home/userdata/")
        doc = Document()
        renk=doc.toprettyxml
        liste = doc.createElement("rssfeeds")
        doc.appendChild(liste)
        veri_ad = doc.createTextNode(base64.b64decode(nos))
        liste.appendChild(veri_ad)
        filepath = base64.b64decode(rss)
        f = open(pfile+filepath, "w")
        f.write(htmlp.unescape(renk(indent="")))


def showMessage(heading='DreamTR', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
