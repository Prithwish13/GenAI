from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('nodejs.pdf')

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=15)

docs = loader.load()
result = splitter.split_documents(docs)


print(result[99].page_content)

print('\n\n')

print(result[100].page_content)