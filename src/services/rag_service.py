# -*- coding: utf-8 -*-
# File: services/rag_service.py
# Description: Service for handling Retrieval-Augmented Generation from PDFs.

import logging
from typing import List

from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings


class RAGService:
    """Encapsulates the logic for PDF processing and vector search."""

    def __init__(self):
        # Initialize the embedding model once.
        # This model runs locally and converts text to vectors.
        self.embedding_model = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        logging.info("RAGService initialized with SentenceTransformer model.")

    def extract_text_from_pdfs(self, pdf_docs: List[any]) -> str:
        """Extracts raw text from a list of uploaded PDF files."""
        text = ""
        for pdf in pdf_docs:
            try:
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
            except Exception as e:
                logging.error(f"Error reading PDF {pdf.name}: {e}")
        return text

    def get_text_chunks(self, text: str) -> List[str]:
        """Splits a long text into smaller, manageable chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(text)
        return chunks

    def create_vector_store(self, text_chunks: List[str]) -> FAISS:
        """Creates a FAISS vector store from text chunks."""
        if not text_chunks:
            logging.warning("No text chunks provided to create vector store.")
            return None

        logging.info(
            f"Creating vector store from {len(text_chunks)} text chunks...")
        vector_store = FAISS.from_texts(
            text_chunks, embedding=self.embedding_model)
        logging.info("Vector store created successfully.")
        return vector_store

    def get_context_from_query(self, vector_store: FAISS, user_question: str) -> str:
        """Retrieves relevant context from the vector store based on a user query."""
        if not vector_store:
            return "No documents have been processed yet."

        docs = vector_store.similarity_search(user_question)
        context = "\n".join([doc.page_content for doc in docs])
        return context
