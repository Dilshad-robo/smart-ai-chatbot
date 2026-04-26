import random

# Responses database
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine, thanks!", "Doing great!", "All good!"],
    "your name": ["I'm SmartBot 🤖", "You can call me SmartBot"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "help": ["I can chat with you. Try saying hello!"]
}

def chatbot():
    print("🤖 SmartBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 SmartBot:", random.choice(responses["bye"]))
            break

        found = False

        for key in responses:
            if key in user_input:
                print("🤖 SmartBot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("🤖 SmartBot: Sorry, I don't understand that.")

# Run chatbot
chatbot()