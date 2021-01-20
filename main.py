from flask import Flask,request,absort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import os

app=Flask(__name__)

YOUR_CHANNEL_ACCESS-TOKEN　=　"WXxwsnhHb8dZ9UCl7mgV1vx4js8887TMjYwiDZh+jXLapUOi/7isvtcOmZP9m+prCkf1A4hpCMlBfNaRPTAiCzid+mPvNMhcpnfHPHz98cxR2bTTJCjghADZnyk7JOjWFYJVC14reFW39QdF6p607gdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "U51f48c4a84fe544502cf3f944737c16e"
line-bot-api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback",method=["POST"])
def callback():
    signature=request.handlers["X-Line-Signature"]

    body=request.get_data(as_text=True)
    app.logger.info("Request body" + body)

    try:
        handler.handle(body,signature)

    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__=="__main__":
    port=int(os.getenv("PORT,5000"))
    app.run(host="0.0.0.0",port=port)