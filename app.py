from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = Flask(__name__)

configuration = Configuration(access_token='MVhsGgoI8G+OAptf0uDThTVHf9qKzq2i1RcwteRQ+bOGVb0/3n2R1CPgYjpbXhEQW2IQvHNib+ieyLRwe91pxiHbVWyHRFiHCikFxmSvf9vLTVWBP73S8hk9u49SaWVNyMck8UF+nS+0jeAyjS3MswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6a9d7859928537988a8a0c23ed0d0fca')


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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info( ReplyMessageRequest( reply_token=event.reply_token, messages=[TextMessage(text=event.message.text)]))

if __name__ == "__main__":
    app.run()