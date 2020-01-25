#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import 

import urllib2


from sgmllib import SGMLParser
 
class WeatherList(SGMLParser):
    is_li=""
    name=[]
    def start_li(self, attrs):
        self.is_li = 1
    def end_td(self):
        self.is_li=""
    def handle_data(self, text):  
        if self.is_li:
                self.name.append(text)  
def weather():
    
    content = urllib2.urlopen('https://www.cwb.gov.tw/V8/C/W/Town/Map_66.html').read()
    Tempreature = WeatherList()
    Tempreature.feed(content)
    k=[]
    for i in Tempreature.name:
         if '\t' not in i:
             k[]= i.decode('utf-8')
             
    message = TemplateSendMessage(text=k)
    return message