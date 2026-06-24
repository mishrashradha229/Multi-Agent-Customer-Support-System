def escalation_agent(state):

    query = state.get("query", "").lower()

    if (
        "book ticket" in query
        or "raise ticket" in query
        or "create ticket" in query
        or state.get("priority") == "High"
    ):

        state["create_ticket"] = True
        state["ticket_status"] = "Open"
        state["response"] = "Your ticket has been created successfully. Our team will contact you."

    else:
        state["response"] = state.get("response", "Issue resolved.")

    return state