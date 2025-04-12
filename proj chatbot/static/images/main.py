from flask import Flask, render_template, request, jsonify
from ml_process import find_answer,display_images

app = Flask(__name__)

responses = {
    "hi": "Hello, how can <br> I assist you today?",
    "hello": "Hi there! How can I help?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you ask something else?"
}

 

# Get chatbot text response
def chatbot_response(message):
    return responses.get(message.lower(), responses["default"])



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    user_message = request.args.get('msg')
    response = find_answer(user_message)
    response= response[0:20]
    response.index(10,'<br>')
    print(response)
    image = display_images(user_message)
    print("user images..........")
    print(image)
    return jsonify({'response': response, 'image': image})

if __name__ == "__main__":
    app.run(debug=True)
