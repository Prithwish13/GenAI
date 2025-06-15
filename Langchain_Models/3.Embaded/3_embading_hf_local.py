from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# text = "Delhi is the capital of India."

# vector = embedding.embed_query(text)

# print(str(vector))

documents = [
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo.",
    "The capital of India is New Delhi."
]
vectors = embedding.embed_documents(documents)

print(str(vectors))