from itertools import chain
from fastapi import FastAPI
from server.utils.embedings import initialize_embeddings
import uvicorn
from server.utils.retrieval import query_agent
from fastapi import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/initialize")
async def initialize():
    return initialize_embeddings()


class AgentRequest(BaseModel):
    query: str


@app.post("/chat")
async def chat(request: AgentRequest):
    response = query_agent(request.query)
    return response


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
