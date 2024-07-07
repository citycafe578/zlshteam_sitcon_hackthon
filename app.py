from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, ImageMessage
import json
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
    app.logger.info(user_message)
    response = ai.receive(user_message)
    response = response.replace("ChatCompletionMessage(content='", "")
    response = response.replace("', role='assistant', function_call=None, tool_calls=None)", "")
    response = response.replace("\n", "%0D%0A")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

@handler.add(MessageEvent, message=ImageMessage)
def handle_img_message(event):
    app.logger.info("img")
    message_content = line_bot_api.get_message_content(event.message.id)
    img_id = event.message.id
    with open(f"images/{img_id}.jpg", "wb") as photo:
        for chunk in message_content.iter_content():
            photo.write(chunk)
    
    response = ai.img_receive(img_id)
    response = response.replace("ChatCompletionMessage(content='", "")
    response = response.replace("', role='assistant', function_call=None, tool_calls=None)", "")
    response = response.replace("\n", "%0D%0A")
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=response)
    )



if __name__ == "__main__":
    app.run(debug=True, port=8080)
