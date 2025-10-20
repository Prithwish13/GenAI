from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from langchain.schema import Document
from langchain.retrievers.multi_query import MultiQueryRetriever

from dotenv import load_dotenv

load_dotenv()

from langchain.schema import Document

document_1 = Document(
    page_content="I had a bowl of oatmeal with fresh fruits and green tea for breakfast — trying to start my mornings healthy!",
    metadata={"source": "tweet"},
)

document_2 = Document(
    page_content="Experts warn that lack of sleep can significantly impact heart health and increase stress hormone levels.",
    metadata={"source": "news"},
)

document_3 = Document(
    page_content="Building a mindful eating habit is just like building a project — small consistent improvements matter the most.",
    metadata={"source": "tweet"},
)

document_4 = Document(
    page_content="New study finds that 30 minutes of brisk walking daily reduces the risk of diabetes by nearly 40%.",
    metadata={"source": "news"},
)

document_5 = Document(
    page_content="Just watched a documentary on plant-based diets — I’m seriously thinking about cutting down on processed foods.",
    metadata={"source": "tweet"},
)

document_6 = Document(
    page_content="Top 5 apps that help you track your calorie intake and daily workouts effectively.",
    metadata={"source": "website"},
)

document_7 = Document(
    page_content="The top 10 athletes in the world share one secret: consistency in diet and sleep routine.",
    metadata={"source": "website"},
)


document_8 = Document(
    page_content="LangGraph is the best framework for building stateful, agentic applications!",
    metadata={"source": "tweet"},
)

document_9 = Document(
    page_content="The stock market is down 500 points today due to fears of a recession.",
    metadata={"source": "news"},
)

document_10 = Document(
    page_content="Feeling low energy? Hydration might be the key — drink at least 2.5 liters of water daily.",
    metadata={"source": "tweet"},
)

document_11 = Document(
    page_content="Regular exercise not only boosts physical health but also sharpens memory and creativity.",
    metadata={"source": "website"},
)

documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11
]

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

v_store = QdrantVectorStore.from_documents(
    documents=documents,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="retriever"
    )
# making a similarity search retriever
similarity_retriever = v_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k': 3}
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=v_store.as_retriever(search_kwargs={'k': 3}),
    llm=ChatOpenAI(model='gpt-4.1')
)

query='How to improve energy levels and maintain balance?'

result_similarity = similarity_retriever.invoke(query)
result_multiquery = multiquery_retriever.invoke(query)


for i, doc in enumerate(result_similarity):
    print(f"\n----Result {i+1} ------ ")
    print(f"content:\n{doc.page_content}...")
    
print("------------------------------------------------------------------ DFF ------------------------------------------------------")

for i, doc in enumerate(result_multiquery):
    print(f"\n----Result {i+1} ------ ")
    print(f"content:\n{doc.page_content}...")