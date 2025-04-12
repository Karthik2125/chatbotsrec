from flask import Flask, render_template, request, jsonify
from ml_process import find_answer,display_images

app = Flask(__name__)

responses = {
    "hi": "Hello, how can I assist you today?",
    "hello": "Hi there! How can I help?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you ask something else?"
}
image_paths = {
    "hi": "/static/images/principal.jpg",            
    "hello": "/static/images/principal.jpg",
    "how are you": "/static/images/principal.jpg",
    "bye": "/static/images/principal.jpg",
    "default": "/static/images/principal.jpg"
}
 


def chatbot_response(message):
    return responses.get(message.lower(), responses["default"])



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    user_message = request.args.get('msg')
    response = find_answer(user_message)
    image = display_images(user_message)
    image = "/static/images/"+image
    print("user images..........")
    print(image)
    return jsonify({'response': response, 'image': image})

if __name__ == "__main__":
    app.run(debug=True)
