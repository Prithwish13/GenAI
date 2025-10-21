from langchain.prompts import PromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
 
from dotenv import load_dotenv

load_dotenv()

v_store = QdrantVectorStore.from_existing_collection(
    collection_name="youtube-chatbot",
    url="http://localhost:6333",
    embedding=OpenAIEmbeddings(model="text-embedding-3-large")
)

chat_model = ChatOpenAI(model="gpt-4-turbo", temperature=0)
retriever = v_store.as_retriever(search_kwargs={"k": 4}, search_type="similarity")
parser = StrOutputParser()


template = PromptTemplate(
    template="""You are a helpful AI assistant that helps people find information about YouTube videos based on the provided context.
    Use the following context to answer the question at the end.
    Context: {context}
    Question: {question}
    If you don't know the answer, just say that you don't know. Do not try to make up an answer.
    """,
    input_variables=["context", "question"],
    )

def format_docs(content):
    return "\n\n\n".join(doc.page_content for doc in content)



query = "Is ere any discussion about aliens in the video? if yes provide details."
# ------------- Without using a chain -----------------------------------

# response = retriever.invoke(query)
# context_text = "\n\n".join(doc.page_content for doc in response)

# final_prompt = template.invoke(
#    { 
#     "context": context_text,
#      "question": query
#    }
# )

# chat_response = chat_model.invoke(final_prompt)
# print(f"🤖 {chat_response.content}")

# ---------------------------------------- With using a chain ----------------------------------------
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})
main_chain = parallel_chain | template | chat_model | parser

response = main_chain.invoke("What is the future of AI?")

print(response)

