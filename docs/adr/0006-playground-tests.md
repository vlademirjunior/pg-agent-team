# 0006: Adopt an Interactive Web UI for Testing

* **Status:** Accepted
* **Date:** 2025-07-04

## Context

The primary method for interacting with the agent team was through a single execution of the `main.py` script. This command-line approach is inefficient for iterative testing, debugging, and demonstration. It does not allow for a conversational flow and makes it cumbersome to quickly test different prompts or switch between interacting with the main team and its individual member agents.

## Decision

Iwill implement the **`agno.playground.Playground`** feature to provide an interactive, browser-based user interface for the agent system.

1. A new entry point, `playground.py`, will be created to house the web server logic, keeping it separate from the primary command-line application.
2. The Playground will be configured to serve all relevant agents: the main `db_query_team` for end-to-end testing, and the individual `sql_agent` and `db_inspector_agent` for isolated debugging.

## Consequences

### Positive

* **Improved Developer Experience:** Enables rapid, real-time testing and debugging of agents in a conversational format, significantly speeding up the development cycle.
* **Enhanced Demonstrability:** Provides a user-friendly web interface to showcase the project's capabilities to stakeholders without requiring them to use the command line.
* **Granular Testing:** The ability to select and chat with individual agents in the UI makes it easy to test and validate their specific behaviors in isolation.

### Negative

* **Added Dependencies:** Introduces web framework dependencies into the project, slightly increasing its complexity and installation size.
* **Local Server Requirement:** Running the playground requires running a local web server, which consumes system resources and occupies a network port.
