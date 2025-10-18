from pathlib import Path
from langchain_community.document_loaders import TextLoader

doc_path = Path(__file__).parent / "documents" / "cricket.txt"

if not doc_path.exists():
    raise FileNotFoundError(f"{doc_path} not found")

loader = TextLoader(str(doc_path))

doc = loader.load()

print(doc[0].page_content)
print(doc[0].metadata)
print(type(doc[0]))