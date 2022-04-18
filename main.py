import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # cursor
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f'Server version: {cursor.fetchone()}')

    # create a new table

    cursor.execute('''
        create table users(
        id serial primary key,
        first_name varchar(50) NOT NULL,
        nickname varchar(50) NOT NULL
        )
    ''')
    connection.commit()
    print('[INFO] Table created successfully')

    # insert data into a table

    cursor.execute(
        """insert into users(first_name, nickname) values
        ('Sergay', 'firstclass')
        """
    )

    print('[info] data was writed successfully')

    # get data from table

    cursor.execute("select nickname from users where first_name='Sergay'")
    print(cursor.fetchall())

    # delete a table

    # cursor.execute("DROP TABLE users")
    # print('[info] table was successfully deleted')


except Exception as _ex:
    print("[INFO] Error while working with postgre", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
