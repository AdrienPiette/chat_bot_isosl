from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


data_dir = os.path.join("data", "raw_procedures")

def load_procedures():
    loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    docs = load_procedures()


def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    txt_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_fonction=len
    )
    splits = txt_splitter.splitdocuments(documents)
    return splits

if __name__ == "__main__":
    splits = split_documents(docs)

