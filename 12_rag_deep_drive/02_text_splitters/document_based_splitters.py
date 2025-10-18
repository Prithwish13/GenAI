from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


text = """
# ...existing code...
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from pathlib import Path
from typing import List

def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200, language: Language = Language.English) -> List[str]:
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=language,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    # Example: load a sample document if available, otherwise use fallback text
    doc_file = Path(__file__).parent.parent.parent / "01_document_loaders" / "documents" / "cricket.txt"
    if doc_file.exists():
        text = doc_file.read_text(encoding="utf-8")
    else:
        text = (
            "Cricket is a bat-and-ball game played between two teams of eleven players. "
            "It originated in England and has become popular in many countries. "
            "Matches are played on an oval field with a rectangular 22-yard long pitch at the center. "
            "The objective is to score more runs than the opposing team."
        )

    chunks = split_text(text, chunk_size=200, chunk_overlap=40, language=Language.English)
    print(f"Split into {len(chunks)} chunks.\n")
    for i, c in enumerate(chunks[:5], 1):  # print first 5 chunks
        print(f"--- Chunk {i} ---\n{c}\n")
```# filepath: /Users/prithwishdey/Developer/GEN_AI_ENGINEERING/12_rag_deep_drive/02_text_splitters/document_based_splitters.py
# ...existing code...
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from pathlib import Path
from typing import List

def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200, language: Language = Language.English) -> List[str]:
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=language,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    # Example: load a sample document if available, otherwise use fallback text
    doc_file = Path(__file__).parent.parent.parent / "01_document_loaders" / "documents" / "cricket.txt"
    if doc_file.exists():
        text = doc_file.read_text(encoding="utf-8")
    else:
        text = (
            "Cricket is a bat-and-ball game played between two teams of eleven players. "
            "It originated in England and has become popular in many countries. "
            "Matches are played on an oval field with a rectangular 22-yard long pitch at the center. "
            "The objective is to score more runs than the opposing team."
        )

    chunks = split_text(text, chunk_size=200, chunk_overlap=40, language=Language.English)
    print(f"Split into {len(chunks)} chunks.\n")
    for i, c in enumerate(chunks[:5], 1):  # print first 5 chunks
        print(f"--- Chunk {i} ---\n{c}\n")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0    
)

splitted_text = splitter.split_text(text=text)

print(splitted_text[1])