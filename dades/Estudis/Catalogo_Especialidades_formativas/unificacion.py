import pandas as pd
import openpyxl

files = ["Actividades_Fisicas.xlsx",
"Administracion_con.xlsx",
"Administracion_sin_PT_M_PM.xlsx",
"Administracion_sin_P_T.xlsx",
"Agraria.xlsx",
"Alimentarias.xlsx",
"Artesanias.xlsx",
"Artes_Graficas.xlsx",
"Comercio.xlsx",
"Edificacion_con.xlsx",
"Edificacion_sin.xlsx",
"Electricidad.xlsx",
"Energia.xlsx",
"Extractivas.xlsx",
"Hosteleria.xlsx",
"Imagen_personal.xlsx",
"Imagen_sonido.xlsx",
"Informatica_con_12.xlsx",
"Informatica_con_345.xlsx",
"Informatica_sin.xlsx",
"Madera.xlsx",
"Mantenimiento.xlsx",
"Maritimo.xlsx",
"Mecanica.xlsx",
"Quimica.xlsx",
"Sanidad.xlsx",
"Seguridad.xlsx",
"Socioculturales_con_nivel.xlsx",
"Socioculturales_sin_nivel.xlsx",
"Textil.xlsx",
"Transporte.xlsx",
"Vidrio.xlsx"]


dataframes = []

for file in files:
    print(f"procesando {file}")
    df = pd.read_excel(files[0], sheet_name='Resultados')
    dataframes.append(df)
df_consolidado = pd.concat(dataframes)
# Selecciona todos los campos salvo el último
df_consolidado = df_consolidado.iloc[:, :-1]
df_consolidado.to_csv('catalogo.csv', index=False)

