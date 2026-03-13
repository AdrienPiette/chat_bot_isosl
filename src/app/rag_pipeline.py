from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

DATA_DIR = os.path.join("data", "raw_procedures")


def load_procedures():
    """Charge tous les PDF du dossier en Documents LangChain."""
    loader = DirectoryLoader(DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Découpe les Documents en chunks plus petits."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    
    splits = text_splitter.split_documents(documents)
    return splits


if __name__ == "__main__":
    docs = load_procedures()
    print(f"Docs bruts : {len(docs)}")

    if not docs:
        print("Aucun PDF trouvé dans data/raw_procedures. Ajoute des fichiers pour continuer.")
    else:
        splits = split_documents(docs)
        print(f"Chunks après découpe : {len(splits)}")
        print("\nExemple de chunk :")
        print(splits[0].page_content[:400])
        print("Métadonnées :", splits[0].metadata)
