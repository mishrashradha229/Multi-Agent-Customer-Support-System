from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.triage_agent import triage_agent
from agents.faq_agent import faq_agent
from agents.resolution_agent import resolution_agent
from agents.escalation_agent import escalation_agent
from agents.autoreply_agent import auto_reply_agent
from agents.closure_agent import closure_agent


class AgentState(TypedDict):
    query: str
    language: str
    category: str
    priority: str
    response: str
    resolved: bool
    create_ticket: bool
    ticket_status: str

def triage_node(state):
    return triage_agent(state)


def faq_node(state):
    return faq_agent(state)


def resolution_node(state):
    return resolution_agent(state)


def escalation_node(state):
    return escalation_agent(state)


def autoreply_node(state):
    return auto_reply_agent(state)


def closure_node(state):
    return closure_agent(state)

def faq_router(state):
    if state.get("resolved", False):
        return "autoreply"
    return "resolution"


def escalation_router(state):
    if state.get("create_ticket", False):
        return "closure"
    return "autoreply"

def final_output_node(state):
    """
    This is the ONLY clean output returned to UI.
    Prevents debug leakage.
    """
    return {
        "response": state.get("response", "No response generated."),
        "category": state.get("category", "General"),
        "priority": state.get("priority", "Medium"),
        "ticket_status": state.get("ticket_status", "Open"),
        "create_ticket": state.get("create_ticket", False),
        "resolved": state.get("resolved", False)
    }

def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("triage", triage_node)
    workflow.add_node("faq", faq_node)
    workflow.add_node("resolution", resolution_node)
    workflow.add_node("escalation", escalation_node)
    workflow.add_node("autoreply", autoreply_node)
    workflow.add_node("closure", closure_node)

    workflow.add_node("final_output", final_output_node)

    workflow.set_entry_point("triage")

    workflow.add_edge("triage", "faq")

    workflow.add_conditional_edges(
        "faq",
        faq_router,
        {
            "autoreply": "autoreply",
            "resolution": "resolution"
        }
    )

    workflow.add_edge("resolution", "escalation")

    workflow.add_conditional_edges(
        "escalation",
        escalation_router,
        {
            "autoreply": "autoreply",
            "closure": "closure"
        }
    )

    workflow.add_edge("autoreply", "closure")

    workflow.add_edge("closure", "final_output")

    workflow.add_edge("final_output", END)

    return workflow.compile()



if __name__ == "__main__":

    graph = build_graph()

    result = graph.invoke({
        "query": "My payment failed and money was deducted",
        "language": "English",
        "category": "",
        "priority": "",
        "response": "",
        "resolved": False,
        "create_ticket": True,
        "ticket_status": "Open"
    })

    print(result["response"])