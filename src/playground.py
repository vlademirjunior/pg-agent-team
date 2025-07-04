# -*- coding: utf-8 -*-
# File: playground.py
# Description: Starts the Agno Playground UI using the AgentFactory.

import logging
import sys
from dotenv import load_dotenv

from agno.playground import Playground, serve_playground_app
from agents.agent_factory import agent_factory

# --- Setup ---
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)

# --- Global App Definition ---
# Create agent instances from the factory at the module level.
data_analyst_agent = agent_factory.create_data_analyst_agent()
presentation_agent = agent_factory.create_presentation_agent()

# Define the list of agents to be served.
agents_for_playground = [
    data_analyst_agent,
    presentation_agent
]

# Create the Playground instance.
playground = Playground(agents=agents_for_playground)

# Define the 'app' variable at the global scope so the server can find it.
app = playground.get_app()


# --- Main execution block to run the web server ---
if __name__ == "__main__":
    """
    This block is executed when the script is run directly.
    It starts the web server to serve the globally defined 'app' object.
    """
    logging.info("Starting Agno Playground UI at http://localhost:7777")
    serve_playground_app("playground:app", reload=True, port=7777)
