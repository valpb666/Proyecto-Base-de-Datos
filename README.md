# Proyecto Base de Datos

## 📌 Introducción al conjunto de datos y al problema a estudiar

**Equipo:**  
Julia Rojas Pereyra, Nuria Garcia Valdecasas, Valentina Pineda, Valentina Covarrubias Faure, Alejandro Salas Aguilar

La base de datos escogida fue la siguiente: https://datos.cdmx.gob.mx/dataset/certificados-de-defuncion-sedesa/resource/fc38b701-964d-4c36-8c63-cca9205ab53f

Este reporte presenta un análisis detallado del conjunto de datos de Certificados de Defunción proporcionado por la Secretaría de Salud de la Ciudad de México. El objetivo principal es identificar patrones y tendencias en la mortalidad, considerando variables clave como la causa de defunción, la edad, el género y la ubicación geográfica. Asimismo, se abordan las consideraciones éticas inherentes al manejo de información sensible relacionada con los fallecidos.

El conjunto de datos se utiliza para ofrecer una perspectiva epidemiológica de los fallecimientos en la Ciudad de México. Permite describir las condiciones de salud de la población, identificar las principales causas de defunción, evaluar la eficacia de la atención médica y detectar patrones temporales y geográficos en la mortalidad.

La información es recolectada por la Secretaría de Salud de la Ciudad de México a partir de los Certificados de Defunción. Los datos son procesados y codificados por médicos codificadores, siguiendo los criterios establecidos por la Organización Mundial de la Salud (OMS), y se capturan en el Subsistema Epidemiológico y Estadístico de las Defunciones (SEED) a nivel federal. Esta base de datos se encuentra disponible en el portal de datos abiertos de la Ciudad de México, en la sección de administración y finanzas, específicamente en el apartado correspondiente a la Secretaría de Salud.

El conjunto fue creado el 13 de marzo del 2021 y su última actualización se realizó el 7 de julio del 2023. Aunque no se especifica la frecuencia exacta de actualización, es relevante mencionar que ha pasado más de un año desde la última actualización.

El dataset cuenta con 127,286 tuplas y 28 atributos, descritos a continuación:

| Atributo                   | Tipo de dato en SQL (Variable)  | Descripción                                                   |
|----------------------------|---------------------------------|---------------------------------------------------------------|
| sexo                       | text (Categórica)              | Género de la persona.                                         |
| fecha_nacimiento           | date (Fecha)                   | Fecha de nacimiento de la persona.                           |
| nacionalidad               | text (Categórica)              | Nacionalidad declarada.                                       |
| lengua_indigena            | text (Categórica)              | Indica si habla una lengua indígena.                         |
| estado_civil               | text (Categórica)              | Estado civil de la persona.                                   |
| entidad_residencia         | text (Categórica)              | Entidad federativa de residencia.                            |
| municipio_residencia       | text (Categórica)              | Municipio o alcaldía de residencia.                           |
| escolaridad                | text (Categórica)              | Nivel educativo alcanzado por la persona.                     |
| ocupacion                  | text (Categórica)              | Ocupación o trabajo habitual.                                 |
| afiliacion_medica          | text (Categórica)              | Tipo de afiliación médica que tiene la persona.               |
| fecha_defuncion1           | date (Fecha)                   | Fecha exacta de la defunción.                                 |
| hora_defuncion             | time (Fecha)                   | Hora exacta de la defunción.                                  |
| lugar_defuncion            | text (Categórica)              | Lugar donde ocurrió la defunción.                             |
| entidad_defuncion          | text (Categórica)              | Entidad federativa donde ocurrió la defunción.                |
| alcaldia                   | text (Categórica)              | Alcaldía o municipio donde ocurrió la defunción.              |
| atencion_medica            | text (Categórica)              | Indica si recibió atención médica antes de la defunción.      |
| necropsia                  | text (Categórica)              | Indica si se realizó necropsia.                                |
| causa_defuncion            | text (Categórica)              | Causa oficial de la defunción.                                |
| durante_embarazo           | text (Categórica)              | Indica si la defunción ocurrió durante el embarazo.           |
| causado_embarazo           | text (Categórica)              | Indica si la defunción fue causada por el embarazo.           |
| complicacion_embarazo      | text (Categórica)              | Indica si hubo complicaciones relacionadas con el embarazo.   |
| muerte_accidental_violenta | text (Categórica)              | Indica si la muerte fue accidental o violenta.                |
| tipo_evento                | text (Categórica)              | Tipo de evento relacionado con la muerte.                     |
| en_trabajo                 | text (Categórica)              | Indica si el evento ocurrió en el trabajo.                    |
| sitio_lesion               | text (Categórica)              | Lugar físico donde ocurrió la lesión.                         |
| municipio_ocurrencia       | text (Categórica)              | Municipio donde ocurrió el evento.                            |
| fecha_defuncion            | date (Fecha)                   | Fecha de la defunción.                                         |
| edad                       | int (Numérica)                 | Edad de la persona en años.                                   |

El objetivo del conjunto de datos es llevar un control riguroso y detallado de los patrones de mortalidad en la Ciudad de México. Esto incluye estudios epidemiológicos para identificar la incidencia de diversas enfermedades, el análisis de épocas con mayor mortalidad (como la pandemia de COVID-19), la evaluación geográfica de las tasas de defunción en distintas alcaldías, y el análisis demográfico de los fallecimientos. Este análisis permitirá detectar correlaciones entre factores demográficos, socioeconómicos y de salud, y evaluar la eficacia de la atención médica brindada.

El uso previsto por el equipo consiste en realizar un análisis profundo de la mortalidad en la ciudad, identificando y comparando tendencias a lo largo del tiempo. El estudio buscará establecer correlaciones entre variables demográficas y geográficas para comprender mejor la incidencia de diferentes causas de defunción, lo que podría aportar elementos clave para mejorar las estrategias de prevención y atención médica, y optimizar la distribucion de servicios de salud en la ciudad de México. 

El manejo y análisis de esta base de datos conlleva importantes consideraciones éticas, ya que se trata de información sensible sobre personas fallecidas. Es esencial respetar la privacidad y confidencialidad de los datos, asegurándose de que la información procesada no permita identificar a individuos específicos, con el fin de proteger la dignidad de los fallecidos y la integridad de sus familias. Debemos ser concientes en la eliminación o modificación de tuplas de no invisibilizar a las personas que estas tuplas representan. Además, se debe evitar la introducción de sesgos en la interpretación de los resultados, ya que conclusiones erróneas o discriminatorias podrían tener repercusiones negativas en ciertos grupos poblacionales o regiones. La transparencia en la comunicación de los hallazgos y en las limitaciones del análisis es crucial para mantener la objetividad y la responsabilidad ética en todo el estudio.

Este análisis, realizado con un enfoque riguroso y ético, pretende ofrecer una visión integral de la situación epidemiológica en la Ciudad de México y contribuir a la toma de decisiones informadas en materia de salud pública.
    
## 📌 Carga Inicial

Para realizar la carga inicial del set de datos a una base de datos de tipo **PostgreSQL**, sigue los siguientes pasos:  

