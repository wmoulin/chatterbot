from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import logging
from flask import Flask, request, jsonify

# Enable info level logging
logging.basicConfig(level=logging.INFO)

# The only required parameter for the ChatBot is a name. This can be anything you want.
chatbot = ChatBot("My First Chatbot")

# Training your ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./corpus/"
)

#chatbot.learn_response(Statement('LEA'), Statement(text='Comment tu t\'appelles ?'))

# Get a response
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def hello():
  ask = request.get_json()["ask"]
  #print(ask)
  return jsonify(responseTo=ask, response=chatbot.get_response(ask).text)
  #return jsonify(request.get_json())