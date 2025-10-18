from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('nodejs.pdf')

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=15, separator='')

docs = loader.load()

result = splitter.split_documents(docs)

print(result[0].page_content)