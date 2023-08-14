import logging

from psycopg2 import DatabaseError

from lesson02.connection import create_connection


def create_table(conn, sql_expression):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_expression = """CREATE TABLE IF NOT EXISTS users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(120),
     email VARCHAR(120),
     password VARCHAR(120),
     age numeric CHECK (age > 10 AND age < 90)
    );"""

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_expression)
            else:
                logging.error('Error: can\'t create the database connection')
    except RuntimeError as err:
        logging.error(err)
