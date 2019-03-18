from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'

conn = urlopen(url)

raw_data = conn.read()

html_content = raw_data.decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')

section = soup.find('section','section chart-grid')

li_list = section.div.find_all('li')

ls =[]
for li in li_list : 
    h3 = li.h3
    song = h3.string
    h4 = li.h4
    artists = h4.string
    dic = {
        'song':song.lstrip().rstrip(),
        'artists':artists.lstrip().rstrip(),
    }
    ls.append(dic)

pyexcel.save_as(records=ls, dest_file_name="baihat_nghesi.xlsx")

keyls = []

for j in ls:
    key = j['song']+''+j['artists']
    keyls.append(key)

options = {
    'default_search': 'ytsearch' , # tell downloader to search instead of directly downloading
    'max_downloads': len(keyls) # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(keyls)