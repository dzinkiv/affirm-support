# affirm-support
A customer support website for Affirm utilizing LLMs for a personalized issue resolution. This is a Retrieval-Augmented Generation (RAG) application, leveraging LLMs and Affirm's support docs to provide accurate, context-aware support responses.

## Diagram
![Affirm Support Flow Diagram](resources/flow.jpeg)
> _Note: This project was inspired by concepts from the [LangChain: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) course on DeepLearning.ai_

### Running Backend
#### Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
#### Install all dependencies
```
pip install -r requirements.txt
```
#### Start the server
```
uvicorn server.main:app --reload --host 0.0.0.0 --port 8000
```

### Running Frontend
#### Install all dependencies
```
cd frontend
npm i
```
#### Start the app
```
npm run dev
```