import sqlite3

conn = sqlite3.connect("user.sqlite3")
cursor = conn.cursor()
cursor.execute(
    """
        delete from user_database;

        """
)
conn.commit()
conn.close()