### ✅ Requisitos Previos  
Antes de comenzar, asegúrate de tener:  
- **PostgreSQL** instalado (`psql` o `pgAdmin`).  
- El archivo de datos **CSV** completamente descomprimido:  
  [Certificados de Defunción - SEDESA](https://datos.cdmx.gob.mx/dataset/certificados-de-defuncion-sedesa).  

---

#### 1️⃣ Creación de la Base de Datos  
En la consola de **psql**, ejecuta el siguiente comando:  

```sql
CREATE DATABASE mortalidad;
```
#### 2️⃣ Creación de Tablas en TablePlus
Abre TablePlus y crea una nueva conexión con la base de datos mortalidad (categoría PostgreSQL).

Abre la opción SQL Query e ingresa el siguiente comando para crear la tabla:

```sql
CREATE TABLE staging(
	sexo text,
	fecha_nacimiento date,
	nacionalidad text,
	lengua_indigena text,
	estado_civil text,
	entidad_residencia text,
	municipio_residencia text,
	escolaridad text,
	ocupacion text,
	afiliacion_medica text,
	fecha_defuncion1 date,
	hora_defuncion time,
	lugar_defuncion text,
	entidad_defuncion text,
	alcaldia text,
	atencion_medica text,
	necropsia text,
	causa_defuncion text,
	durante_embarazo text,
	causado_embarazo text,
	complicacion_embarazo text,
	muerte_accidental_violenta text,
	tipo_evento text,
	en_trabajo text,
	sitio_lesion text,
	municipio_ocurrencia text,
	fecha_defuncion date,
	edad bigint
);

```
#### 3️⃣ Conexión a la Base de Datos y Carga Inicial de Datos
Regresa a la consola psql y ejecuta los siguientes comandos:

```sql
\c mortalidad;
SET CLIENT_ENCODING TO 'UTF8';
\copy staging(sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica, fecha_defuncion1, hora_defuncion, lugar_defuncion, entidad_defuncion, alcaldia, atencion_medica, necropsia, causa_defuncion, durante_embarazo, causado_embarazo, complicacion_embarazo, muerte_accidental_violenta, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, fecha_defuncion, edad) FROM 'path_to_downloaded_csv' WITH (FORMAT CSV, HEADER true, DELIMITER ',', NULL 'NA');
```
## 📊 Análisis Preliminar

Para comenzar con el análisis de los datos, ejecutamos los siguientes comandos en **SQL Query** en **TablePlus**:

### 1. **Columnas con valores únicos**
Para identificar si una columna contiene únicamente valores únicos, utilizamos la siguiente consulta:

```sql
SELECT column_name
FROM staging
GROUP BY column_name
HAVING COUNT(DISTINCT column_name) = COUNT(*);
```

📌 **Las columnas con valores únicos fueron:**  
- `municipio_residencia`  
- `fecha_nacimiento`  
- `alcaldia`  
- `causa_defuncion`  
- `municipio_ocurrencia`  

---

### 2. **Mínimos y máximos de fechas**
Para obtener el rango de fechas en el dataset, ejecutamos:

```sql
SELECT 
    MIN(fecha_nacimiento) AS fecha_nacimiento_min,
    MAX(fecha_nacimiento) AS fecha_nacimiento_max,
    MIN(fecha_defuncion) AS fecha_defuncion_min,
    MAX(fecha_defuncion) AS fecha_defuncion_max
FROM staging
WHERE fecha_nacimiento NOT IN ('NA');
```

📌 **Resultados:**  
- `fecha_nacimiento_min`: **1900-08-29**  
- `fecha_nacimiento_max`: **2020-12-29**  
- `fecha_defuncion_min`: **2020-01-01**  
- `fecha_defuncion_max`: **2020-12-31**  

---

### 3. **Mínimos, máximos y promedios de valores numéricos**
Para analizar los valores numéricos en la columna `edad`, ejecutamos:

```sql
SELECT 
    MIN(edad::INTEGER) AS edad_min,
    MAX(edad::INTEGER) AS edad_max,
    AVG(edad::NUMERIC) AS edad_promedio
FROM staging
WHERE edad NOT IN ('NA');
```

📌 **Resultados:**  
- `edad_min`: **0 años**  
- `edad_max`: **119 años**  
- `edad_promedio`: **65.48 años**  

---

### 4. **Duplicados en atributos categóricos**
En este conjunto de datos, la mayoría de las columnas contienen **valores categóricos**, es decir, datos que representan categorías o grupos específicos en lugar de valores numéricos continuos.

✔ **Todas las columnas categóricas tienen al menos un valor que se repite varias veces**, lo que indica que existen categorías dominantes dentro de cada atributo.

Para analizar la distribución de valores en estas columnas, se puede usar una consulta como esta en SQL:

```sql
SELECT columna_categorica, COUNT(*) AS frecuencia
FROM staging
GROUP BY columna_categorica
ORDER BY frecuencia DESC;
```
📌 **Esto permite identificar los valores más frecuentes en cada categoría y detectar posibles errores o inconsistencias.**

### 5. **Columnas redundantes**

En este conjunto de datos, se ha identificado una columna redundante:  

- **`fecha_defuncion1`**: Esta columna se repite y debe ser eliminada, ya que no aporta valor adicional.

Además, aunque no es estrictamente redundante, podría considerarse la columna **`fecha_nacimiento`** como tal, ya que contamos con la columna **`edad`** que podría derivarse de la fecha de nacimiento. Sin embargo, no es redundante en sí misma, sino que proporciona una referencia directa que puede ser útil en ciertos análisis.

### 6. **Conteo de tuplas por cada categoría**
En esta sección, analizamos la distribución de valores dentro de las columnas categóricas del conjunto de datos. Esto nos permite identificar qué categorías son más comunes y si hay valores atípicos o poco frecuentes.

Para obtener estos conteos, utilizamos la siguiente consulta en SQL:

```sql
SELECT column_name, COUNT(*) 
FROM staging
GROUP BY column_name
ORDER BY COUNT(*) DESC;
```

📌 **Resultados:** 

| sexo                | numero_tuplas  |
|---------------------|----------------|
| hombre            | 73907   |
| mujer           | 53311    |
| se ignora              | 55    |
| no especificado              | 13   |


| estado_civil                | numero_tuplas  |
|---------------------|----------------|
| CASADO(A)            | 54353   |
| VIUDO(A)              | 28596    |
| SOLTERO(A)              | 19390    |
| UNION LIBRE              | 12009    |
| DIVORCIADO(A)           | 4039    |
| SE IGNORA              | 3196    |
| SEPARADO(A)              | 2631    |
| NO APLICA              | 2297   |
| NO ESPECIFICADO              | 775    |

| escolaridad                | numero_tuplas  |
|---------------------|----------------|
| PRIMARIA COMPLETA            | 33301   |
| SECUNDARIA COMPLETA              | 21340    |
| PRIMARIA INCOMPLETA              | 16378    |
| BACHILLERATO O PREPARATORIA COMPLETA              | 15948    |
| LICENCIATURA O PROFESIONAL COMPLETO           | 14750    |
| NINGUNA              | 8557    |
| BACHILLERATO O PREPARATORIA INCOMPLETA              | 3868    |
| SECUNDARIA INCOMPLETA              | 3467   |
| LICENCIATURA O PROFESIONAL COMPLETO           | 2673    |
| SE IGNORA              | 2367    |
| NO APLICA             | 1885    |
| POSGRADO COMPLETO              | 1682    |
| NO ESPECIFICADO             | 767    |
| PREESCOLAR COMPLETO              | 139    |
| POSGRADO INCOMPLETO              | 84    |
| PREESCOLAR INCOMPLETO              | 80    |

| atencion_medica                | numero_tuplas  |
|---------------------|----------------|
| SI            | 122668   |
| NO              | 3068    |
| NO ESPECIFICADO              | 795    |
| SE IGNORA             | 755    |

| necropsia                | numero_tuplas  |
|---------------------|----------------|
| NO            | 120887   |
| SI              | 3991    |
| NO ESPECIFICADO              | 1762    |
| SE IGNORA             | 646    |

| durante_embarazo                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|114389|
|NO ESPECIFICADO|	64291|
|NO ESTUVO EMBARAZADA EN LOS Ì_LTIMOS 11 MESES PREVIOS A LA MUERTE|	6381|
|EL PUERPERIO|	44|
|43 DÌAS A 11 MESES DESPUÌäS DEL PARTO O ABORTO	|24|
|EL EMBARAZO|	17|
|EL PARTO|	2|

| causado_embarazo                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|117454|
|NO ESPECIFICADO|	6855|
|NO|	2636|
|SE IGNORA|	313|
|SI	|28|

| complicacion_embarazo                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|117465|
|NO ESPECIFICADO|	6888|
|NO|	2571|
|SE IGNORA|	310|
|SI	|52|

| muerte_accidental_violenta                | numero_tuplas  |
|---------------------|----------------|
|NO 	|123884|
|SI|	3402|

| tipo_evento                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|123884|
|SE IGNORA|	1583|
|HOMICIDIO|	796|
|ACCIDENTE|	600|
|SUICIDIO	|355|
|NO ESPECIFICADO	|68|

| en_trabajo                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|123978|
|NO|	1918|
|SE IGNORA|	854|
|SI|	460|
|NO ESPECIFICADO	|76|

| lugar_lesion                | numero_tuplas  |
|---------------------|----------------|
|NO APLICA	|123884|
|CALLE O CARRETERA (VÌA PÌ_BLICA)	|1393|
|SE IGNORA	|739|
|VIVIENDA PARTICULAR	|725|
|OTRO	|157|
|ÌREA COMERCIAL O DE SERVICIOS	|156|
|NO ESPECIFICADO	|81|
|VIVIENDA COLECTIVA (ASILO, ORFANATO, ETC)	|78|
|ÌREA INDUSTRIAL (TALLER, FABRICA U OBRA)	|38|
|ESCUELA U OFICINA PUBLICA	|14|
|ÌREA DEPORTIVA	|12|
|GRANJA (RANCHO O PARCELA)	|9|

### 7. **Conteo de valores nulos**
Para contar los valores nulos contamos las casillas que dijeran 'se ingora' o 'no especificado' ya que es lo mismo a no tener el dato, en realidad es un valor nulo.
```sql
WITH valores_nulos AS (
	SELECT 'sexo' AS columna, COUNT(*) as nulos
	FROM staging
	WHERE sexo IS NULL OR sexo=''
	UNION ALL
	SELECT 'fecha_nacimiento' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE fecha_nacimiento IS NULL
	UNION ALL
	SELECT 'nacionalidad' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE nacionalidad IS NULL OR nacionalidad ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'lengua_indigena' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE lengua_indigena IS NULL OR lengua_indigena ILIKE 'SE IGNORA' OR lengua_indigena ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'estado_civil' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE estado_civil IS NULL OR estado_civil ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'entidad_residencia' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE entidad_residencia IS NULL OR entidad_residencia ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'municipio_residencia' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE municipio_residencia IS NULL OR municipio_residencia ILIKE 'SE IGNORA' OR municipio_residencia ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'escolaridad' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE escolaridad IS NULL OR escolaridad ILIKE 'SE IGNORA' OR escolaridad ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'ocupacion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE ocupacion IS NULL OR ocupacion ILIKE 'SE IGNORA' OR ocupacion ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'afiliacion_medica' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE afiliacion_medica IS NULL OR afiliacion_medica ILIKE 'SE IGNORA' OR afiliacion_medica ILIKE 'NO ESPECIFICADO' --Tambien hay valores que dicen ninguna, no se si esos contabilizarlos, porque realmente si se tiene la informacion que no tienen afiliación médica
	UNION ALL
	SELECT 'fecha_defuncion1' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE fecha_defuncion1 IS NULL
	UNION ALL
	SELECT 'hora_defuncion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE hora_defuncion IS NULL
	UNION ALL
	SELECT 'lugar_defuncion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE lugar_defuncion IS NULL OR estado_civil ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'entidad_defuncion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE entidad_defuncion IS NULL OR entidad_defuncion ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'alcaldia' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE alcaldia IS NULL OR alcaldia ILIKE 'SE IGNORA' OR alcaldia ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'atencion_medica' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE atencion_medica IS NULL OR atencion_medica ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'necropsia' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE necropsia IS NULL OR necropsia ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'causa_defuncion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE causa_defuncion IS NULL OR causa_defuncion ILIKE 'SE IGNORA' OR causa_defuncion ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'durante_embarazo' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE durante_embarazo IS NULL OR durante_embarazo ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'causado_embarazo' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE causado_embarazo IS NULL OR causado_embarazo ILIKE 'NO ESPECIFICADO' OR causado_embarazo ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'complicacion_embarazo' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE complicacion_embarazo IS NULL OR complicacion_embarazo ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'muerte_accidental_violenta' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE muerte_accidental_violenta IS NULL OR muerte_accidental_violenta ILIKE 'SE IGNORA' OR muerte_accidental_violenta ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'tipo_evento' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE tipo_evento IS NULL OR tipo_evento ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'en_trabajo' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE en_trabajo IS NULL OR en_trabajo ILIKE 'SE IGNORA'
	UNION ALL
	SELECT 'sitio_lesion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE sitio_lesion IS NULL OR sitio_lesion ILIKE 'SE IGNORA' OR sitio_lesion ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'municipio_ocurrencia' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE municipio_ocurrencia IS NULL OR municipio_ocurrencia ILIKE 'SE IGNORA' OR municipio_ocurrencia ILIKE 'NO ESPECIFICADO'
	UNION ALL
	SELECT 'fecha_defuncion' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE fecha_defuncion IS NULL
	UNION ALL
	SELECT 'edad' AS columna, COUNT(*) AS nulos
	FROM staging
	WHERE edad IS NULL
)
SELECT *
FROM valores_nulos
WHERE nulos>0;
```
📌 **Resultados:** 
| Columna                | Nulos  |
|------------------------|--------|
| tipo_evento            | 1583   |
| sitio_lesion           | 820    |
| ocupacion              | 6611   |
| necropsia              | 646    |
| nacionalidad           | 1038   |
| municipio_residencia   | 9267   |
| municipio_ocurrencia   | 17453  |
| lugar_defuncion        | 3196   |
| lengua_indigena        | 2627   |
| hora_defuncion         | 226    |
| fecha_nacimiento       | 834    |
| estado_civil           | 3196   |
| escolaridad            | 3134   |
| entidad_residencia     | 1039   |
| en_trabajo             | 854    |
| edad                   | 834    |
| durante_embarazo       | 6429   |
| complicacion_embarazo  | 6888   |
| causado_embarazo       | 7168   |
| atencion_medica        | 755    |
| alcaldia               | 3897   |
| afiliacion_medica      | 9935   |

### 8. **Inconsistencias en las fechas**
Para checar si hay alguna inconsistencia en lsa fechas, que la fecha de nacimiento sea después de la feha de defunción, ejecutamos:
```sql
SELECT fecha_nacimiento, fecha_defuncion
FROM staging
WHERE fecha_nacimiento>fecha_defuncion;
```
📌 **Resultados:**  
Obtuvimos 1 caso en el que la fecha de nacimiento es después de la fecha de defunción

fecha de nacimiento: 2020-11-01

fecha de defunción: 2020-03-20

### 9. **Inconsistencias en la edad**
Para checar si hay alguna inconsitencia en las edades de la base de datos, checamos si la edad que está en la base de datos va concorde a la fecha de nacimiento y fecha de defunción:
```sql
SELECT edad, 
       EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) AS edad_checada, 
       (EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) = edad) AS coincide
FROM staging
WHERE EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) <> edad;
```

📌 **Resultados:**  
Obtuvimos 33 casos en donde la edad no coincide, pero solamente es por 1 año.

### 10. **Inconsistencias en la hora de defunción**
Para checar si hay alguna hora que este fuera de los rangos de un día, ejecutamos:
```sql
SELECT hora_defuncion
FROM staging
WHERE hora_defuncion<'00:00:00' OR hora_defuncion>'23:59:59';
```

📌 **Resultados:**  
No obtuvimos ningun caso que estuviera fuera de los rangos de un día de 24 horas.


### 11. **Inconsistencias en el sexo**
Para checar si hay alguna incosistencia en el sexo, checamos si algun hombre esta embarazado:
```sql
SELECT sexo, durante_embarazo
FROM staging
WHERE sexo ILIKE 'hombre' AND (durante_embarazo NOT ILIKE 'NO APLICA' AND durante_embarazo NOT ILIKE 'NO ESPECIFICADO');
```

📌 **Resultados:**  
No obtuvimos ninguna inconsistencia.

### 12. **Inconsistencias en las dos columnas de fecha de defunción**
Para checar si la fecha de defunción coincide en ambas columnas, ejectuamos:
```sql
SELECT fecha_defuncion1, fecha_defuncion, fecha_defuncion1=fecha_defuncion AS coincide
FROM staging
WHERE fecha_defuncion1!=fecha_defuncion;
```

📌 **Resultados:**  
No obtuvimos ninguna inconsistencia, todas las fechas son iguales en ambas columnas.

### 13. **Inconsistencias entre los municipios residenciales y las entidades residenciales**
Para checar si hay algun municipio que tenga varias entidades residenciales, ejecutamos:
```sql
SELECT municipio_residencia, COUNT(DISTINCT entidad_residencia) AS entidades_distintas
FROM staging
GROUP BY municipio_residencia
HAVING COUNT(DISTINCT entidad_residencia) > 1
ORDER BY municipio_residencia;
```
----------------------------------------------------------------------------------------------------------------------------------------------
📌 **Resultados:**  
Se obutiveron varias inconsistencias, las siguientes:

| municipio_residencia                | entidades_distintas  |
|------------------------|--------|
|10 DE ABRIL	|2|
|ACAJETE	|2|
|ACAYUCAN	|2|
|ACTOPAN	|2|
|AGUA BENDITA	|2|
|AGUA DULCE	|4|
|AGUA ZARCA	|2|
|ALVARO OBREGON	|3|
|AMATEPEC	|2|
|AZCAPOTZALCO|	7|
|BARRIO DE GUADALUPE|	2|
|BENITO JUAREZ	|7|
|BUENAVISTA	|2|
|COYOACAN	|3|
|CRUZ BLANCA|	2|
|CUAUHTEMOC|	7|
|CUAUTEPEC|	2|
|DOS RIOS|	2|
|EL ARENAL	|2|
|EL CARMEN	|2|
|EMILIANO ZAPATA|	3|	
|GUADALUPE VICTORIA|	3|
|GUSTAVO A. MADERO|	3|
|IZTACALCO	|2|
|LA LOMA	|2|
|LA NOPALERA	|2|
|LA PAZ	2|
|METEPEC|	3|
|NINGUNO|	8|
|OJO DE AGUA|	2|
|PAPALOTLA|	2|
|PARACUARO|	2|
|PIEDRAS NEGRAS|	2|
|SAN AGUSTIN|	2|
|SAN FELIPE|	3|
|SAN FERNANDO	|2|
|SAN ISIDRO	|2|
|SAN MARCOS	|2|
|SAN MIGUEL	|3|
|SANTA CLARA	|2|
|TECAMACHALCO	|2|
|TENANGO	|2|
|TEPETITLAN	|2|
TEPETZINTLA	|2|
|TLALNEPANTLA	|2|
|TLAXCO	|2|
|TONALA	|2|
|TUXPAN	|3|
|VENUSTIANO CARRANZA	|2|
|VILLA CUAUHTEMOC	|2|
|XICO	|2|
|ZACUALPAN	|2|
|ZARAGOZA	|3|
|NULL	|32|

----------------------------------------------------------------------------------------------------------------------------------------------

### 14. **Inconsistencias entre entidad de defuncion y alcaldia**
Para checar si hay alguna alcaldia que tenga varias entidades de defuncion, ejecutamos:
```sql
SELECT 
    alcaldia, 
    COUNT(DISTINCT entidad_defuncion) AS entidades_distintas
FROM staging
GROUP BY alcaldia
HAVING COUNT(DISTINCT entidad_defuncion) > 1;
```

📌 **Resultados:**  
No obtuvimos ninguna inconsistencia; todas las alcaldias solo tienen una entidad de defunción.

## 🧹 Limpieza de datos

### • Actualización de Valores Nulos
Este cambio en la base de datos tiene como objetivo mejorar la consistencia y calidad de los datos almacenados en la base de datos. Se reemplazan valores ambiguos o indeterminados ('SE IGNORA', 'NO ESPECIFICADO', cadenas vacías '', entre otros) por NULL, asegurando una mejor interpretación de la información y facilitando su análisis posterior.

En los datos de entrada, existen valores que representan información desconocida o no registrada de manera inconsistente (por ejemplo, 'SE IGNORA' en algunas columnas y 'NO ESPECIFICADO' en otras). Al convertir estos valores a NULL:
- Se facilita la manipulación y filtrado de datos en consultas SQL.
- Se evita la confusión entre valores reales y datos faltantes.
- Se estandariza la interpretación de información no disponible en toda la base de datos.

Se ejecutan una serie de consultas UPDATE sobre la tabla staging, estableciendo NULL en las columnas afectadas cuando se encuentran valores ambiguos.

```sql
UPDATE staging
SET sexo = NULL WHERE sexo IS NULL OR sexo = '';

UPDATE staging
SET fecha_nacimiento = NULL WHERE fecha_nacimiento IS NULL;

UPDATE staging
SET nacionalidad = NULL WHERE nacionalidad IS NULL OR nacionalidad ILIKE 'SE IGNORA';

UPDATE staging
SET lengua_indigena = NULL WHERE lengua_indigena IS NULL OR lengua_indigena ILIKE 'SE IGNORA' OR lengua_indigena ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET estado_civil = NULL WHERE estado_civil IS NULL OR estado_civil ILIKE 'SE IGNORA';

UPDATE staging
SET entidad_residencia = NULL WHERE entidad_residencia IS NULL OR entidad_residencia ILIKE 'SE IGNORA';

UPDATE staging
SET municipio_residencia = NULL WHERE municipio_residencia IS NULL OR municipio_residencia ILIKE 'SE IGNORA' OR municipio_residencia ILIKE 'NO ESPECIFICADO' OR municipio_residencia ILIKE 'NINGUNO;

UPDATE staging
SET escolaridad = NULL WHERE escolaridad IS NULL OR escolaridad ILIKE 'SE IGNORA' OR escolaridad ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET ocupacion = NULL WHERE ocupacion IS NULL OR ocupacion ILIKE 'SE IGNORA' OR ocupacion ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET afiliacion_medica = NULL WHERE afiliacion_medica IS NULL OR afiliacion_medica ILIKE 'SE IGNORA' OR afiliacion_medica ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET fecha_defuncion1 = NULL WHERE fecha_defuncion1 IS NULL;

UPDATE staging
SET hora_defuncion = NULL WHERE hora_defuncion IS NULL;

UPDATE staging
SET lugar_defuncion = NULL WHERE lugar_defuncion IS NULL OR lugar_defuncion ILIKE 'SE IGNORA';

UPDATE staging
SET entidad_defuncion = NULL WHERE entidad_defuncion IS NULL OR entidad_defuncion ILIKE 'SE IGNORA';

UPDATE staging
SET alcaldia = NULL WHERE alcaldia IS NULL OR alcaldia ILIKE 'SE IGNORA' OR alcaldia ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET atencion_medica = NULL WHERE atencion_medica IS NULL OR atencion_medica ILIKE 'SE IGNORA';

UPDATE staging
SET necropsia = NULL WHERE necropsia IS NULL OR necropsia ILIKE 'SE IGNORA';

UPDATE staging
SET causa_defuncion = NULL WHERE causa_defuncion IS NULL OR causa_defuncion ILIKE 'SE IGNORA' OR causa_defuncion ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET durante_embarazo = NULL WHERE durante_embarazo IS NULL OR durante_embarazo ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET causado_embarazo = NULL WHERE causado_embarazo IS NULL OR causado_embarazo ILIKE 'NO ESPECIFICADO' OR causado_embarazo ILIKE 'SE IGNORA';

UPDATE staging
SET complicacion_embarazo = NULL WHERE complicacion_embarazo IS NULL OR complicacion_embarazo ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET muerte_accidental_violenta = NULL WHERE muerte_accidental_violenta IS NULL OR muerte_accidental_violenta ILIKE 'SE IGNORA' OR muerte_accidental_violenta ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET tipo_evento = NULL WHERE tipo_evento IS NULL OR tipo_evento ILIKE 'SE IGNORA';

UPDATE staging
SET en_trabajo = NULL WHERE en_trabajo IS NULL OR en_trabajo ILIKE 'SE IGNORA';

UPDATE staging
SET sitio_lesion = NULL WHERE sitio_lesion IS NULL OR sitio_lesion ILIKE 'SE IGNORA' OR sitio_lesion ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET municipio_ocurrencia = NULL WHERE municipio_ocurrencia IS NULL OR municipio_ocurrencia ILIKE 'SE IGNORA' OR municipio_ocurrencia ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET fecha_defuncion = NULL WHERE fecha_defuncion IS NULL;

UPDATE staging
SET edad = NULL WHERE edad IS NULL;
```

### • Cambio a Booleanos 

Se estandarizaron los valores en las columnas lengua_indigena, necropsia, atencion_medica y muerte_accidental_violenta para mejorar la consistencia y calidad de los datos. "SI" se reemplazó por TRUE, y "NO" / "NO APLICA" por FALSE, facilitando el análisis y optimizando consultas en la base de datos.

```sql
UPDATE staging
SET lengua_indigena = TRUE WHERE lengua_indigena  ILIKE 'SI';

UPDATE staging
SET lengua_indigena = FALSE WHERE lengua_indigena  ILIKE 'NO' or lengua_indigena ILIKE 'NO APLICA';

UPDATE staging
SET necropsia = TRUE WHERE necropsia  ILIKE 'SI';

UPDATE staging
SET necropsia = FALSE WHERE necropsia  ILIKE 'NO';

UPDATE staging
set atencion_medica = TRUE where atencion_medica ILIKE 'SI';

UPDATE staging
set atencion_medica = FALSE where atencion_medica ILIKE 'NO';

UPDATE staging
set muerte_accidental_violenta = TRUE where muerte_accidental_violenta ILIKE 'SI';

UPDATE staging
set muerte_accidental_violenta = FALSE where muerte_accidental_violenta ILIKE 'NO';

ALTER TABLE staging
ALTER COLUMN lengua_indigena TYPE BOOLEAN USING lengua_indigena::boolean;

ALTER TABLE staging
ALTER COLUMN necropsia TYPE BOOLEAN USING necropsia::boolean;

ALTER TABLE staging
ALTER COLUMN muerte_accidental_violenta TYPE BOOLEAN USING muerte_accidental_violenta::boolean;

ALTER TABLE staging
ALTER COLUMN atencion_medica TYPE BOOLEAN USING atencion_medica::boolean;
```

### • Reclasificación de las ocupaciones

Se llevó a cabo una reclasificación de las ocupaciones dentro de la tabla staging, agrupándolas en categorías más generales y funcionales. Se aplicó una actualización (UPDATE) con una estructura CASE para normalizar las distintas denominaciones de ocupaciones y reducir la complejidad de la información, facilitando su análisis y uso en procesos posteriores.

La clasificación original contenía múltiples variaciones y denominaciones específicas que dificultaban la agregación y el análisis de datos. Con esta limpieza, se unificaron ocupaciones en categorías más manejables. Al reducir la granularidad de las ocupaciones en categorías más generales (ej. "Directivos y gerentes", "Profesionales y científicos", "Trabajadores en servicios"), se mejora la comprensión de los datos. Al estructurar los datos de esta manera, se simplifican consultas y reportes estadísticos sin perder información relevante, manteniendo la integridad de la base de datos. 

```sql
UPDATE staging
SET ocupacion = CASE 
    WHEN ocupacion IN ('NO REMUNERADO, AMA DE CASA', 'NO OCUPADO, JUBILADO O PENSIONADO', 
                       'NO OCUPADOS', 'NO REMUNERADO, ESTUDIANTE', 'NO APLICA') 
         THEN 'Sin actividad económica'
	 WHEN ocupacion IN ('FUNCIONARIOS Y ALTAS AUTORIDADES DE LOS SECTORES PÌ_BLICO, PRIVADO Y SOCIAL', 
                       'DIRECTORES Y GERENTES DE VENTAS, RESTAURANTES, HOTELES Y OTROS ESTABLECIMIENTOS', 
                       'DIRECTORES Y GERENTES EN SERVICIOS FINANCIEROS, LEGALES, ADMINISTRATIVOS Y SOCIALES', 
                       'DIRECTORES Y GERENTES EN PRODUCCIÌÒN, TECNOLOGÌA Y TRANSPORTE', 
                       'COORDINADORES Y JEFES DE ÌREA EN PRODUCCIÌÒN Y TECNOLOGÌA',
                       'COORDINADORES Y JEFES DE ÌREA EN SERVICIOS FINANCIEROS, ADMINISTRATIVOS Y SOCIALES', 
                       'COORDINADORES Y JEFES DE ÌREA DE VENTAS, RESTAURANTES, HOTELES Y OTROS ESTABLECIMIENTOS',
                       'OTROS DIRECTORES, FUNCIONARIOS, GERENTES, COORDINADORES Y JEFES DE ÌREA, NO CLASIFICADOS ANTERIORMENTE',
                       'OTROS TRABAJADORES AUXILIARES EN ACTIVIDADES ADMINISTRATIVAS, NO CLASIFICADOS ANTERIORMENTE',
                       'SUPERVISORES DE PERSONAL DE APOYO ADMINISTRATIVO, SECRETARIAS, CAPTURISTAS, CAJEROS Y TRABAJADORES DE CONTROL DE ARCHIVO Y TRANSPORTE',
                       'SUPERVISORES Y TRABAJADORES QUE BRINDAN Y MANEJAN INFORMACIÌÒN 39 OTROS TRABAJADORES AUXILIARES EN ACTIVIDADES ADMINISTRATIVAS, NO CLASIFICADOS ANTERIORMENTE'
                       ) 
         THEN 'Directivos y gerentes'

    WHEN ocupacion IN ('INVESTIGADORES Y PROFESIONISTAS EN CIENCIAS EXACTAS, BIOLÌÒGICAS, INGENIERÌA, INFORMÌTICA Y EN TELECOMUNICACIONES', 
                       'PROFESIONISTAS EN CIENCIAS ECONÌÒMICO-ADMINISTRATIVAS, CIENCIAS SOCIALES, HUMANISTAS Y EN ARTES',
                       'AUXILIARES Y TÌäCNICOS EN CIENCIAS EXACTAS, BIOLÌÒGICAS, INGENIERÌA, INFORMÌTICA Y EN TELECOMUNICACIONES',
                       'AUXILIARES Y TÌäCNICOS EN CIENCIAS ECONÌÒMICO-ADMINISTRATIVAS, CIENCIAS SOCIALES, HUMANISTAS Y EN ARTES'
                       ) 
         THEN 'Profesionales y científicos'
         
    WHEN ocupacion IN ('MÌäDICOS, ENFERMERAS Y OTROS ESPECIALISTAS EN 						SALUD', 
    				   'ENFERMERAS, TÌäCNICOS EN MEDICINA Y TRABAJADORES DE APOYO EN SALUD'
                       ) 
         THEN 'Salud'
         
    WHEN ocupacion IN ('PROFESORES Y ESPECIALISTAS EN DOCENCIA',
    				   'AUXILIARES Y TÌäCNICOS EN EDUCACIÌÒN, INSTRUCTORES Y CAPACITADORES'
                       ) 
         THEN 'Educación'

    WHEN ocupacion IN ('EMPLEADOS DE VENTAS EN ESTABLECIMIENTOS', 
                       'COMERCIANTES EN ESTABLECIMIENTOS', 
                       'VENDEDORES AMBULANTES', 
                       'OTROS COMERCIANTES, EMPLEADOS EN VENTAS Y AGENTES DE VENTAS EN ESTABLECIMIENTO, NO CLASIFICADOS ANTERIORMENTE') 
         THEN 'Comerciantes y vendedores'

    WHEN ocupacion IN ('TRABAJADORES EN SERVICIOS DE PROTECCIÌÒN Y VIGILANCIA', 
                       'TRABAJADORES EN CUIDADOS PERSONALES Y DEL HOGAR', 
                       'TRABAJADORES DOMÌäSTICOS, DE LIMPIEZA, PLANCHADORES Y OTROS TRABAJADORES DE LIMPIEZA', 
                       'TRABAJADORES EN SERVICIOS DE ALQUILER', 
                       'TRABAJADORES EN LA PREPARACIÌÒN Y SERVICIO DE ALIMENTOS Y BEBIDAS, ASÌ COMO EN SERVICIOS DE ESPARCIMIENTO Y DE HOTELERÌA', 
                       'AYUDANTES EN LA PREPARACIÌÒN DE ALIMENTOS') 
         THEN 'Trabajadores en servicios'

    WHEN ocupacion IN ('TRABAJADORES EN ACTIVIDADES AGRÌCOLAS Y GANADERAS', 
                       'TRABAJADORES EN ACTIVIDADES PESQUERAS, FORESTALES, CAZA Y SIMILARES', 
                       'OTROS TRABAJADORES EN ACTIVIDADES AGRÌCOLAS, GANADERAS, FORESTALES, CAZA Y PESCA, NO CLASIFICADOS ANTERIORMENTE INEGI.', 
                       'OPERADORES DE MAQUINARIA AGROPECUARIA Y FORESTAL',
                       'TRABAJADORES DE APOYO EN ACTIVIDADES AGROPECUARIAS, FORESTALES, PESCA Y CAZA') 
         THEN 'Trabajadores agrícolas y pesqueros'

    WHEN ocupacion IN ('ARTESANOS Y TRABAJADORES EN LA ELABORACIÌÒN DE PRODUCTOS DE MADERA, PAPEL, TEXTILES Y DE CUERO Y PIEL', 
                       'ARTESANOS Y TRABAJADORES EN EL TRATAMIENTO Y ELABORACIÌÒN DE PRODUCTOS DE METAL', 
                       'ARTESANOS Y TRABAJADORES EN LA ELABORACIÌÒN DE PRODUCTOS DE CERÌMICA, VIDRIO, AZULEJO Y SIMILARES', 
                       'ARTESANOS Y TRABAJADORES EN LA ELABORACIÌÒN DE PRODUCTOS DE HULE, CAUCHO, PLÌSTICOS Y DE SUSTANCIAS QUÌMICAS', 
                       'OTROS TRABAJADORES ARTESANALES NO CLASIFICADOS ANTERIORMENTE') 
         THEN 'Artesanos y manufactura'

    WHEN ocupacion IN ('ENSAMBLADORES Y MONTADORES DE HERRAMIENTAS, MAQUINARIA, PRODUCTOS METÌLICOS Y ELECTRÌÒNICOS', 
                       'OPERADORES DE INSTALACIONES Y MAQUINARIA INDUSTRIAL', 
                       'OTROS OPERADORES DE MAQUINARIA INDUSTRIAL, ENSAMBLADORES Y CONDUCTORES DE TRANSPORTE, NO CLASIFICADOS ANTERIORMENTE') 
         THEN 'Operadores de maquinaria y ensambladores'

    WHEN ocupacion IN ('CONDUCTORES DE TRANSPORTE Y DE MAQUINARIA MÌÒVIL', 
                       'AYUDANTES DE CONDUCTORES DE TRANSPORTE, CONDUCTORES DE TRANSPORTE DE TRACCIÌÒN HUMANA Y ANIMAL Y CARGADORES', 
                       'TRABAJADORES DE PAQUETERÌA, DE APOYO PARA ESPECTÌCULOS, MENSAJEROS Y REPARTIDORES DE MERCANCÌAS') 
         THEN 'Transporte y logística'

    WHEN ocupacion IN ('TRABAJADORES DE APOYO EN LA MINERÌA, CONSTRUCCIÌÒN E INDUSTRIA', 
                       'TRABAJADORES EN LA EXTRACCIÌÒN Y LA EDIFICACIÌÒN DE CONSTRUCCIONES') 
         THEN 'Construcción y minería'

    WHEN ocupacion IN ('TRABAJADORES DE LA ARMADA, EJÌäRCITO Y FUERZA AÌäREA') 
         THEN 'Fuerzas armadas'
         
    WHEN ocupacion IN ('TRABAJADORES EN LA ELABORACIÌÒN Y PROCESAMIENTO DE ALIMENTOS, BEBIDAS Y PRODUCTOS DE TABACO') 
         THEN 'Producción de bienes alimenticios y tabaco'
    
    WHEN ocupacion IN (NULL, 'SE IGNORA', 'NO ESPECIFICADO') 
         THEN NULL

    ELSE 'Ocupaciones no especificadas'
    END;
```
### • Agrupar enfermedades (Causa de defunción)

Se decidió agrupar las causas de defunción en categorías ya que esto simplifica y facilita su análisis. Dado que la base de datos contiene una gran cantidad de causas de muerte específicas que, en muchos casos, pueden resultar redundantes o muy detalladas, se optó por clasificarlas en categorías generales, cuidandonos de no perder información. Esta agrupación permite identificar patrones y tendencias más facilmente, facilitando asi la toma de decisiones basadas en datos y garantizando que los análisis sean más comprensibles y manejables. 

```sql
--LIMPIEZA
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

UPDATE staging
SET causa_defuncion=unaccent(causa_defuncion);

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%NEUMONIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PULMONAR' 
WHERE causa_defuncion ILIKE '%NEUMONIA%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%PULMONAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PULMONAR' 
WHERE causa_defuncion ILIKE '%PULMONAR%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%BRONQUITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PULMONAR' 
WHERE causa_defuncion ILIKE '%BRONQUITIS%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%COVID-19%';

UPDATE staging
SET causa_defuncion='COVID-19' 
WHERE causa_defuncion ILIKE '%COVID-19%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%LEUCEMIA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%LEUCEMIA%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%TUMOR%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%TUMOR%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CARCINOMA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%CARCINOMA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%MELANOMA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%MELANOMA%'; 
 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%INFARTO%';

UPDATE staging
SET causa_defuncion='INFARTO' 
WHERE causa_defuncion ILIKE '%INFARTO%'; 

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%DIABETES%';

UPDATE staging
SET causa_defuncion='DIABETES' 
WHERE causa_defuncion ILIKE '%DIABETES%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%SINDROME%';

UPDATE staging
SET causa_defuncion='SINDROME' 
WHERE causa_defuncion ILIKE '%SINDROME%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CEREBR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%CEREBR%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ALZHEIMER%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ALZHEIMER%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%DEMENCIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%DEMENCIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANEURI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ANEUR%';


SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%PARKINSON%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%PARKINSON%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CARDIACA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%CARDIACA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%FIBRILACIION Y ALETEO VENTRICULAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%FIBRILACIION Y ALETEO VENTRICULAR%';


SELECT LEVENSHTEIN('INFECCIION', 'INFECCION');

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%INFEC%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%INFEC%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEPATITIS%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%HEPATITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%DESNUTRI%';

UPDATE staging
SET causa_defuncion='MALA ALIMENTACIÓN' 
WHERE causa_defuncion ILIKE '%DESNUTRI%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%OBESIDAD%';

UPDATE staging
SET causa_defuncion='MALA ALIMENTACIÓN' 
WHERE causa_defuncion ILIKE '%OBESIDAD%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%SEPSIS%';

UPDATE staging
SET causa_defuncion='SEPSIS' 
WHERE causa_defuncion ILIKE '%SEPSIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HIDROPESIA%';

UPDATE staging
SET causa_defuncion='HIDROPESIA' 
WHERE causa_defuncion ILIKE '%HIDROPESIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEMORRAGIA%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMORRAGIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEMATEMESIS%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMATEMESIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%PANCRE%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL PANCREAS' 
WHERE causa_defuncion ILIKE '%PANCRE%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%APENDIC%';

UPDATE staging
SET causa_defuncion='APENDICITIS' 
WHERE causa_defuncion ILIKE '%APENDIC%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%GENERALE%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%GENERALE%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%COLECISTITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN LA VESICULA BILIAR' 
WHERE causa_defuncion ILIKE '%COLECISTITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%COLANGITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN LA VESICULA BILIAR' 
WHERE causa_defuncion ILIKE '%COLANGITIS%';


SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HERNIA%';

UPDATE staging
SET causa_defuncion='HERNIA' 
WHERE causa_defuncion ILIKE '%HERNIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ALCOH%';

UPDATE staging
SET causa_defuncion='ALCOHOLISMO' 
WHERE causa_defuncion ILIKE '%ALCOH%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEP%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD HEPATICA'  
WHERE causa_defuncion ILIKE '%HEP%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ACCIDENTE%';

UPDATE staging
SET causa_defuncion='ACCIDENTE' 
WHERE causa_defuncion ILIKE '%ACCIDENTE%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%RENAL%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RENAL' 
WHERE causa_defuncion ILIKE '%RENAL%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%INTESTINO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL INTESTINO' 
WHERE causa_defuncion ILIKE '%INTESTINO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%MUCORMIC%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%MUCORMIC%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%TROMBOCITOPENIA%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%TROMBOCITOPENIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HIGADO%';


UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL HIGADO' 
WHERE causa_defuncion ILIKE '%HIGADO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%MENINGITIS%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%MENINGITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%EPILEPSIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%EPILEPSIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AGRE%';

UPDATE staging
SET causa_defuncion='AGRESION' 
WHERE causa_defuncion ILIKE '%AGRE%';


SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HIPERPOTASEMIA%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%HIPERPOTASEMIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%PERITONITIS';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%PERITONITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HIPERTENSI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%HIPERTENSI%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ABDOMEN AGUDO%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%ABDOMEN AGUDO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ABORTO%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%ABORTO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%EMBARAZO%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%EMBARAZO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ABSCESO%';

UPDATE staging
SET causa_defuncion='ABSCESO' 
WHERE causa_defuncion ILIKE '%ABSCESO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ACONDROPLASIA%';

UPDATE staging
SET causa_defuncion='SINDROME' 
WHERE causa_defuncion ILIKE '%ACONDROPLASIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ADHERENCIAS%';

UPDATE staging
SET causa_defuncion='ADHERENCIAS' 
WHERE causa_defuncion ILIKE '%ADHERENCIAS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEMORR%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMORR%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AGRANULOCITOSIS%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%AGRANULOCITOSIS%';


SELECT causa_defuncion
FROM staging
ORDER BY causa_defuncion;
```
### • Revisar ubicación residencial (municipio residencia y entidad residencia)

Para verificar si había inconsistencias, se decidió comprobar si cada municipio de residencia correspondía con una única entidad de residencia, ya que así debería ser. Detectamos que había muchas inconsistencias, las cuales fuimos corrigiendo una por una, identificando a qué entidad pertenecía cada municipio con error.

```sql
--Código para detectar las inconsistencias
SELECT municipio_residencia, COUNT(DISTINCT entidad_residencia) AS entidades_distintas
FROM staging
GROUP BY municipio_residencia
HAVING COUNT(DISTINCT entidad_residencia) > 1
ORDER BY municipio_residencia;

--10 de ABRIL:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '10 DE ABRIL';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '10 DE ABRIL';

--17 de JUNION:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '17 DE JUNIO';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '17 DE JUNIO';

--18 de MARZO:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '18 DE MARZO';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '18 DE MARZO';

--20 de NOVIEMBRE:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '20 DE NOVIEMBRE';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '20 DE NOVIEMBRE';

--28 de MAYO:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '28 DE MAYO%';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '28 DE MAYO%';

--3 Generaciones:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '3 GENERACIONES%';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '3 GENERACIONES%';

--6 Hermanos:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '6 HERMANOS';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '6 HERMANOS';

--ARON JONGITUD:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '%ARON JONGITUD';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '%ARON JONGITUD';

--AB Plastic
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE '%PLASTIC';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE '%PLASTIC';

--Abelardo Mendoza:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ABELARDO MENDOZA';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ABELARDO MENDOZA';

--Abimeri:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ABIMERI%';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ABIMERI%'; 

--Abundio Lopez:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ABUNDIO LOPEZ';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ABUNDIO LOPEZ';

--Abuya:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ABUYA';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ABUYA';

--Acajete:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACAJETE' AND entidad_residencia NOT LIKE 'VERACRUZ%';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'ACAJETE' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Acayucan:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACAYUCAN' AND entidad_residencia NOT LIKE 'VERACRUZ%';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'ACAYUCAN' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Acequia Blanca:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACEQUIA BLANCA';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ACEQUIA BLANCA';

--Acolman...:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACOLMAN DE NEZA%' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ACOLMAN DE NEZA%' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Acopiaxco:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACOPIAXCO%';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ACOPIAXCO%';

--ACOSTA MAZA:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACOSTA MAZA' AND entidad_residencia NOT LIKE 'VERACRUZ%';

UPDATE staging
SET municipio_residencia='TIERRA BLANCA'
WHERE municipio_residencia ILIKE 'ACOSTA MAZA';

SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TIERRA BLANCA' AND entidad_residencia NOT LIKE 'VERACRUZ%';

--Actipan:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACTIPAN';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'ACTIPAN';

--Actopan V:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia ILIKE 'VERACRUZ%';

UPDATE staging
SET municipio_residencia='ACTOPAN V'
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia LIKE 'VERACRUZ%';

--Actopan H:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia ILIKE 'HIDALGO';

UPDATE staging
SET municipio_residencia='ACTOPAN H'
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia LIKE 'HIDALGO';

--Azcapotzalco:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'AZCAPOTZALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'AZCAPOTZALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Gustavo A. Madero:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'GUSTAVO A. MADERO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'GUSTAVO A. MADERO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Ecatepec de Morelos:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ECATEPEC DE MORELOS' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ECATEPEC DE MORELOS' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Ecatzingo de hidalgo:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ECATZINGO DE HIDALGO' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ECATZINGO DE HIDALGO' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Ecatzingo de hidalgo:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ECATZINGO DE HIDALGO' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ECATZINGO DE HIDALGO' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Agua bendita:
SELECT municipio_residencia, entidad_residencia
FROM staging
WHERE municipio_residencia ILIKE 'AGUA BENDITA';

UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'AGUA BENDITA';

--Agua dulce:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'AGUA DULCE' AND entidad_residencia NOT LIKE 'VERACRUZ%';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'AGUA DULCE' AND entidad_residencia NOT LIKE 'VERACRUZ%';

--CAMBIAR TODOS LOS VERACRUZ IGUALES
SELECT entidad_residencia
FROM staging
WHERE entidad_residencia ILIKE 'VERACRUZ%';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE entidad_residencia ILIKE 'VERACRUZ%';

--Agua zarca:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'AGUA ZARCA' AND entidad_residencia NOT LIKE 'QUERETARO';

UPDATE staging
SET entidad_residencia='QUERETARO'
WHERE municipio_residencia ILIKE 'AGUA ZARCA' AND entidad_residencia NOT LIKE 'QUERETARO';

--Alvaro Obregon:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ALVARO OBREGON' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'ALVARO OBREGON' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Amatepec:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'AMATEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'AMATEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Barrio de Guadalupe:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'BARRIO DE GUADALUPE'  AND entidad_residencia NOT LIKE 'NUEVO LEON';

UPDATE staging
SET entidad_residencia='NUEVO LEON'
WHERE municipio_residencia ILIKE 'BARRIO DE GUADALUPE' AND entidad_residencia NOT LIKE 'NUEVO LEON';
  
--Benito Juarez:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'BENITO JUAREZ'  AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'BENITO JUAREZ' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Buenavista:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'BUENAVISTA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'BUENAVISTA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Coyoacan:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'COYOACAN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'COYOACAN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Cruz Blanca:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'CRUZ BLANCA';

UPDATE staging
SET municipio_residencia='Zacualpan'
WHERE municipio_residencia ILIKE 'CRUZ BLANCA';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ZACUALPAN' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Cuauhtemoc CDMX:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND (entidad_residencia LIKE 'CIUDAD DE MEXICO' OR entidad_residencia LIKE 'MEXICO');

UPDATE staging
SET municipio_residencia='CUAUHTEMOC CDMX'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND (entidad_residencia LIKE 'CIUDAD DE MEXICO' OR entidad_residencia LIKE 'MEXICO');

SELECT municipio_residencia, entidad_residencia
FROM staging
WHERE municipio_residencia ILIKE 'CUAUHTEMOC CDMX' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC CDMX' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Cuauhtemoc:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND entidad_residencia NOT LIKE 'CHIHUAHUA';

UPDATE staging
SET entidad_residencia='CHIHUAHUA'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND entidad_residencia NOT LIKE 'CHIHUAHUA';

--Cuautepec:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'CUAUTEPEC' AND entidad_residencia NOT LIKE 'HIDALGO';

UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'CUAUTEPEC' AND entidad_residencia NOT LIKE 'HIDALGO';

--Dos rios:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'DOS RIOS' AND entidad_residencia NOT LIKE 'VERACRUZ';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'DOS RIOS' AND entidad_residencia NOT LIKE 'VERACRUZ';

--El arenal:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'EL ARENAL' AND entidad_residencia NOT LIKE 'HIDALGO';

UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'EL ARENAL' AND entidad_residencia NOT LIKE 'HIDALGO';

--El carmen:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'EL CARMEN' AND entidad_residencia NOT LIKE 'CAMPECHE';

UPDATE staging
SET entidad_residencia='CAMPECHE'
WHERE municipio_residencia ILIKE 'EL CARMEN' AND entidad_residencia NOT LIKE 'CAMPECHE';

--Emiliano zapata:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'EMILIANO ZAPATA' AND entidad_residencia NOT LIKE 'HIDALGO';

UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'EMILIANO ZAPATA' AND entidad_residencia NOT LIKE 'HIDALGO';

--Guadalupe Victoria:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'GUADALUPE VICTORIA';

UPDATE staging
SET municipio_residencia='GUADALUPE VICTORIA PUEBLA'
WHERE municipio_residencia ILIKE 'GUADALUPE VICTORIA' AND entidad_residencia LIKE 'PUEBLA';

--Iztacalco:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'IZTACALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'IZTACALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--La loma:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'LA LOMA' AND entidad_residencia NOT LIKE 'PUEBLA';

UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'LA LOMA' AND entidad_residencia NOT LIKE 'PUEBLA';

--La nopalera:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'LA NOPALERA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'LA NOPALERA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--La paz:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'LA PAZ' AND entidad_residencia NOT LIKE 'BAJA CALIFORNIA SUR';

UPDATE staging
SET entidad_residencia='BAJA CALIFORNIA SUR'
WHERE municipio_residencia ILIKE 'LA PAZ' AND entidad_residencia NOT LIKE 'BAJA CALIFORNIA SUR';

--Metepec:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'METEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'METEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Ojo de Agua:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'OJO DE AGUA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'OJO DE AGUA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Papalotla:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'PAPALOTLA' AND entidad_residencia NOT LIKE 'TLAXCALA';

UPDATE staging
SET entidad_residencia='TLAXCALA'
WHERE municipio_residencia ILIKE 'PAPALOTLA' AND entidad_residencia NOT LIKE 'TLAXCALA';

--Paracuaro:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'PARACUARO' AND entidad_residencia NOT LIKE 'GUANAJUATO';

UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'PARACUARO' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--Piedras negras:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'PIEDRAS NEGRAS' AND entidad_residencia NOT LIKE 'COAHUILA';

UPDATE staging
SET entidad_residencia='COAHUILA'
WHERE municipio_residencia ILIKE 'PIEDRAS NEGRAS' AND entidad_residencia NOT LIKE 'COAHUILA';

--San Agustin:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN AGUSTIN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'SAN AGUSTIN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--San Felipe:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN FELIPE' AND entidad_residencia NOT LIKE 'GUANAJUATO';

UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'SAN FELIPE' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--San Fernando:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN FERNANDO' AND entidad_residencia NOT LIKE 'CHIAPAS';

UPDATE staging
SET entidad_residencia='CHIAPAS'
WHERE municipio_residencia ILIKE 'SAN FERNANDO' AND entidad_residencia NOT LIKE 'CHIAPAS';

--San Isidro:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN ISIDRO' AND entidad_residencia NOT LIKE 'PUEBLA';

UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'SAN ISIDRO' AND entidad_residencia NOT LIKE 'PUEBLA';

--San Marcos:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN MARCOS' AND entidad_residencia NOT LIKE 'GUERRERO';

UPDATE staging
SET entidad_residencia='GUERRERO'
WHERE municipio_residencia ILIKE 'SAN MARCOS' AND entidad_residencia NOT LIKE 'GUERRERO';

--San Miguel:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SAN MIGUEL' AND entidad_residencia NOT LIKE 'GUANAJUATO';

UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'SAN MIGUEL' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--Santa clara:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'SANTA CLARA' AND entidad_residencia NOT LIKE 'DURANGO';

UPDATE staging
SET entidad_residencia='DURANGO'
WHERE municipio_residencia ILIKE 'SANTA CLARA' AND entidad_residencia NOT LIKE 'DURANGO';

--Tecamachalco:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TECAMACHALCO' AND entidad_residencia NOT LIKE 'PUEBLA';

UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'TECAMACHALCO' AND entidad_residencia NOT LIKE 'PUEBLA';

--Tenango:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TENANGO' AND entidad_residencia NOT LIKE 'HIDALGO';

UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'TENANGO' AND entidad_residencia NOT LIKE 'HIDALGO';

--Tepetitlan:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TEPETITLAN' AND entidad_residencia NOT LIKE 'HIDALGO';

UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'TEPETITLAN' AND entidad_residencia NOT LIKE 'HIDALGO';

--Tepetzintla:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TEPETZINTLA' AND entidad_residencia NOT LIKE 'VERACRUZ';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'TEPETZINTLA' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Tlalnepantla:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TLALNEPANTLA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'TLALNEPANTLA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Tlaxco:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TLAXCO' AND entidad_residencia NOT LIKE 'TLAXCALA';

UPDATE staging
SET entidad_residencia='TLAXCALA'
WHERE municipio_residencia ILIKE 'TLAXCO' AND entidad_residencia NOT LIKE 'TLAXCALA';

--Tonala:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'CHIAPAS';

UPDATE staging
SET municipio_residencia='TONALA CHIAPAS'
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'CHIAPAS';

SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'JALISCO';

UPDATE staging
SET municipio_residencia='TONALA JALISCO'
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'JALISCO';

--Tuxpan:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'TUXPAN' AND entidad_residencia NOT LIKE 'MICHOACAN%';

UPDATE staging
SET entidad_residencia='MICHOACAN DE OCAMPO'
WHERE municipio_residencia ILIKE 'TUXPAN' AND entidad_residencia NOT LIKE 'MICHOACAN%';

--Venustiano Carranza:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'VENUSTIANO CARRANZA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'VENUSTIANO CARRANZA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Villa Cuauhtemoc:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'VILLA CUAUHTEMOC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'VILLA CUAUHTEMOC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Xico:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'XICO' AND entidad_residencia NOT LIKE 'VERACRUZ';

UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'XICO' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Zaragoza:
SELECT entidad_residencia, municipio_residencia
FROM staging
WHERE municipio_residencia ILIKE 'ZARAGOZA' AND entidad_residencia NOT LIKE 'PUEBLA';

UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'ZARAGOZA' AND entidad_residencia NOT LIKE 'PUEBLA';
```

### • Arreglar las inconsistencias en las edades (edad)

Para corregir las inconsistencias en las edades que habíamos detectado previamente, calculamos la edad a partir de la fecha de nacimiento y la fecha de defunción, y sustituimos el valor de la edad por el correcto. 

```sql
SELECT edad, 
       EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) AS edad_checada, 
       (EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) = edad) AS coincide
FROM staging
WHERE EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) <> edad;

UPDATE staging
SET edad=EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento))
WHERE EXTRACT(YEAR FROM AGE(fecha_defuncion, fecha_nacimiento)) <> edad;
```
### • Arreglar las inconsistencias en las complicaciones en el embarazo (complicacion embarazo)

Para corregir las inconsistencias en las complicaciones durante el embarazo, se verificó que hubiera coincidencia entre la causa de defunción y la complicación en el embarazo. Cuando se detectaron discrepancias entre estos campos, se actualizó el valor de la complicación en el embarazo para que coincidiera con la causa de defunción correspondiente.

```sql
SELECT causa_defuncion, complicacion_embarazo
FROM staging
WHERE causa_defuncion ILIKE '%EMBARAZO%';

UPDATE staging
SET complicacion_embarazo='SI'
WHERE causa_defuncion ILIKE '%EMBARAZO%';

SELECT durante_embarazo, complicacion_embarazo
FROM staging
WHERE durante_embarazo ILIKE 'NO ESTUVO EMBARAZADA%';

UPDATE staging
SET complicacion_embarazo='NO'
WHERE durante_embarazo ILIKE 'NO ESTUVO EMBARAZADA%' AND complicacion_embarazo ILIKE 'SI';
```

## Normalización de datos

### • Entidades intuitivas
A partir de los datos contenidos en la base de datos, se decidió dividirlos en las siguientes entidades:

#### Entidad: Persona
| Persona           |
|-------------------|
| id_persona        |
| sexo              |
| fecha_nacimiento  |
| nacionalidad      |
| lengua_indígena   |
| estado_civil      |
| escolaridad       |
| ocupación         |
| edad              |

#### Entidad: Residencia
| Residencia             |
|------------------------|
| id_persona (clave foránea) |
| municipio_residencia   |
| entidad_residencia     |

#### Entidad: Evento Defunción
| Evento Defunción       |
|------------------------|
| id_evento              |
| fecha_defuncion        |
| hora_defuncion         |
| lugar_defuncion        |
| tipo_evento            |
| en_trabajo             |
| sitio_lesion           |
| municipio_ocurrencia   |
| entidad_defuncion      |
| alcaldía               |

#### Entidad: Atención Médica
| Atención Médica    |
|--------------------|
| id_atencion        |
| afiliación_medica  |
| atención_medica    |
| necropsia          |

#### Entidad: Muerte
| Muerte                    |
|---------------------------|
| id_muerte                 |
| causa_defuncion           |
| durante_embarazo          |
| causado_embarazo          |
| complicacion_embarazo     |
| muerte_accidental_violenta|

### • Dependencias funcionales y multivaluadas
Después de analizar los datos se encontraron las siguientes dependencias:

#### Dependencias Funcionales no triviales:

**-DF1: {municipio_residencia} → {entidad_residencia}**  
Esta dependencia funcional existe porque cada municipio se encuentra ubicado únicamente dentro de una entidad federativa, por lo tanto, al conocer el municipio, se puede determinar sin ambigüedad la entidad de residencia correspondiente.

**-DF2: {municipio_ocurrencia} → {entidad_defuncion}**  
Cada municipio donde ocurre una defunción pertenece a una sola entidad federativa. Esto implica que, dado un municipio de ocurrencia, se puede identificar de forma única la entidad en la que se registró la defunción.

**-DF3: {fecha_nacimiento, fecha_defuncion} → {edad}**  
La edad de una persona al fallecer puede calcularse directamente a partir de su fecha de nacimiento y la fecha de su defunción. Esta relación permite determinar la edad sin necesidad de que sea almacenada de manera independiente.

**-DF4: {causa_defuncion, durante_embarazo} → {complicacion_embarazo}**  
La combinación entre una causa específica de defunción y el hecho de que la persona estuviera embarazada permite inferir si hubo una complicación relacionada con el embarazo, lo que define una dependencia entre estos atributos.

**-DF5: {alcaldía} → {entidad_defuncion}**  
Cada alcaldía pertenece exclusivamente a una entidad federativa. Por ello, con solo conocer la alcaldía en la que ocurrió la defunción, se puede determinar de manera única la entidad correspondiente.

**-DF6: {causa_defuncion, tipo_evento} → {muerte_accidental_violenta}**  
Ciertas combinaciones entre la causa de defunción y el tipo de evento (como accidente, homicidio, suicidio) permiten determinar si se trata o no de una muerte accidental o violenta. Esta relación expresa una dependencia directa entre esas variables.


#### Dependencias Multivaluadas no triviales

**-DM1: {sexo, fecha_nacimiento, edad} →→ {causa_defuncion}**  
Esta dependencia multivaluada indica que para una misma combinación de sexo, fecha de nacimiento y edad, pueden existir múltiples causas de defunción asociadas. Esto refleja la variedad de posibles causas estadísticas en personas con esas características.

**-DM2: {fecha_defuncion, hora_defuncion} →→ {lugar_defuncion}**  
Dado un conjunto específico de fecha y hora de defunción, pueden estar asociadas múltiples ubicaciones posibles donde pudo haber ocurrido el fallecimiento (como hospital, domicilio, vía pública), lo cual establece una dependencia multivaluada.

### • Normalización de los datos hasta cuarta forma normal
Nos dimos cuenta que la base de datos no tenia ningun atributo que fuera el id de cada persona, por lo que decidimos agregar un id_persona que determina a cada una de las personas, todos los atributos de esa persona. Se decidió agregar este id_persona en la entidad de persona.

Para llegar hasta cuarta forma normal, hicimos:

**-DF1: {municipio_residencia} → {entidad_residencia}** 

Los atributos que conforman esta dependencia pertenecen a la entidad de Residencia con los atributos siguientes.

Residencia={municipio_residencia, entidad_residencia}

{municipio_residencia}<sup>+</sup>={municipio_residencia, entidad_residencia}
 
 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que municipio_residencia es la clave y no hay dependencias transitivas. |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | Sí     | Cumple, ya que municipio_residencia es superclave                            |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | Sí     | Cumple, no hay dependencia multivaluada en esta relación                

**-DF2: {municipio_ocurrencia} → {entidad_defuncion} y DF5: {alcaldia} → {entidad_defuncion}** 

Los atributos que conforman estas dependencias pertenecen a la entidad de Evento Defunción con los atributos siguientes.

Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, entidad_defuncion, alcaldia}

