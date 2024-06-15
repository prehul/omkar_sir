"""
In order to implement RAG application
Step:1 Load the data
      ==================================
       pip install langchain
       pip install langchain-community
       ==================================
Step-2: Split into chunks
       ====================================
       pip install -qU langchain-text-splitters
       =====================================
Step-3: Apply any embedding model and get the embedding vectors
        This is a kind of plugin
        A) we can use Gemini Embedding model
           =================================
           pip install google-generativeai
           pip install GoogleGenerativeAIEmbeddings (Langchain)
           pip install --upgrade --quiet  langchain-google-genai (Langchain)
           ==================================
        B) we can use openai GPT model
        C) we can use Bert transformer models
           Sentence transformers model
           ===================================
           pip install sentence-transformers
           ====================================
        D) Meta models
Step-4: We can store the embeddings
        A) Chroma
        ==========================================
        pip install langchain-chroma
        ============================================
        B) Fasis

pip install langchain-chroma
pip install sentence-transformers
pip install langchain (Done)
pip install langchain-community(Done)
pip install -qU langchain-text-splitters(Done)
pip install -qU langchain-text-splitters(Done)
"""

# import
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter



# load the document and split it into chunks
loader = TextLoader("chatbot.txt")
documents = loader.load()
documents
print("documentsdocuments", documents)

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
embedding_function


# load it into Chroma
db = Chroma.from_documents(docs, embedding_function)


# query it
query = "What are the contents in Data science"
docs = db.similarity_search(query)

# print results
print(docs[0].page_content)