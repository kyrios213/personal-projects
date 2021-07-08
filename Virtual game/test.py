import sqlite3
import csv

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

filename = 'class'
profile = 'lance'
cur.execute('''SELECT name FROM Players WHERE name = ?''', (profile,))
select = cur.fetchone()[0]
print(select)