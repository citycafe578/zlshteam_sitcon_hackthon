from flask import Flask, request, abort
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot import LineBotApi
import main_word

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = 'hRsI4WZ1V2Z3woqQSZhV4WURqylDxywDp1ZKJTUPp9QmD4D6IRTWQo4docrR+DToW2IQvHNib+ieyLRwe91pxiHbVWyHRFiHCikFxmSvf9sQgVhfup1eFswOVQ+dJE2CPGsF4YAo5i+Ud1z0aJ98NwdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '6a9d7859928537988a8a0c23ed0d0fca'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.error("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    app.logger.debug(f"Received message: {user_message}")

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=main_word.main_word(user_message))
    )

if __name__ == "__main__":
    app.run(debug=True, port = 8000)
