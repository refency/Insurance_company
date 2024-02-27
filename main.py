import sys
sys.path.insert(1, './modules')

import sqlite3
try:
    connection = sqlite3.connect('./db/Insurance.db')
    cursor = connection.cursor()
except sqlite3.Error as error:
    print(error)
    sys.exit()

import menu
menu.main(connection, cursor)
