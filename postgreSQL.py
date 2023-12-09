import psycopg2

# to connect:
# conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
# print("connected succesfully")

# Adding a table:

def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''create table employees(Name text, ID int, Age int);''')
    print('Table created successfully')

    conn.commit()
    conn.close()

# table()

# Adding data:

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values('John', 101, 22);''')
    cursor.execute('''insert into employees(Name, ID, Age) values('Sam', 102, 25);''')
    print("data added succesfully")

    conn.commit()
    conn.close()

# data()

# Extracting data:

def extract():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    print(cursor.fetchall())
    # print(cursor.fetchone())

    conn.commit()
    conn.close()

# extract()

# Giving user input:

def user():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
    cursor = conn.cursor()

    name = input('Enter name: ')
    id = input('Enter ID: ')
    age = input('Enter age:')

    query = '''insert into employees(Name, ID, Age) values(%s, %s, %s);'''
    cursor.execute(query, (name, id, age))

    print("data added succesfully")

    conn.commit()
    conn.close()

# user()

def truncate():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="bagdadi@2721", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''truncate table employees;''')
    print("Table contents deleted")

    conn.commit()
    conn.close()

truncate()