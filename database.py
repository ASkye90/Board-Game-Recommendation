from psycopg2 import connect


__bg_ranks_file = ".\\boardgames_ranks.csv"


class DataBase:
    def __init__(self, db="mydb"):
        # Connect to an existing database
        self.conn = connect(user="postgres",
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database=db)
        # Create a cursor to perform database operations
        self.cursor = self.conn.cursor()

    def doSomething(self, query):
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(self.conn.get_dsn_parameters(), "\n")

        # Executing a SQL query
        self.cursor.execute("SELECT id,name from boardgame WHERE is_expansion='True' LIMIT 100")

        # Fetch result
        record = self.cursor.fetchall()
        for item in enumerate(record):
            print(str(item[1][0]) + ': ' + item[1][1])

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("PostgreSQL connection is closed")





