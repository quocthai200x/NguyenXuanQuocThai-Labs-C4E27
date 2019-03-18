from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'

conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content,'html.parser')


# with open ('congtisua.html','wb') as f :
    # f.write(raw_data)


bangthongke = []

div_style = soup.find('div',style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
ls_tr = div_style.table.find_all('tr')
# print(ls_tr)
for tr in ls_tr :
    ls_td = tr.find_all('td')
    # print(ls_td)
    dòng =OrderedDict({})
    for x in range(len(ls_td)) :
        
        dulieu = ls_td[x].string
        
        if x == 0 :
            dòng['STT'] = dulieu
        elif x == 1 :
            dòng['Quý 4 - 2016'] = dulieu 
        elif x == 2 :
            dòng['Quý 1 - 2017'] = dulieu
        elif x == 3 :
            dòng['Quý 2 - 2017'] = dulieu
        elif x == 4 :
            dòng['Quý 3 - 2017'] = dulieu
    bangthongke.append(dòng)
# print(bangthongke)

pyexcel.save_as(records=bangthongke, dest_file_name="bảng_thống_kê.xlsx")


