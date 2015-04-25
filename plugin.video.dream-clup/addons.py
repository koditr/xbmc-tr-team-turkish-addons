import xbmcgui
import xbmcaddon
import buggalo
from test import MyClass

buggalo.SUBMIT_URL = 'https://koditr.org/denemebugalo/submit.php'

try:
    w = xbmcgui.WindowXML("xbmc.xml", xbmcaddon.Addon().getAddonInfo('path'), "DefaultSkin/720p" )
    w.doModal()
    del w
    print 'Hello!'

    mydisplay = MyClass()
    mydisplay.doModal()

except Exception:
    buggalo.onExceptionRaised()
