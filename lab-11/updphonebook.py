import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(host="localhost", dbname="lab-10", user="postgres",
                        password="Beka_1604", port=5432)
cur = conn.cursor()

def insert_data():
    print('Type "csv" or "con" to choose between uploading csv or console input:')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter the file path: ")
        data = []
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                data.append(row)
        cur.execute("SELECT insert_many(%s)", (data,))
        invalid = cur.fetchone()[0]
        if invalid:
            print("Invalid entries:", invalid)

def update_data():
    column = input("Enter column to update (name/surname/phone): ").lower()
    old = input(f"Current {column}: ")
    new = input(f"New {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new, old))
    conn.commit()

def delete_data():
    val = input("Enter name, surname, or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (val,))
    conn.commit()

def query_data():
    pattern = input("Enter pattern to search (part of name/surname/phone): ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def paginated_display():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def display_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

while True:
    print("""
Commands:
1. i - INSERT data
2. u - UPDATE data
3. q - QUERY by pattern
4. d - DELETE by value
5. s - SHOW all data
6. p - PAGINATED view
7. f - FINISH
""")
    cmd = input().lower()
    if cmd == 'i':
        insert_data()
    elif cmd == 'u':
        update_data()
    elif cmd == 'q':
        query_data()
    elif cmd == 'd':
        delete_data()
    elif cmd == 's':
        display_all()
    elif cmd == 'p':
        paginated_display()
    elif cmd == 'f':
        break

conn.commit()
cur.close()
conn.close()
