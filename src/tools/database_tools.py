# -*- coding: utf-8 -*-
# File: tools/database_tools.py
# Description: Object-oriented, clean tools for database interaction.

import logging
from contextlib import contextmanager
from typing import Any, Dict, List, Iterator

import psycopg2
from psycopg2.extras import DictCursor
from agno.tools import tool

from config.database import DB_CONFIG


class DatabaseManager:
    """Manages the lifecycle of the database connection."""

    def __init__(self, db_config: Dict[str, Any]):
        self._db_config = db_config
        self._connection = None

    @contextmanager
    def get_connection(self) -> Iterator[psycopg2.extensions.connection]:
        """Provides a database connection as a context manager."""
        try:
            self._connection = psycopg2.connect(
                **self._db_config, cursor_factory=DictCursor)
            yield self._connection
        except psycopg2.Error as e:
            logging.error(f"Database connection error: {e}")
            raise
        finally:
            if self._connection:
                self._connection.close()
                self._connection = None


# Create a single instance of the manager to be used by all tools.
db_manager = DatabaseManager(DB_CONFIG)


@tool
def list_available_schemas() -> List[str]:
    """Lists all non-system schemas available in the database."""
    logging.info("Executing list_available_schemas")
    query = "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'pg_toast');"
    try:
        with db_manager.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return [row['schema_name'] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        return [f"Database error: {e}"]


@tool
def list_tables_in_schema(schema_name: str = "public") -> List[str]:
    """Lists all available tables within a specific schema."""
    logging.info(f"Executing list_tables_in_schema for schema: {schema_name}")
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = %s ORDER BY table_name;"
    try:
        with db_manager.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (schema_name,))
                return [row['table_name'] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        return [f"Database error: {e}"]


@tool
def fetch_table_schema(table_name: str, schema: str = "public") -> str:
    """Fetches the schema (columns and data types) for a specific table."""
    logging.info(f"Executing fetch_table_schema for: {schema}.{table_name}")
    query = "SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position;"
    try:
        with db_manager.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (schema, table_name))
                schema_info = cursor.fetchall()

        if not schema_info:
            return f"Error: Table '{schema}.{table_name}' not found."

        return "\n".join(f"- {col['column_name']} ({col['data_type']})" for col in schema_info)
    except psycopg2.Error as e:
        return f"Database error: {e}"


@tool
def execute_sql_query(query: str) -> List[Dict[str, Any]]:
    """Executes a final, read-only SQL SELECT query and returns the results."""
    logging.info(f"Executing SQL query: {query}")
    forbidden_keywords = ['INSERT', 'UPDATE', 'DELETE',
                          'DROP', 'CREATE', 'ALTER', 'TRUNCATE', 'GRANT', 'REVOKE']
    if any(keyword in query.upper() for keyword in forbidden_keywords):
        raise ValueError(
            "Security Error: Only read-only SELECT queries are permitted.")

    try:
        with db_manager.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return [dict(row) for row in cursor.fetchall()]
    except psycopg2.Error as e:
        logging.error(f"Error executing SQL query: {e}")
        return [{"error": f"Error executing SQL query: {e}"}]
