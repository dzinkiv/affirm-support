from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()


def initialize_embeddings(
    articles_path="./affirm_support_articles", persist_directory="./chroma_db"
):
    loader = DirectoryLoader(
        path=articles_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
    )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700, chunk_overlap=0, separators=["\n\n", "\n", r"(?<=\. )", " ", ""]
    )
    docs = text_splitter.split_documents(documents)
    embedding = OpenAIEmbeddings()
    db = Chroma.from_documents(
        documents=docs, embedding=embedding, persist_directory=persist_directory
    )
    db.persist()
    print("Documents loaded and stored.")
    return {"status": "initialized", "count": len(docs)}
