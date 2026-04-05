import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel

from agent.advertising_agent import run_agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Amazon Advertising Intelligence Agent API running"}

@app.post("/analyze")
def analyze(request: QueryRequest):

    user_query = request.query

    result = run_agent(user_query)

    return {
        "query": user_query,
        "analysis": result
    }