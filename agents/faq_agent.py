from rag.retriever import retrieve_faq


def faq_agent(state):

    query = state.get("query", "")

    answer = retrieve_faq(query)

    if answer:

        state["response"] = answer
        state["resolved"] = True
        state["create_ticket"] = True
        state["ticket_status"] = "Resolved"

    else:

        state["resolved"] = False
        state["response"] = "I couldn't find an answer in the knowledge base."

        state["ticket_status"] = "Pending Escalation"

    return state