# -*- coding: cp1254 -*-

import sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

addon_id = 'script.module.xbmctr'
Addon = xbmcaddon.Addon(id=addon_id)
home = Addon.getAddonInfo('path')
print "home",home 
folders = xbmc.translatePath(os.path.join(Addon.getAddonInfo('path'), 'resources', 'lib'))
sys.path.append(folders)


def run():
    Addon.openSettings()
    return True


run()
