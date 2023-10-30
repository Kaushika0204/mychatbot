import json
import random

# Load the rules from the JSON file
with open('bot.json', 'r') as json_file:
    rules_data = json.load(json_file)

# Get the rules from the JSON data
rules = rules_data.get('rules', {})

def chatbot_response(user_input):
    user_input = user_input.lower()

    for key in rules:
        if key in user_input:
            return random.choice(rules[key])

    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Main loop
while True:
    user_input = raw_input("You: ") 
    if user_input.lower() == 'thanks':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot: " + response)

