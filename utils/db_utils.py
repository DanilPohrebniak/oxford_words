import sqlite3


class DB:
    def __init__(self, db_name='resources/main.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def fetch_words(self):
        self.cursor.execute("SELECT Eng, Rus FROM Words ORDER BY RANDOM() LIMIT 4")
        words = self.cursor.fetchall()
        return words

    def check_translation(self, eng_text, rus_text):
        query = "SELECT * FROM Words WHERE Rus = ? AND Eng = ?"
        self.cursor.execute(query, (rus_text, eng_text))

        row = self.cursor.fetchone()
        exists = bool(row)

        return exists
