#!/usr/bin/python# -*- coding: utf-8 -*-import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmcimport re,HTMLParserimport os,base64,timeimport sysfrom xml.dom.minidom import Documentaddon_id = 'plugin.video.xbmcTRIPTV'__settings__ = xbmcaddon.Addon(id=addon_id)__language__ = __settings__.getLocalizedStringhome = __settings__.getAddonInfo('path')icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))sys.path.append(folders)addon_icon    = __settings__.getAddonInfo('icon')tk="|User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection', 'keep-alive')"def playlist2():	test='YWR2YW5jZWRzZXR0aW5ncy54bWw='	nos='PGxvZ2xldmVsIGhpZGU9InRydWUiPi0xPC9sb2dsZXZlbD4='	htmlp = HTMLParser.HTMLParser()	pfile=xbmc.translatePath("special://home/userdata/")	doc = Document()	renk=doc.toprettyxml	liste = doc.createElement("advancedsettings")	doc.appendChild(liste)	veri_ad = doc.createTextNode(base64.b64decode(nos))	liste.appendChild(veri_ad)	filepath = base64.b64decode(test)	f = open(pfile+filepath, "w")	f.write(htmlp.unescape(renk(indent="")))xbmcPlayer = xbmc.Player()xbmcPlayer.stop()playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)playList.clear()exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])if exec_version > 13.2:	playlist2()else:    passaddon_icon    = __settings__.getAddonInfo('icon')adonversiyonu =   xbmcaddon.Addon().getAddonInfo("version")def acilis():        url = 'lmx.nwodtuhs/nwodtuhs/bulc.rtmaerd//:ptth'[::-1]        link=get_url(url)        r = re.findall(r'SISTEM ="KAPALI"',link)        if r:                windows()                exit()        else:                passdef CATEGORIES():        acilis()        try:                login = __settings__.getSetting("Username")                password = __settings__.getSetting("password")                url = '=emanresu?php.teg/0808:piv.keug//:ptth'[::-1]+login+'&password='+password+'&type=m3u&output=m3u8'                print url                list1(url)        except:                addDir('[COLOR red][COLOR beige]>>>>>[/COLOR]'+'Bilgilendirme'+'[COLOR beige]<<<<<'+'[/COLOR]',url,1,'','http://dreamtr.club/ipitv/ikonlar/fanart.jpg')                urlkul='lmx.ssap/vtipi/bulc.rtmaerd//:ptth'[::-1]                link=get_url(urlkul)                match1=re.compile('pass ="(.*?)"log ="(.*?)"').findall(link)                for passs,log in match1:                    login=log                    password=passs                    url = '=emanresu?php.teg/0808:piv.keug//:ptth'[::-1]+login+'&password='+password+'&type=m3u&output=m3u8'                    addLink(' [COLOR gold]*! '+'DreamTR Team Tum Eklentiler 40 € / Basic User'+' *![/COLOR]','plugin://plugin.video.dailymotion_com/?mode=playVideo&url=k5oTGQcTXobdZOqWGjr','','http://dreamtr.club/ipitv/ikonlar/fanart.jpg')                           link=get_url(url)                    match=re.compile("#EXTINF:-1,(.*?)\r\nhttp://(.*?)/(.*?)/(.*?)/(.*?)/(.*?)\r").findall(link)                    for name,url,live,pas,sif,kan in match:                        url='http://'+url+'/'+live+'/'+pas+'/'+sif+'/'+kan                        thumbnail='http://dreamtr.club/ipitv/ikonlar/'+kan                        thumbnail=thumbnail.replace("ts","png").replace("mkv","png").replace("avi","png").replace("mp4","png").replace("m3u8","png")                        addLink('[COLOR beige][COLOR orange]>[/COLOR]'+name+'[/COLOR]'+'[COLOR gold]'+' -Free'+'[/COLOR]',url,'','http://dreamtr.club/ipitv/ikonlar/fanart.jpg')                    addDir('[COLOR beige]*** ONLY 100 € / Year - Platinium User ***[/COLOR]',"","",'',"http://dreamtr.club/ipitv/ikonlar/fanart.jpg")                    url='st=tuptuo&u3m=epyt&IJBvDsp067=drowssap&itnelkertmaerd=emanresu?php.teg/0808:piv.keug//:ptth'[::-1]                    link=get_url(url)                    match=re.compile("#EXTINF:-1,(.*?)\r\nhttp://(.*?)\r").findall(link)                    for name,url in match:                        if "ilgilendirme" in name:                            pass                        else:                            name=name.replace('Bein','****').replace('Sky','***').replace('SKY','***').replace('TVBU','****').replace('BEIN','****')                            addDir('[COLOR gold]>'+name+' - Platinium User[/COLOR]',url,19,'','')def azplay(name,url):        if "Kanal D" in name:                link=get_url(url)                match=re.compile('hls: \'(.*?)\'\n').findall(link)                for url in match:                    url=url+tk                    azplay1(name,url)        else:                                                link=get_url(url)                match1=re.compile('file : "(.*?)"').findall(link)                for url in match1:                    if url:                        xbmcPlayer = xbmc.Player()                        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)                        playList.clear()                        addLink(name,url,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')                        listitem = xbmcgui.ListItem(name)                        playList.add(url, listitem)                        xbmcPlayer.play(playList)                        exit()                    else:                            pass	def azplay1(name,url):        xbmcPlayer = xbmc.Player()        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)        playList.clear()        addLink(name,url,'','')        listitem = xbmcgui.ListItem(name)        playList.add(url, listitem)        xbmcPlayer.play(playList)	def list1(url):        addDir('[COLOR pink]Sifrenizi PAYLASMAYIN,Sistem sizi Siler ve ACAMAYIZ![/COLOR]','','','http://img.pngget.com/clip1/puyqcrl42fs.png','http://dreamtr.club/ipitv/ikonlar/fanart.jpg')        link=get_url(url)        addDir('[COLOR orange]** Alternatif SD YAYINLAR TIKLA **[/COLOR]',url,9,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')        match=re.compile("#EXTINF:-1,(.*?)\r\nhttp://(.*?)/(.*?)/(.*?)/(.*?)/(.*?)\r").findall(link)        for name,url,live,pas,sif,kan in match:                url='http://'+url+'/'+live+'/'+pas+'/'+sif+'/'+kan                thumbnail=''                if ".ts" in url:                    addDir('[COLOR lightblue]>> [/COLOR][COLOR lightgreen]'+ name+'[/COLOR]',url,2,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')                else:                    addLink('[COLOR beige][COLOR orange]>[/COLOR] '+name+'[/COLOR]',url,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')        try:                urlkesme='http://fm.kesmeseker.de:8000/music.mp3'                addLink('[COLOR beige][COLOR orange]>[/COLOR] '+"Radyo -KesmeSekerFM"+'[/COLOR]',urlkesme,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')##                urlk='https://ams.tvizlehd.com/live/tv1/playlist.m3u8'##                addLink('[COLOR beige][COLOR orange]>[/COLOR] '+"Kayseri - TV1"+'[/COLOR]',urlk,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')##                urlk1='http://live3.canlitv7.com:1935/live/kanal38/playlist.m3u8'##                addLink('[COLOR beige][COLOR orange]>[/COLOR] '+"Kayseri - Kanal 38"+'[/COLOR]',urlk1,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')##                urlk2='http://stream2.taksimbilisim.com:1935/kenttv/bant1/KentTV.m3u8'##                addLink('[COLOR beige][COLOR orange]>[/COLOR] '+"Kayseri - Kent Tv"+'[/COLOR]',urlk2,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')                                        except:                passdef SD():        url=''        urlD='http://212.224.109.109/S2/HLS_LIVE/kanald/500/prog_index.m3u8'        name='>> Kanal D'        addLink(name,urlD,'','')        urlF='niyay-ilnac/rt.moc.xof.www//:ptth'[::-1]        name='Fox Tv - TR'        link=get_url(urlF)        match=re.compile("videoSrc : \'(.*?)\'").findall(link)        for urlS in match:                addLink('[COLOR lightblue]>> [/COLOR][COLOR lightgreen]'+ name+'[/COLOR]',urlS,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')                        urlO='https://www.maxikanal.com/'#[::-1]        link=get_url(urlO)        match=re.compile('<a href="(.*?)"><img typeof=".*?" src="(.*?)" width="130" height="100" alt=".*?" title=".*?" /></a></div> </div>\n<div class=".*?"> <span class=".*?"><a href=".*?">(.*?)</a></span>').findall(link)        for url,thumbnail,name in match:                addDir('[COLOR lightblue]>> [/COLOR][COLOR lightgreen]'+ name+'[/COLOR]',url,2,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')        urlO1='https://www.maxikanal.com/?page=1'#[::-1]        link=get_url(urlO1)        match=re.compile('<a href="(.*?)"><img typeof=".*?" src="(.*?)" width="130" height="100" alt=".*?" title=".*?" /></a></div> </div>\n<div class=".*?"> <span class=".*?"><a href=".*?">(.*?)</a></span>').findall(link)        for url,thumbnail,name in match:                addDir('[COLOR lightblue]>> [/COLOR][COLOR lightgreen]'+ name+'[/COLOR]',url,2,'https://www.iconsdb.com/icons/preview/barbie-pink/play-3-xxl.png','')        def get_url(url):    req = urllib2.Request(url)    req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; SmartTV) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Encoding', 'none'),('Accept-Language', 'none'),('Connection', 'False')    response = urllib2.urlopen(req)    link=response.read()    response.close()    return linkdek = 'txt.nwodtuhs/nwodtuhs/bulc.rtmaerd//:ptth'[::-1]link=get_url(dek)konumuz=linkclass windows():        WINDOW = 10147        CONTROL_LABEL = 1        CONTROL_TEXTBOX = 5        def __init__( self, *args, **kwargs ):                xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )                self.window = xbmcgui.Window( self.WINDOW )                xbmc.sleep( 100 )                self.setControls()        def setControls( self ):                heading, text = self.getText()                self.window.getControl( self.CONTROL_LABEL ).setLabel( "%s - %s" % ( heading, addon_id +"- Versiyon:"+adonversiyonu) )                self.window.getControl( self.CONTROL_TEXTBOX ).setText( text )        def getText( self ):                txt = str(konumuz)                return "DUYURU ",txtdef bak():        windows2()	       dak = 'txt.emridneligliB/vtipi/bulc.rtmaerd//:ptth'[::-1]link9=get_url(dak)konumuz1=link9class windows2():        WINDOW = 10147        CONTROL_LABEL = 1        CONTROL_TEXTBOX = 5        def __init__( self, *args, **kwargs ):                                            xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )                self.window = xbmcgui.Window( self.WINDOW )                xbmc.sleep( 100 )                self.setControls()        def setControls( self ):                                heading, text = self.getText()                self.window.getControl( self.CONTROL_LABEL ).setLabel( "%s - %s" % ( heading, addon_id +"- Versiyon:"+adonversiyonu) )                self.window.getControl( self.CONTROL_TEXTBOX ).setText( text )        def getText( self ):                txt = str(konumuz1)                return "DUYURU ",txt  def showMessage(heading='iptvTR', message = '', times = 5000, pics = addon_icon):        try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))        except Exception, e:                xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )    def addLink(name, url, thumbnail, fanart):        ok=True        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)        liz.setInfo(type="Video", infoLabels={"Title":name})        liz.setProperty("IsPlayable", "true")        liz.setProperty('fanart_image', fanart)        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)        return ok    def addDir(name,url,mode,iconimage,fanart):                u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)        ok=True        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)        liz.setProperty('fanart_image', fanart)        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)        return okdef get_params():        param=[]        paramstring=sys.argv[2]        if len(paramstring)>=2:            params=sys.argv[2]            cleanedparams=params.replace('?','')            if (params[len(params)-1]=='/'):                    params=params[0:len(params)-2]            pairsofparams=cleanedparams.split('&')            param={}            for i in range(len(pairsofparams)):                    splitparams={}                    splitparams=pairsofparams[i].split('=')                    if (len(splitparams))==2:                            param[splitparams[0]]=splitparams[1]        return paramparams=get_params()url=Nonename=Nonemode=Nonetry:    url=urllib.unquote_plus(params["url"])except:    passtry:    name=urllib.unquote_plus(params["name"])except:    passtry:    mode=int(params["mode"])except:    passif mode==None or url==None or len(url)<1:    CATEGORIES()elif mode==1: bak()elif mode==2: azplay(name,url)elif mode==3: azplay1(name,url)elif mode==4: tsd(name,url)elif mode==9: SD() xbmcplugin.endOfDirectory(int(sys.argv[1]))