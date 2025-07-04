# AI Database Analyst for PostgreSQL

## Overview

An autonomous AI agent that understands natural language. Ask complex questions, and it will explore your PostgreSQL database, write advanced read-only SQL, and get you the answers-all while enforcing strict security constraints.

The system is built using the `agno` library and is designed with a modular, object-oriented architecture, making it easy to understand, maintain, and extend.

This project use RAG (Retrieval-Augmented Generation) to enhance the agent's capabilities.

## Features

- **Autonomous Reasoning**: The agent can independently plan and execute a multi-step process to answer complex questions, including exploring the database schema and fetching context from multiple tables.
- **Advanced SQL Generation**: Capable of writing complex, read-only `SELECT` queries that include `JOINs`, aggregations, and CTEs as needed.
- **Database Exploration**: Includes tools to dynamically list available schemas and tables, allowing it to work with databases it has never seen before.
- **Layered Security**: Enforces security through multiple layers: input sanitization before processing, strict "Prompt Shielding" with non-negotiable rules for the agent, and code-based validation on the final query to ensure it is read-only.
- **Interactive Playground**: Comes with a real-time web UI for interactively testing and chatting with the AI agents.
- **Dev Container Ready**: Includes a pre-configured development container for a consistent, one-click setup with zero local dependencies required besides Docker.

## Project Structure

The project is organized into a clean, modular structure to separate concerns:

```
├── .devcontainer/
│   ├── ...                     # Files for the Dev Container environment.
│   └── postgres/
│       ├── schema.sql          # SQL script to initialize the database schema.
├── docs/
│   ├── adr/                    # Architecture Decision Records.
│   ├── TESTS.md                # Documentation for testing the agent.
├── src/
│   ├── agents/
│   │   ├── agent_factory.py     # Builds and configures AI agents using a Factory pattern.
│   ├── config/
│   │   ├── database.py          # Configuration for database connection.
│   ├── services/
│   │   ├── rag_service.py       # Service for handling Retrieval-Augmented Generation from PDFs.
│   ├── tools/
│   │   ├── database_tools.py    # Contains functions (tools) for database interaction.
│   ├── __init__.py
│   ├── main.py                 # The CLI entry point that uses an AgentOrchestrator.
│   ├── playground.py           # The entry point for the interactive web UI.
│   ├── app.py                  # The Streamlit app (Helo) for interacting with AI Agents.
│   ├── .env-example            # Example environment variables file. (rename to .env and fill in your keys)
│   └── requirements.txt        # Lists the project's Python dependencies.
...
```

- **`agents/`**: The `AgentFactory` is responsible for creating configured agent instances.
- **`config/`**: Holds all static configuration, primarily the database connection details.
- **`services/`**: Contains services like `rag_service.py` for handling Retrieval-Augmented Generation from PDFs.
- **`tools/`**: Contains standalone functions decorated with `@tool` that the agent can use to interact with the database.
- **`main.py`**: A clean entry point that uses an `AgentOrchestrator` to run the agent via the command line.
- **`app.py`**: A Streamlit app (Helo) that provides a user-friendly interface for interacting with the AI agents.
- **`playground.py`**: Starts a web server to provide an interactive chat interface for the agent.

---

## Getting Started

### With Dev Containers (Recommended)

This is the easiest and most reliable way to run the project.

**Prerequisites:**

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Steps:**

1. **Clone the Repository:**

    ```bash
    git clone [https://github.com/vlademirjunior/pg-db-analyst-agent.git](https://github.com/vlademirjunior/pg-db-analyst-agent.git)
    cd pg-db-analyst-agent
    ```

2. **Set Environment Variables:** Create a file named `.env` in the root of the project and add your API keys:

    ```env
    # .env
    GROQ_API_KEY="your_groq_api_key_here"
    AGNO_API_KEY="your_agno_api_key_here"
    ```

3. **Open in Dev Container:**
    - Open the project folder in VS Code.
    - A notification will appear asking to "Reopen in Container". Click it.
    - VS Code will build the containers. The PostgreSQL database will be automatically created and seeded with the data from `.devcontainer/postgres/schema.sql`.

### Manual Local Setup

**Prerequisites:**

- Python 3.11+
- A running PostgreSQL instance.

**Steps:**

1. **Clone & Install Dependencies:**

    ```bash
    git clone [https://github.com/vlademirjunior/pg-db-analyst-agent.git](https://github.com/vlademirjunior/pg-db-analyst-agent.git)
    cd pg-db-analyst-agent
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. **Set Environment Variables:** Create a `.env` file as shown in the Dev Container setup above.
3. **Configure & Seed Database:**
    - Ensure your local PostgreSQL server is running.
    - Update `config/database.py` to point to your local instance (e.g., `host: "localhost"`).
    - Connect to your database and run the SQL commands from `.devcontainer/postgres/schema.sql` to create and populate the tables.

---

## Usage

You can interact with the agent in three ways.

### 1. Running the CLI Application

Execute the `main.py` script to run a predefined request. You can edit the `request` variable inside the script to test different questions.

```bash
python main.py
```

### 2. Running the Interactive Playground

Start the web server to connect a real-time chat interface (agno).

```bash
python playground.py
```

### 3. Using the Helo UI

Run Helo, a Streamlit app that provides a user-friendly interface for interacting with the AI agents.

```bash
streamlit run app.py
```

Open your browser and navigate to the URL provided in the terminal, which will look like:
**<https://app.agno.com/playground?endpoint=localhost:7777>**

---

## How It Works

This project uses a single, powerful autonomous agent that follows a dynamic reasoning process:

1. **Understand & Plan:** The agent first analyzes the user's request to determine the goal.
2. **Explore & Gather Context:** If it lacks knowledge of the database structure, it uses tools like `list_available_schemas` and `list_tables_in_schema` to explore. It then uses `fetch_table_schema` (potentially multiple times) to get the context needed to answer the question.
3. **Formulate & Secure Query:** With the necessary context, it constructs an advanced, read-only SQL query, applying its security constraints to ensure safety.
4. **Execute & Respond:** The final, validated query is run via the `execute_sql_query` tool, and the raw data is returned, ready for presentation.

## Next Steps

If you're interested in extending the agent's capabilities, consider:

- Adding more tools for different database operations.
- Implementing additional security measures.
- Adding @database and @rag to be specific about the database and RAG service (Helo app).
- Receive a document to get context from it to learn more about the database.
  - Improving the Answering process by integrating a Retrieval-Augmented Generation (RAG) service.
- Enhancing the RAG service to support more complex document retrieval scenarios.
  - Accepting multiple document formats (e.g., CSV, JSON).
- Integrating with other AI models or services for more advanced reasoning capabilities.

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
