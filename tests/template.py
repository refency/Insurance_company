import sqlite3
import sys

def initialization_database(connection, cursor):
    try:
        create_database(connection, cursor)
        insert_rows_to_database(connection, cursor)
    except sqlite3.Error as error:
        print(error)
        sys.exit()

# Create the database structure
def create_database (connection, cursor):
    sql_create_branches_table = ''' CREATE TABLE IF NOT EXISTS Branches (
                                        id INTEGER PRIMARY KEY,
                                        name VARCHAR(255) NOT NULL,
                                        address VARCHAR(255),
                                        phone VARCHAR(50)
                                    ); '''

    sql_create_agents_table = ''' CREATE TABLE IF NOT EXISTS Agents (
                                    id INTEGER PRIMARY KEY,
                                    branch_id INTEGER REFERENCES Branches (id),
                                    name VARCHAR(255),
                                    surname VARCHAR(255),
                                    phone VARCHAR(50),
                                    FOREIGN KEY (branch_id) REFERENCES Branches (id)
                                ); '''

    sql_create_insurances_table = ''' CREATE TABLE IF NOT EXISTS Insurances (
                                        id INTEGER PRIMARY KEY,
                                        name VARCHAR(255),
                                        type VARCHAR(255)
                                    ); '''

    sql_create_agreements_table = ''' CREATE TABLE IF NOT EXISTS Agreements (
                                        id INTEGER PRIMARY KEY,
                                        number INTEGER NOT NULL,
                                        date DATETIME,
                                        value INTEGER,
                                        rate FLOAT,
                                        object VARCHAR(255),
                                        branch_id INTEGER,
                                        type_id INTEGER,
                                        FOREIGN KEY (branch_id) REFERENCES Branches (id),
                                        FOREIGN KEY (type_id) REFERENCES Insurances (id)
                                    ); '''

    create_table(cursor, sql_create_branches_table)
    create_table(cursor, sql_create_agents_table)
    create_table(cursor, sql_create_insurances_table)
    create_table(cursor, sql_create_agreements_table)

    connection.commit()

def create_table(cursor, create_table_sql):
    try:
        cursor.execute(create_table_sql)
    except sqlite3.Error as error:
        print(error)
        sys.exit()

# Insert testing data to database
def insert_rows_to_database(connection, cursor):
    records_to_table_branches = [('РосСтрахование', 'Пушкина 28, стр. 33', '+7(933)5962877'),
                                ('БТБ страхование', 'Семенова 77А', '+7(395)4440044'),
                                ('Иньгосьстрахование', 'Пелеменова 11/2', '+8(800)5553535')]


    records_to_table_agents = [(1, 'Иван', 'Иванов', '+7(933)5320499'),
                                (2, 'Семен', 'Семенов', '+7(395)7096432'),
                                (3, 'Игнат', 'Терепков', '+7(395)0390022'),
                                (3, 'Кирилл', 'Тульков', '+7(800)9534421'),]

    records_to_table_insurances = [('Жилищное страхование', 'Страхование имущества'),
                                    ('Огневые риски и риски стихийных бедствий', 'Страхование имущества'),
                                    ('Страхование перерыва в бизнесе', 'Страхование имущества'),
                                    ('Страхование строительно-монтажных рисков', 'Страхование имущества'),
                                    ('Страхование транспортных средств', 'Страхование имущества'),
                                    ('Страхование грузов', 'Страхование имущества'),
                                    ('Страхование общей гражданской ответственности перед третьими лицами', 'Страхование ответственности'),
                                    ('Страхование ответственности товаропроизводителя, производителя услуг', 'Страхование ответственности'),
                                    ('Страхование ответственности директоров и должностных лиц (D&O)', 'Страхование ответственности'),
                                    ('Страхование профессиональной ответственности', 'Страхование ответственности'),
                                    ('Страхование ответственности работодателя', 'Страхование ответственности'),
                                    ('Страхование ответственности за нанесение вреда экологии', 'Страхование ответственности'),
                                    ('Накопительное страхование жизни, пенсионное страхование', 'Личное страхование'),
                                    ('Страхование от несчастного случая', 'Личное страхование'),
                                    ('Медицинское страхование', 'Личное страхование'),
                                    ('Страхование выезжающих за рубеж', 'Личное страхование')]

    records_to_table_agreements = [('MMM№1502304959304232', '2024-20-02 14:23:19', 12500, 1.4, 'LADA Priora 2170', 3, 5),
                                    ('XXX№7493294832864623', '2024-20-02 16:29:11', 9200, 1.3, 'Строительство дома', 2, 8),
                                    ('HHH№0843829384838293', '2024-21-02 11:48:05', 21500, 1.1, 'Поездка в командировку в Китай', 3, 16),
                                    ('TTT№320402340490', '2024-21-02 17:12:45', 8800, 1.2, 'Общее медицинское страхование', 1, 15)]

    create_rows(cursor, 'INSERT INTO Branches (name, address, phone) VALUES (?, ?, ?)', records_to_table_branches)
    create_rows(cursor, 'INSERT INTO Agents (branch_id, name, surname, phone) VALUES (?, ?, ?, ?)', records_to_table_agents)
    create_rows(cursor, 'INSERT INTO Insurances (name, type) VALUES (?, ?)', records_to_table_insurances)
    create_rows(cursor, 'INSERT INTO Agreements (number, date, value, rate, object, branch_id, type_id) VALUES (?, ?, ?, ?, ?, ?, ?)', records_to_table_agreements)

    connection.commit()

def create_rows(cursor, row, records):
    try:
        cursor.executemany(row, records)
    except sqlite3.Error as error:
        print(error)
        sys.exit()
