# 0002: Implement a Multi-Agent Team Architecture

* **Status:** Accepted
* **Date:** 2025-07-02

## Context

The initial single-agent approach required one agent to handle multiple, distinct responsibilities: understanding the database schema, generating a SQL query, and executing it. This monolithic design is not robust. A single, complex prompt trying to define all these steps is more prone to error, hallucinations, and security vulnerabilities like prompt injection. As the complexity of the task grows, the reliability of a single agent decreases.

## Decision

Iwill refactor the system to use a **multi-agent team architecture** using `agno.team.Team` in "coordinate" mode. This involves breaking down the problem into specialized roles handled by different agents:

1. **`Database_Inspector_Agent`:** A simple agent whose only responsibility is to use the `fetch_table_schema` tool.
2. **`SQL_Generation_Agent`:** A powerful agent focused exclusively on writing secure SQL code, without access to any tools.
3. **`Database_Query_Team`:** A coordinator agent that follows a strict procedure to manage the workflow between the other two agents and execute the final query.

## Consequences

### Positive

* **Separation of Concerns:** Each agent has a single, well-defined job, making its prompts simpler, more direct, and more reliable.
* **Enhanced Security:** The agent responsible for writing SQL (`SQL_Generation_Agent`) has no access to execution tools, reducing the risk of unauthorized actions. The coordinator's rigid instructions also limit its ability to perform unintended operations.
* **Improved Reliability:** Simpler tasks for each agent lead to a lower probability of failure or unexpected behavior. The overall workflow becomes more predictable.
* **Easier Debugging:** If a step fails, it's immediately clear which specialized agent was responsible, simplifying the debugging process.

### Negative

* **Increased Workflow Complexity:** The overall system logic is now distributed across multiple agents and a coordinator, which can be more complex to trace than a single prompt.
* **Potential for Higher Latency:** There is a small overhead for passing information between agents, which could slightly increase the total response time compared to a single LLM call.
