import psycopg2
import pandas as pd 

"""
Script queries titanic data from elephantSQL
"""

# Database info
dbname = 'bbhudnlj'
user = 'bbhudnlj'
password = 'wvVskx2m_CkKzdz3ET4npCKU3UxkN3hR'
host = 'salt.db.elephantsql.com'

# Initalize connection and cursor to db 
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

# pg_cursor = pg_conn.cursor()


# questions to answer
question_list = [
    "How many passengers survived, and how many died?",
    "How many passengers were in each class?",
    "How many passengers survived/died within each class?",
    "What was the average age of survivors vs nonsurvivors?",
    "What was the average age of each passenger class?",
    "What was the average fare by passenger class? By survival?",
    "How many siblings/spouses aboard on average, by passenger class? By survival?",
    "How many parents/children aboard on average, by passenger class? By survival?",
]

# List into dict 
question_dict = {}
for q in question_list:
    entry = {question_list.index(q) + 1: q}
    question_dict.update(entry)

# Dict querries 
query_dict = {
    1: """
    SELECT survived, COUNT(*) 
    FROM titanic
    GROUP BY survived;
""",
    2: """
    SELECT pclass, COUNT(*) 
    FROM titanic
    GROUP BY pclass 
    ORDER BY pclass;
    
""",
    3: """
    SELECT pclass, survived, COUNT(survived) 
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass;
""",
    4: """
    SELECT survived, AVG(age) 
    FROM titanic
    GROUP BY survived;
""",
    5: """
    SELECT pclass, AVG(age) 
    FROM titanic
    GROUP BY pclass;
""",
    6: """
    SELECT pclass, survived, AVG(fare)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    7: """
    SELECT pclass, survived, COUNT(sibs_abd)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    8: """
    SELECT pclass, survived, COUNT(p_c_abd)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
""",
    9: """
    SELECT name, COUNT(passenger_id) 
    FROM titanic 
    GROUP BY name HAVING COUNT(passenger_id) > 1;
""",
}

q_all_names = """
    SELECT name
    FROM titanic;
"""

# Answer 

# For loop questions
for question_key, question_val in question_dict.items():

    # print questions
    print("Question ", question_key)
    print(question_val)

    # print query
    print("SQL query :")
    print(query_dict[question_key])

    # Connection and execute 
    cursor = pg_conn.cursor()
    cursor.execute(query_dict[question_key])
    output = cursor.fetchall()

    print("Output: ")
    print(output, "\n")

    # close 
    cursor.close()
    pg_conn.close()