{municipio_ocurrencia}<sup>+</sup>={municipio_ocurrencia, entidad_defunción}

{alcaldia}<sup>+</sup>={alcaldia, entidad_defunción}

 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | No-Sí     | No es super clave, aplicar Heath                            |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | Sí     | Cumple, no hay dependencia multivaluada en esta relación                

Nos dimos cuenta que no se cumplia la forma norma de Boyce_Codd en ninguna de las dos dependencias, por lo que decidimos utilizar el Teroema de Heath para descomponer las dependencias
X: {municipio_ocurrencia}   Y: {entidad_defuncion}
 
 Evento Defuncion 2={municipio_ocurrencia, entidad_defuncion}
  
 Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia} (ya no tiene entidad_defunción)

Nos damos cuenta que al aplicar el Teorema de Heath entidada_defuncion ya no esta en la entidad Evento Defuncion, ya no estan los atributos alcaldia y entidad_defuncion en la misma entidad, por lo tanto la dependencia de DF5: {alcaldia} → {entidad_defuncion} ya no existe en la tabla original, lo que indica que no puede violar ninguna forma normal.

**-DF3: {fecha_nacimiento, fecha_defuncion} → {edad}** 

Los atributos que conforman esta dependencia pertenecen a diferentes entidades, fecha_nacimiento y edad pertenecen a la entidad de Persona y fecha_defuncion pertenece a Evento Defuncion, con los atributos siguientes

