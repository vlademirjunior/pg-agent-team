# 0004: Utilize Dev Containers for Environment Management

* **Status:** Accepted
* **Date:** 2025-07-03

## Context

Setting up a local development environment for this project requires multiple components: a specific Python version, Python package dependencies, a running PostgreSQL database, and environment variables. Managing this setup manually across different developer machines (and different operating systems) is prone to errors, inconsistencies, and "it works on my machine" issues. This friction slows down onboarding and development.

## Decision

Iwill adopt the **VS Code Dev Containers** specification to define and manage the development environment. This will be implemented using a `.devcontainer/` directory containing:

1. **`Dockerfile`:** To build a container image for the Python application with all necessary system dependencies.
2. **`docker-compose.yml`:** To orchestrate the startup of both the application container and a separate PostgreSQL database container.
3. **`devcontainer.json`:** To configure the VS Code environment, including extensions, settings, and port forwarding.
4. An `init.sql` script will be used to automatically provision the database on its first launch.

## Consequences

### Positive

* **Consistency & Reproducibility:** Every developer gets an identical, fully configured environment with a single click, eliminating setup errors.
* **Simplified Onboarding:** New contributors can get started immediately without needing to manually install a database or configure Python environments.
* **Integrated Services:** The application and its database dependency are managed together, simplifying startup and shutdown.
* **Clean Host Machine:** All dependencies are encapsulated within Docker containers, keeping the developer's local machine clean.

### Negative

* **Prerequisite:** Requires developers to have Docker Desktop installed and running.
* **Resource Consumption:** Running Docker containers consumes more system resources (RAM, CPU) than running services natively.
* **Abstraction Layer:** Adds a layer of abstraction that can slightly complicate debugging low-level networking or file system issues.
