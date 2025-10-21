from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

load_dotenv()

video_id = "Gfr50f6ZBvo"

ytt_api = YouTubeTranscriptApi()
splitter =  RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

try:
    transcript_list = ytt_api.fetch(video_id=video_id,languages=['en'])
    transcript = " ".join(item.text for item in transcript_list)
        
except TranscriptsDisabled:
    print("NO Caption available for this video")
    
chunks = splitter.split_text(transcript)

v_store = QdrantVectorStore.from_texts(
    collection_name="youtube-chatbot",
    url="http://localhost:6333",
    embedding=embedding_model,
    texts=chunks
)

print("Indexing of YouTube video transcript is done")
    