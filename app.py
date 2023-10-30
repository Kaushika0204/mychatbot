# import bottle
# import json
# import random

# from bottle import static_file

# app = bottle.Bottle()

# with open('./bot.json', 'r') as json_file:
#     rules_data = json.load(json_file) 

# # Get the rules from the JSON data
# rules = rules_data.get('rules', {})

# @app.route('/static/<filepath:path>')
# def serve_static(filepath):
#     return bottle.static_file(filepath, root='static')


# @app.route('/chatbot')
# def chatbot():
#     # Serve an HTML page for the chatbot interface
#     return bottle.template("templates/base.html")

# @app.route('/chat', method='POST')
# def chat():
#     user_input = bottle.request.forms.get('user_input')
#     response = chatbot_response(user_input)
#     return {'chatbot_response': response}

# def chatbot_response(user_input):
#     if user_input:
#         user_input = user_input.lower()
#         print("User Input:", user_input)
#         for key in rules:
#             if key in user_input:
#                 return random.choice(rules[key])
#         return "I'm sorry, I don't understand. Can you please rephrase your question?"
#     else:
#         return "I'm sorry, I didn't receive your message."


# if __name__ == '__main__':
#     bottle.run(app, host='localhost', port=8000)



# import bottle
# import json
# import random
# import re 

# from bottle import static_file

# app = bottle.Bottle()

# with open('./bot.json', 'r') as json_file:
#     rules_data = json.load(json_file) 

# # Get the rules from the JSON data
# rules = rules_data.get('rules', {})

# @app.route('/static/<filepath:path>')
# def serve_static(filepath):
#     return bottle.static_file(filepath, root='static')


# @app.route('/chatbot')
# def chatbot():
#     # Serve an HTML page for the chatbot interface
#     return bottle.template("templates/base.html")

# @app.route('/chat', method='POST')
# def chat():
#     user_input = bottle.request.forms.get('user_input')
#     response = chatbot_response(user_input)
#     return {'chatbot_response': response}

# def chatbot_response(user_input):
#     user_input = user_input.lower()

#     for key in rules:
#         if key in user_input:
#             return random.choice(rules[key])

#     return "I'm sorry, I don't understand. Can you please rephrase your question?"


# if __name__ == '__main__':
#     bottle.run(app, host='localhost', port=8000)

# import bottle
# import json
# import random
# from bottle import HTTPResponse
# import logging
# from bottle import route, request
# from bottle import Bottle, response

# app = bottle.Bottle()
# bottle.TEMPLATE_PATH.insert(0, 'templates')  # Specify the path to your templates directory

# @app.hook('after_request')
# def enable_cors():
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

# # Load the rules from the JSON file
# with open('bot.json', 'r') as json_file:
#     rules_data = json.load(json_file)

# # Get the rules from the JSON data
# rules = rules_data.get('rules', {})

# @app.route('/static/<filepath:path>')
# def serve_static(filepath):
#     return bottle.static_file(filepath, root='static')

# @app.route('/chat')
# def chat_template():
#     return bottle.template("templates/base.html")

# @app.route('/chatbot', method='POST')
# def chatbot():
#     user_input = bottle.request.forms.get('user_input')
#     try:
#         response = chatbot_response(user_input)
#         logging.info("Received POST request to /chatbot with user input: %s" % user_input)
#         logging.info("Chatbot response: %s" % response)

#         # Create a JSON response
#         response_data = {'chatbot_response': response}
#         return bottle.HTTPResponse(body=json.dumps(response_data), content_type='application/json')

#     except Exception as e:
#         # Log the error for debugging purposes
#         logging.error("Error in /chatbot: %s" % str(e))
#         # Return an error response
#         return HTTPResponse(status=500, body='Internal Server Error')

# def chatbot_response(user_input):
#     if user_input is not None:
#         user_input = user_input.lower()
#         for key in rules:
#             if key in user_input:
#                 return random.choice(rules[key])

#     return "I'm sorry, I don't understand. Can you please rephrase your question."

# if __name__ == '__main__':
#     bottle.run(app, host='localhost', port=8000)

# import bottle
# import json
# import random
# import logging
# from bottle import route, request, response

# app = bottle.Bottle()
# bottle.TEMPLATE_PATH.insert(0, 'templates')  # Specify the path to your templates directory

# # Enable CORS for all routes
# @app.hook('after_request')
# def enable_cors():
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

# # Load the rules from the JSON file
# with open('bot.json', 'r') as json_file:
#     rules_data = json.load(json_file)

# # Get the rules from the JSON data
# rules = rules_data.get('rules', {})

# @app.route('/static/<filepath:path>')
# def serve_static(filepath):
#     return bottle.static_file(filepath, root='static')

# # Route to display your chat template
# @app.route('/chat')
# def chat_template():
#     return bottle.template("templates/base.html")

# # Route for chatbot logic
# @app.route('/chatbot', method=['POST', 'GET'])
# def chatbot():
#     user_input = bottle.request.forms.get('user_input')
#     try:
#         response = chatbot_response(user_input)
#         logging.info("Received POST request to /chatbot with user input: %s" % user_input)
#         logging.info("Chatbot response: %s" % response)

#         # Create a JSON response
#         response_data = {'chatbot_response': response}
#         return bottle.HTTPResponse(body=json.dumps(response_data), content_type='application/json')

#     except Exception as e:
#         # Log the error for debugging purposes
#         logging.error("Error in /chatbot: %s" % str(e))
#         # Return an error response
#         return bottle.HTTPResponse(status=500, body='Internal Server Error')

# def chatbot_response(user_input):
#     user_input = user_input.lower()  # Convert user input to lowercase
#     for key in rules:
#         if key.lower() in user_input:  # Convert rule key to lowercase for case-insensitive matching
#             # Return a random response from the matching rule
#             return random.choice(rules[key])
#     return "I'm sorry, I don't understand. Can you please rephrase your question?"


#     return "I'm sorry, I don't understand. Can you please rephrase your question?"

# if __name__ == '__main__':
#     bottle.run(app, host='localhost', port=8000)

import bottle
import json
import random
import logging
from bottle import route, request, response, run
from bottle import Bottle

# Load the rules from the JSON file
with open('bot.json', 'r') as json_file:
    rules_data = json.load(json_file)

print("Loaded data from bot.json:", rules_data)

# Get the rules from the JSON data
rules = rules_data.get('intents', {})

app = Bottle()

@app.route('/')
def chatbot():
    return bottle.template("index.html")

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return bottle.static_file(filepath, root='static')

@app.route('/chat', method='POST')
def chat():
    user_input = request.json.get('user_input')  
    response = chatbot_response(user_input, rules)
    return {'chatbot_response': response}

def chatbot_response(user_input, intents):
    if user_input:
        user_input = user_input.lower()

        for intent in intents:
            for pattern in intent['patterns']:
                if pattern.lower() in user_input:
                    return random.choice(intent['responses'])

        return "I'm sorry, I don't understand. Can you please rephrase your question?"
    else:
        return "I'm sorry, I didn't receive your message."

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

if __name__ == '__main__':
    bottle.run(app, host='127.0.0.1', port=5000)


