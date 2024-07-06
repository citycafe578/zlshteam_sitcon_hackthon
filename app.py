from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage
import ai
import assemble

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = assemble.access_token
CHANNEL_SECRET = assemble.secret

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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    response = ai.receive(user_message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

@handler.add(MessageEvent, message=ImageMessage)
def handle_img_message(event):
    img_id = event.message.id
    message_content = line_bot_api.get_message_content(img_id)
    with open(f"images/{message_id}.jpg", "wb") as photo:
        for chunk in message_content.iter_content():
            photof.write(chunk)



if __name__ == "__main__":
    app.run(debug=True, port=8000)
