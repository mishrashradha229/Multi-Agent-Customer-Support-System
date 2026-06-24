from rag.chroma_db import search_documents


def retrieve_faq(query):

    documents = search_documents(query)

    if len(documents) == 0:

        return None

    context = "\n".join(documents)

    return context


def retrieve_context(query):

    docs = search_documents(query)

    return "\n".join(docs)