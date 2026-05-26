import sqlite3

conn = sqlite3.connect("Road_Accidents.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Accident")
result = cursor.fetchone()

print("Total crashes:", result[0])

conn.close()