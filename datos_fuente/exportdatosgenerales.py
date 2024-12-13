import sqlite3

def list_tables(db_file):
    """Lists all tables in a given SQLite database file.

    Args:
        db_file (str): The path to the SQLite database file.
    """

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("las tablas son")
    for table in tables:
        print(table[0])
    conn.close()

def list_tables_and_columns(db_file):
    """Lists all tables and their columns in an SQLite database.

    Args:
        db_file (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get a list of all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = cursor.fetchall()

    for table_name in table_names:
        table_name = table_name[0]
        print(f"\nTable: {table_name}")
        # Get column names for the current table
        cursor.execute(f"PRAGMA table_info('{table_name}')")
        columns = cursor.fetchall()
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            print(f"  - {column_name} ({data_type})")
            
    conn.close()

def list_tables_and_columns_and_data(db_file):
    """Lists all tables and their columns in an SQLite database and fetch 5 first records if any.

    Args:
        db_file (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get a list of all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = cursor.fetchall()

    for table_name in table_names:
        table_name = table_name[0]
        print(f"\nTable: {table_name}")
        # Get column names for the current table
        cursor.execute(f"PRAGMA table_info('{table_name}')")
        columns = cursor.fetchall()
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            print(f"  - {column_name} ({data_type})")
            
        # Get the first 5 rows of data for the current table (if any)
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        rows = cursor.fetchall()
        if rows:
            print("\n  First 5 records:")
            for row in rows:
                print("   ", row)
        else:
            print("  No data in this table.")
    conn.close()

def get_tabla_generales(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    table_name = "Generales"
    cursor.execute(f"SELECT * FROM {table_name}")
    
    with open("datos_fuente\generales.csv", "a") as file:
        rows = cursor.fetchall()
        for row in rows:
            row_str = ",".join(map(str, row))
            file.write(row_str)
            file.write('\n')
            
def get_tabla_responsables(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    table_name = "Responsables"
    cursor.execute(f"SELECT * FROM {table_name}")
    
    with open("responsables.csv", "w") as file:
        rows = cursor.fetchall()
        for row in rows:
            row_str = ",".join(map(str, row))
            file.write(row_str)
            file.write('\n')
            
def insert_direcciones(conn, cursor):
    sqlsentence = f"""INSERT INTO direcciones 
    (dir_pk, dir_str, dir_num, dir_cit_fk_id) 
    VALUES (?, ?, ?, ?)"""
    with open("datos_fuente\direcciones.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[0],data[1],data[2],data[3])
            cursor.execute(sqlsentence, (data[0],data[1],data[2],data[3]))
            conn.commit()
            
def insert_ports(conn, cursor):
    sqlsentence = f"""INSERT INTO port 
    (por_nam, por_tel, por_email, por_aut_fk_id, por_dir_fk_id) 
    VALUES (?, ?, ?, ?, ?)"""
    with open("datos_fuente\puertos.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[1],data[2],data[3],data[4],data[0])
            cursor.execute(sqlsentence, (data[1],data[2],data[3],data[4],data[0]))
            conn.commit()
            
def insert_personas(conn, cursor):
    sqlsentence = f"""INSERT INTO person 
    (per_nam, per_ap1, per_ap2) 
    VALUES (?, ?, ?)"""
    with open("datos_fuente\personas.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[0],data[1],data[2])
            cursor.execute(sqlsentence, (data[0],data[1],data[2]))
            conn.commit()
            
def insert_responsabilities(conn, cursor):
    sqlsentence = f"""INSERT INTO responsability 
    (res_pk, res_nam) 
    VALUES (?, ?)"""
    with open("datos_fuente\cargos.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[0], data[1])
            cursor.execute(sqlsentence, (data[0], data[1]))
            conn.commit()
            
def insert_roles(conn, cursor):
    sqlsentence = f"""INSERT INTO roles 
    (rol_per_fk_id, rol_res_fk_id) 
    VALUES (?, ?)"""
    with open("datos_fuente\person_rol.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()
                  
def insert_roles_ports(conn, cursor):
    sqlsentence = f"""INSERT INTO rol_port
    (rol_por_ini, rol_por_end, rol_por_por_fk_id, rol_por_rol_fk_id) 
    VALUES (?, ?, ?, ?)"""
    with open("datos_fuente\persons_roles_ports.csv", "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[0],data[1],data[2],data[3])
            cursor.execute(sqlsentence, (data[0],data[1],data[2],data[3]))
            conn.commit()


# --------------- PARA VER QUE HAY EN LAS TABLAS ---------------
# list_tables_and_columns_and_data('puertos\db.sqlite3')
# --------------------------------------------------------------

# ----- PARA OBTENER LOS DATOS DE LAS TABLAS DE puertos.db -----
get_tabla_generales('datos_fuente\puertos.db')
# get_tabla_responsables('datos_fuente\puertos.db')
# --------------------------------------------------------------


# ------------ PARA INSERTAR DATOS GENERALES -------------------
# conn = sqlite3.connect('puertos\db.sqlite3')
# cursor = conn.cursor()

# insert_direcciones(conn, cursor)
# insert_ports(conn, cursor)
# insert_personas(conn, cursor)
# insert_responsabilities(conn, cursor)
# insert_roles(conn, cursor)
# insert_roles_ports(conn, cursor)

# conn.close()
# --------------------------------------------------------------
