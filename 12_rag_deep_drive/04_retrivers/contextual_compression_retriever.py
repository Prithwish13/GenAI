from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

doc1= Document(
    page_content="The capital of France is Paris, known for its art, fashion, and culture.And the Eiffel Tower is one of its most iconic landmarks.Pizza is a popular dish originating from Italy.",
    metadata={"source": "geography_book"},
)
doc2 = Document(
    page_content="The Great Wall of China is one of the most famous landmarks in the world.",
    metadata={"source": "history_book"},
)
doc3 = Document(
    page_content="Python is a popular programming language known for its simplicity and versatility.",
    metadata={"source": "tech_blog"},
)
docs = [doc1, doc2, doc3]

model = OpenAIEmbeddings(model="text-embedding-3-large")

store = QdrantVectorStore.from_documents(
    documents=docs,
    embedding=model,
    url="http://localhost:6333",
    collection_name="retriever"
)

# setting up the base retriever

base_retriever = store.as_retriever(search_kwargs={"k":5})

# setup the compressor
llm = ChatOpenAI(model='gpt-4.1')
compressor = LLMChainExtractor.from_llm(llm=llm)


#setting up the compressor retriever

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)


query = 'Where pizza is a popular dish?'
compressed_result = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_result):
    print(f"\n----Result {i+1} ------ ")
    print(f"content:\n{doc.page_content}...")