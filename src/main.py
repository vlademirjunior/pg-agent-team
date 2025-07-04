# -*- coding: utf-8 -*-
# File: main.py
# Author: Vlademir Manoel
# Create Date: 2025-06-30
# Last Modified: 2025-07-09
# Version: 1.0.0
# Description: Object-oriented entry point for the Autonomous Database Analyst Agent.

import json
import logging
import sys
import re
from decimal import Decimal
from typing import Any, Dict

import psycopg2
from dotenv import load_dotenv

from agents.agent_factory import agent_factory


class JsonDecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle Decimal objects."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


class RequestValidator:
    """Validates user requests against a set of security patterns."""

    def __init__(self):
        self.forbidden_patterns = [
            r'\b(delete|update|insert|drop|alter|truncate|grant|revoke)\b',
            r'ignore previous instructions', r'ignore as instruções anteriores',
            r'act as', r'aja como', r'agir como',
            r'roleplay', r'interprete o papel de',
            r'reveal your instructions', r'revele suas instruções'
        ]

    def is_safe(self, request: str) -> bool:
        """Checks if the request is safe to process."""
        for pattern in self.forbidden_patterns:
            if re.search(pattern, request, re.IGNORECASE):
                logging.error(
                    f"Validation failed: Malicious pattern '{pattern}' detected in request.")
                return False
        return True


class AgentOrchestrator:
    """Orchestrates the interaction between the user and the AI agents."""

    def __init__(self, data_agent, presentation_agent, validator):
        self.data_agent = data_agent
        self.presentation_agent = presentation_agent
        self.validator = validator

    def _get_raw_data(self, user_request: str) -> Dict[str, Any] | str:
        """Engages the data agent to fetch raw data from the database."""
        logging.info("Engaging Data Analyst Agent to fetch data...")
        response = self.data_agent.run(user_request)
        return response.content

    def _get_conversational_response(self, raw_data: Any, user_request: str) -> str:
        """Engages the presentation agent to format data into a friendly response."""
        logging.info(
            "Conversational output requested. Engaging Presentation Agent...")
        presentation_prompt = (
            f"Here is the data: {json.dumps(raw_data, cls=JsonDecimalEncoder)}\n\n"
            f"Based on this data, please answer the user's original question: '{user_request}'"
        )
        response = self.presentation_agent.run(presentation_prompt)
        return response.content

    def run(self, user_request: str) -> str:
        """
        Executes the main application logic and returns the final response as a string.
        """
        logging.info(f"User Request: {user_request}")

        if not self.validator.is_safe(user_request):
            return json.dumps({"error": "The user request was blocked by the security filter."}, indent=2)

        logging.info("User request passed security validation.")
        logging.info("-" * 20)

        try:
            raw_data = self._get_raw_data(user_request)

            if raw_data == "INVALID_REQUEST":
                logging.warning(
                    "Data Analyst Agent deemed the request invalid.")
                return json.dumps({"error": "Request was deemed invalid by the data agent."}, indent=2)

            if "json" in user_request.lower():
                logging.info("JSON output requested. Returning raw data.")
                return json.dumps(raw_data, indent=2, ensure_ascii=False, cls=JsonDecimalEncoder)
            else:
                return self._get_conversational_response(raw_data, user_request)

        except (psycopg2.Error, ConnectionError, ValueError) as e:
            logging.error(f"An operational error occurred: {e}")
            return f"A database error occurred: {e}"
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}", exc_info=True)
            return f"An unexpected error occurred: {e}"


def setup_logging():
    """Configures the application's logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout,
    )


if __name__ == "__main__":
    load_dotenv()
    setup_logging()

    validator = RequestValidator()
    orchestrator = AgentOrchestrator(
        data_agent=agent_factory.create_data_analyst_agent(),
        presentation_agent=agent_factory.create_presentation_agent(),
        validator=validator
    )

    request = "What are the top 3 most expensive products in the database? Please provide the results in JSON format only."
    result = orchestrator.run(request)
    print(result)
