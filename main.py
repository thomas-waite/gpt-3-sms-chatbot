import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS
from chatbot import GPT
load_dotenv()

# TODO: use a session cookie rather than a stateful class.
# This will maintain the history for all users

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello_world():
    return 'hello'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']

    answer = gpt.ask(incoming_msg)
    r = MessagingResponse()
    r.message(answer)
    return str(r)


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    gpt = GPT(API_KEY)
    app.run(host='0.0.0.0', port='80')
