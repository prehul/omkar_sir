import os
import google.generativeai as genai

# Initialize the GenerativeModel with 'gimini-paraphrase'
model = genai.GenerativeModel('gimini-paraphrase')

# Configure the library with your API key
# os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
genai.configure(api_key='')

def paraphrase(text):
    # Set up the prompt for the model
    prompt = f"Paraphrase the following text: {text}"

    # Generate a response from the model
    response = model.generate_content(prompt)

    # Return the paraphrased text
    return response.text

# Test the function
print(paraphrase("The cat is sitting on the mat."))