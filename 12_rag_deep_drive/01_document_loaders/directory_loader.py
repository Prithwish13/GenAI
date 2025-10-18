from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path='documents',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# data = loader.load()
data = loader.lazy_load()

for doc in data:
    print(doc.metadata)