from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('ee05ESUwHuxDDhg87os3K0F5eNFB4cOLIxlbCOB+OOeYKTKyDIh30B/PPDrgQEdCuiP4EQcdAcmwQtb7z8wN8fIDHL6j08hpPb1I0UIbF7JuEd7Sjip3MmYjz2nqwOyvUid8QYHXxRmehAvhZpqH9wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0c9425f26e439d3979e84b0f4cc9c016')

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = f"你說了：{msg}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run()

