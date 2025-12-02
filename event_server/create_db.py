import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="cs401",
    password="cs401ricsoftwareengineering",
    host="108.34.175.31",
    port="4001",
)

conn.autocommit = True
cur = conn.cursor()

try:
    cur.execute('CREATE DATABASE "cs401_fatima";')
    print("Database created")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists")

cur.close()
conn.close()
