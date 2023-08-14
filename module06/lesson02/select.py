import logging

from psycopg2 import DatabaseError

from lesson02.connection import create_connection

if __name__ == '__main__':
    sql_expression_all = "SELECT * FROM users WHERE id = %s"
    sql_expression_custom_field = """
        select id, name, age
        from users
        where age > 30
        order by name, age desc
        limit 10;
    """
    sql_expression_regex = """
    select name from users where name similar to '%(ma|am)%' limit 100;
    """
    try:
        with create_connection() as conn:
            if conn is not None:
                cur = conn.cursor()
                try:
                    # cur.execute(sql_expression_all, (4, ))
                    # cur.execute(sql_expression_custom_field)
                    cur.execute(sql_expression_regex)
                    # print(cur.fetchone())
                    print(cur.fetchall())
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
