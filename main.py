from database import Database

db = Database()
db.query("SELECT * from boardgame LIMIT %s", ("100",))
db.close()