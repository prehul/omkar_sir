import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyAVCDV6pk0emIuzevv88qwoOjYiTefBXvU")


def generate_image(prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(prompt)
    return response.content

import base64
prompt = "A red apple on a table"
image = generate_image(prompt)

# Encode the image data as base64
image_b64 = base64.b64encode(image).decode()

# Display the image in an HTML tag
html = f'<img src="data:image/jpeg;base64,{image_b64}" alt="{prompt}">'
print(html)