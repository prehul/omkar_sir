from langchain_google_genai import GoogleGenerativeAIEmbeddings
api_key=""
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
#                                           google_api_key=api_key)
# vector = embeddings.embed_query("hello, world!")
# print(vector[:5])
# print(len(vector))

# """
# each sentence represnts with a vector has 768 value
# dimensionality: 768
# """

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
# vector = embeddings.embed_query("hello, world!")
# print(vector[:5])

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

os.environ["GOOGLE_API_KEY"] = api_key
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
# dd = embedding.embed_documents('taahul')
vector = embedding.embed_query("india")
print(vector[:5])
