def closure_agent(state):

    query = state.get("query", "").lower()

    close_words = [

        "thanks",
        "thank you",
        "resolved",
        "fixed",
        "done",
        "okay",
        "ok"

    ]

    if any(word in query for word in close_words):

        state["ticket_status"] = "Closed"

        state["response"] = (
            "Glad we could help! "
            "Your support ticket has been closed."
        )

    else:

        state["ticket_status"] = "Open"

    return state