import requests
from flask import Flask

# Import the application views
from app import views

app = Flask(__name__)
@app.route('/')
def receive_message():
        # get whatever message a user sent the bot
        output = request.get_json()
        message = output['message']['text']
        params = {'chat_id': output['message']['chat']['id'], 'text': "you have sent this : " + message }
        response = requests.post("https://api.telegram.org/bot546273093:AAFwUs0V9bY72ocYZzFw_3feJB3adTorK3U/sendMessage"    , data=params)
        return "Message Processed"
if __name__ == '__main__':
    app.run()
