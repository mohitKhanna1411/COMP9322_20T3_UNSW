import sqlite3
from sqlite3 import Error
import os
import re


db_name = "z5266543.db"


def database_controller(database, command):
    try:
        connection = sqlite3.connect(database)
        connection.set_trace_callback(print)
    except Error as e:
        print(e)
    cursor = connection.cursor()
    if len(re.findall(';', command)) > 1:
        cursor.executescript(command)
    else:
        cursor.execute(command)
    # cursor.execute(command)
    # examples = [
    #     ("Tom", "Chatswood", "Paediatric Dentistry"),
    #     ("Jake", "Parramatta", "Orthodontics"),
    #     ("James", "Castle Hill", "Oral Surgery"),
    #     ("Bob", "Kellyville", "Orthodontics"),
    #     ("Lilly", "Kingsford", "Oral Surgery"),
    #     ("Tracey", "CBD", "Paediatric Dentistry")
    # ]
    # cursor.executemany("INSERT INTO Dentists VALUES (?, ?, ?)", examples)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def create_db(db_file):
    # print(os.path.exists(db_file))
    if os.path.exists(db_file):
        print("Database already exists.")
        return False

    print("Creating database ...")
    create_table_dentist = '''
        CREATE TABLE Dentists(
        dentist_name VARCHAR(100),
        location VARCHAR(100),
        specialization VARCHAR(100)
        );
        '''
    database_controller(db_file, create_table_dentist)
    # database_controller(db_file, create_table_values)
    dentist_names = ["Tom", "Jake", "James", "Bob", "Lilly", "Tracey"]
    dentist_location = ["Chatswood", "Parramatta",
                        "Castle Hill", "Kellyville", "Kingsford", "CBD"]
    dentist_specialization = ["Paediatric Dentistry", "Paediatric Dentistry",
                              "Orthodontics", "Orthodontics", "Oral Surgery", "Oral Surgery"]
    entry = ""
    for i in range(0, 6):
        entry += f" INSERT INTO Dentists VALUES ('{dentist_names[i]}', '{dentist_location[i]}', '{dentist_specialization[i]}');"
    database_controller(db_name, entry)

    return True
