

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



   
