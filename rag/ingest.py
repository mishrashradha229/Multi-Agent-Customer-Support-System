from rag.knowledge_loader import load_knowledge
from rag.chroma_db import add_document


def ingest_documents():

    docs = load_knowledge("knowledge_base")

    for index, document in enumerate(docs):

        paragraphs = document.split("\n")

        for chunk_index, chunk in enumerate(paragraphs):

            chunk = chunk.strip()

            if len(chunk) > 20:

                add_document(

                    f"{index}_{chunk_index}",

                    chunk

                )

    print("Knowledge Base Indexed Successfully")


if __name__ == "__main__":

    ingest_documents()