import psycopg2
import os

from psycopg2.sql import Identifier, SQL

"""

"""

_TABLE_NAMES = {
    'bg_similar',
    'boardgame' ,
    'bg_collection'
}

conn = psycopg2.connect(user="postgres",
                        password="admin",
                        host="127.0.0.1",
                        port="5432",
                        database="mydb",
                        )
cursor = conn.cursor()

for table_name in _TABLE_NAMES:
    cursor.execute(SQL("TRUNCATE TABLE {};").format(Identifier(table_name)))

path = os.getcwd() + '/boardgames_ranks.csv'
cursor.execute("COPY boardgame FROM %s (format csv, header true, delimiter ',', encoding 'UTF_8');",(path,))

conn.commit()
cursor.close()
conn.close()
