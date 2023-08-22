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


class WordDB:
    def __init__(self, db_name='resources/main.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def check_existing_word(self, word_eng):
        self.cursor.execute('SELECT Eng FROM Words WHERE Eng = ?', (word_eng,))
        return self.cursor.fetchone() is None

    def add_new_word(self, word_eng, word_rus):
        self.cursor.execute('INSERT INTO Words (Eng, Rus) VALUES (?, ?)', (word_eng, word_rus))
        self.conn.commit()


class UserDB:
    def __init__(self, db_name='resources/main.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def check_user(self, username, password):
        self.cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (username, password))
        user_exists = self.cursor.fetchone() is not None
        return user_exists

    def create_user(self, username, password):
        self.cursor.execute('SELECT * FROM Users WHERE Username=?', (username,))
        existing_user = self.cursor.fetchone()
        if existing_user:
            return False
        else:
            self.cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)',
                                (username, password))
            self.conn.commit()
            return True

    def get_user_id(self, username):
        self.cursor.execute('SELECT Id FROM Users WHERE Username = ?', (username,))
        result = self.cursor.fetchone()
        return result[0]

    def update_score(self, username, score_increment):
        query = "UPDATE Users SET Score = Score + ? WHERE Username = ?"
        self.cursor.execute(query, (score_increment, username))
        self.conn.commit()

    def get_user_score(self, username):
        self.cursor.execute('SELECT Score FROM Users WHERE Username = ?', (username,))
        result = self.cursor.fetchone()
        return result[0]
