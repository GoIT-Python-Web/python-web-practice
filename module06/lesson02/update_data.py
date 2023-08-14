import logging

from faker import Faker
from psycopg2 import DatabaseError

from lesson02.connection import create_connection

fake = Faker()

if __name__ == '__main__':
    sql_expression = "UPDATE users SET phone = %s WHERE id = %s"

    try:
        with create_connection() as conn:
            if conn is not None:
                cur = conn.cursor()
                try:
                    for i in range(50_000):
                        cur.execute(sql_expression, (fake.phone_number(), i + 1))
                    conn.commit()
                except DatabaseError as err:
                    logging.error(err)
                    conn.rollback()
                finally:
                    cur.close()
            else:
                print('Error: can\'t create the database connection')
    except RuntimeError as err:
        logging.error(err)
