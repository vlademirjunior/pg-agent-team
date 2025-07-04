# Changelog - AI Agent Team for PostgreSQL Interaction

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
