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
    else:
        msg=str(len(msg))
        message = TextSendMessage(text='你輸入'+msg+'個字')
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
