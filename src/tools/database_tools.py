# -*- coding: utf-8 -*-
# File: tools/database_tools.py
# Description: Tools for interacting with the PostgreSQL database.

import logging
from typing import Any, Dict, List

import psycopg2
from psycopg2.extras import DictCursor
from agno.tools import tool

# Import the database configuration modularly
from config.database import DB_CONFIG


@tool
def fetch_table_schema(table_name: str, schema: str = "public") -> str:
    """
    Fetches and returns the schema for a specific table from the PostgreSQL database.
    This tool should be used first to understand the table structure before writing a query.

    Args:
        table_name: The name of the table.
        schema: The schema of the table (defaults to 'public').

    Returns:
        A formatted string describing the table schema, or an error message.
    """
    logging.info(f"Executing fetch_table_schema for: {schema}.{table_name}")
    try:
        with psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor) as conn:
            with conn.cursor() as cursor:
                query = """
                    SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_schema = %s AND table_name = %s
                    ORDER BY ordinal_position;
                """
                cursor.execute(query, (schema, table_name))
                schema_info = cursor.fetchall()

        if not schema_info:
            return f"Error: Table '{schema}.{table_name}' not found."

        formatted_schema = "\n".join(
            f"- {col['column_name']} ({col['data_type']})" for col in schema_info
        )
        return f"Schema for table '{schema}.{table_name}':\n{formatted_schema}"
    except psycopg2.Error as e:
        logging.error(f"Database error in fetch_table_schema: {e}")
        return f"Database error: {e}"


@tool
def execute_sql_query(query: str) -> List[Dict[str, Any]]:
    """
    Executes a read-only SQL SELECT query and returns the results as a list of dictionaries.
    This tool should only be used after a query has been generated.

    Args:
        query: The SQL SELECT statement to execute.

    Returns:
        A list of dictionaries representing the query results, or an error message.
    """
    logging.info(f"Executing SQL query: {query}")
    forbidden_keywords = [
        'INSERT', 'UPDATE', 'DELETE', 'DROP', 'CREATE', 'ALTER', 'TRUNCATE', 'GRANT', 'REVOKE'
    ]
    if any(keyword in query.upper() for keyword in forbidden_keywords):
        raise ValueError(
            "Security Error: Only read-only SELECT queries are permitted.")

    try:
        with psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = [dict(row) for row in cursor.fetchall()]
        logging.info(
            f"Query executed successfully, {len(results)} rows returned.")
        return results
    except psycopg2.Error as e:
        logging.error(f"Error executing SQL query: {e}")
        return [{"error": f"Error executing SQL query: {e}"}]
