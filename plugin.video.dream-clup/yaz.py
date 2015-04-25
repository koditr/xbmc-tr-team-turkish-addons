import xbmc,base64
import re,os,sys,urllib,urllib2

url = "aHR0cDovL3hibWMtdHItdGVhbS10dXJraXNoLWFkZG9uLXMuZ29vZ2xlY29kZS5jb20vc3ZuL3RydW5rL2R1eXVydS9jaGFuZ2Vsb2cueG1s"


def replace_fix(x):
    x=x.replace('[COLOR violet]','').replace('[/COLOR]','').replace('[COLOR tomato]','').replace('[COLOR olivedrab]','').replace('[COLOR lightsteelblue]','')
    return x


req = urllib2.Request(base64.b64decode(url))
req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
response = urllib2.urlopen(req)
link=response.read()
response.close()
match=re.compile('name="(.+?)"').findall(link)
name ="\n".join(map(str, match))
name=replace_fix(name)




pfile=xbmc.translatePath("special://home/addons/plugin.video.dream-clup/")
filepath = pfile+'changelog.txt'
f = open(filepath, "w")
f.write(name)
f.flush()
f.close()
