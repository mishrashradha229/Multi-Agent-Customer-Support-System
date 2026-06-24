import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(path="chroma_db")


collection = client.get_or_create_collection(
    name="customer_support_kb"
)


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(text):

    embedding = embedding_model.encode(text)

    return embedding.tolist()


def add_document(doc_id, text):

    collection.add(

        ids=[doc_id],

        documents=[text],

        embeddings=[get_embedding(text)]

    )


def search_documents(query, top_k=3):

    result = collection.query(

        query_embeddings=[get_embedding(query)],

        n_results=top_k

    )

    return result["documents"][0]