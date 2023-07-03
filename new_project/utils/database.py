from sqlalchemy import create_engine, MetaData

host = 'localhost'
port = 3306
user = 'root'
password = ''
database = 'IndustrialTroubleshootDB'

# def get_list_names():
#     engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
#     connection = engine.connect()
#     metadata = MetaData()
#     metadata.reflect(bind=engine)
#     tabelas = metadata.tables.keys()
#     connection.close()
#     dict_ = {
#         "database": ["equipment_failures"],
#         "tables": list(tabelas)
#     }
#     return dict_



# teste
import sqlite3
from collections import OrderedDict
def get_list_names(database_file=r"new_project\database\bd_test\IndustrialTroubleshootDB.db"):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    table_names = [name[0] for name in table_names if name[0] != "sqlite_sequence"]
    cursor.close()
    connection.close()
    return {"database": ["IndustrialTroubleshootDB"], "tables": table_names}

def get_table(database, table_name):
    database_file = f"new_project\\database\\bd_test\\{database}.db"
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    result = []
    result.append(tuple(columns))
    for row in rows:
        result.append(tuple(row))
    cursor.close()
    connection.close()
    return result


def update_table():
    ...