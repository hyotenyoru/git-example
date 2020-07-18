import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
def star():

    target_url = 'https://forum.gamer.com.tw/search.php?bsn=60076&q=星爆'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.gsc-table-cell-snippet-close div a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    return content
    