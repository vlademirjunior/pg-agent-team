# -*- coding: utf-8 -*-
# File: config/database.py
# Description: Configuration for connecting to a PostgreSQL database.

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",  # Ideally, use environment variables for credentials
}