Persona={sexo, fecha_nacimiento, nacionalidad, lengua_indígena, estado_civil, escolaridad, ocupación, edad)

Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia} (Recordamos que ya no tiene entidad_defuncion)

Como los atributos de la dependencia funcional estan en diferentes entidades, necesitamos crear una nueva entidad en donde los atributos esten juntos:

Edad={fecha_nacimiento, fecha_defuncion, edad}

 Para checar si esta nueva entidad Edad en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, edad depende completamente de ambas                                       |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas. |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | Sí     | Cumple ya que es super clave                           |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | Sí     | Cumple, no hay dependencia multivaluada en esta relación                

Al ver que eta nueva entidad si está en cuarta forma normal, es correcta. Persona ya no necesita contener el atributo edad, ya que ahora va a estar en la nueva entidad de Edad.

Las entidades se verian de la siguiente manera:

Persona={sexo, fecha_nacimiento, nacionalidad, lengua_indígena, estado_civil, escolaridad, ocupación}

Evento Defuncion={fecha_defuncion, hora_defuncion, lugar_defuncion, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia}

Edad={fecha_nacimiento, fecha_defuncion, edad}

**-DF4: {causa_defuncion, durante_embarazo} → {complicacion_embarazo}**  

Los atributos que conforman esta dependencia pertenecen a la entidad de Muerte con los atributos siguientes.

