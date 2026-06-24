def triage_agent(state):

    query = state.get("query", "").lower()

    category = "General"
    priority = "Medium"

    if any(word in query for word in [
        "payment",
        "refund",
        "billing",
        "money",
        "transaction"
    ]):
        category = "Billing"

    elif any(word in query for word in [
        "error",
        "bug",
        "login",
        "password",
        "issue",
        "technical"
    ]):
        category = "Technical"

    elif any(word in query for word in [
        "complaint",
        "bad",
        "angry",
        "worst"
    ]):
        category = "Complaint"
        priority = "High"

    elif any(word in query for word in [
        "urgent",
        "immediately",
        "asap"
    ]):
        priority = "High"

    state["category"] = category
    state["priority"] = priority

    return state