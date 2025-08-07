from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = DirectoryLoader(
    path="./affirm_support_articles",  # your directory
    glob="**/*.txt",
    loader_cls=TextLoader,
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)

docs = text_splitter.split_documents(documents)
