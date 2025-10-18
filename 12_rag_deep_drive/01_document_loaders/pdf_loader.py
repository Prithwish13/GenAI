from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# PDF loaders (purpose : name)

# PyPDFLoader (simple clean pdf), PDFPlumerLoader (pdf with table/colums), unstructuredPDFLoader or amazon-textract-pdf-loader (for complex pdfs with images, tables, etc.)

# https://python.langchain.com/docs/concepts/document_loaders/
doc_path = Path(__file__).parent / "documents" / "nodejs.pdf"

if not doc_path.exists():
    raise FileNotFoundError(f"{doc_path} is not available")

loader = PyPDFLoader(str(doc_path))

doc = loader.load()

print(doc[0].page_content)
print(doc[0].metadata)
