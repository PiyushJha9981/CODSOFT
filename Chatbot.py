import random
from datetime import datetime

print("Lionbot: Hey there! I'm Lionbot, your friendly chatbot. Type 'bye' whenever you want to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("YLionot: Hey! Nice to see you. How can I help you today?")

    elif "your name" in user_input:
        print("Lionbot: I'm Lionbot, your virtual buddy. What's your name?")

    elif "how are you" in user_input:
        print("Lionbot: I'm doing great, thanks for asking! What about you?")

    elif "help" in user_input:
        print("Lionbot: Sure! I can chat, tell jokes, show the time, and talk about random stuff. Go ahead!")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Lionbot: Right now, it's {current_time}.")

    elif "your age" in user_input:
        print("Lionbot: Well, I don’t have a birth certificate, but I was created pretty recently!")

    elif "where are you from" in user_input:
        print("Lionbot: I'm from the digital world, floating around in your computer or phone.")

    elif "weather" in user_input:
        print("Lionbot: I wish I could feel the weather! But I bet it's a good day to smile.")

    elif "joke" in user_input:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why was the computer cold? Because it forgot to close its windows!",
            "What do you call a fish wearing a bowtie? Sofishticated!"
        ]
        print("Lionbot:", random.choice(jokes))

    elif "thank" in user_input:
        print("Lionbot: Anytime! I'm happy to chat with you.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Lionbot: It was great talking to you! See you soon.")
        break

    else:
        print("Lionbot: Hmm... I'm not sure how to respond to that. Try asking me something else?")


