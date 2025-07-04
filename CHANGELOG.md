# Changelog - AI Agent Team for PostgreSQL Interaction

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Released]

### Added

- ...

## [1.1.0] - 2025-07-09

### Added

- Streamlit Web Application: Introduced a full-featured web application (app.py) for a rich, interactive chat experience.

- RAG Functionality: Implemented a Retrieval-Augmented Generation (RAG) pipeline using a RAGService to allow users to upload PDF documents and ask questions about their content.

- New Services and Dependencies: Integrated streamlit, langchain, faiss-cpu, pypdf, and sentence-transformers.

### Changed

Agent Factory was updated to include the new RAG agent, which can now handle document-based queries in addition to database queries. Also, the agent's instructions were updated to reflect the new capabilities (Added workflow structure as well).

## [1.0.0] - 2025-07-06

- This marks the first stable public release of the AI Database Analyst.

### Added

- Autonomous AI Agent: Core functionality driven by a single, autonomous agent capable of reasoning, planning, and executing complex database queries.

- Advanced SQL Generation: Agent can generate complex, read-only SELECT queries, including JOINs and aggregations, based on natural language.

- Database Exploration: Tools for the agent to dynamically discover schemas and tables (list_available_schemas, list_tables_in_schema), allowing it to work with unfamiliar databases.

- Layered Security Model: Implemented a robust security posture including input sanitization, strict prompt shielding with non-negotiable rules, and code-based validation of SQL queries.

- Modular & OOP Architecture: The project was refactored to follow Clean Code principles, using an AgentFactory pattern and an AgentOrchestrator to separate concerns (SRP, DRY).

- Interactive Web UI: An Agno Playground was added (playground.py) for real-time testing and interaction with the agents.

- Dev Container Environment: Full support for a consistent development environment using Docker, including a PostgreSQL service and automatic database seeding (init.sql).

- Comprehensive Documentation: Includes a detailed README.md, Architectural Decision Records (ADRs), and this CHANGELOG.md.

## [0.7.0] - 2025-07-05

### Changed

- Clean Code Refactor: Applied OOP, SOLID, and Clean Code principles across the project.
- Refactored tools/database_tools.py to use an object-oriented DatabaseManager class, centralizing connection logic and applying SRP/DRY.
- Refactored main.py into an AgentOrchestrator class to encapsulate the main application flow and separate concerns.
- Refactored agents/team_definitions.py into agents/agent_factory.py, using a Factory pattern to build agents, improving modularity and applying the Single Responsibility Principle.

## [0.6.0] - 2025-07-05

### Added

- New `list_available_schemas` and `list_tables_in_schema` tools to enable the agent to perform full database exploration.

### Changed

- **Architectural Refactor**: Replaced the entire multi-agent team with a single, more powerful `Autonomous_DB_Analyst_Agent`.
- Modified agent instructions from a rigid, step-by-step algorithm to a dynamic, reasoning-based workflow to handle complex, multi-table queries (e.g., with JOINs).
- Integrated security constraints directly into the autonomous agent's prompt, combining flexibility with safety.

### Removed

- Deprecated the specialized `Database_Query_Team`, `SQL_Generation_Agent`, and `Database_Inspector_Agent` in favor of the new single-agent model.

## [0.5.0] - 2025-07-04

### Added

- Interactive `Agno Playground UI` via `playground.py` for real-time agent interaction.
- Security sanitization layer in `main.py` to validate user input against common injection patterns.

### Changed

- **Security Hardening**: Hardened agent and team prompts to implement security best practices like Prompt Shielding and reducing Excessive Agency (OWASP LLM01, LLM05).
- Translated all Python source files, comments, and docstrings from Portuguese to English for broader accessibility.

## [0.4.0] - 2025-07-03

### Added

- Full **Dev Container** support with a `.devcontainer/` directory.
- `Dockerfile` for the Python application service, including necessary system dependencies.
- `docker-compose.yml` to orchestrate the application and a PostgreSQL database service.
- `init.sql` script for automatic database table creation and data seeding on first launch.

### Changed

- Updated database configuration in `config/database.py` to connect to the Docker service name (`db`) instead of `localhost`.

## [0.3.0] - 2025-07-03

### Added

- Modular project structure with `agents/`, `config/`, and `tools/` directories.
- `__init__.py` files to define Python packages, enabling cross-module imports.
- `requirements.txt` for explicit dependency management.

### Changed

- **Refactor**: Migrated all code from a single `main.py` script into their respective modules for better organization and maintainability.

## [0.2.0] - 2025-07-02

### Added

- Multi-agent architecture using `agno.team.Team` to orchestrate a complex workflow.
- Introduced `SQL_Generation_Agent` for the specialized task of writing SQL queries.
- Introduced `Database_Inspector_Agent` for fetching table schemas using tools.
- Created `Database_Query_Team` to coordinate the workflow between the specialized agents and execute the final query.

### Changed

- Replaced the initial single-agent logic with a more robust, coordinated team approach.

## [0.1.0] - 2025-06-30

### Added

- Initial project concept in a single `main.py` script.
- Core logic to generate and execute a SQL query from a natural language prompt using a single `agno` agent.
- Basic database connection management for PostgreSQL.
