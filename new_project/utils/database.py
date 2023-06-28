from sqlalchemy import create_engine, MetaData

host = 'localhost'
port = 3306
user = 'root'
password = ''
database = 'equipment_failures'

def get_list_names():
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tabelas = metadata.tables.keys()

    connection.close()
    dict_ = {
        "database": ["equipment_failures"],
        "tables": list(tabelas)
    }
    return dict_

def get_table():
    ...

def update_table():
    ...