import database
import sqlite3
import sys

# The main function of menu
def main(connection, cursor):
    description_functionality.main_option()

    match input('Insert the command: ').lower():
        case 'insert':
            create_agreements(connection, cursor)
        case 'edit':
            edit_database(connection, cursor)
        case 'exit':
            print('Aborting the program ...')
            connection.commit()
            connection.close()
            sys.exit()
        case _:
            main(connection, cursor)

# Function of work with only agreements
def create_agreements(connection, cursor):
    description_functionality.create_agreement()
    description_functionality.back_option()

    match input('Enter the command: ').lower():
        case 'create':
            database.create_agreement(connection, cursor)
        case 'select':
            database.select_agreement(connection, cursor)
        case 'back':
            main(connection, cursor)
        case _:
            create_agreements(connection, cursor)

# Functionality of work with database
def edit_database(connection, cursor):
    description_functionality.edit_option()
    description_functionality.back_option()

    match input('Enter the command: ').lower():
        case 'create':
            database.insert(connection, cursor)
        case 'delete':
            database.delete(connection, cursor)
        case 'select':
            database.select(connection, cursor)
        case 'update':
            database.update(connection, cursor)
        case 'back':
            main(connection, cursor)
        case _:
            edit_database(connection, cursor)

def select_current_table(connection, cursor):
    description_functionality.all_tables()

    try:
        # Get list of all tables from database
        for table in cursor.execute('SELECT name from sqlite_master where type= "table"'):
            print(*table)
    except sqlite3.Error as error:
        print(error)

    description_functionality.back_option()
    
    # Select the required table
    match input('Enter the database: '):
        case 'Branches':
            return 'Branches'
        case 'Agents':
            return 'Agents'
        case 'Insurances':
            return 'Insurances'
        case 'Agreements':
            return 'Agreements'
        case 'back':
            main(connection, cursor)
            return
        case _:
            database.select(connection, cursor)

# Class to optimize code of readable
class description_functionality:
    def main_option():
        print('\n', 'Available functions:')
        print('insert - Create the agreement')
        print('edit - Edit the database')
        print('exit - Abort the program', '\n')

    def edit_option():
        print('\n', 'Available functions:')
        print('create - Create row of table')
        print('delete - Delete row of table')
        print('select - View table of database')
        print('update - Update row of table')

    def create_agreement():
        print('\n', 'Available functions:')
        print('create - Create the agreement')
        print('select - View rows of table')


    def total_rows(rows):
        print('Total rows are: ', len(rows))
        print('Printing each row', '\n')

    def all_tables():
        print('\n', 'All tables: ')

    def back_option():
        print('back - Return to main menu', '\n')
