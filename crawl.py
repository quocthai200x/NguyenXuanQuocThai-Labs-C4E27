from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

# 1. Create connection
url = 'https://dantri.com.vn'
conn = urlopen(url)


# 1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
# print(html_content)
with open('dantri.html','wb') as f : 
    f.write(raw_data)
# # 2. Find ROI
# soup = BeautifulSoup(html_content,'html.parser')
# ul = soup.find('ul','ul1 ulnew')
# # print(ul.prettify())


# # 3. Extract ROI
# li_list = ul.find_all('li')
# # print(li_list)
# ls = []
# for li in li_list : 
#     h4 = li.h4
#     a = h4.a
#     title = a.string
#     link = url + a['href']
#     dictionary = OrderedDict({
#         'Title': title.lstrip().rstrip(),
#         'link': link
#     })   
#      # print('Title : ',title.lstrip())
#     # print('link : ',link.lstrip())
#     # dictionary['Title : '] = title
#     # dictionary['link : '] = link
#     ls.append(dictionary)



# # 4. Save Data

# pyexcel.save_as(records=ls, dest_file_name="dantri.xlsx")
