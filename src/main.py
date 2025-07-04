# -*- coding: utf-8 -*-
# File: main.py
# Author: Vlademir Manoel
# Date: 2025-06-30
# Description: Entry point to generate and execute SQL queries using an agent team.

import json
import logging
import sys
import psycopg2
import re

from decimal import Decimal
from agents.team_definitions import db_query_team
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)


def convert_decimal(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(
        f"Object of type {type(obj).__name__} is not JSON serializable")


def sanitize_and_validate_request(request: str) -> bool:
    """
    Performs basic input sanitization to block obviously malicious prompts.
    This is a critical first line of defense before the LLM sees the input.
    """
    # Block common SQL injection keywords and prompt injection phrases
    forbidden_patterns = [
        # SQL Injection Keywords
        r'\b(delete|update|insert|drop|alter|truncate|grant|revoke)\b',
        # Prompt Injection Phrases (English)
        r'ignore previous instructions',
        r'act as',
        r'roleplay',
        r'reveal your instructions',
        # Prompt Injection Phrases (Portuguese)
        r'ignore as instruções anteriores',
        r'aja como',
        r'agir como',
        r'interprete o papel de',
        r'revele suas instruções'
    ]

    for pattern in forbidden_patterns:
        if re.search(pattern, request, re.IGNORECASE):
            logging.error(
                f"Validation failed: Malicious pattern '{pattern}' detected in request.")
            return False

    return True


def main():
    """The main function that orchestrates the agent team."""
    table_name = "items"
    user_data_request = (
        f"For the table named '{table_name}', please provide the total count of all items, sum prices, and a JSON array of all items, where each object in the array contains the item's id, name, and price."
    )

    logging.info(f"User Request: {user_data_request}")

    # --- Input Sanitization Layer ---
    if not sanitize_and_validate_request(user_data_request):
        print(json.dumps(
            {"error": "The user request was blocked by the security filter."}, indent=2))
        return

    logging.info("User request passed security validation.")
    logging.info("-" * 20)

    try:
        response = db_query_team.run(user_data_request)

        logging.info("Final Consolidated Result:")
        print(json.dumps(response.content, indent=2,
              ensure_ascii=False, default=convert_decimal))

    except (psycopg2.Error, ConnectionError, ValueError) as e:
        logging.error(f"An operational error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
