import pandas as pd
import sqlite3
import os

try: # Código que puede generar un error ... 
    def Exp_Exp(nombre_archivo,tb,col):  
        directorio_actual = os.getcwd()           
        rt_archivo = os.path.join(directorio_actual, nombre_archivo)
        df = pd.read_csv(rt_archivo, sep=';') 
        columnas_deseadas = col #['pk_com', 'nom_com'] 
        df_seleccionado = df[columnas_deseadas]
        conexion = sqlite3.connect('db.sqlite3')
        df.to_sql(tb, conexion, if_exists='replace', index=False) #'Comarca'
        conexion.close()

    def Exp_Com():
        nombre_archivo = "01_comarques.csv"
        col =['pk_com', 'nom_com'] 
        Tabla = 'Comarca'
        Exp_Exp(nombre_archivo,Tabla,col)
    def Exp_Pro():
        nombre_archivo = "03_provincias.csv"
        col =['pk_pro', 'nom_pro'] 
        Tabla = 'Provincias'
        Exp_Exp(nombre_archivo,Tabla,col)
    def Exp_Com_Pro():
        nombre_archivo = "datos_fuente/04_Comarca_provincias.csv"
        col =['pk_cam_pro', 'fk_com','fk_pro'] 
        Tabla = 'Comarca_provincias'
        Exp_Exp(nombre_archivo,Tabla,col)
    
    Exp_Com_Pro()
    """
    directorio_actual = os.getcwd()
    print(f"El directorio actual es: {directorio_actual}")
    nombre_archivo = "01_comarques.csv"
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

    print(f"El archivo debería estar en: {ruta_archivo}")

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        print("El archivo existe.")
    else:
        print("El archivo no existe. Verifica la ruta y el nombre del archivo.")

    archivo = ruta_archivo#directorio_actual+"\01_comarques.csv" 
    existe = os.path.exists(archivo) 
    print(f"estoy aqui {os.path.basename}")
    print(f"¿El archivo existe? {existe}")

    # Leer el archivo CSV
    archivo_csv = '01_comarques.csv'
    df = pd.read_csv(ruta_archivo, sep=';') #archivo_csv

    # Seleccionar solo las columnas deseadas 
    columnas_deseadas = ['pk_com', 'nom_com'] 
    df_seleccionado = df[columnas_deseadas]

    # Conectar a la base de datos SQLite (se creará si no existe)
    conexion = sqlite3.connect('db.sqlite3')

    # Exportar los datos del DataFrame a la tabla SQLite
    df.to_sql('Comarca', conexion, if_exists='replace', index=False)

    # Cerrar la conexión
    conexion.close()
    """
except Exception as e:
    print(f"Error: {e}") 
    os.system("pause")
print("Datos exportados exitosamente a la base de datos SQLite.")
