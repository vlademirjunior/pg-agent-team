# -*- coding: utf-8 -*-
# File: playground.py
# Description: Starts the Agno Playground UI for real-time interaction with agents.

import logging
import sys
from dotenv import load_dotenv

from agno.playground import Playground, serve_playground_app
from agents.team_definitions import db_query_team, sql_agent, db_inspector_agent

load_dotenv()

# Configure logging to see agent activity in the terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)

# --- Define which agents and teams will be available in the Playground UI ---

# A list for individual agents
individual_agents = [
    sql_agent,
    db_inspector_agent
]

# A list for teams
teams_for_playground = [
    db_query_team
]

# --- Create the Playground instance with the correct parameters ---
# The Playground class takes separate lists for `agents` and `teams`.
playground = Playground(agents=individual_agents, teams=teams_for_playground)

# Get the underlying FastAPI app object
app = playground.get_app()


# --- Main execution block to run the web server ---
if __name__ == "__main__":
    logging.info("Starting Agno Playground UI at http://localhost:7777")
    serve_playground_app("playground:app", reload=True, port=7777)
