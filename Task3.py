import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you?", "Hey! What's up?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me ChatBot.", "I go by the name ChatBot.", "You can call me ChatBot!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer your questions, and help you with basic tasks.", "I'm here to chat and assist you with simple queries."]
    ],
    [
        r"what is the weather like today?",
        ["I'm not sure, but you can check a weather website or app for the latest updates.", "I don't have access to real-time weather data, but I hope it's a nice day!"]
    ],
    [
        r"who created you?",
        ["I was created by a developer using Python and the NLTK library.", "I'm a product of programming and artificial intelligence!"]
    ],
    [
        r"how old are you?",
        ["I'm just a program, so I don't have an age. But I was created recently!", "Age is just a number, and I don't have one!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!", "See you later! Have a great day!"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm a chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    if response:
        print("ChatBot:", response)
    else:
        print("ChatBot: I'm sorry, I don't have an answer for that.")