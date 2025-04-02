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

El uso previsto por el equipo consiste en realizar un análisis profundo de la mortalidad en la ciudad, identificando y comparando tendencias a lo largo del tiempo. El estudio buscará establecer correlaciones entre variables demográficas y geográficas para comprender mejor la incidencia de diferentes causas de defunción, lo que podría aportar elementos clave para mejorar las estrategias de prevención y atención médica.

El manejo y análisis de esta base de datos conlleva importantes consideraciones éticas, dado que se trata de información sensible sobre personas fallecidas. Es esencial respetar la privacidad y confidencialidad de los datos, asegurándose de que la información procesada no permita identificar a individuos específicos, con el fin de proteger la dignidad de los fallecidos y la integridad de sus familias. Además, se debe evitar la introducción de sesgos en la interpretación de los resultados, ya que conclusiones erróneas o discriminatorias podrían tener repercusiones negativas en ciertos grupos poblacionales o regiones. La transparencia en la comunicación de los hallazgos y en las limitaciones del análisis es crucial para mantener la objetividad y la responsabilidad ética en todo el estudio.

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
SET municipio_residencia = NULL WHERE municipio_residencia IS NULL OR municipio_residencia ILIKE 'SE IGNORA' OR municipio_residencia ILIKE 'NO ESPECIFICADO';

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

La clasificación original contenía múltiples variaciones y denominaciones específicas que dificultaban la agregación y el análisis de datos. Con esta limpieza, se unificaron ocupaciones en categorías más manejables. Al reducir la granularidad de las ocupaciones en categorías más generales (ej. "Directivos y gerentes", "Profesionales y científicos", "Trabajadores en servicios"), se mejora la comprensión de los datos. Al estructurar los datos de esta manera, se simplifican consultas y reportes estadísticos sin perder información relevante.

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
    
    WHEN ocupacion IN (NULL) 
         THEN NULL

    ELSE 'Ocupaciones no especificadas'
    END;
```

