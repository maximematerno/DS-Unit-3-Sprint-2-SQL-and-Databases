import sqlite3

# Connect to database
conn = sqlite3.connect('demo_data.sqlite3')


# Cursor to read the database
cursor = conn.cursor()


# Make table
demo ='''
CREATE TABLE demo (
    s CHAR(1),
    x INT,
    y INT
)
'''


# demo_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='demo'"
# if not conn.execute(demo_exists).fetchone():
#     conn.execute(demo)


# Execute demo
cursor.execute(demo)


# Create new values of columns
insert = "INSERT INTO demo VALUES ('g',3,9), ('v',5,7), ('f',8,7);"


# Execute insert and commit 
cursor.execute(insert)
conn.commit()


#Count how many rows you have 
numbers_rows_query = cursor.execute("SELECT COUNT(*) FROM demo;").fetchone()[0]
print(f' The number of rows are {numbers_rows_query}')


#How many rows are there where both x and y are at least 5?
at_least_five_query = '''
SELECT COUNT(*) FROM demo
WHERE x >=5 AND y >= 5;
'''
at_least_five = cursor.execute(at_least_five_query).fetchone()[0]
print(f' The number of rows for x and y are at least 5 are {at_least_five}')


#How many unique values of y are there
unique_val_query = cursor.execute("SELECT COUNT(DISTINCT y) FROM demo;").fetchone()[0]
print(f' The unique values are {unique_val_query}')


# close cursors and connection
cursor.close()
conn.close()