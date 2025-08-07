from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()


loader = DirectoryLoader(
    path="./server/affirm_support_articles",  # your directory
    glob="**/*.txt",
    loader_cls=TextLoader,
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700, chunk_overlap=0, separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)

docs = text_splitter.split_documents(documents)

# Embed and store in Chroma
embedding = OpenAIEmbeddings()  # Or HuggingFaceEmbeddings(), etc.
db = Chroma.from_documents(
    documents=docs, embedding=embedding, persist_directory="./chroma_db"
)
db.persist()
print("Documents loaded and stored.")
