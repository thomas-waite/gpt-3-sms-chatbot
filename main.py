from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS
from chatbot import GPT

app = Flask(__name__)
CORS(app)

# TODO: use a session cookie rather than a stateful class.
# This will maintain the history for all users
gpt = GPT()


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
    app.run(host='0.0.0.0', port='80')
