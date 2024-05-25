from flask import Flask, send_from_directory, request, jsonify, render_template
from flask_cors import CORS
import openai
import google.generativeai as genai

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all routes

# Your OpenAI API key
# openai.api_key = ''
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def send_html(path):
    return send_from_directory('static', path)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get the JSON data from the request
    user_message = data['message']  # Extract the message from the JSON data

    # Call to OpenAI API using the new ChatCompletion method
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": user_message}
    #     ]
    # )
    # ai_message = response['choices'][0]['message']['content'].strip()  # Get the AI-generated response

    chat=model.start_chat(history=[])
    response=chat.send_message("dhoni")
    dataa = ""
    for value in response:
        dataa += value.text
        # print("valueeeee", value.text)

    return jsonify({'response': dataa})  # Return the AI response as JSON

if __name__ == '__main__':
    app.run(debug=True)
