from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


responses = {
    "hi": "Hello, how can I assist you today?",
    "hello": "Hi there! How can I help?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you ask something else?"
}


def chatbot_response(message):
    return responses.get(message.lower(), responses["default"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    user_message = request.args.get('msg')  
    return jsonify({'response': chatbot_response(user_message)})

if __name__ == "__main__":
    app.run(debug=True)
