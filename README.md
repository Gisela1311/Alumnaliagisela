
## Datos Personales

| Datos Personales      | Información                     | Tipo de Dato          |
|-----------------------|---------------------------------|-----------------------|
| **nom_per**           | Nombre completo                 | CharField (max_length=150)         |
| **dni_per**           | DNI/NIE                         | CharField (max_length=15)           |
| **fn_per**            | Fecha de nacimiento             | date                  |
| **nc_per**            | Nacionalidad                    | CharField (max_length=150)           |
| **tel_per**           | Número de contacto              | IntegerField (verbose_name)          |
| **email_per**         | Correo electrónico              | EmailField (verbose_name)         |
| **dir_per**           | Dirección completa              | CharField (max_length=150)          |
| **sexo**              | ¿Cuál es tu género?             | CharField (max_length=150)         |

| Declaraciones y Consentimientos | Información                              | Tipo de Dato |
|---------------------------------|------------------------------------------|--------------|
| **uso_datos_per**               | ¿Autorizas el uso de tus datos con fines de gestión académica y administrativa? |BooleanField     |
| **term_per**                    | ¿Aceptas los términos y condiciones del portal ALUMNALIA?                       | BooleanField     |
| **noti_per**                    | ¿Quieres recibir notificaciones sobre nuevas oportunidades formativas?          | BooleanField      |





## Datos Formadores

| Información Profesional | Detalles                     | Tipo de Dato  |
|-------------------------|------------------------------|---------------|
| **tit_inf_pro**         | Título académico más alto obtenido | varchar(50) |
| **esp_inf_pro**         | ¿En qué área está tu especialización principal? | varchar(50) |
| **exp_inf_pro**         | ¿Cuántos años de experiencia tienes como formador/a? | int         |
| **for_imp_inf_pro**     | ¿Qué tipo de formación has impartido? | varchar(100)|
| **cv_adj_inf_pro**      | Adjunta tu currículum en formato PDF | file        |

| Preferencias de Formación | Detalles                      | Tipo de Dato  |
|---------------------------|-------------------------------|---------------|
| **mod_inf_pro**           | ¿Qué modalidades de enseñanza prefieres impartir? | int  |
| Presencial -> 1           |                               |               |
| En línea -> 2             |                               |               |
| Mixta -> 3                |                               |               |
| **tipo_alu_inf_pro**      | ¿Qué tipo de alumnado prefieres formar? | int  |
| Jóvenes, hasta 25 años -> 1 |                               |               |
| Adultos, más de 25 años -> 2 |                               |               |
| Empresas -> 3             |                               |               |
| Otros (especificar) -> 4  |                               |               |
| **franja_inf_pro**        | ¿En qué franjas horarias estás disponible para impartir clases? | varchar(50) |
| Mañana (8:00-14:00)       |                               |               |
| Tarde (14:00-20:00)       |                               |               |
| Noche (20:00-23:00)       |                               |               |

| Competencias y Certificaciones | Detalles                       | Tipo de Dato |
|--------------------------------|--------------------------------|--------------|
| **cert_inf_pro**               | ¿Tienes alguna certificación docente? | boolean     |
| Sí (especificar)               |                                |              |
| No                             |                                |              |
| **herr_inf_pro**               | ¿Qué herramientas tecnológicas utilizas en tus clases? | varchar(50) |
| Moodle                         |                                |              |
| Microsoft Teams                |                                |              |
| Zoom                           |                                |              |
| Google Classroom               |                                |              |
| Otras (especificar)            |                                |              |
| **comp_dig_inf_pro**           | ¿Posees competencias digitales específicas (ej. DigCompEdu)? | boolean     |
| Sí (especificar)               |                                |              |
| No                             |                                |              |


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



   
