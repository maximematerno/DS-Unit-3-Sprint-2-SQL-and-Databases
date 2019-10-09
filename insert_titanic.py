import pandas as pd
import psycopg2
import sqlite3

# import data titanic.csv
df = pd.read_csv("titanic.csv")
df['Name'] = df['Name'].str.replace("'", " ")

# Sqlite3 file and Connect 
conn = sqlite3.connect('titanic.sqlite3')
cursor = conn.cursor()

# data to sql 

df.to_sql('titanic', conn, index=False, if_exists='replace')

# See data types
cursor_s = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'

cursor_s.execute(query).fetchall()

titanic = cursor_s.execute('SELECT * FROM titanic;').fetchall()

cursor_s.execute('PRAGMA table_info(titanic);').fetchall()

# Psycopg2 + password 
dbname = 'USER'
user = 'USER'
password = 'PassWord'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

pg_conn
pg_cursor = pg_conn.cursor()

# Create table

create_titanic_table = """
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name TEXT,
        Sex TEXT,
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare REAL
);
"""
pg_cursor.execute(create_titanic_table)

# Insert_titanic

for t in titanic:
    insert_titanic = """
      INSERT INTO titanic
      (Survived, PClass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES """ + str(titanic[0]) + ';'

pg_cursor.execute(insert_titanic)

pg_cursor.close()
pg_conn.commit()