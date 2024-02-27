import menu
import sqlite3

# Created the agreement
def create_agreement(connection, cursor):
    data_to_agreement = []

    data_to_agreement.append(input('Insert number of agreement: '))
    data_to_agreement.append(input('Insert date of agreement ex. 1900-01-01 00:00:00: '))
    data_to_agreement.append(input('Insert value of agreement: '))
    data_to_agreement.append(input('Insert rate of agreement: '))
    data_to_agreement.append(input('Insert object of agreement: '))

    try:
        # Output of all branches
        branches = cursor.execute(f'SELECT name FROM Branches').fetchall()
        for iteration, branch in enumerate(branches):
            print(f'{iteration} {branch[0]}')

        data_to_agreement.append(input('Insert number of branch: '))

        # Output of all types of insurances
        types = cursor.execute(f'SELECT name FROM Insurances').fetchall()
        for iteration, type in enumerate(types):
            print(f'{iteration} {type[0]}')

        data_to_agreement.append(input('Insert type_id of agreement: '))

        sql_query = f'INSERT INTO Agreements (number, date, value, rate, object, branch_id, type_id) VALUES (?, ?, ?, ?, ?, ?, ?)'

        cursor.execute(sql_query, data_to_agreement)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

    menu.create_agreements(connection, cursor)

# Insert all agreements
def select_agreement(connection, cursor):
    try:
        rows = cursor.execute('SELECT * FROM Agreements').fetchall()
        headers = [description[0] for description in cursor.description]

        menu.description_functionality.total_rows(rows)

        for row_data in rows:
            for iteration, column_data in enumerate(row_data):
                print(headers[iteration] + ': ', column_data)
    except sqlite3.Error as error:
        print(error)

    menu.create_agreements(connection, cursor)

def insert(connection, cursor):
    table, rows, headers  = get_data_table(connection, cursor)

    columns = []
    values = []
    count_of_variables = []

    # Cycle to unified create and input data
    for iteration in range(1, len(headers)):
        columns.append(headers[iteration])
        values.append(input(headers[iteration] + ': '))
        count_of_variables.append('?')

    try:
        sql_query = f'INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join(count_of_variables)})'

        cursor.execute(sql_query, values)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

    menu.edit_database(connection, cursor)

def delete(connection, cursor):
    table, rows, headers = display_current_table(connection, cursor)

    try:
        sql_query = f'DELETE FROM {table} WHERE id = {input('Enter the id to delete row: ')}'

        cursor.execute(sql_query)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

    menu.edit_database(connection, cursor)

def select(connection, cursor):
    display_current_table(connection, cursor)
   
    menu.edit_database(connection, cursor)

def update(connection, cursor):
    table, rows, headers = display_current_table(connection, cursor)
    
    try:
        row_to_update = input('Enter the id of the row to update: ')

        columns = []
        values = []

        for iteration in range(1, len(headers)):
            # Input columns from current table
            columns.append(headers[iteration])
            # Input data to insert database
            values.append(input(headers[iteration] + ': '))

        rows_to_update = []

        # Collation data
        for iteration, column in enumerate(columns):
            rows_to_update.append(f'{column} = ?')

        sql_query = f'UPDATE {table} SET {','.join(rows_to_update)} WHERE id = {row_to_update}'

        cursor.execute(sql_query, values)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

    menu.edit_database(connection, cursor)

# Function to optimize get current table to work
def display_current_table(connection, cursor):
    table, rows, headers = get_data_table(connection, cursor)

    menu.description_functionality.total_rows(rows)

    for row_data in rows:
        for iteration, column_data in enumerate(row_data):
            print(headers[iteration] + ': ', column_data)

    return table, rows, headers

# Query to database to get table
def get_data_table(connection, cursor):
    try:
        table = menu.select_current_table(connection, cursor)
        rows = cursor.execute('SELECT * FROM ' + table).fetchall()
        headers = [description[0] for description in cursor.description]
    except sqlite3.Error as error:
        print(error)

    return table, rows, headers
