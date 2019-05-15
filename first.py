from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# The only required parameter for the ChatBot is a name. This can be anything you want.
chatbot = ChatBot("My First Chatbot")

# Training your ChatBot
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Get a response
response = chatbot.get_response("Good morning!")
print(response)