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
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def create_db(db_file):
    if os.path.exists(db_file):
        print("Database already exists.")
        return False

    print("Creating database ...")
    create_table_dentist = '''
        CREATE TABLE Appointments(
        dentist_name VARCHAR(100),
        timeslot VARCHAR(100),
        status INTEGER DEFAULT 0
        );
        '''
    database_controller(db_file, create_table_dentist)
    # database_controller(db_file, create_table_values)
    dentist_names = ["Tom", "Jake", "James", "Bob", "Lilly", "Tracey"]
    timeslot = ["Mon 9to10am", "Mon 10to11am", "Mon 11to12pm", "Mon 12to1pm", "Mon 1to2pm", "Mon 2to3pm", "Mon 3to4pm", "Mon 4to5pm",
                "Tue 9to10am", "Tue 10to11am", "Tue 11to12pm", "Tue 12to1pm", "Tue 1to2pm", "Tue 2to3pm", "Tue 3to4pm", "Tue 4to5pm",
                "Wed 9to10am", "Wed 10to11am", "Wed 11to12pm", "Wed 12to1pm", "Wed 1to2pm", "Wed 2to3pm", "Wed 3to4pm", "Wed 4to5pm",
                "Thu 9to10am", "Thu 10to11am", "Thu 11to12pm", "Thu 12to1pm", "Thu 1to2pm", "Thu 2to3pm", "Thu 3to4pm", "Thu 4to5pm",
                "Fri 9to10am", "Fri 10to11am", "Fri 11to12pm", "Fri 12to1pm", "Fri 1to2pm", "Fri 2to3pm", "Fri 3to4pm", "Fri 4to5pm",
                "Sat 9to10am", "Sat 10to11am", "Sat 11to12pm", "Sat 12to1pm", "Sat 1to2pm", "Sat 2to3pm", "Sat 3to4pm", "Sat 4to5pm",
                "Sun 9to10am", "Sun 10to11am", "Sun 11to12pm", "Sun 12to1pm", "Sun 1to2pm", "Sun 2to3pm", "Sun 3to4pm", "Sun 4to5pm"
                ]

    entry = ""
    for i in range(0, 6):
        for j in range(0, 8*7):
            entry += f" INSERT INTO Appointments (dentist_name,timeslot) VALUES ('{dentist_names[i]}', '{timeslot[j]}');"
    database_controller(db_name, entry)

    return True
