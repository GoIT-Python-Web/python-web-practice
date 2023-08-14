import logging

from psycopg2 import DatabaseError

from lesson02.connection import create_connection

if __name__ == '__main__':
    sql_expression = "ALTER TABLE users ADD COLUMN phone VARCHAR(30);"

    try:
        with create_connection() as conn:
            if conn is not None:
                cur = conn.cursor()
                try:
                    cur.execute(sql_expression)
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
