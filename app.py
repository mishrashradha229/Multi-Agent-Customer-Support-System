import streamlit as st

from graph.workflow import build_graph
from database.ticket_manager import (
    create_ticket,
    get_all_tickets,
    close_ticket
)

from agents.voice_agent import speech_to_text, text_to_speech
from agents.multilingual_agent import translate_text



st.set_page_config(
    page_title="Multi-Agent Customer Support System",
    page_icon="🤖",
    layout="wide"
)
if "messages" not in st.session_state:
    st.session_state.messages = []

if "graph" not in st.session_state:
    st.session_state.graph = build_graph()



st.sidebar.title("🤖 Customer Support")

page = st.sidebar.radio(
    "Navigation",
    ["Chat Support", "Voice Support", "Service", "Tickets", "Billing and payment"]
)

language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "French", "Spanish"]
)

st.sidebar.markdown("---")
st.sidebar.success("System Status: Online")



if page == "Chat Support":

    st.title("🤖 Multi-Agent Customer Support System")
    st.caption("Hi! Ask your query below.")

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Type your query...")

    if prompt:

        
        translated_query = translate_text(prompt, target_language="English")

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.write(prompt)

        with st.spinner("Thinking..."):

            state = {
                "query": translated_query,
                "language": language,
                "category": "",
                "priority": "",
                "response": "",
                "resolved": False,
                "create_ticket": False,
                "ticket_status": "Open"
            }

            
            result = st.session_state.graph.invoke(state)

            
            response = result.get("response", "No response from system.")

            
            translated_response = translate_text(
                response,
                target_language=language
            )

        with st.chat_message("assistant"):
            st.write(translated_response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": translated_response
        })

        if result.get("create_ticket", False):

            ticket_id = create_ticket(
                customer="Guest",
                query=prompt,
                category=result.get("category", "General"),
                priority=result.get("priority", "Medium"),
                status="Open"
            )

            st.success(f"🎫 Ticket Created Successfully: {ticket_id}")

elif page == "Voice Support":

    st.title("🎤 Voice Support")
    st.write("Click the button and speak your issue.")

    if st.button("Start Recording"):

        user_text = speech_to_text()

        st.write("You said:")
        st.info(user_text)

        state = {
            "query": user_text,
            "language": language,
            "category": "",
            "priority": "",
            "response": "",
            "resolved": False,
            "create_ticket": False,
            "ticket_status": "Open"
        }

        result = st.session_state.graph.invoke(state)

        response = result.get("response", "No response generated.")

        st.success("AI Response:")
        st.write(response)
        audio_file = text_to_speech(response)

        if audio_file:
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")

elif page == "Service":

    st.title("📚 Service / Knowledge Base")

    question = st.text_input("Ask your question")

    if st.button("Search"):

        state = {
            "query": question,
            "language": language,
            "route": "faq",
            "category": "",
            "priority": "",
            "response": "",
            "resolved": False,
            "create_ticket": False,
            "ticket_status": "Open"
        }

        result = st.session_state.graph.invoke(state)

        st.write(result.get("response", "No answer found."))

elif page == "Tickets":

    st.title("🎫 Customer Tickets")

    tickets = get_all_tickets()

    if not tickets:
        st.info("No tickets found.")
    else:
        for ticket in tickets:

            with st.expander(f"Ticket {ticket['ticket_id']}"):

                st.write(f"Customer: {ticket['customer']}")
                st.write(f"Query: {ticket['query']}")
                st.write(f"Category: {ticket['category']}")
                st.write(f"Priority: {ticket['priority']}")
                st.write(f"Status: {ticket['status']}")

                if ticket["status"] == "Open":

                    if st.button(f"Close {ticket['ticket_id']}"):

                        close_ticket(ticket["ticket_id"])
                        st.success("Ticket Closed Successfully")
                        st.rerun()

st.markdown("---")
st.caption("Multi-Agent Customer Support System | made by Anjana")