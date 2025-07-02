#CHATBOT WITH RULE-BASED

#RESPONSES

#Build a simple chatbot that responds to user inputs based on
#predefined rules. Use if-else statements or pattern matching
#techniques to identify user queries and provide appropriate
#responses. This will give you a basic understanding of natural

#language processing and conversation flow.

import random
from datetime import datetime

print("SilyBot: Hey there! I'm SilyBot, your friendly chatbot. Type 'bye' whenever you want to end the chat.")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("SilyBot: Hey! Nice to see you. How can I help you today?")

    # Name
    elif "your name" in user_input:
        print("SilyBot: I'm SilyBot, your virtual buddy. What's your name?")

    # Mood
    elif "how are you" in user_input:
        print("SilyBot: I'm doing great, thanks for asking! What about you?")

    # Help
    elif "help" in user_input:
        print("SilyBot: Sure! I can chat, tell jokes, show the time, and talk about random stuff. Go ahead!")

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"SilyBot: Right now, it's {current_time}.")

    # Age
    elif "your age" in user_input:
        print("SilyBot: Well, I don’t have a birth certificate, but I was created pretty recently!")

    # Location
    elif "where are you from" in user_input:
        print("SilyBot: I'm from the digital world, floating around in your computer or phone.")

    # Weather (mock response)
    elif "weather" in user_input:
        print("SilyBot: I wish I could feel the weather! But I bet it's a good day to smile.")

    # Joke
    elif "joke" in user_input:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why was the computer cold? Because it forgot to close its windows!",
            "What do you call a fish wearing a bowtie? Sofishticated!"
        ]
        print("SilyBot:", random.choice(jokes))

    # Thanks
    elif "thank" in user_input:
        print("SilyBot: Anytime! I'm happy to chat with you.")

    # Bye
    elif user_input in ["bye", "exit", "quit"]:
        print("SilyBot: It was great talking to you! See you soon.")
        break

    # Unknown response
    else:
        print("SilyBot: Hmm... I'm not sure how to respond to that. Try asking me something else?")


