import logging

from faker import Faker

from random import randint
from psycopg2 import DatabaseError

from lesson02.connection import create_connection

fake = Faker()
COUNT = 50_000


def insert_data(conn, sql_expression):
    cur = conn.cursor()
    try:
        for _ in range(COUNT):
            cur.execute(sql_expression, (fake.name(), fake.email(), fake.password(), randint(11, 89)))
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        cur.close()


if __name__ == '__main__':
    sql_expression = "INSERT INTO users(name,email,password, age) VALUES(%s, %s, %s, %s)"
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn, sql_expression)
            else:
                print('Error: can\'t create the database connection')
    except RuntimeError as err:
        logging.error(err)
