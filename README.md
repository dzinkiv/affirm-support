# affirm-support
A customer support website for Affirm utilizing LLMs for a personalized issue resolution. This is a Retrieval-Augmented Generation (RAG) application, leveraging LLMs and Affirm's support docs to provide accurate, context-aware support responses.
> ⚠️ _**Note**: This project was built in 1 day as a proof of concept, not a production-ready or polished application. It demonstrates the core functionality and architecture of a RAG (Retrieval-Augmented Generation) system, but lacks proper error handling, scalability optimizations, security hardening, and UI refinements._

## Demo
![UI Demo](https://github.com/dzinkiv/affirm-support/blob/ee624bdbd96d205b0a94a60bca2497de23554af0/resources/ui_demo.gif?raw=true)

## Diagram
![Affirm Support Flow Diagram](resources/flow.jpeg)
> _Note: This project was inspired by concepts from the [LangChain: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) course on DeepLearning.ai_

### Running Backend
#### Add OpenAI API key to .env
```
OPENAI_API_KEY=<sk-proj-your-api-key>
```

#### Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
#### Install all dependencies
```
cd server
pip install -r requirements.txt
cd ..
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
