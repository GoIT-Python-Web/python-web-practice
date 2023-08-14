import logging

import psycopg2
from contextlib import contextmanager
from psycopg2 import OperationalError, DatabaseError


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    try:
        conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='567234')
        yield conn
        conn.close()
    except OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")

