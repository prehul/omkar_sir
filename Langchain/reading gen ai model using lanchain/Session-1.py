# pip install --upgrade --quiet  langchain-google-genai
from langchain_google_genai import GoogleGenerativeAI
# api_key="AIzaSyBUUejpbU_3eouCT96lkHmkE2mQ6jQb8TU"
import os
api_key =""

llm = GoogleGenerativeAI(model="gemini-pro", 
                         google_api_key=api_key)
print(
    llm.invoke(
        "List of top 5 Indain crickters"
    )
)