Muerte={causa_defuncion, durante_embarazo, causado_embarazo, muerte_accidental_violenta, complicacion_embarazo}

{causa_defuncion, durante_embarazo}<sup>+</sup>={causa_defuncion, durante_embarazo, complicacion_embarazo}

 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | No-Sí     | No es super clave, aplicar Heath                            |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | Sí     | Cumple, no hay dependencia multivaluada en esta relación                

Nos dimos cuenta que no se cumplia la forma norma de Boyce_Codd en esta dependencia, por lo que decidimos utilizar el Teroema de Heath para descomponer la dependencia
X: {causa_defuncion, durante_embarazo}   Y: {complicacion_embarazo}
 
 Muerte 2={causa_defuncion, durante_embarazo, complicacion_embarazo}
  
 Muerte={causa_defuncion, durante_embarazo, causado_embarazo, muerte_accidental_violenta}

**-DF6: {causa_defuncion, tipo_evento} → {muerte_accidental_violenta}** 

Los atributos que conforman esta dependencia pertenecen a dos entidades, los atributos de causa_defuncion y muerte_acidental_violenta pertenecen a la entidad de Muerte y tipo_evento pertence a le entidad de Evento Defuncion, con los atributos siguientes.

Muerte={causa_defuncion, durante_embarazo, causado_embarazo, muerte_accidental_violenta} (recordemos que ya no tiene complicacion embarazo)

Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia} (recordemos que ya no tiene entidad_defunción)

