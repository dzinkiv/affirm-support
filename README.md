# affirm-support
The current Affirm support website only supports keyword-based search, which means natural language questions like “What happens if I miss my payment?” often return "Showing 0 of 0 results", even though relevant information exists in the support docs.

This project is a Retrieval-Augmented Generation (RAG) application that integrates LLMs with Affirm’s existing support documentation to provide more personalized, context-aware, and conversational responses to user questions.

By using semantic search and generative answers, it allows users to ask real-world, natural language questions and receive accurate answers drawn directly from Affirm’s documentation.
> ⚠️ _**Note**: This project was built in 1 day as a proof of concept, not a production-ready or polished application. It demonstrates the core functionality and architecture of a RAG system, but lacks proper error handling, scalability optimizations, security hardening, and UI refinements._

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
