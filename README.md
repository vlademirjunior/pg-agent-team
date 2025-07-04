# AI Agent Team for PostgreSQL Interaction

## Overview

This project demonstrates the power of a multi-agent AI team to translate natural language requests into secure, read-only SQL queries and execute them against a PostgreSQL database. Instead of writing complex SQL manually, you can simply describe the data you need, and the agent team will handle the rest.

The system is built using the `agno` library and is designed with a modular architecture, making it easy to understand, maintain, and extend.

## Features

- **Natural Language to SQL**: Converts plain English requests into precise PostgreSQL queries.
- **Multi-Agent System**: Utilizes a specialized team of AI agents, each with a distinct role (coordination, schema inspection, SQL generation).
- **Secure by Design**: Enforces read-only operations by validating queries to prevent unauthorized data modification (`INSERT`, `UPDATE`, `DELETE`, etc.).
- **Modular & Extensible**: The codebase is organized into logical modules for configuration, tools, and agent definitions, making it easy to add new functionality.
- **Automated Workflow**: The team coordinator autonomously manages the entire process, from understanding the database structure to executing the final query and returning the result.
- **Dev Container Ready**: Comes with a pre-configured development container for a consistent, reproducible environment with zero local setup required.

## Project Structure

The project is organized into a clean, modular structure to separate concerns:

```text
├── agents/
│   ├── __init__.py
│   └── team_definitions.py   # Defines the individual agents and the coordinating team.
├── config/
│   ├── __init__.py
│   └── database.py           # Stores database connection settings.
├── tools/
│   ├── __init__.py
│   └── database_tools.py     # Contains functions (tools) for database interaction.
├── main.py                   # The main entry point to run the application.
└── requirements.txt          # Lists the project's Python dependencies.
````

- **`config/`**: Holds all static configuration, primarily the database connection details.
- **`tools/`**: Contains standalone functions decorated with `@tool` that agents can use. These functions are the bridge between the AI and the database.
- **`agents/`**: Defines the properties, roles, and instructions for each AI agent and assembles them into a cohesive team.
- **`main.py`**: A clean entry point that initializes the system and starts the agent team with a user request.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.11+
- A running PostgreSQL instance.
- An API key from [Groq](https://console.groq.com/keys) (or another model provider supported by `agno`).

### 2. Clone the Repository

```bash
git clone git@github.com:vlademirjunior/pg-agent-team.git
cd pg-agent-team
````

## Getting Started with Dev Containers (Recommended)

This is the easiest and most reliable way to run the project. It automatically sets up the database, Python environment, and VS Code.

### Prerequisites

- Docker
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Steps

1. **Set Environment Variable**: Before opening the project, ensure your `GROQ_API_KEY` is available as an environment variable on `.devcontainer/devcontainer.json` or your host machine. The Dev Container is configured to inherit it.

    ```bash
    export GROQ_API_KEY="your_groq_api_key_here"
    ```

2. **Open in Dev Container**:
    - Clone the repository to your local machine.
    - Open the project folder in VS Code.
    - A notification will appear in the bottom-right corner asking if you want to "Reopen in Container". Click it.

    ![Reopen in Container](https://code.visualstudio.com/assets/docs/remote/reopen-in-container.png)

3. **Run the Application**:
    - VS Code will build and start the containers. This might take a few minutes on the first run. The PostgreSQL database will be automatically created and initialized with the data from `init.sql`.
    - Once the container is ready, open a new terminal in VS Code (it will be a terminal inside the container).
    - Run the application:

        ```bash
        python main.py
        ```

### 3. Install Dependencies (Without Dev Container)

Create a virtual environment (recommended) and install the required packages.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venvScriptsactivate`

# Install dependencies (Without Dev Container)
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (Without Dev Container)

For security, it's best to handle your API key via an environment variable.

```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

### 5. Configure the Database

Update the database connection details in `config/database.py` to match your PostgreSQL setup.

```python
# config/database.py
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "your_db_name",
    "user": "your_db_user",
    "password": "your_db_password",
}
```

### 6. Create the Database Table (Example)

Connect to your PostgreSQL database and run the following SQL script to create the `items` table and populate it with some sample data.

```sql
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price NUMERIC(10, 2),
    stock_quantity INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, category, price, stock_quantity) VALUES
('Laptop', 'Electronics', 1200.00, 50),
('Smartphone', 'Electronics', 800.00, 150),
('Desk Chair', 'Furniture', 250.50, 75),
('Coffee Maker', 'Appliances', 89.99, 200),
('Running Shoes', 'Apparel', 120.00, 300);
```

## Usage (v1.0)

With the setup complete, you can run the project from the root directory:

```bash
python main.py
```

The script will execute with the predefined request in `main.py`. You can modify the `user_data_request` variable to ask for different data and see how the agent team responds.

## How It Works

The magic of this project lies in its autonomous, coordinated workflow:

1. **Initiation**: The `main.py` script provides an initial natural language request to the `db_query_team`.
2. **Delegation (Schema)**: The team coordinator first delegates a task to the `Database_Inspector_Agent`, asking it to fetch the schema for the requested table using the `fetch_table_schema` tool.
3. **Delegation (SQL Generation)**: With the schema in hand, the coordinator delegates a new task to the `SQL_Generation_Agent`. It provides the schema and the original user request, asking the agent to write a valid and secure SQL query.
4. **Execution**: The coordinator receives the generated SQL query. It then uses its own `execute_sql_query` tool to run the query against the database.
5. **Response**: The final JSON result from the database is returned as the output of the team's run.
