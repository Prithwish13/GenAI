from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/#use-in-subgraphs")

doc = loader.load()

print(doc[0].page_content)
# print(doc[0].metadata)