import pandas as pd
import openpyxl


campos_escuelas=["__id", "email","nif_entitat_formaci", "codi_municipi", "nom_entitat_formaci", "nom_municipi",	"codi_comarca",	"web", "nom_comarca", "tel_fon"]
campos_escuelas_nom=["__id", "email","nif_entitat_formaci", "nom_entitat_formaci", "web", "tel_fon"]
campos_escuelas_dir=["nif_entitat_formaci", "codi_municipi"]
campos_cursos=["__id", "identificador", "area_professional", "familia_professional","denominacio","ambit", "hores", "modalitat"]
# pongo "num_grup" en Calendario, ya que no tengo muy claro para que sirve
campos_calendario=["__id", "data_final","data_inici", "num_grup"]
df = pd.read_excel("foap2024_original.xlsx", sheet_name='Hoja1')

df_calendario = df[campos_calendario]
df_cursos = df[campos_cursos]


df_escuelas =df[campos_escuelas]
df_escuelas_nom = df[campos_escuelas_nom]
df_escuelas_mun = df[campos_escuelas_dir]

df_escuelas_nom_aux=df_escuelas_nom.iloc[:, 1:]
df_escuelas_unicas = df_escuelas_nom_aux.drop_duplicates()
df_escuelas_mun_unicos = df_escuelas_mun.drop_duplicates()
df_calendario.to_csv('calendario.csv', index=False)
df_cursos.to_csv('cursos.csv', index=False)
df_escuelas_unicas.to_csv('escuelas_nom.csv', index=False)
df_escuelas_mun_unicos.to_csv('escuelas_mun.csv', index=False)
print(df.head())
