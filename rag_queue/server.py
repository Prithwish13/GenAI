from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app = FastAPI()

@app.get('/')
def root():
    return {"status": "server is up and running"}


@app.post('/chat')
def chat(
    user_query: str = Query(..., description="the chat message")
):
    job = queue.enqueue(process_query, user_query)
    return {"status": "queued", "job_id": job.id}


# 518a5c85-2a22-4968-bcce-d8e9240fe485

@app.get('/job-status')
def get_result(
    job_id: str = Query(..., description="provide the job id")
):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result": result}