Como los atributos de la dependencia funcional están en diferentes entidades, necesitamos crear una nueva entidad en donde los atributos esten juntos:

Muerte Accidental={causa_defuncion, tipo_evento, muerte_accidental_violenta}

 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | Sí     | Cumple, ya que es super clave                           |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | Sí     | Cumple, no hay dependencia multivaluada en esta relación                

Al ver que eta nueva entidad si está en cuarta forma normal, es correcta. Muerte ya no necesita contener el atributo muerte_accidental_violenta, ya que ahora va a estar en la nueva entidad de Muerte Accidental.

Las entidades se verian de la siguiente manera:

Muerte={causa_defuncion, durante_embarazo, causado_embarazo}

Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia} (recordemos que ya no tiene entidad_defunción)

Muerte Accidental={causa_defuncion, tipo_evento, muerte_accidental_violenta}

**-DM1: {sexo, fecha_nacimiento, edad} →→ {causa_defuncion}**

Los atributos que conforman esta dependencia multivaluada pertenecen a varias entidades diferentes, los atributos sexo y fecha de nacimiento pertencen a la entidad de Persona, el atributo de edad pertenece a la nueva entidad de Edad y causa defuncion pertenece a la entidad de Muerte, con los atributos siguientes (después de aplicar todas las dependencias funcionales):

