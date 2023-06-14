import pandas as pd
import sqlite3

data = pd.read_excel('oxford.xlsx', engine='openpyxl')

conn = sqlite3.connect('resources/main.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Words
             (Eng TEXT, Rus TEXT)''')

for index, row in data.iterrows():
    eng = row[0]
    rus = row[2]
    c.execute("INSERT INTO Words (Eng, Rus) VALUES (?, ?)", (eng, rus))

conn.commit()
conn.close()