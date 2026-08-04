import sqlite3

conn = sqlite3.connect("enterprise_ai.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(chats)")

for column in cursor.fetchall():
    print(column)

conn.close()