Muerte={causa_defuncion, durante_embarazo, causado_embarazo}

Persona={sexo, fecha_nacimiento, nacionalidad, lengua_indígena, estado_civil, escolaridad, ocupación}

Edad={fecha_nacimiento, fecha_defuncion, edad}

Como los atributos de la dependencia multivaluada están en diferentes entidades, necesitamos crear una nueva entidad en donde los atributos esten juntos:

Sexo Edad Causa={sexo, fecha_nacimiento, edad, causa_defuncion}

 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | Sí     | Cumple, es super clave        |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | No-Sí     | No ya que hay dependencias multivaluadas, aplicamos Fagin


Nos dimos cuena que era una dependencia multivaluada, por lo que aplicamos Teorema Fagin
X: {sexo, fecha_nacimiento, edad}   Y: {causa_defuncion}
 
 Sexo Edad Causa={sexo, fecha_nacimiento, edad, causa_defuncion}
  
 Muerte={causa_defuncion, durante_embarazo, causado_embarazo, muerte_accidental_violenta} (se mantiene igual)

**-DM2: {fecha_defuncion, hora_defuncion} →→ {lugar_defuncion}**

Los atributos que conforman esta dependencia multivaluada pertenecen a la entidad de Evento Defuncion, con los siguientes atributos:

Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia}

