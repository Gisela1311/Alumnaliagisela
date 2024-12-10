
## Datos Personales

| Datos Personales      | Información                     | Tipo de Dato          |
|-----------------------|---------------------------------|-----------------------|
| **nom_per**           | Nombre completo                 | varchar(50)           |
| **dni_per**           | DNI/NIE                         | varchar(20)           |
| **fn_per**            | Fecha de nacimiento             | date                  |
| **nc_per**            | Nacionalidad                    | varchar(30)           |
| **tel_per**           | Número de contacto              | varchar(15)           |
| **email_per**         | Correo electrónico              | varchar(50)           |
| **dir_per**           | Dirección completa              | varchar(100)          |
| **sexo**              | ¿Cuál es tu género?             | varchar(10)           |

| Declaraciones y Consentimientos | Información                              | Tipo de Dato |
|---------------------------------|------------------------------------------|--------------|
| **uso_datos_per**               | ¿Autorizas el uso de tus datos con fines de gestión académica y administrativa? | boolean      |
| **term_per**                    | ¿Aceptas los términos y condiciones del portal ALUMNALIA?                       | boolean      |
| **noti_per**                    | ¿Quieres recibir notificaciones sobre nuevas oportunidades formativas?          | boolean      |



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





   
