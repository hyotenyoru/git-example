from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from D import*
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Snr5bl0ZKPFCxvzqrFnga9tSCDzTlulc24bXm1v3Lwhy591RZJ6jsEM2n1FyL+X3/RwH49XfaG8P4uoG/WjcEs+dRAx01OjnDrwOJCSbQMB6a2OkjWP3GIL12E8oTHP35HxeRJfUEI0kgYU8Xsxp3wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('10839d7e9bc086837c8575a69c71a064')
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '桐人' in msg:
        message =  TextSendMessage(text='原名為鳴坂和人（鳴坂なるさか和人かずと，Narusaka Kazuto），出生後不久父母便因車禍雙亡，大難不死的和人被阿姨桐谷翠和姨丈桐谷峰嵩收養，並改姓「桐谷」。根據桐谷直葉所述，和人從小就被祖父強逼學習劍道，但當擁有個人思想後就放棄劍道而迷上電腦。生性冷靜聰明，外觀如同柔弱的少女般，態度冷淡，帶給不認識的人一種「捉摸不定」、「年齡不詳」的印象。如果穿著和妹妹同樣的衣服出門的話，甚至有被當成姊妹的可能[2]。在電子機械工程方面非常有天賦，在六歲時第一次用廢棄的零件組出了一台電腦，十歲時發現自己的電子戶口有被修改過的痕跡，更進一步發覺自己作為養子的身世，令養父母十分驚訝。自從發現自己作為養子的身世後，和人就開始對現實世界的人際關係產生疏離感，並開始以本名縮寫來的暱稱「桐人」沉浸在網路遊戲的世界中，成為名副其實的「重度玩家」，在遊戲環境內累積了諸多相關的知識及反應力，而這些才能通通因為SAO嚴酷的淬鍊而開花結果，論遊戲的才能甚至被SAO的開發者茅場晶彥評為最強等級。由於SAO時代長期在最前線作戰的緣故，使得桐人經歷了許多在VRMMORPG的環境下真正危及性命的「實戰」經驗，也讓現實中的和人保有著相當強勁的劍術實力，配合原本就過人、甚至在SAO裡進一步得到淬鍊的洞察力及反射神經，甚至能夠在技巧上壓制住全國中學劍道大賽前八強的妹妹直葉。而這些經歷生死關頭累積下來的實力也讓桐人在某些非等級制的VRMMORPG中得以和頂尖玩家平起平坐。後來在SAO跟西莉卡透露桐谷直葉不是自己的親妹妹，而是自己的表妹。')
        line_bot_api.reply_message(event.reply_token, message)
    elif '犽' in msg:
        message =  TextSendMessage(text='Death like wind always by my side.')
        line_bot_api.reply_message(event.reply_token, message)
    elif '星' in msg:
        message =  TextSendMessage(text='スターバースト・ストリーム')
        line_bot_api.reply_message(event.reply_token, message)    
    elif '1' in msg:
        message =  TextSendMessage(text='測試')
        line_bot_api.reply_message(event.reply_token, message) 
    elif '理智' in msg:
        message =  TextSendMessage(text='ㄐㄐ')
        line_bot_api.reply_message(event.reply_token, message) 
    elif '女' in msg:
        message =  TextSendMessage(text='可憐')
        line_bot_api.reply_message(event.reply_token, message)  
    elif '你很爛' in msg:
        message =  TextSendMessage(text='我就爛')
        line_bot_api.reply_message(event.reply_token, message)  
    else: 
        message=ImageSendMessage(original_content_url='https://truth.bahamut.com.tw/s01/201901/66e047c5ee25f1afd236f873ea4fa55e.JPG', preview_image_url='https://truth.bahamut.com.tw/s01/201901/66e047c5ee25f1afd236f873ea4fa55e.JPG')
        line_bot_api.reply_message(event.reply_token,message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
