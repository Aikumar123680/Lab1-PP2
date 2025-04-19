import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(host="localhost", dbname="lab-10", user="postgres",
                        password="Beka_1604", port=5432)
cur = conn.cursor()

# === Создание таблицы ===
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);
""")

# === Функция поиска по шаблону ===
cur.execute("""
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(user_id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# === Процедура вставки или обновления пользователя ===
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_surname TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name AND surname = p_surname) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook(name, surname, phone) VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;
""")

# === Функция пагинации ===
cur.execute("""
CREATE OR REPLACE FUNCTION get_users_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(user_id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    ORDER BY user_id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
""")

# === Процедура удаления по имени или номеру ===
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;
""")

# === Процедура массовой вставки пользователей ===
cur.execute("""
CREATE OR REPLACE FUNCTION insert_many_users(users TEXT[][])
RETURNS TEXT[] AS $$
DECLARE
    user_row TEXT[];
    wrong_phones TEXT[] := '{}';
BEGIN
    FOREACH user_row SLICE 1 IN ARRAY users
    LOOP
        IF user_row[2] ~ '^[0-9]{10,15}$' THEN
            BEGIN
                CALL insert_or_update_user(user_row[0], user_row[1], user_row[2]);
            EXCEPTION WHEN OTHERS THEN
                wrong_phones := array_append(wrong_phones, user_row[0] || ' ' || user_row[1]);
            END;
        ELSE
            wrong_phones := array_append(wrong_phones, user_row[0] || ' ' || user_row[1]);
        END IF;
    END LOOP;
    RETURN wrong_phones;
END;
$$ LANGUAGE plpgsql;
""")

conn.commit()

# === Python функции ===

def insert_data():
    print('Type "csv" or "con" to choose option between uploading CSV file or typing from console:')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("CALL insert_or_update_user(%s, %s, %s);", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter file path: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            user_list = []
            for row in reader:
                user_list.append(row)
            cur.execute("SELECT insert_many_users(%s);", (user_list,))
            incorrect = cur.fetchone()[0]
            if incorrect:
                print("Incorrect entries:", incorrect)

def update_data():
    column = input('Which column do you want to update? (name/surname/phone): ')
    value = input(f"Enter current {column}: ")
    new_value = input(f"Enter new {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

def delete_data():
    value = input('Enter name or phone to delete: ')
    cur.execute("CALL delete_by_name_or_phone(%s);", (value,))
    conn.commit()

def query_data():
    pattern = input("Enter search pattern (partial name/surname/phone): ")
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

def display_data():
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def paginated_display():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# === Главный цикл ===
while True:
    print("""
    Commands:
    1. 'i' - Insert user(s)
    2. 'u' - Update user
    3. 'q' - Query with pattern
    4. 'd' - Delete user
    5. 's' - Show all users
    6. 'p' - Paginated display
    7. 'f' - Finish program
    """)
    command = input("Enter command: ").lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "p":
        paginated_display()
    elif command == "f":
        break

conn.commit()
cur.close()
conn.close()