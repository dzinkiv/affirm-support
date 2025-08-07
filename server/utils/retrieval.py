from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

# Setup
persist_directory = "./chroma_db"
llm = ChatOpenAI(model="gpt-4", temperature=0)
embeddings = OpenAIEmbeddings()

# Load the vectorstore
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Define a prompt
template = """You are Affirm's customer support assistant.
Your task is to help the user by answering their questions based on the provided context from Affirm's support articles.
Use the following pieces of context to answer the question at the end.
In the case you don't know the answer, don't try to make up an answer, instead suggest submitting the form at https://helpcenter.affirm.ca/s/contact-us?language=en_US or call on toll-free number, 888-484-4282, or at 416-987-1436 between the hours of 8:00 am and 11:00 pm ET seven days a week.
Always say "If there's anything else I can help you with, please let me know." at the end of the answer.
Always use first person pronouns like "we" and "us" in the answer.

{context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)

# Optional: memory to keep chat history
memory = ConversationBufferMemory(return_messages=True)

# LCEL pipeline
chain = (
    {
        "question": RunnablePassthrough(),
        "context": retriever
        | (lambda docs: "\n\n".join([doc.page_content for doc in docs])),
    }
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)


def query_agent(query: str) -> str:
    response = chain.invoke(query)
    return response


# # Interactive loop
# try:
#     print("How can I help you?")
#     while True:
#         query = input()
#         if query.lower() == "/exit":
#             break

#         response = chain.invoke(query)
#         print("\nAnswer:", response)
# except KeyboardInterrupt:
#     print("Exiting...")
