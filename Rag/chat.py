

from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

# Vector embedding for the above chunks
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# Take the user query

user_query = input("Ask something 👉 ")

# Doing a similarity search (returns relevant chunks)

search_result = vector_db.similarity_search(user_query)

context= "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
          for result in search_result
         ])

SYSTEM_PROMPT = f"""
 You are a helpful AI Assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

 You should only answer the user based on the following context and navigate the user to open the right page number to know more.
 
 Context: {context}
"""
messages  = [
    SystemMessage(
        content=SYSTEM_PROMPT
    ),
    HumanMessage(
        content=user_query
    )
]

model = ChatOpenAI(model="gpt-5")
response = model.invoke(messages)

print(f"🤖 {response.content}")
