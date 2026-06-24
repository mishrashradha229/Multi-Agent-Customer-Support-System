def auto_reply_agent(state):

    reply = f"""
Hello,

Thank you for contacting our support team.

{state.get("response","")}

If you have any further questions, feel free to reach out.

Regards,
Customer Support Team
"""

    state["response"] = reply.strip()

    return state