{fecha_defuncion, hora_defuncion}<sup>+</sup>={lugar_defuncion}

 Para checar si está en 4FN checaremos si cumple cada una de las formas normales anteriores:
 
| Forma Normal | Pregunta                                                             | Cumple | Justificación                                                                 |
|--------------|----------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|
| 1FN          | ¿Todos los atributos contienen valores atómicos?                     | Sí     | Cumple, ya que no hay listas ni estructuras repetidas                        |
| 2FN          | ¿Algún atributo no clave depende solo de parte de la clave?          | Sí     | Cumple, ya que no hay clave compuesta                                        |
| 3FN          | ¿Hay dependencias transitivas?                                       | Sí     | Cumple, ya que no hay dependencias transitivas |
| BCNF         | ¿Toda DF tiene como determinante una superclave?                    | Sí     | Cumple, es super clave        |
| 4FN          | ¿Toda DMV tiene como determinante una superclave?                    | No-Sí     | No ya que hay dependencias multivaluadas, aplicamos Fagin

Nos dimos cuena que era una dependencia multivaluada, por lo que aplicamos Teorema Fagin
X: {fecha_defuncion, hora_defuncion}   Y: {lugar_defuncion}
 
 Fecha Hora Lugar={fecha_defuncion, hora_defuncion, lugar_defuncion}
  
 Evento Defuncion={fecha_defunción, hora_defunción, lugar_defunción, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia} (se mantiene igual)

 ### • Entidades finales
A partir de las entidades que generamos intuitivamente y las dependenciales funcionales y multivaluadas que encontramos normalizamod los datos y llegamos a las siguientes entidades:

#### Entidad: Persona
| Persona           |
|-------------------|
| id_persona        |
| sexo              |
| fecha_nacimiento  |
| nacionalidad      |
| lengua_indígena   |
| estado_civil      |
| escolaridad       |
| ocupación         |

#### Entidad: Residencia
| Residencia             |
|------------------------|
| id_persona (clave foránea) |
| municipio_residencia   |
| entidad_residencia     |

#### Entidad: Evento Defunción
| Evento Defunción       |
|------------------------|
| id_evento              |
| fecha_defuncion        |
| hora_defuncion         |
| lugar_defuncion        |
| tipo_evento            |
| en_trabajo             |
| sitio_lesion           |
| municipio_ocurrencia   |
| alcaldía               |
 
#### Entidad: Atención Médica
| Atención Médica    |
|--------------------|
| id_atencion        |
| afiliación_medica  |
| atención_medica    |
| necropsia          |

#### Entidad: Muerte
| Muerte                    |
|---------------------------|
| id_muerte                 |
| causa_defuncion           |
| durante_embarazo          |
| causado_embarazo          |

#### Entidad: Edad
| Edad                      |
|---------------------------|
| id_edad                   |
| fecha_nacimiento          |
| fecha_defuncion           |
| edad                      |

#### Entidad: SexoEdadCausa
| SexoEdadCausa             |
|---------------------------|
| id_sexo_edad_causa        |
| sexo                      |
| fecha_nacimiento          |
| edad                      |
| causa_defuncion           |

#### Entidad: FechaHoraLugar
| FechaHoraLugar            |
|---------------------------|
| id_fecha_hora_lugar       |
| fecha_defuncion           |
| hora_defuncion            |
| lugar_defuncion           |

#### Entidad: MuerteAccidental
| MuerteAccidental          |
|---------------------------|
| id_muerte_accidental      |
| causa_defuncion           |
| tipo_evento               |
| muerte_accidental_violenta|

#### Entidad: MuerteEmbarazo
| MuerteAccidental          |
|---------------------------|
| id_muerte_embarazo        |
| durante_embarazo          |
| complicacion_embarazo     |

#### Entidad: DefuncionOcurrencia
| DefuncionOcurrencia       |
|---------------------------|
| id_defuncion_ocurrencia   |
| municipio_ocurrencia      |
| entidad_defuncion         |
