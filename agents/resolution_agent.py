from llm.gemini import ask_llm


def resolution_agent(state):

    query = state["query"]

    prompt = f"""
You are an expert customer support assistant.

Customer Query:

{query}

Provide:
1. Problem analysis
2. Solution
3. Next steps

Respond politely.
"""

    response = ask_llm(prompt)

    state["response"] = response
    state["resolved"] = True

    return state