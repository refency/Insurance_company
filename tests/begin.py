import sys
sys.path.insert(1, './modules')

import sqlite3
import template

database_name = '../db/Insurance.db'
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

template.initialization_database(connection, cursor)

connection.close()
