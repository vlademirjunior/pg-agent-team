Com certeza. Aqui estão todos os Arquivos de Decisão de Arquitetura (ADRs) em formato Markdown cru, prontos para você copiar e colar.

```markdown
# 0001: Adopt the `agno` Library for Agentic AI

* **Status:** Accepted
* **Date:** 2025-07-02

## Context

The project's core requirement is to translate natural language user requests into executable SQL queries. This involves complex interactions with a Large Language Model (LLM), including managing prompts, defining agent roles, providing tools for execution, and handling the model's responses. Building this infrastructure from scratch using raw API calls would be time-consuming, error-prone, and would require reinventing common patterns for agentic systems. Ineed a framework that abstracts this complexity and provides a structured way to build and manage AI agents.

## Decision

Iwill adopt the **`agno` library** as the foundational framework for building our AI agent system. Iwill leverage its core components:

1.  **`agno.agent.Agent`:** To define individual, specialized AI agents with specific roles, instructions, and models.
2.  **`agno.tools`:** To create and provide functions (like database interaction) that agents can execute.
3.  **`agno.team.Team`:** To orchestrate multiple agents, enabling them to collaborate on more complex tasks.

## Consequences

### Positive

* **Rapid Development:** `agno` provides high-level abstractions for agents, tools, and teams, significantly accelerating the development process.
* **Structured Approach:** The library encourages a structured way of thinking about agent design, promoting clear separation of roles and capabilities.
* **Built-in Tool Use:** The `@tool` decorator and tool-handling logic are built-in, simplifying the process of giving agents real-world capabilities.
* **Extensibility:** The framework is designed to be extensible, allowing for easy integration of different models and custom tools.

### Negative

* **Dependency:** The project becomes dependent on the `agno` library's architecture, features, and release cycle. Any limitations or bugs in the library could impact our project.
* **Learning Curve:** The team must learn the specific patterns and conventions of the `agno` library, which differs from using a model provider's raw API.
