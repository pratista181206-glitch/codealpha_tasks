# Simple Rule-Based Chatbot

def get_reply(message):
    message = message.lower()

    if "hello" in message or "hi" in message or "hey" in message:
        return "Hi there! How are you ?"

    elif "how are you" in message:
        return "I'm fine, thanks! How about you?"

    elif "good" in message or "fine" in message or "great" in message:
        return "That's great to hear!"

    elif "name" in message:
        return "My name is Jarvis. Nice to meet you!"
    
    elif "how" in message or "day" in message:
        return "it was good"

    elif "help" in message:
        return "Sure! You can ask me how I am, my name, or just say hello!"

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day!"

    else:
        return "I'm not sure how to reply to that. Try saying hi or bye!"

# Main loop
print("ChatBot is ready! Type 'bye' to exit.")
print()

while True:
    user = input("You: ")

    if user == "":
        print("Bot: Please type something!")
        continue

    reply = get_reply(user)
    print("Bot:", reply)
    print()

    if "bye" in user.lower() or "goodbye" in user.lower():
        break
