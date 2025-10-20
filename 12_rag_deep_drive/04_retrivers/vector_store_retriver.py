from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

q_client = QdrantClient(url="http://localhost:6333")

vector_store = QdrantVectorStore(
    client=q_client,
    collection_name='learning_rag',
    embedding=embedding_model
)

# result = vector_store.similarity_search(query='tell me about the Rahu in my chat', k=3)

retriever = vector_store.as_retriever(search_kwargs={'k': 2})
query="How rahu will give result in my chat?"
result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\n----Result {i+1} ------ ")
    print(f"content:\n{doc.page_content}...")