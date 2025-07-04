# 0009: Adopt Langchain and FAISS for RAG Functionality

* **Status:** Accepted
* **Date:** 2025-07-09

## Context

The application requires a "Chat with Documents" feature, which necessitates a Retrieval-Augmented Generation (RAG) pipeline. This pipeline involves extracting text from PDFs, splitting it into chunks, generating vector embeddings for those chunks, and storing them in a vector database to enable semantic similarity searches.

The use of the native knowledge management tools from the `agno` library was considered, specifically `agno.knowledge` in conjunction with `agno.vectordb.PgVector`.

## Decision

I decided to implement the RAG pipeline using a stack of technologies external to `agno`, composed of **PyPDF, Langchain, Sentence-Transformers, and FAISS**.

1. **PyPDF:** For text extraction from PDF files.
2. **Langchain:** For the logic of splitting text into chunks (`RecursiveCharacterTextSplitter`).
3. **Sentence-Transformers:** For generating vector embeddings locally.
4. **FAISS:** For creating a fast and efficient in-memory vector database.

This decision was made because the alternative (`agno.knowledge` + `PgVector`) would require installing and configuring the `pgvector` extension in our PostgreSQL database, which would add significant dependency and complexity to our database infrastructure.

## Consequences

### Positive

* **Decoupled Architecture:** Our RAG functionality is completely independent of our main database. The vector database (FAISS) is created in memory for each session, which is ideal for an application where documents are temporary.
* **Simplicity and Portability:** It avoids the need to manage a complex database extension. The solution is self-contained within the Python application.
* **Use of Industry Standards:** Langchain is the industry-standard library for LLM and RAG orchestration, offering robust and well-tested components.
* **Efficiency:** FAISS is extremely fast for in-memory similarity searches, which is perfect for the scale of this application.

### Negative

* **Increased Dependencies:** It adds several significant dependencies to the project (`langchain`, `faiss-cpu`, etc.) that need to be managed.
* **State Management:** Since the vector database is created in memory, it needs to be managed via `st.session_state` to persist during the user's session, but not between different sessions.
