from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


data_dir = os.path.join("data", "raw_procedures")

def load_procedures():
    loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

if __name__ == "__main__": # veut dire que ce code ne s'exécutera que si ce fichier est exécuté directement, pas s'il est importé comme module
    docs = load_procedures()


def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    txt_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    splits = txt_splitter.splitdocuments(documents)
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
