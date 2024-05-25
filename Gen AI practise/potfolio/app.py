from flask import Flask, render_template_string
import google.generativeai as genai
# from kaggle_secrets import UserSecretsClient

app = Flask(__name__)

# user_secrets = UserSecretsClient()
# gemini_key = user_secrets.get_secret("GEMINI_API_KEY")

# genai.configure(api_key = gemini_key)
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def generate_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            stop_sequences=['time'],
            max_output_tokens=1000,
            temperature=0.7
        )
    )
    return response.text



@app.route('/')
def home():
    return render_template_string('''
        <h1>Data Science Portfolio Website</h1>
        <p>Welcome to my data science portfolio website! Here, you can view some of my latest projects and learn more about my skills and experience.</p>
        <p><a href="/generate">Generate a new response</a></p>
    ''')

@app.route('/generate')
def generate():
    prompt = "Build a simple data science portfolio website using Flask"
    response = generate_response(prompt)
    # os.mkdir("flasknew")
    with open("app1.py","w") as file:
        file.write(response)
        
    return render_template_string(f'''
        <h1>Generated Response:</h1>
        <p>{response}</p>
        <p><a href="/">Go back</a></p>
    ''')
    
    
if __name__ == '__main__':
    app.run(debug=True)

