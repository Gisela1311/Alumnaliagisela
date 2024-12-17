
## Tabla de Datos Personales

| Campo            | Tipo de Dato        | Descripción                                                                                 |
|------------------|---------------------|---------------------------------------------------------------------------------------------|
| `pk_per`         | `SmallAutoField`    | Id de la Dat_Per (clave primaria).                                                          |
| `nom_per`        | `CharField` (150)   | Nombre de la persona.                                                                       |
| `dni_per`        | `CharField` (15)    | Nombre de la autoridad, debe ser único y validado.                                          |
| `cn_per`         | `CharField` (150)   | Nacionalidad de la persona.                                                                 |
| `tel_per`        | `IntegerField`      | Teléfono de la persona (opcional).                                                          |
| `email_per`      | `EmailField`        | Email de la persona.                                                                        |
| `dir_per`        | `CharField` (150)   | Dirección de la persona.                                                                    |
| `sex_per`        | `CharField` (150)   | Género de la persona.                                                                       |
| `uso_datos_per`  | `BooleanField`      | Aceptación de fines de gestión académica y administrativa.                                  |
| `term_per`       | `BooleanField`      | Aceptación de términos y condiciones.                                                       |
| `noti_per`       | `BooleanField`      | Aceptación para recibir notificaciones de oportunidades formativas.                         |



## Datos Formadores
## Tabla de Información Profesional

| Campo                     | Tipo de Dato       | Descripción                                                                                     |
|---------------------------|--------------------|-------------------------------------------------------------------------------------------------|
| `pk_inf_pro`              | `SmallAutoField`   | Id de la Información Profesional (clave primaria).                                              |
| `tit_inf_pro`             | `IntegerField`     | Título académico más alto obtenido.                                                             |
| `tit_esp_inf_pro`         | `CharField` (15)   | Especificar título académico más alto obtenido.                                                 |
| `esp_inf_pro`             | `CharField` (15)   | Área de la especialización principal.                                                           |
| `exp_inf_pro`             | `CharField` (15)   | Años de experiencia como formador/a.                                                            |
| `for_imp_inf_pro`         | `CharField` (15)   | Tipo de formación impartida.                                                                    |
| `cv_adj_inf_pro`          | `CharField` (15)   | Adjuntar currículum en formato PDF.                                                             |
| `mod_inf_pro`             | `CharField` (15)   | Modalidades de enseñanza preferidas para impartir.                                              |
| `tipo_alu_inf_pro`        | `CharField` (15)   | Tipo de alumnado preferido para formar.                                                         |
| `tipo_alu_esp_inf_pro`    | `CharField` (15)   | Especificar tipo de alumnado preferido.                                                         |
| `franja_inf_pro`          | `CharField` (15)   | Franjas horarias disponibles para impartir clases.                                              |
| `cert_inf_pro`            | `CharField` (15)   | Certificaciones docentes.                                                                       |
| `cert_esp_inf_pro`        | `CharField` (15)   | Especificar certificaciones docentes.                                                           |
| `herr_inf_pro`            | `CharField` (15)   | Herramientas tecnológicas utilizadas en clases.                                                 |
| `herr_esp_inf_pro`        | `CharField` (15)   | Especificar herramientas tecnológicas utilizadas.                                               |
| `comp_dig_inf_pro`        | `CharField` (15)   | Competencias digitales específicas (ej. DigCompEdu).                                            |
| `comp_dig_esp_inf_pro`    | `CharField` (15)   | Especificar competencias digitales específicas.                                                 |
| `fk_per_inf_pro`          | `ForeignKey`       | Foreign key de Datos de Personas.                                                               |


   ## Tabla de Entidad de Formación

| Campo                | Tipo de Dato      | Descripción                                                                              |
|----------------------|-------------------|------------------------------------------------------------------------------------------|
| **pk_ent_Form**        | CharField (20)  | Id de la Entidad de Formación (clave primaria). |
| **nom_ent**            | CharField (44)  | Nombre de la entidad de formación.                                                       |
| **Area_forma**         | CharField (44)  | Área de formación de la entidad.                                                         |
| **email**             | EmailField       | Correo electrónico de la entidad.                                                        |
| **nif_ent**            | CharField (20)  | Número de Identificación Fiscal de la entidad.                                           |
| **fecha_final**        | DateField       | Fecha final del periodo de formación.                                                    |
| **fecha_inicial**      | DateField       | Fecha inicial del periodo de formación.                                                  |
| **Area_prof**          | CharField (44)  | Área profesional a la que pertenece la entidad de formación.                             |
| **horas**              | IntegerField    | Horas de formación proporcionadas por la entidad.                                        |
| **CP**                 | CharField (5)   | Código Postal asociado a la entidad de formación.                                        |
| **identificador**      | IntegerField    | Identificador del registro de la entidad de formación.                                   |
| **denominacion**       | CharField (100) | Denominación del registro de la entidad de formación.                                    |
| **ambito**             | CharField (100) | Ámbito de la formación proporcionada por la entidad.                                     |
| **modalidad**          | CharField (50)  | Modalidad de formación (presencial, online, etc.).                                       |
| **num_grupo**          | IntegerField    | Número de grupo asociado a la entidad de formación.                                      |
| **telefono**           | CharField (15)  | Teléfono de contacto de la entidad.


## Tabla de Oferta de Estudio

| Campo               | Tipo de Dato      | Descripción                                                                                |
|---------------------|-------------------|--------------------------------------------------------------------------------------------|
| `pk_ofe_est`        | CharField (20)  | Id de la Oferta de Estudio (clave primaria).                                               |
| `Curs_acad`         | VarChar (44)    | Curso académico correspondiente a la oferta de estudio.                                    |
| `Any_ofe_est`       | NVarChar (44)   | Año de la oferta de estudio.                                                               |
| `Oferta`            | TextField       | Descripción detallada de la oferta de estudio.                                             |
| `nom_ofe_est`       | CharField (100) | Nombre de la oferta de estudio.                                                            |
| `Tip_ofe_est`       | CharField (50)  | Tipo de oferta de estudio (ej. Grado, Máster, Doctorado, etc.).                             |
| `sig_uni_ofe_est`   | VarChar (44)    | Sigla de la universidad que ofrece el estudio.                                             |
| `resp_ofe_est`      | CharField (100) | Responsable de la oferta de estudio.                                                       |
| `via_acc_ofe_est`   | CharField (100) | Vías de acceso a la oferta de estudio.                                                     |
| `Not_tall`          | DecimalField    | Nota de corte para acceder a la oferta de estudio.                                         |
| `Mun_ofe_est`       | CharField (100) | Municipio donde se ofrece el estudio.                                                      |
| `Nom_plazas_ofe_est`| IntegerField    | Número de plazas disponibles en la oferta de estudio.                                      |

