from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = Flask(__name__)

configuration = Configuration(access_token='hRsI4WZ1V2Z3woqQSZhV4WURqylDxywDp1ZKJTUPp9QmD4D6IRTWQo4docrR+DToW2IQvHNib+ieyLRwe91pxiHbVWyHRFiHCikFxmSvf9sQgVhfup1eFswOVQ+dJE2CPGsF4YAo5i+Ud1z0aJ98NwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6a9d7859928537988a8a0c23ed0d0fca')


@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info( ReplyMessageRequest( reply_token=event.reply_token, messages=[TextMessage(text=event.message.text)]))
        print(event.message.text)

if __name__ == "__main__":
    app.run()