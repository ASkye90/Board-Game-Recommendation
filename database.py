import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self, db="mydb"):
        # Connect to an existing database
        self.conn = psycopg2.connect(user="postgres",
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database=db,
                              cursor_factory=RealDictCursor
                                     )
        # Create a cursor to perform database operations
        self.cursor = self.conn.cursor()

    def query(self, sql, data=()):

        # Executing a SQL query
        self.cursor.execute(sql,data)

        # Fetch result
        # record = self.cursor.fetchall()
        for item in self.cursor:
            print(str(item['id']) + ': ' + item['name'])

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("PostgreSQL connection is closed")


