from pathlib import Path
from langchain_community.document_loaders import CSVLoader

file_path = Path(__file__).parent / "documents" / "random_user_data_100.csv"

if not file_path.exists():
    raise FileNotFoundError(f"{file_path} is not available")    

loader = CSVLoader(file_path=file_path)

rows = loader.load()

print(len(rows))