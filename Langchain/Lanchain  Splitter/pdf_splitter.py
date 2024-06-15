# Load the PDF document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

pdf_loader = PyPDFLoader("mlops.pdf")
pages = pdf_loader.load()

# Extract the page content from each Document object
#texts = [doc.page_content for doc in pages]

# Split the text into documents using the CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs_mlops = text_splitter.split_documents(pages)

# Print the number of documents
print(len(docs_mlops))