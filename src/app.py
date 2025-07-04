# -*- coding: utf-8 -*-
# File: app.py
# Description: A clean, object-oriented Streamlit application for interacting with AI agents.

import streamlit as st
from dotenv import load_dotenv
import json
import pandas as pd
from typing import Any

from agents.agent_factory import agent_factory
from services.rag_service import RAGService
from main import JsonDecimalEncoder  # Reusing the custom encoder


class ChatUI:
    """Handles the rendering of the Streamlit user interface."""

    def __init__(self, title: str, page_icon: str = "🤖"):
        st.set_page_config(
            page_title=title,
            page_icon=page_icon,
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.title(title)
        st.caption(
            "Ask questions about your database or the documents you've uploaded.")

    def setup_sidebar(self, rag_service: RAGService):
        """Sets up the sidebar for PDF document uploads and processing."""
        with st.sidebar:
            st.header("Document Analysis")
            pdf_docs = st.file_uploader(
                "Upload your PDF documents here", accept_multiple_files=True, type="pdf"
            )
            if st.button("Process Documents"):
                if not pdf_docs:
                    st.warning("Please upload at least one PDF document.")
                    return

                with st.spinner("Processing documents..."):
                    raw_text = rag_service.extract_text_from_pdfs(pdf_docs)
                    text_chunks = rag_service.get_text_chunks(raw_text)
                    st.session_state.vector_store = rag_service.create_vector_store(
                        text_chunks)
                    st.success("Documents processed successfully!")

    def display_chat_history(self):
        """Displays the entire chat history from the session state."""
        for message in st.session_state.get("messages", []):
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html=True)

    def add_message(self, role: str, content: str):
        """Adds a message to the chat history and displays it."""
        st.session_state.messages.append({"role": role, "content": content})
        with st.chat_message(role):
            st.markdown(content, unsafe_allow_html=True)


class AppController:
    """Handles the core application logic, including routing and agent orchestration."""

    def __init__(self, data_agent, presentation_agent, rag_agent, rag_service):
        self.data_agent = data_agent
        self.presentation_agent = presentation_agent
        self.rag_agent = rag_agent
        self.rag_service = rag_service
        self.db_keywords = ['table', 'database', 'sql',
                            'customer', 'order', 'item', 'schema']

    def _format_response(self, raw_data: Any) -> str:
        """Intelligently formats the raw data from the agent into a displayable string."""
        if isinstance(raw_data, str):
            return raw_data
        if isinstance(raw_data, list) and all(isinstance(i, str) for i in raw_data):
            return "Here are the results I found:\n\n" + "\n".join([f"- `{item}`" for item in raw_data])
        if isinstance(raw_data, list) and raw_data and isinstance(raw_data[0], dict):
            df = pd.DataFrame(raw_data)
            return "Here are the results I found:\n\n" + df.to_markdown(index=False)

        # Fallback for any other data type
        return f"```json\n{json.dumps(raw_data, indent=2, cls=JsonDecimalEncoder, ensure_ascii=False)}\n```"

    def _handle_database_request(self, prompt: str) -> str:
        """Orchestrates the database agent and presentation agent."""
        with st.spinner("Analyzing your question and querying the database..."):
            # The orchestrator from main.py is no longer needed here.
            # We directly call the agents.
            data_response = self.data_agent.run(prompt)
            raw_data = data_response.content

            if raw_data == "INVALID_REQUEST":
                return "The request was deemed invalid by the data agent."

            if "json" in prompt.lower():
                return self._format_response(raw_data)
            else:
                presentation_prompt = (
                    f"Here is the data: {json.dumps(raw_data, cls=JsonDecimalEncoder)}\n\n"
                    f"Based on this data, please answer the user's original question: '{prompt}'"
                )
                presentation_response = self.presentation_agent.run(
                    presentation_prompt)
                return presentation_response.content

    def _handle_rag_request(self, prompt: str) -> str:
        """Handles a request for document analysis."""
        if not st.session_state.get("vector_store"):
            return "Please upload and process documents before asking questions about them."

        with st.spinner("Searching documents..."):
            context = self.rag_service.get_context_from_query(
                st.session_state.vector_store, prompt)
            rag_prompt = f"Context:\n{context}\n\nQuestion: {prompt}"
            rag_response = self.rag_agent.run(rag_prompt)
            return rag_response.content

    def handle_prompt(self, prompt: str) -> str:
        """Routes the user prompt to the correct handler and returns the final response."""
        if any(keyword in prompt.lower() for keyword in self.db_keywords):
            return self._handle_database_request(prompt)
        else:
            return self._handle_rag_request(prompt)


class ChatApplication:
    """The main application class that ties the UI and Controller together."""

    def __init__(self):
        load_dotenv()
        self.ui = ChatUI(title="Helo")
        self.controller = self._initialize_controller()
        self._initialize_session_state()

    def _initialize_controller(self) -> AppController:
        """Initializes all necessary services and agents for the controller."""
        rag_service = RAGService()
        return AppController(
            data_agent=agent_factory.create_data_analyst_agent(),
            presentation_agent=agent_factory.create_presentation_agent(),
            rag_agent=agent_factory.create_rag_docs_agent(),
            rag_service=rag_service
        )

    def _initialize_session_state(self):
        """Sets up the initial session state for chat messages and the vector store."""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "vector_store" not in st.session_state:
            st.session_state.vector_store = None

    def run(self):
        """Runs the main application loop."""
        self.ui.setup_sidebar(self.controller.rag_service)
        self.ui.display_chat_history()

        if prompt := st.chat_input("Ask a question..."):
            self.ui.add_message("user", prompt)

            with st.chat_message("assistant"):
                response = self.controller.handle_prompt(prompt)
                st.markdown(response, unsafe_allow_html=True)
                # Add the final assistant message to history *after* displaying it
                st.session_state.messages.append(
                    {"role": "assistant", "content": response})


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
