exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("IyEvMTJkLzEzMC9lYwojIC0qLSBlZTogMTI5LTggLSotCgozMyAzOCw1MSwxZSwyYSwzZiwxMzMKMzMgOGUsMzIKMzMgZGIsNmEsMTE1CjMzIDRiCjExZiBjMy4xMmUuMTIxIDMzIDdmCgoyMSA9ICcxZC41Ni5iYycKMyA9IDNmLmIwKDEzND0yMSkKYTIgPSAzLjY2CjVlID0gMy4xNignNWQnKQo3OCA9IDEzMy4xNCggZGIuNWQuOWMoIDVlLCAnNzguMjQnICkgKQoxNDIgPSAxMzMuMTQoIGRiLjVkLjljKCA1ZSwgJzE0Mi4zZScgKSApCjg5ID0gMTMzLjE0KGRiLjVkLjljKDVlLCAnYzgnLCAnMTI3JykpCjRiLjVkLmViKDg5KQozNSAgICA9IDMuMTYoJzc4JykKCjE4IDcxKCk6CgljZj0nM2Q9JwoJZWY9JzE3PScKCWMxID0gMzIuMzIoKQoJYWU9MTMzLjE0KCJlNTovLzVlL2Q1LyIpCgk4NyA9IDdmKCkKCWQyPTg3LmFjCgk4NiA9IDg3LjkzKCI4MiIpCgk4Ny41MCg4NikKCThiID0gODcuOTAoNmEuNmUoZWYpKQoJODYuNTAoOGIpCgk3MyA9IDZhLjZlKGNmKQoJZiA9IDEyNChhZSs3MywgIjE0MyIpCglmLjEwMShjMS5kMChkMihlOT0iIikpKQoKNTkgPSAxMzMuZjUoKQo1OS4xMTEoKQo3OSA9IDEzMy5jZSgxMzMuOTEpCjc5LjEwYigpCgo0YSA9IDEwMyg5NygxMzMuYTcoImU4Ljk4IikpWzA6NF0pCjY1IDRhID4gMTMuMjoKCTcxKCkKNTc6CiAgICAxM2YKMzUgICAgPSAzLjE2KCc3OCcpCjEzNiA9ICAgM2YuYjAoKS4xNigiZTIiKQoxOCBhNCgpOgogICAgMTM3ID0gJ2YyLjJmLzJmLzc2LjNjLy86ODEnWzo6LTFdCiAgICAxMzg9MTBmKDEzNykKICAgIGFkID0gOGUuMWIoYWQnZjMgPSJlZCInLDEzOCkKICAgIDY1IGFkOgoJOTIoKQoJMTEzKCkKICAgIDU3OgoJMTNmCgoxOCA1YygpOgoJYTQoKQoJODQ6CgkJNTQgPSAzLjU4KCJkNCIpCgkJYiA9IDMuNTgoImIiKQoJCTEzNyA9ICdjOi8vMmQuOWEuYzc6YTMvYzQuY2I/NDc9Jys1NCsnJmI9JytiKycmN2I9YzkmNjE9NzUnCgkJMTM4PTEwZigxMzcpCgkJMzY9OGUuMjkoIiM0YzotMSwoLio/KVxhZFw4NTovLyguKj8pLyguKj8pLyguKj8pLyguKj8pLyguKj8pXGFkIikuMWIoMTM4KQoJCTY5IDYsMTM3LDQ2LDZkLDZiLDQ5IDgwIDM2OgoJCQk2NSAiZGUiIDgwIDY6CgkJCQkxM2YKCQkJNTc6CgkJCQkxMzc9J2M6Ly8nKzEzNysnLycrNDYrJy8nKzZkKycvJys2YisnLycrNDkKCQkJCTEyOD0nJwoJCQkJMTNkKCdbZDEgNDFdW2QxIDI2XT5bL2QxXSAnKzYrJ1svZDFdJywxMzcsJycsJ2M6Ly8xM2EuMjAvMTUvMTQxLzE0Mi4zZScpCgkJNzA9OGUuMjkoIiM0YzotMSwxMzkoLio/KVxhZFwxM2IoLio/KVxhZFwxM2IiKS4xYigxMzgpCgkJNjUgNzA6CgkJCTY5IDYsMTM3IDgwIDcwIDoKCQkJCTEzZCgnW2QxIGFhXVtkMSAyNl0+Wy9kMV0gMTM5Jys2KydbL2QxXScsMTM3LCcnLCdjOi8vMTNhLjIwLzE1LzE0MS8xNDIuM2UnKQoJCTU3OgoJCQkxM2QoJyBbZDEgMjZdJysnKiEgZDggYjkgMjcgMTM1ICAxMDIgMTFiIDExNiArIDEwIGU2IDg4ICohJysnIFsvZDFdJywnMWQ6Ly8xZC41Ni41My8/NjM9MzQmNTI9MmInLCcnLCdjOi8vMTNhLjIwLzE1LzE0MS8xNDIuM2UnKSAgICAgICAKCQkKCQkJCgkzNzoKCQk5YignW2QxIGZiXVtkMSA0MV0+Pj4+PlsvZDFdJysnOTUnKydbZDEgNDFdPDw8PDwnKydbL2QxXScsMTM3LDEsJycsJ2M6Ly8xM2EuMjAvMTUvMTQxLzE0Mi4zZScpCgkJOWQ9J2YyLjEyMy9iYS83Ni4zYy8vOjgxJ1s6Oi0xXQoJCTEzOD0xMGYoOWQpCgkJYTk9OGUuMjkoJzEzZiA9IiguKj8pImE1ID0iKC4qPykiJykuMWIoMTM4KQoJCTY5IGJkLGE1IDgwIGE5OgoJCQk1ND1hNQoJCQliPWJkCgkJCTEzNyA9ICdjOi8vMmQuOWEuYzc6YTMvYzQuY2I/NDc9Jys1NCsnJmI9JytiKycmN2I9YzkmNjE9NzUnCgkJCTEzZCgnIFtkMSBhYV0qISAnKydlMCAxMjIgMTJhIGIxIDMwIGU2IDg4JysnICohWy9kMV0nLCcxZDovLzFkLjU2LjUzLz82Mz0zNCY1Mj0yYicsJycsJ2M6Ly8xM2EuMjAvMTUvMTQxLzE0Mi4zZScpICAgICAgIAoJCQkxMzg9MTBmKDEzNykKCQkJMzY9OGUuMjkoIiM0YzotMSwoLio/KVxhZFw4NTovLyguKj8pLyguKj8pLyguKj8pLyguKj8pLyguKj8pXGFkIikuMWIoMTM4KQoJCQk2OSA2LDEzNyw0Niw2ZCw2Yiw0OSA4MCAzNjoKCQkJCTEzNz0nYzovLycrMTM3KycvJys0NisnLycrNmQrJy8nKzZiKycvJys0OQoJCQkJMTI4PSdjOi8vMTNhLjIwLzE1LzE0MS8nKzQ5CgkJCQkxMjg9MTI4LjcoIjExNyIsIjI0IikuNygiZjAiLCIyNCIpLjcoImY5IiwiMjQiKS43KCJmNiIsIjI0IikuNygiNzUiLCIyNCIpCgkJCQkxM2QoJ1tkMSA0MV1bZDEgMjZdPlsvZDFdJys2KydbL2QxXScrJ1tkMSBhYV0nKycgLTEyMCcrJ1svZDFdJywxMzcsJycsJ2M6Ly8xM2EuMjAvMTUvMTQxLzE0Mi4zZScpCgkJCWQzID0gJ2M6Ly8yZC45YS5jNzphMy9jNC5jYj80Nz1jMiZiPWMyJjdiPWM5JjYxPTEyYicKCQkJMTM4PTEwZihkMykKCQkJMzY9OGUuMjkoIiM0YzotMSwoLio/KVxhZFw4NTovLyguKj8pLyguKj8pLyguKj8pLyguKj8pLyguKj8pXGFkIikuMWIoMTM4KQoJCQk2OSA2LDEzNyw0Niw2ZCw2Yiw0OSA4MCAzNjoKCQkJCTY1ICJkZSIgODAgNjoKCQkJCQkxM2YKCQkJCTU3OgoJCQkJCTEzNz0nYzovLycrMTM3KycvJys0NisnLycrNmQrJy8nKzZiKycvJys0OQoJCQkJCTEyOD0nYzovLzEzYS4yMC8xNS8xNDEvJys0OQoJCQkJCTEyOD0xMjguNygiMTE3IiwiMjQiKS43KCJmMCIsIjI0IikuNygiZjkiLCIyNCIpLjcoImY2IiwiMjQiKS43KCI3NSIsIjI0IikKCQkJCQkxM2QoJ1tkMSA0MV1bZDEgMjZdPlsvZDFdJys2KydbL2QxXScrJ1tkMSBmYl0nKycgLSAgMTJmIDExYScrJ1svZDFdJywxMzcsJycsJ2M6Ly8xM2EuMjAvMTUvMTQxLzE0Mi4zZScpCgkJMTNkKCcgW2QxIDI2XScrJyohICsgMjcgYjkgZDggYzUgICohJysnIFsvZDFdJywnMWQ6Ly8xZC41Ni41My8/NjM9MzQmNTI9MmInLCcnLCdjOi8vMTNhLjIwLzE1LzE0MS8xNDIuM2UnKSAgICAgICAKMTggMTBmKDEzNyk6CgljNiA9IDUxLmRkKDEzNykKCWM2LmI4KCcxMjYtMTBhJywgJ2RmLzUuMCAoMTJjOyAxMDkgZmE7IGUzKSBhYi9lNy4xMSAoMTBjLCAxMGUgMTA1KSBmNC8yMy4wLjEwZC42NCBmNy9lNy4xMScpLCgnNmMnLCAnNTUvMTEyLDRkL2VhK2MzLDRkL2MzOzEzMT0wLjksKi8qOzEzMT0wLjgnKSwoJzZjLWQ3JywgJ2RhJyksKCc2Yy1kNicsICdkYScpLCgnYmInLCAnYmYnKQoJNDMgPSA1MS5kYyhjNikKCTEzOD00My4xMWQoKQoJNDMuMTA2KCkKCTI4IDEzOAoKZjEgPSAnNmYuMmYvMmYvNzYuM2MvLzo4MSdbOjotMV0KMTM4PTEwZihmMSkKOGE9MTM4CgpiNSA5MigpOgogICAgMTEwID0gYmUKICAgIDEzZSA9IDEKICAgIDEzYyA9IDUKICAgIDE4IDc3KCBlNCwgKmNkLCAqKmExICk6CgkxMzMuMWMoICIzOSglZCkiICUgKCBlNC4xMTAsICkgKQoJZTQuMjUgPSAyYS5hMCggZTQuMTEwICkKCTEzMy5jMCggMTAwICkKCWU0LjE5KCkKICAgIDE4IDE5KCBlNCApOgoJMWEsIDU1ID0gZTQuM2IoKQoJZTQuMjUuMWYoIGU0LjEzZSApLjdhKCAiJWIzIC0gJWIzIiAlICggMWEsIDIxICsiLSA3MjoiKzEzNikgKQoJZTQuMjUuMWYoIGU0LjEzYyApLjhjKCA1NSApCiAgICAxOCAzYiggZTQgKToKCTZmID0gOTcoOGEpCgkyOCAiOTkgIiw2ZgoKMTggZmUoKToKCTgzKCkKCSAgICAgICAKZmYgPSAnNmYuOTYvYmEvNzYuM2MvLzo4MSdbOjotMV0KYjI9MTBmKGZmKQo3ZD1iMgoKYjUgODMoKToKICAgIDExMCA9IGJlCiAgICAxM2UgPSAxCiAgICAxM2MgPSA1CiAgICAxOCA3NyggZTQsICpjZCwgKiphMSApOgoJMTMzLjFjKCAiMzkoJWQpIiAlICggZTQuMTEwLCApICkKCWU0LjI1ID0gMmEuYTAoIGU0LjExMCApCgkxMzMuYzAoIDEwMCApCgllNC4xOSgpCiAgICAxOCAxOSggZTQgKToKCTFhLCA1NSA9IGU0LjNiKCkKCWU0LjI1LjFmKCBlNC4xM2UgKS43YSggIiViMyAtICViMyIgJSAoIDFhLCAyMSArIi0gNzI6IisxMzYpICkKCWU0LjI1LjFmKCBlNC4xM2MgKS44YyggNTUgKQogICAgMTggM2IoIGU0ICk6Cgk2ZiA9IDk3KDdkKQoJMjggIjk5ICIsNmYKICAKMTggNGUoMWE9J2ZjJywgOGYgPSAnJywgYjQgPSAxMWMsIGQ5ID0gMzUpOgoJCTg0OiAxMzMuMWMoJzExNC45ZSgiJWIzIiwgIiViMyIsICViMywgIiViMyIpJyAlICgxYSwgOGYsIGI0LCBkOSkpCgkJMzcgY2EsIGU6CgkJCTEzMy5hNSggJ1slYjNdOiA0ZTogMTI1IGY4IFslYjNdJyAlICgyMSwgZSksIDIgKSAgICAKCjE4IDEzZCg2LCAxMzcsIDEyOCwgMTQyKToKICAgIDQ0ID0gMmEuN2UoNiwgNjc9ImE4LjI0IiwgM2E9MTI4KQogICAgNDQuZTEoN2I9IjEwNyIsIGI2PXsiMTA0Ijo2fSkKICAgIDQ0LjJjKCJiNyIsICIxMTgiKQogICAgNDQuMmMoJzQyJywgMTQyKQogICAgMjggMWUuMmUoOWY9YTYoNGIuNDVbMV0pLDEzNz0xMzcsNzQ9NDQsN2M9YmYpICAgCjE4IDliKDYsMTM3LDMxLDYyLDE0Mik6CgkxMzI9NGIuNDVbMF0rIj8xMzc9IiszOC41ZigxMzcpKyImMzE9Iis5NygzMSkrIiY2PSIrMzguNWYoNikKCWZkPWNjCgk0ND0yYS43ZSg2LCA2Nz0iOTQuMjQiLCAzYT02MikKCTQ0LjJjKCc0MicsIDE0MikKCWZkPTFlLjJlKDlmPWE2KDRiLjQ1WzFdKSwxMzc9MTMyLDc0PTQ0LDdjPWNjKQoJMjggZmQKMTggNWIoKToKCTVhPVtdCgk0Zj00Yi40NVsyXQoJNjUgNjgoNGYpPj0yOgoJCWE9NGIuNDVbMl0KCQk0MD1hLjcoJz8nLCcnKQoJCTY1IChhWzY4KGEpLTFdPT0nLycpOgoJCQlhPWFbMDo2OChhKS0yXQoJCTIyPTQwLmFmKCcmJykKCQk1YT17fQoJCTY5IDE0MCA4MCAxMDgoNjgoMjIpKToKCQkJMTI9e30KCQkJMTI9MjJbMTQwXS5hZignPScpCgkJCTY1ICg2OCgxMikpPT0yOgoJCQkJNWFbMTJbMF1dPTEyWzFdCgkyOCA1YQphPTViKCkKMTM3PTYwCjY9NjAKMzE9NjAKODQ6CgkxMzc9MzguNDgoYVsiMTM3Il0pCjM3OgoJMTNmCjg0OgoJNj0zOC40OChhWyI2Il0pCjM3OgoJMTNmCjg0OgoJMzE9YTYoYVsiMzEiXSkKMzc6CgkxM2YKCjY1IDMxPT02MCAxMTkgMTM3PT02MCAxMTkgNjgoMTM3KTwxOgoKICAgIDVjKCkKMTFlIDMxPT0xOiBmZSgpICAgICAgIAoKMWUuOGQoYTYoNGIuNDVbMV0pKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|__settings__|4|5|name|replace|8|9|params|password|http|d|e|f|10|11|splitparams|13|translatePath|ipitv|getAddonInfo|PGxvZ2xldmVsIGhpZGU9InRydWUiPi0xPC9sb2dsZXZlbD4|def|setControls|heading|findall|executebuiltin|plugin|xbmcplugin|getControl|club|addon_id|pairsofparams|23|png|window|orange|27|return|compile|xbmcgui|xIPBV5TGeQo|setProperty|dreamtriptv|addDirectoryItem|nwodtuhs|30|mode|HTMLParser|import|play_video|addon_icon|match|except|urllib|ActivateWindow|thumbnailImage|getText|rtmaerd|YWR2YW5jZWRzZXR0aW5ncy54bWw|jpg|xbmcaddon|cleanedparams|beige|fanart_image|response|liz|argv|live|username|unquote_plus|kan|exec_version|sys|EXTINF|application|showMessage|paramstring|appendChild|urllib2|videoid|youtube|login|text|video|else|getSetting|xbmcPlayer|param|get_params|CATEGORIES|path|home|quote_plus|None|output|iconimage|action|64|if|getLocalizedString|iconImage|len|for|base64|sif|Accept|pas|b64decode|txt|match2|playlist2|Versiyon|filepath|listitem|m3u8|bulc|__init__|icon|playList|setLabel|type|isFolder|konumuz1|ListItem|Document|in|ptth|advancedsettings|windows2|try|nhttp|liste|doc|Senelik|folders|konumuz|veri_ad|setText|endOfDirectory|re|message|createTextNode|PLAYLIST_VIDEO|windows|createElement|DefaultFolder|Bilgilendirme|emridneligliB|str|BuildVersion|DUYURU|ddns|addDir|join|urlkul|Notification|handle|Window|kwargs|__language__|8000|acilis|log|int|getInfoLabel|DefaultVideo|match1|gold|AppleWebKit|toprettyxml|r|pfile|split|Addon|Eklentiler|link9|s|times|class|infoLabels|IsPlayable|add_header|Alman|vtipi|Connection|xbmcTRIPTV|passs|10147|False|sleep|htmlp|lisit|xml|get|Kanallari|req|net|resources|m3u|Exception|php|True|args|PlayList|test|unescape|COLOR|renk|url1|Username|userdata|Language|Encoding|FREE|pics|none|os|urlopen|Request|DE|Mozilla|DreamTR|setInfo|version|SmartTV|self|special|Eur|537|System|indent|xhtml|append|python|KAPALI|coding|nos|mkv|dek|lmx|SISTEM|Chrome|Player|mp4|Safari|failed|avi|x86_64|red|iptvTR|ok|bak|dak|100|write|Kanal|float|Title|Gecko|close|Video|range|Linux|agent|clear|KHTML|1271|like|get_url|WINDOW|stop|html|exit|XBMC|time|Ozel|ts|true|or|USER|Size|5000|read|elif|from|Free|minidom|Team|ssap|open|exec|User|lib|thumbnail|utf|Tum|hls|X11|usr|dom|Pro|bin|q|u|xbmc|id|HD|adonversiyonu|url|link|D|dreamtr|n|CONTROL_TEXTBOX|addLink|CONTROL_LABEL|pass|i|ikonlar|fanart|w".split("|")))