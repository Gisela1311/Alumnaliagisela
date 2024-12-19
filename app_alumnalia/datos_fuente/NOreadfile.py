import sqlite3
import os
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


#06 insertar Estudio Profecional en la DB de alumnalia
def inserta_Estudio_Profecional(conn, cursor):
    sqlsentence = f"""INSERT INTO Estudio_Profesional
    (pk_est_pro, desc_est_pro) 
    VALUES (?, ?)"""
    filename = "06_estudis.csv"
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()

# insertar municipis 


# insertar Comarques 
def inserta_Comarca(conn, cursor):
    sqlsentence = f"""INSERT INTO Comarca
    (pk_com, nom_com) 
    VALUES (?, ?)"""
    filename =  "01_comarques.csv"    
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()

# insertar Comarque y provicias
def inserta_Municipios(conn, cursor):
    sqlsentence = f"""INSERT INTO Municipios
    (pk_mun, nom_mun, fk_com) 
    VALUES (?, ?, ?)"""
    filename = "02_municipis.csv"
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1],data[2])
            cursor.execute(sqlsentence, (data[0],data[1],data[2]))
            conn.commit()

# insertar Provicias 
def inserta_Provicias(conn, cursor):
    sqlsentence = f"""INSERT INTO Provincias
    (pk_pro, nom_pro) 
    VALUES (?, ?)"""
    filename = "03_provincias.csv"
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1])
            cursor.execute(sqlsentence, (data[0],data[1]))
            conn.commit()


# insertar Comarque y provicias
def inserta_Comarca_provincias(conn, cursor):
    sqlsentence = f"""INSERT INTO Comarca_provincias
    (pk_cam_pro, fk_com, fk_pro) 
    VALUES (?, ?, ?)"""
    filename = "04_Comarca_provincias.csv"
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(";")            
            print(data[0],data[1],data[2])
            cursor.execute(sqlsentence, (data[0],data[1],data[2]))
            conn.commit()



# insertar paises en la DB de alumnalia

def inserta_countries(conn, cursor):
    sqlsentence = f"""INSERT INTO countries 
    (cou_iso_pk, cou_nam_esp, cou_nam_fra, cou_nam_eng, cou_ddi) 
    VALUES (?, ?, ?, ?, ?)"""
    filename = "01_paises.csv"
    with open(prefix + filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().replace('"','').split(",")
            print(data[4],data[0],data[1],data[2],data[5])
            cursor.execute(sqlsentence, (data[4],data[0],data[1],data[2],data[5]))
            conn.commit()






# list_tables('db.sqlite3')
# list_tables_and_columns('db.sqlite3')

directorio_actual = os.path.dirname(os.path.realpath(__file__)) 
print(f"Directorio actual: {directorio_actual}")



conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

base="./datos_fuente"
if os.name == 'nt':
    prefix = base + "\\"
else:
    prefix = base + "/"

archivo = '"01_comarques.csv"' 
existe = os.path.exists(archivo) 
print(f"¿El archivo existe? {existe}")


# list_tables('/workspaces/web_puertos/puertos/db.sqlite3')
# list_tables_and_columns('puertos\db.sqlite3')

"""
inserta_countries(conn, cursor)
inserta_comunidades(conn, cursor)
inserta_provincias(conn, cursor)
inserta_ciudades(conn, cursor)
inserta_direcciones(conn, cursor)
inserta_autoridades(conn, cursor)
inserta_puertos(conn, cursor)
inserta_cargos(conn, cursor)
inserta_personas(conn, cursor)
inserta_roles(conn, cursor)
inserta_roles_puertos(conn, cursor)
inserta_subcategorias(conn, cursor)
inserta_categorias(conn, cursor)
"""


inserta_Comarca(conn, cursor)#llamada a insertar Comarques (pk_com, nom_com)
#inserta_Estudio_Profecional(conn, cursor)
conn.close()

#exec(open("path/to/your_script.py").read())

