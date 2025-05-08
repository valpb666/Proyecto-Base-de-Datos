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
| tipo_evento                | text (Categórica)              | Tipo de evento relacionado con la muerte accidental o violenta|
| en_trabajo                 | text (Categórica)              | Indica si la muerte accidental o violenta ocurrió en el trabajo.                    |
| sitio_lesion               | text (Categórica)              | Lugar físico donde ocurrió la muerte accidental o violenta                  |
| municipio_ocurrencia       | text (Categórica)              | Municipio donde ocurrió la muerte accidental o violenta.                            |
| fecha_defuncion            | date (Fecha)                   | Fecha de la defunción.                                         |
| edad                       | int (Numérica)                 | Edad de la persona en años.                                   |

El objetivo del conjunto de datos es llevar un control riguroso y detallado de los patrones de mortalidad en la Ciudad de México, enfocándose exclusivamente en personas mexicanas y en defunciones por causas naturales o relacionadas con la salud, excluyendo aquellas de origen accidental o violento. Esto incluye estudios epidemiológicos para identificar la incidencia de diversas enfermedades, el análisis de épocas con mayor mortalidad (como la pandemia de COVID-19), la evaluación geográfica de las tasas de defunción en distintas alcaldías, y el análisis demográfico de los fallecimientos. Este análisis permitirá detectar correlaciones entre factores demográficos, socioeconómicos y de salud, y evaluar la eficacia de la atención médica brindada.

El uso previsto por el equipo consiste en realizar un análisis profundo de la mortalidad en la ciudad, identificando y comparando tendencias a lo largo del tiempo. El estudio buscará establecer correlaciones entre variables demográficas y geográficas para comprender mejor la incidencia de diferentes causas de defunción natural o sanitaria, lo que podría aportar elementos clave para mejorar las estrategias de prevención y atención médica, así como optimizar la distribución de servicios de salud en la Ciudad de México.

El manejo y análisis de esta base de datos conlleva importantes consideraciones éticas, ya que se trata de información sensible sobre personas fallecidas. Debemos ser concientes en la eliminación o modificación de tuplas de no invisibilizar a las personas que estas tuplas representan. Además, se debe evitar la introducción de sesgos en la interpretación de los resultados, ya que conclusiones erróneas o discriminatorias podrían tener repercusiones negativas en ciertos grupos poblacionales o regiones. La transparencia en la comunicación de los hallazgos y en las limitaciones del análisis es crucial para mantener la objetividad y la responsabilidad ética en todo el estudio.

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

En este conjunto de datos, se han identificado varias columnas redundantes o innecesarias, considerando el enfoque específico del análisis, que se limita a personas mexicanas fallecidas por causas naturales o relacionadas con la salud, y dentro del territorio de la Ciudad de México.

`fecha_defuncion1`: Esta columna está duplicada y debe ser eliminada, ya que no aporta información adicional respecto a fecha_defuncion.

`edad`: Aunque puede parecer útil como referencia directa, es una columna redundante, ya que puede calcularse a partir de la diferencia entre fecha_nacimiento y fecha_defuncion. Por lo tanto, puede eliminarse para evitar inconsistencias entre valores calculados y registrados manualmente.

`entidad_defuncion`: Es redundante porque todas las muertes consideradas ocurrieron en la Ciudad de México. No aporta variabilidad al conjunto de datos, por lo que puede eliminarse.

`nacionalidad`: También se considera redundante, ya que el análisis solo incluirá personas de nacionalidad mexicana, lo cual hace innecesaria esta columna.

Además, debido a que el estudio no considera muertes accidentales ni violentas, sino únicamente aquellas relacionadas con causas naturales o de salud, se eliminarán las siguientes columnas, ya que no aportan valor dentro del objetivo definido:

`muerte_accidental_violenta`: Indica si la muerte fue accidental o violenta. Esta categoría queda fuera del enfoque del análisis.

`tipo_evento`: Describe si el fallecimiento fue por homicidio, suicidio u otro evento violento. Esta información no es relevante dado que se excluyen dichas causas.

`en_trabajo`: Especifica si la muerte violenta o accidental ocurrió durante una actividad laboral.

`sitio_lesion`: Señala el lugar físico donde ocurrió un accidente o lesión. Dado el enfoque sanitario del análisis, esta columna es irrelevante.

`municipio_ocurrencia`: Indica el municipio donde ocurrió el incidente, utilizado en casos de muertes accidentales o violentas. Como el análisis se restringe a la Ciudad de México y a causas naturales, esta columna también puede eliminarse.

Estas eliminaciones ayudarán a depurar el conjunto de datos, reducir su complejidad y mejorar la precisión de los análisis centrados exclusivamente en la mortalidad natural de personas mexicanas en la Ciudad de México.

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

Aunque inicialmente podría parecer que existen inconsistencias debido a que algunos municipios aparecen asociados con múltiples entidades federativas, esto no representa un error en sí mismo. En México, es común que distintos estados tengan municipios con nombres homónimos, como "Benito Juárez", "Álvaro Obregón" o "San Miguel", por lo que es perfectamente posible que un mismo nombre de municipio aparezca con distintas entidades en el conjunto de datos. Esta situación no indica una contradicción, sino una limitación del uso de nombres sin claves geográficas únicas, como los códigos del INEGI. Por otro lado, el valor NULL en la columna municipio_residencia no representa una inconsistencia con entidad_residencia, sino un dato faltante que debe tratarse como tal. Por lo tanto, no se eliminarán estos registros por considerarse inconsistentes, pero se recomienda revisar y, de ser posible, normalizar la información utilizando catálogos oficiales para mayor precisión en el análisis.

### 14. Inconsistencias en las causas de muerte 

Aunque ciertos registros no están etiquetados explícitamente como "muerte_accidental_violenta" en la columna correspondiente, al revisar la columna "causa_defuncion", se observa que las causas de defunción reportadas corresponden a situaciones que deberían ser clasificadas como muertes accidentales violentas.
```sql
SELECT
	causa_defuncion,
	COUNT(causa_defuncion) AS causas_inconsistentes
FROM
	staging
WHERE
	muerte_accidental_violenta = 'NO'
	AND causa_defuncion ILIKE '%AHOGAMIENTO%'
GROUP BY
	causa_defuncion;
```
📌 **Resultados:**  

| causa_defuncion                | causas_inconsistentes  |
|------------------------|--------|
|AHOGAMIENTO Y SUMERSIÌÒN NO ESPECIFICADOS, LUGAR NO ESPECIFICADO	|3|
|AHOGAMIENTO Y SUMERSIÌÒN, DE INTENCIÌÒN NO DETERMINADA, LUGAR NO ESPECIFICADO	|1|
|LESIÌÒN AUTOINFLIGIDA INTENCIONALMENTE POR AHOGAMIENTO Y SUMERSIÌÒN, LUGAR NO ESPECIFICADO	|1|

```sql

SELECT
	causa_defuncion,
	COUNT(causa_defuncion) AS causas_inconsistentes
FROM
	staging
WHERE
	muerte_accidental_violenta = 'NO'
	AND causa_defuncion ILIKE '%AUTOINFLIGIDA%'
	AND causa_defuncion NOT ILIKE '%AHOGAMIENTO%'
GROUP BY
	causa_defuncion;
```
📌 **Resultados:**  
| causa_defuncion                | causas_inconsistentes  |
|------------------------|--------|
|LESIÌÒN AUTOINFLIGIDA INTENCIONALMENTE POR AHORCAMIENTO, ESTRANGULAMIENTO O SOFOCACIÌÒN, LUGAR NO ESPECIFICADO	|30|
|ALESIÌÒN AUTOINFLIGIDA INTENCIONALMENTE POR OTROS MEDIOS ESPECIFICADOS, LUGAR NO ESPECIFICADO	|1|


```sql
SELECT
	causa_defuncion,
	COUNT(causa_defuncion) AS causas_inconsistentes
FROM
	staging
WHERE
	muerte_accidental_violenta = 'NO'
	AND causa_defuncion ILIKE '%ASFIXIA%'
	AND causa_defuncion NOT ILIKE '%NACIMIENTO%'
GROUP BY
	causa_defuncion;
```
📌 **Resultados:**  
| causa_defuncion                | causas_inconsistentes  |
|------------------------|--------|
ASFIXIA	|2|


----------------------------------------------------------------------------------------------------------------------------------------------

## 🧹 Limpieza de datos

### • Eliminación de Tuplas 

Las tuplas donde la nacionalidad no es mexicana o donde la muerte fue clasificada como accidental o violenta fueron eliminadas, ya que el estudio se enfoca exclusivamente en muertes por causas naturales o de salud de personas mexicanas. Esta depuración garantiza que el análisis se mantenga alineado con el objetivo principal del proyecto y evita introducir sesgos derivados de casos que no corresponden al enfoque epidemiológico buscado.

```sql
DELETE FROM staging
WHERE nacionalidad != 'MEXICANA' OR muerte_accidental_violenta = 'SI';
```

### • Eliminación de columnas

Se eliminaron columnas que ya no aportan valor al conjunto de datos tras el filtrado anterior o que resultan redundantes. Por ejemplo, la columna edad se considera redundante porque puede calcularse a partir de `fecha_nacimiento` y `fecha_defuncion`. También se eliminó `nacionalidad` al haberse filtrado previamente solo a personas mexicanas. Las columnas `muerte_accidental_violenta`, `tipo_evento`, `en_trabajo`, `sitio_lesion` y `municipio_ocurrencia` quedaron fuera del análisis al excluirse las muertes accidentales o violentas. Finalmente, `fecha_defuncion1` fue eliminada por ser una duplicación sin valor adicional.

```sql
ALTER TABLE staging 
DROP COLUMN edad,
DROP COLUMN nacionalidad,
DROP COLUMN muerte_accidental_violenta,
DROP COLUMN tipo_evento,
DROP COLUMN en_trabajo,
DROP COLUMN sitio_lesion,
DROP COLUMN municipio_ocurrencia,
DROP COLUMN fecha_defuncion1
DROP COLUMN entidad_defuncion;
```


### • Actualización de Valores No Especificados

Este cambio en la base de datos tiene como objetivo mejorar la consistencia y calidad de los datos almacenados en la tabla staging, estandarizando la representación de valores ambiguos o indeterminados. Dependiendo del tipo de información y el uso previsto de cada campo, se reemplazan valores como 'SE IGNORA', 'NO ESPECIFICADO' o NULL por representaciones uniformes: ya sea la cadena 'NO ESPECIFICADO' o el valor nulo NULL.

La lógica aplicada distingue dos casos:

Campos categóricos (como sexo, estado_civil, ocupacion, afiliacion_medica, etc.): se utiliza 'NO ESPECIFICADO' como valor explícito cuando la información no está disponible, permitiendo mantener la variable como categórica y útil para análisis o visualización.

Campos que se transformarán posteriormente en atributos de tipo booleano (como lengua_indigena, necropsia, atencion_medica): en estos casos, los valores ambiguos son reemplazados por NULL, ya que representan la ausencia de información verificada. Usar NULL facilita una futura conversión lógica (por ejemplo, TRUE, FALSE o NULL) sin arrastrar etiquetas textuales inconsistentes.

Beneficios de esta estrategia:
- Estandariza la representación de datos faltantes, eliminando inconsistencias como 'SE IGNORA' o 'NO ESPECIFICADO'.

- Facilita el análisis y transformación posterior de los datos, especialmente en los campos booleanos que requieren una interpretación clara.

- Permite un tratamiento más preciso de los datos ausentes, tanto en análisis descriptivos como en modelos automatizados.

```sql
UPDATE staging
SET sexo='NO ESPECIFICADO'
WHERE sexo ILIKE '%se ignora%' OR sexo ILIKE 'no especificado';

UPDATE staging
SET lengua_indigena = NULL WHERE lengua_indigena ILIKE 'SE IGNORA' OR lengua_indigena ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET estado_civil = 'NO ESPECIFICADO' WHERE estado_civil ILIKE 'SE IGNORA';

UPDATE staging
SET entidad_residencia = 'NO ESPECIFICADO' WHERE entidad_residencia IS NULL OR entidad_residencia ILIKE 'SE IGNORA';

UPDATE staging
SET municipio_residencia = 'NO ESPECIFICADO' WHERE municipio_residencia ILIKE 'SE IGNORA';

UPDATE staging
SET ocupacion = 'NO ESPECIFICADO' WHERE ocupacion IS NULL OR ocupacion ILIKE 'SE IGNORA';

UPDATE staging
SET afiliacion_medica = 'NO ESPECIFICADO' WHERE afiliacion_medica ILIKE 'SE IGNORA';

UPDATE staging
SET lugar_defuncion = 'NO ESPECIFICADO' WHERE lugar_defuncion ILIKE 'SE IGNORA';

UPDATE staging
SET alcaldia = 'NO ESPECIFICADO' WHERE alcaldia ILIKE 'SE IGNORA';

UPDATE staging
SET atencion_medica = NULL WHERE atencion_medica IS NULL OR atencion_medica ILIKE 'SE IGNORA' OR atencion_medica ILIKE 'NO ESPECIFICADO';


UPDATE staging
SET necropsia = NULL WHERE necropsia IS NULL OR necropsia ILIKE 'SE IGNORA' OR necropsia ILIKE 'NO ESPECIFICADO';

UPDATE staging
SET causado_embarazo = 'NO ESPECIFICADO' WHERE causado_embarazo ILIKE 'SE IGNORA';

UPDATE staging
SET complicacion_embarazo = 'NO ESPECIFICADO' WHERE complicacion_embarazo ILIKE 'SE IGNORA';
```

### • Cambio a Booleanos 

Se estandarizaron los valores en las columnas lengua_indigena, necropsia, atencion_medica y muerte_accidental_violenta para mejorar la consistencia y calidad de los datos. "SI" se reemplazó por TRUE, y "NO" / "NO APLICA" por FALSE, facilitando el análisis y optimizando consultas en la base de datos.

```sql
UPDATE staging
SET lengua_indigena = TRUE WHERE lengua_indigena = 'SI';

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

ALTER TABLE staging
ALTER COLUMN lengua_indigena TYPE BOOLEAN USING lengua_indigena::boolean;

ALTER TABLE staging
ALTER COLUMN necropsia TYPE BOOLEAN USING necropsia::boolean;

ALTER TABLE staging
ALTER COLUMN atencion_medica TYPE BOOLEAN USING atencion_medica::boolean;
```

### • Agrupar enfermedades (Causa de defunción)

Se decidió agrupar las causas de defunción en categorías ya que esto simplifica y facilita su análisis. Dado que la base de datos contiene una gran cantidad de causas de muerte específicas que, en muchos casos, pueden resultar redundantes o muy detalladas, se optó por clasificarlas en categorías generales, cuidandonos de no perder información. Esta agrupación permite identificar patrones y tendencias más facilmente, facilitando asi la toma de decisiones basadas en datos y garantizando que los análisis sean más comprensibles y manejables. 

```sql
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

UPDATE staging
SET causa_defuncion=unaccent(causa_defuncion);

UPDATE staging
SET causa_defuncion='ENFERMEDAD PULMONAR' 
WHERE causa_defuncion ILIKE '%NEUMONIA%' OR causa_defuncion ILIKE '%PULMONAR%' OR causa_defuncion ILIKE '%BRONQUITIS%' ;

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
WHERE causa_defuncion ILIKE '%SUSTANCIAS%';

UPDATE staging
SET causa_defuncion='SUSTANCIAS' 
WHERE causa_defuncion ILIKE '%SUSTANCIAS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%PERINATAL%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%PERINATAL%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ERITEMATOSA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DERMATOLÓGICA' 
WHERE causa_defuncion ILIKE '%ERITEMATOSA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AHOGAMIENTO%';

UPDATE staging
SET causa_defuncion='AHOGAMIENTO' 
WHERE causa_defuncion ILIKE '%AHOGAMIENTO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AUTOINFLIGIDA%';

UPDATE staging
SET causa_defuncion='SUICIDIO' 
WHERE causa_defuncion ILIKE '%AUTOINFLIGIDA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AHORCAMIENTO%';

UPDATE staging
SET causa_defuncion='AHORCAMIENTO' 
WHERE causa_defuncion ILIKE '%AHORCAMIENTO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ALETEO AURICULAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%ALETEO AURICULAR%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CARDIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%CARDIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AMEBIASIS%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%AMEBIASIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%AMILOIDOSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DEGENERATIVA' 
WHERE causa_defuncion ILIKE '%AMILOIDOSIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANEMIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ANEMIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANENCEFALIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ANENCEFALIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ALCALOSIS%';

UPDATE staging
SET causa_defuncion='TRASTORNOS DEL EQUILIBRIO ÁCIDO-BASE' 
WHERE causa_defuncion ILIKE '%ALCALOSIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANGII%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ANGII%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANGINA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%ANGINA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%HEMANGIOMA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%HEMANGIOMA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%MICROANGIOPATIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%MICROANGIOPATIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%NEFROPA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RENAL' 
WHERE causa_defuncion ILIKE '%NEFROPA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%LINFANGIOMA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%LINFANGIOMA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%COLON%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL COLON' 
WHERE causa_defuncion ILIKE '%COLON%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANOMALI%';

UPDATE staging
SET causa_defuncion='ANOMALIA' 
WHERE causa_defuncion ILIKE '%ANOMALI%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ANQUILOSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD AUDITIVA' 
WHERE causa_defuncion ILIKE '%ANQUILOSIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%APLASIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD HEMATOLOGICA' 
WHERE causa_defuncion ILIKE '%APLASIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ARTR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD AUDITIVA' 
WHERE causa_defuncion ILIKE '%ARTR%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ARTERITI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ARTERITI%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ASFIXIA%';

UPDATE staging
SET causa_defuncion='ASFIXIA' 
WHERE causa_defuncion ILIKE '%ASFIXIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ASMA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%ASMA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%APNEA DEL SUEIOO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%APNEA DEL SUEIOO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%APNEA PRIMARIA DEL SUEIOO DEL RECIIaN NACIDO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%APNEA PRIMARIA DEL SUEIOO DEL RECIIaN NACIDO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%ATROFIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD NEUROLOGICA' 
WHERE causa_defuncion ILIKE '%ATROFIA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%BIPOLAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PSIQUIATRICA' 
WHERE causa_defuncion ILIKE '%BIPOLAR%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CARDIO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%CARDIO%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CIRROSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DIGESTIVA' 
WHERE causa_defuncion ILIKE '%CIRROSIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CONVULSIONES%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD NEUROLOGICA' 
WHERE causa_defuncion ILIKE '%CONVULSIONES%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%DEPRESI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PSIQUIATRICA' 
WHERE causa_defuncion ILIKE '%DEPRESI%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%CAIDA%';

UPDATE staging
SET causa_defuncion='CAIDA' 
WHERE causa_defuncion ILIKE '%CAIDA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%COMA %';

UPDATE staging
SET causa_defuncion='COMA' 
WHERE causa_defuncion ILIKE '%COMA %';

SELECT causa_defuncion
FROM stagin
WHERE causa_defuncion ILIKE '%CELULITIS%';

UPDATE staging
SET causa_defuncion='CELULITIS' 
WHERE causa_defuncion ILIKE '%CELULITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%RESPI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%RESPI%';
```

### • Arreglar las inconsistencias en las complicaciones en el embarazo (complicacion embarazo)

Para corregir las inconsistencias en las complicaciones durante el embarazo, se verificó que hubiera coincidencia entre la causa de defunción y la complicación en el embarazo. Cuando se detectaron discrepancias entre estos campos, se actualizó el valor de la complicación en el embarazo para que coincidiera con la causa de defunción correspondiente.

```sql
UPDATE staging
SET complicacion_embarazo='SI'
WHERE causa_defuncion ILIKE '%EMBARAZO%';

UPDATE staging
SET complicacion_embarazo='NO'
WHERE durante_embarazo ILIKE 'NO ESTUVO EMBARAZADA%' AND complicacion_embarazo ILIKE 'SI';
```

## Normalización de datos

### • Entidades intuitivas
A partir de los datos contenidos en la base de datos, se decidió dividirlos en las siguientes entidades:

#### Entidad: Persona
| persona                 |
|-------------------------|
| id                      |
| sexo                    |
| fecha_nacimiento        |
| lengua_indígena         | 
| estado_civil            |
| residencia_id       (fk)|
| escolaridad             |
| ocupación               |
| afiliación_medica       |
| defuncion_id        (fk)|

#### Entidad: municipio
| municipio         |
--------------------|
| id                |
| entidad_id    (fk)|
| nombre            |

#### Entidad: entidad
| entidad           |
|-------------------|
| id                |
| nombre            |

#### Entidad: Defunción
| defunción                   |
|-----------------------------|
| id                          |
| fecha_defuncion             |
| hora_defuncion              |
| lugar_defuncion             |
| causa_defuncion             |
| alcaldia_defuncion_id  (fk) |
| atención                    |
| necropsia                   |


#### Entidad: Embarazo
| embarazo                  |
|---------------------------|
| id                        |
| persona_id           (fk) |
| causado_embarazo          |
| complicacion_embarazo     |

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

Al ver que esta nueva entidad si está en cuarta forma normal, es correcta. Muerte ya no necesita contener el atributo muerte_accidental_violenta, ya que ahora va a estar en la nueva entidad de Muerte Accidental.

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
| id                |
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
| id                     |
| id_persona             |
| municipio_residencia   |
| entidad_residencia     |

#### Entidad: Evento Defunción
| Evento Defunción       |
|------------------------|
| id                     |
| id_persona             |
| id_residencia          |
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
| id                 |
| id_persona         |
| afiliación_medica  |
| atención_medica    |
| necropsia          |

#### Entidad: Muerte
| Muerte                    |
|---------------------------|
| id                        |
| id_persona                |
| causa_defuncion           |
| durante_embarazo          |
| causado_embarazo          |

#### Entidad: Edad
| Edad                      |
|---------------------------|
| id                        |
| id_persona                |
| fecha_nacimiento          |
| fecha_defuncion           |
| edad                      |

#### Entidad: SexoEdadCausa
| SexoEdadCausa             |
|---------------------------|
| id                        |
| id_persona                |
| sexo                      |
| fecha_nacimiento          |
| edad                      |
| causa_defuncion           |

#### Entidad: FechaHoraLugar
| FechaHoraLugar            |
|---------------------------|
| id                        |
| id_persona                |
| fecha_defuncion           |
| hora_defuncion            |
| lugar_defuncion           |

#### Entidad: MuerteAccidental
| MuerteAccidental          |
|---------------------------|
| id                        |
| id_persona                |
| causa_defuncion           |
| tipo_evento               |
| muerte_accidental_violenta|

#### Entidad: MuerteEmbarazo
| MuerteEmbarazo            |
|---------------------------|
| id                        |
| id_persona                |
| durante_embarazo          |
| complicacion_embarazo     |

#### Entidad: DefuncionOcurrencia
| DefuncionOcurrencia       |
|---------------------------|
| id                        |
| id_persona                |
| municipio_ocurrencia      |
| entidad_defuncion         |

### • Creación de tablas en SQL
Dado que ambas columnas de fecha_defuncion contienen valores idénticos, se optó por ignorar la segunda y utilizar únicamente una de ellas para el modelado.

```sql
ALTER TABLE staging ADD COLUMN id BIGSERIAL NOT NULL;

DROP TABLE IF EXISTS persona;
CREATE TABLE persona(
	id BIGSERIAL PRIMARY KEY,
	sexo VARCHAR (10),
	fecha_nacimiento DATE,
	nacionalidad VARCHAR (50),
	lengua_indigena BOOLEAN, 
	estado_civil VARCHAR(50),
	escolaridad VARCHAR(200),
	ocupacion VARCHAR(200),
	id_staging BIGINT--Solo se va a usar para la relación, después se eliminará
);

INSERT INTO persona(sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, escolaridad, ocupacion, id_staging)
SELECT sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, escolaridad, ocupacion, id
FROM staging;

CREATE TABLE residencia(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	municipio_residencia VARCHAR(200),
	entidad_residencia VARCHAR(200)
);

INSERT INTO residencia(id_persona, municipio_residencia, entidad_residencia)
SELECT persona.id, municipio_residencia, entidad_residencia
FROM staging
JOIN persona ON staging.id = persona.id_staging;

DROP TABLE IF EXISTS evento_defuncion;
CREATE TABLE evento_defuncion(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	fecha_defuncion DATE NOT NULL,
	hora_defuncion TIME,
	lugar_defuncion VARCHAR(500),
	tipo_evento VARCHAR(500),
	en_trabajo BOOLEAN DEFAULT FALSE, 
	sitio_lesion VARCHAR(500),
	municipio_ocurrencia VARCHAR(500),
	alcaldia VARCHAR(500),
	id_residencia BIGINT NOT NULL CONSTRAINT fk_id_residencia REFERENCES residencia(id)
);

INSERT INTO evento_defuncion(id_persona, fecha_defuncion, hora_defuncion, lugar_defuncion, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia, id_residencia)
SELECT persona.id, fecha_defuncion, hora_defuncion, lugar_defuncion, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, alcaldia, residencia.id
FROM staging
JOIN persona ON staging.id = persona.id_staging
JOIN residencia ON persona.id = residencia.id_persona;

DROP TABLE IF EXISTS evento_medico;
CREATE TABLE atencion_medica(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	afiliacion_medica VARCHAR(500),
	atencion_medica BOOLEAN DEFAULT FALSE,
	necropsia BOOLEAN DEFAULT FALSE
);

INSERT INTO atencion_medica(id_persona, afiliacion_medica, atencion_medica, necropsia)
SELECT persona.id, afiliacion_medica, atencion_medica, necropsia
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE muerte(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT CONSTRAINT fk_id_persona REFERENCES persona(id),
	causa_defuncion VARCHAR(500),
	durante_embarazo VARCHAR(500),
	causado_embarazo VARCHAR (500)
);

INSERT INTO muerte(id_persona, causa_defuncion, durante_embarazo, causado_embarazo)
SELECT persona.id, causa_defuncion, durante_embarazo, causado_embarazo
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE edad(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	fecha_nacimiento DATE,
	fecha_defuncion DATE,
	edad SMALLINT
);

INSERT INTO edad(id_persona, fecha_nacimiento, fecha_defuncion, edad)
SELECT persona.id, staging.fecha_nacimiento, fecha_defuncion, edad 
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE sexo_edad_causa(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	sexo VARCHAR(10),
	fecha_nacimiento DATE,
	edad SMALLINT,
	causa_defuncion VARCHAR(500)
);

INSERT INTO sexo_edad_causa(id_persona, sexo, fecha_nacimiento, edad, causa_defuncion)
SELECT persona.id, staging.sexo, staging.fecha_nacimiento, edad, causa_defuncion
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE fecha_hora_lugar(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	fecha_defuncion DATE,
	hora_defuncion TIME,
	lugar_defuncion VARCHAR(500)
);

INSERT INTO fecha_hora_lugar(id_persona, fecha_defuncion, hora_defuncion, lugar_defuncion)
SELECT persona.id, fecha_defuncion, hora_defuncion, lugar_defuncion
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE muerte_accidental(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	causa_defuncion VARCHAR(500),
	tipo_evento VARCHAR(500),
	muerte_accidental_violenta BOOLEAN
);

INSERT INTO muerte_accidental(id_persona, causa_defuncion, tipo_evento, muerte_accidental_violenta)
SELECT persona.id, causa_defuncion, tipo_evento, muerte_accidental_violenta
FROM staging
JOIN persona ON staging.id = persona.id_staging;


CREATE TABLE muerte_embarazo(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	durante_embarazo VARCHAR(500),
	complicacion_embarazo VARCHAR(100)
);

INSERT INTO muerte_embarazo(id_persona, durante_embarazo, complicacion_embarazo)
SELECT persona.id, durante_embarazo, complicacion_embarazo
FROM staging
JOIN persona ON staging.id = persona.id_staging;

CREATE TABLE defuncion_ocurrencia(
	id BIGSERIAL PRIMARY KEY,
	id_persona BIGINT NOT NULL CONSTRAINT fk_id_persona REFERENCES persona(id),
	municipio_ocurrencia VARCHAR(500),
	entidad_defuncion VARCHAR(500)
);

INSERT INTO defuncion_ocurrencia(id_persona, municipio_ocurrencia, entidad_defuncion)
SELECT persona.id, municipio_ocurrencia, entidad_defuncion
FROM staging
JOIN persona ON staging.id = persona.id_staging;

ALTER TABLE persona DROP COLUMN id_staging;

ALTER TABLE staging DROP COLUMN id;

ALTER TABLE staging RENAME TO staging_backup;
```
### ERD

El ERD con todas las entidades después de la normalización, es el siguiente:

![ERD de Hockey](https://github.com/user-attachments/assets/7891d217-0efe-4d46-9f3e-0c3083e361b6)

## Análisis de datos a través de consultas SQL

Algunas de las consultas que hicimos son las siguientes:

### 1. **Análisis de mortalidad y contexto socioeconómico**

Pregunta: ¿Existe una relación entre esolaridad y causa de defunción por sexo? 

Ejecutamos:
```sql
SELECT sexo_edad_causa.sexo, causa_defuncion, persona.escolaridad, COUNT(*) as total
FROM sexo_edad_causa
JOIN persona ON sexo_edad_causa.id_persona=persona.id
GROUP BY sexo_edad_causa.sexo, persona.escolaridad, causa_defuncion
HAVING COUNT(*) > 1000
ORDER BY total DESC;
```
📌 **Resultados:**  

| Sexo  | Causa Defunción           | Escolaridad                              | Total |
|-------|------------------------------|------------------------------------------|--------|
| hombre | COVID-19                    | PRIMARIA COMPLETA                        | 10938  |
| hombre | COVID-19                    | SECUNDARIA COMPLETA                      | 10382  |
| mujer  | COVID-19                    | PRIMARIA COMPLETA                        | 7852   |
| hombre | COVID-19                    | LICENCIATURA O PROFESIONAL COMPLETO     | 7554   |
| hombre | COVID-19                    | BACHILLERATO O PREPARATORIA COMPLETA    | 7520   |
| hombre | DIABETES                    | PRIMARIA COMPLETA                        | 5444   |
| mujer  | DIABETES                    | PRIMARIA COMPLETA                        | 5250   |
| hombre | INFARTO                     | PRIMARIA COMPLETA                        | 4890   |
| mujer  | INFARTO                     | PRIMARIA COMPLETA                        | 4720   |
| hombre | COVID-19                    | PRIMARIA INCOMPLETA                      | 4640   |
| mujer  | COVID-19                    | SECUNDARIA COMPLETA                      | 4388   |
| mujer  | COVID-19                    | PRIMARIA INCOMPLETA                      | 3602   |
| mujer  | COVID-19                    | BACHILLERATO O PREPARATORIA COMPLETA    | 3494   |
| hombre | DIABETES                    | SECUNDARIA COMPLETA                      | 3430   |
| mujer  | DIABETES                    | PRIMARIA INCOMPLETA                      | 3014   |
| hombre | ENFERMEDAD PULMONAR         | PRIMARIA COMPLETA                        | 2858   |
| mujer  | INFARTO                     | PRIMARIA INCOMPLETA                      | 2844   |
| mujer  | CANCER                      | PRIMARIA COMPLETA                        | 2816   |
| mujer  | ENFERMEDAD PULMONAR         | PRIMARIA COMPLETA                        | 2578   |
| hombre | INFARTO                     | PRIMARIA INCOMPLETA                      | 2568   |
| hombre | INFARTO                     | SECUNDARIA COMPLETA                      | 2542   |
| hombre | DIABETES                    | PRIMARIA INCOMPLETA                      | 2312   |
| hombre | COVID-19                    | BACHILLERATO O PREPARATORIA INCOMPLETA  | 2244   |
| hombre | INFARTO                     | LICENCIATURA O PROFESIONAL COMPLETO     | 2192   |
| mujer  | INFARTO                     | NINGUNA                                  | 2120   |
| mujer  | COVID-19                    | LICENCIATURA O PROFESIONAL COMPLETO     | 2116   |
| hombre | CANCER                      | PRIMARIA COMPLETA                        | 2072   |
| mujer  | DIABETES                    | SECUNDARIA COMPLETA                      | 2068   |
| hombre | ENFERMEDAD PULMONAR         | SECUNDARIA COMPLETA                      | 2066   |
| mujer  | CANCER                      | SECUNDARIA COMPLETA                      | 2012   |
| mujer  | CANCER                      | BACHILLERATO O PREPARATORIA COMPLETA    | 2010   |
| hombre | CANCER                      | LICENCIATURA O PROFESIONAL COMPLETO     | 2008   |
| hombre | DIABETES                    | LICENCIATURA O PROFESIONAL COMPLETO     | 1984   |
| mujer  | DIABETES                    | NINGUNA                                  | 1952   |
| hombre | DIABETES                    | BACHILLERATO O PREPARATORIA COMPLETA    | 1922   |
| mujer  | COVID-19                    | NINGUNA                                  | 1898   |
| mujer  | CANCER                      | LICENCIATURA O PROFESIONAL COMPLETO     | 1854   |
| hombre | INFARTO                     | BACHILLERATO O PREPARATORIA COMPLETA    | 1800   |
| hombre | ENFERMEDAD PULMONAR         | LICENCIATURA O PROFESIONAL COMPLETO     | 1652   |
| hombre | COVID-19                    | LICENCIATURA O PROFESIONAL INCOMPLETO   | 1634   |
| hombre | CANCER                      | SECUNDARIA COMPLETA                      | 1628   |
| hombre | COVID-19                    | SECUNDARIA INCOMPLETA                    | 1622   |
| mujer  | INFARTO                     | SECUNDARIA COMPLETA                      | 1542   |
| hombre | CANCER                      | BACHILLERATO O PREPARATORIA COMPLETA    | 1478   |
| mujer  | INFARTO                     | BACHILLERATO O PREPARATORIA COMPLETA    | 1476   |
| mujer  | ENFERMEDAD CARDIACA         | PRIMARIA COMPLETA                        | 1386   |
| mujer  | ENFERMEDAD PULMONAR         | PRIMARIA INCOMPLETA                      | 1370   |
| hombre | ENFERMEDAD PULMONAR         | BACHILLERATO O PREPARATORIA COMPLETA    | 1366   |
| hombre | ENFERMEDAD PULMONAR         | PRIMARIA INCOMPLETA                      | 1366   |
| hombre | COVID-19                    | NINGUNA                                  | 1326   |
| hombre | COVID-19                    | NULL                                     | 1314   |
| mujer  | DIABETES                    | BACHILLERATO O PREPARATORIA COMPLETA    | 1294   |
| mujer  | CANCER                      | PRIMARIA INCOMPLETA                      | 1286   |
| mujer  | ENFERMEDAD PULMONAR         | SECUNDARIA COMPLETA                      | 1208   |
| hombre | INFARTO                     | NINGUNA                                  | 1096   |
| hombre | CANCER                      | PRIMARIA INCOMPLETA                      | 1078   |
| mujer  | ENFERMEDAD PULMONAR         | BACHILLERATO O PREPARATORIA COMPLETA    | 1064   |
| mujer  | INFARTO                     | LICENCIATURA O PROFESIONAL COMPLETO     | 1044   |
| hombre | ENFERMEDAD CARDIACA         | PRIMARIA COMPLETA                        | 1008   |

### 2. **Análisis de enfermedades por alcaldías**

Pregunta: ¿Qué alcaldías concentran más muertes por enfermedades respiratorias (o por COVID-19, si tienes esa categoría)?

Ejecutamos:
```sql
SELECT alcaldia, sexo_edad_causa.causa_defuncion, COUNT(*) AS total
FROM evento_defuncion
JOIN sexo_edad_causa ON sexo_edad_causa.id_persona=evento_defuncion.id_persona
WHERE causa_defuncion ILIKE '%RESP%' OR causa_defuncion ILIKE '%COVID%'
GROUP BY alcaldia, sexo_edad_causa.causa_defuncion;
```
📌 **Resultados:**  

| Alcaldía               | Causa Defunción                                                                                     | Total |
|------------------------------------|---------------------------------------------------------------------------------------------------------|-------|
| AZCAPOTZALCO                       | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 12    |
| MIGUEL HIDALGO                     | TUBERCULOSIS RESPIRATORIA NO ESPECIFICADA, SIN MENCIÓN DE CONFIRMACIÓN BACTERIOLÓGICA O HISTOLÓGICA     | 2     |
| IZTAPALAPA                         | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 2     |
| BENITO JUAREZ                      | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 4     |
| GUSTAVO A. MADERO                  | COVID-19                                                                                                | 9430  |
| BENITO JUAREZ                      | OTROS TRASTORNOS RESPIRATORIOS ESPECIFICADOS                                                            | 8     |
| GUSTAVO A. MADERO                  | OTRAS DIFICULTADES RESPIRATORIAS DEL RECIÉN NACIDO                                                      | 2     |
| IZTACALCO                          | INFLUENZA CON OTRAS MANIFESTACIONES RESPIRATORIAS, VIRUS NO IDENTIFICADO                                | 2     |
| ALVARO OBREGON                     | OTROS PROBLEMAS RESPIRATORIOS ESPECIFICADOS DEL RECIÉN NACIDO                                          | 2     |
| VENUSTIANO CARRANZA                | INSUFICIENCIA RESPIRATORIA, NO ESPECIFICADA                                                             | 2     |
| TLALPAN                            | INHALACIÓN E INGESTIÓN DE OTROS OBJETOS QUE CAUSAN OBSTRUCCIÓN DE LAS VÍAS RESPIRATORIAS               | 2     |
| BENITO JUAREZ                      | COVID-19                                                                                                | 8568  |
| TLALPAN                            | OTRAS ENFERMEDADES ESPECIFICADAS DE LAS VÍAS RESPIRATORIAS SUPERIORES                                  | 2     |
| CUAUHTEMOC                         | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 8     |
| CUAUHTEMOC                         | OTRAS OBSTRUCCIONES ESPECIFICADAS DE LA RESPIRACIÓN                                                     | 4     |
| ALVARO OBREGON                     | INSUFICIENCIA RESPIRATORIA AGUDA                                                                        | 28    |
| IZTAPALAPA                         | INSUFICIENCIA RESPIRATORIA, NO ESPECIFICADA                                                             | 4     |
| LA MAGDALENA CONTRERAS             | COVID-19                                                                                                | 212   |
| MIGUEL HIDALGO                     | INSUFICIENCIA RESPIRATORIA AGUDA                                                                        | 2     |
| OJO DE AGUA                        | COVID-19                                                                                                | 4     |
| IZTACALCO                          | OBSTRUCCIÓN NO ESPECIFICADA DE LA RESPIRACIÓN                                                           | 4     |
| ALVARO OBREGON                     | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 2     |
| IZTACALCO                          | TRASTORNO RESPIRATORIO, NO ESPECIFICADO                                                                 | 2     |
| NULL                               | OTRAS OBSTRUCCIONES ESPECIFICADAS DE LA RESPIRACIÓN                                                     | 2     |
| IZTACALCO                          | INSUFICIENCIA RESPIRATORIA AGUDA                                                                        | 18    |
| BENITO JUAREZ                      | TUBERCULOSIS RESPIRATORIA NO ESPECIFICADA, SIN MENCIÓN DE CONFIRMACIÓN BACTERIOLÓGICA O HISTOLÓGICA     | 4     |
| BENITO JUAREZ                      | INSUFICIENCIA RESPIRATORIA AGUDA                                                                        | 8     |
| ALVARO OBREGON                     | COVID-19                                                                                                | 5826  |
| IZTAPALAPA                         | PARO RESPIRATORIO                                                                                       | 2     |
| ...                                | ...                                                                                                     | ...   |


### 3. **Análisis de muertes por fechas**

Pregunta: ¿Se repiten ciertos patrones de mortalidad en los mismos meses a lo largo de los años?

Ejecutamos:
```sql
SELECT EXTRACT (MONTH FROM fecha_defuncion) as año, COUNT(*) cant_muertes
FROM evento_defuncion
GROUP BY EXTRACT (MONTH FROM fecha_defuncion);
```
📌 **Resultados:**  

| Mes_en_numero | Cant Muertes |
|-----|----------------------|
| 1   | 15,834               |
| 2   | 12,746               |
| 3   | 12,814               |
| 4   | 17,516               |
| 5   | 33,940               |
| 6   | 26,764               |
| 7   | 20,212               |
| 8   | 20,348               |
| 9   | 18,952               |
| 10  | 19,686               |
| 11  | 20,338               |
| 12  | 35,422               |

### 4. **Análisis mortalidad materna**

Pregunta: ¿Cuántas muertes relacionadas con embarazo se reportan, y en qué etapas?

Ejecutamos:
```sql
SELECT sexo_edad_causa.edad, persona.escolaridad, durante_embarazo, complicacion_embarazo
FROM muerte_embarazo
JOIN sexo_edad_causa ON sexo_edad_causa.id_persona=muerte_embarazo.id_persona
JOIN persona ON persona.id=muerte_embarazo.id_persona
WHERE complicacion_embarazo IS NOT NULL AND durante_embarazo IS NOT NULL AND durante_embarazo NOT LIKE 'NO %'
GROUP BY sexo_edad_causa.edad, persona.escolaridad, durante_embarazo, complicacion_embarazo
ORDER BY edad ASC;
```
📌 **Resultados:**  

| Edad | Escolaridad                                | Durante Embarazo                                    | Complicación Embarazo |
|------|--------------------------------------------------|---------------------------------------------|------------------------|
| 17   | Secundaria completa                             | El puerperio                                | No                     |
| 19   | Bachillerato o preparatoria incompleta          | 43 días a 11 meses después del parto o aborto | Sí                     |
| 19   | Secundaria completa                             | 43 días a 11 meses después del parto o aborto | No                     |
| 19   | Secundaria completa                             | El embarazo                                 | Sí                     |
| 20   | Licenciatura o profesional incompleto           | El puerperio                                | Sí                     |
| 21   | Bachillerato o preparatoria incompleta          | 43 días a 11 meses después del parto o aborto | No                     |
| 22   | Bachillerato o preparatoria completa            | El puerperio                                | Sí                     |
| 22   | Bachillerato o preparatoria incompleta          | El puerperio                                | Sí                     |
| 22   | Secundaria completa                             | El embarazo                                 | No                     |
| 23   | Bachillerato o preparatoria completa            | El embarazo                                 | No                     |
| 23   | Bachillerato o preparatoria completa            | El puerperio                                | Sí                     |
| 23   | Bachillerato o preparatoria incompleta          | El puerperio                                | Sí                     |
| 24   | Bachillerato o preparatoria completa            | 43 días a 11 meses después del parto o aborto | No                     |
| 24   | Licenciatura o profesional completo             | 43 días a 11 meses después del parto o aborto | No                     |
| 24   | Secundaria completa                             | 43 días a 11 meses después del parto o aborto | No                     |
| 25   | Bachillerato o preparatoria incompleta          | El puerperio                                | Sí                     |
| 25   | Licenciatura o profesional incompleto           | 43 días a 11 meses después del parto o aborto | No                     |
| 26   | Licenciatura o profesional completo             | El embarazo                                 | Sí                     |
| 26   | Licenciatura o profesional completo             | El puerperio                                | Sí                     |
| 27   | Bachillerato o preparatoria completa            | 43 días a 11 meses después del parto o aborto | Sí                     |

### 5. **Análisis entre atención médica y tipo de muerte**

Pregunta: ¿Las personas que recibieron atención médica tienen menor probabilidad de morir por causas violentas?

Ejecutamos:
```sql
SELECT causa_defuncion, atencion_medica.atencion_medica, COUNT(*) AS total
FROM sexo_edad_causa
JOIN atencion_medica ON sexo_edad_causa.id_persona=atencion_medica.id_persona
GROUP BY causa_defuncion, atencion_medica.atencion_medica
ORDER BY total DESC;

SELECT sexo_edad_causa.causa_defuncion, atencion_medica.atencion_medica, muerte_accidental.muerte_accidental_violenta, COUNT(*) AS total
FROM sexo_edad_causa
JOIN atencion_medica ON sexo_edad_causa.id_persona=atencion_medica.id_persona
JOIN muerte_accidental ON
sexo_edad_causa.id_persona=muerte_accidental.id_persona
WHERE muerte_accidental_violenta=TRUE
GROUP BY sexo_edad_causa.causa_defuncion, atencion_medica.atencion_medica, muerte_accidental_violenta
ORDER BY total DESC;
```
📌 **Resultados:**  
| Causa defunción                                      | Atención Médica | Total |
|---------------------------------------------------------|------------|-------|
| COVID-19                                                | true       | 74250 |
| Diabetes                                                | true       | 32658 |
| Infarto                                                 | true       | 30338 |
| Cáncer                                                  | true       | 21764 |
| Enfermedad pulmonar                                     | true       | 19858 |
| Enfermedad cardiaca                                     | true       | 7384  |
| Enfermedad renal                                        | true       | 5802  |
| Infección                                               | true       | 5042  |
| Hemorragia                                              | true       | 4426  |
| Enfermedad cerebral                                     | true       | 3566  |
| Alcoholismo                                             | true       | 3244  |
| Síndrome                                                | true       | 2218  |
| Enfermedad en el hígado                                 | true       | 2132  |
| Accidente                                               | true       | 2010  |
| Enfermedad hepática                                     | true       | 1998  |
| Sepsis                                                  | true       | 1408  |
| Enfermedad en el intestino                              | true       | 1156  |
| Mala alimentación                                       | true       | 1036  |
| Agresión                                                | true       | 998   |

### 6. **Análisis entre municipio residencia y municipio ocurrencia**

Pregunta: ¿Cuántos casos ocurren fuera del municipio o entidad de residencia?

Ejecutamos:
```sql
WITH mismo_lugar AS(
	SELECT municipio_residencia, COUNT(*) as total
	FROM residencia
	JOIN defuncion_ocurrencia ON residencia.id_persona=defuncion_ocurrencia.id_persona
	WHERE municipio_residencia=defuncion_ocurrencia.municipio_ocurrencia
	GROUP BY municipio_residencia
	ORDER BY total DESC
),
diferente_lugar AS(
	SELECT municipio_residencia, COUNT(*) as total
	FROM residencia
	JOIN defuncion_ocurrencia ON residencia.id_persona=defuncion_ocurrencia.id_persona
	WHERE municipio_residencia!=defuncion_ocurrencia.municipio_ocurrencia
	GROUP BY municipio_residencia
	ORDER BY total DESC
)

SELECT mismo_lugar.municipio_residencia, mismo_lugar.total AS total_mismo_lugar, diferente_lugar.total AS total_diferente_lugar
FROM mismo_lugar 
LEFT JOIN diferente_lugar ON mismo_lugar.municipio_residencia= diferente_lugar.municipio_residencia
ORDER BY mismo_lugar.municipio_residencia;
```
📌 **Resultados:**  
| Sexo   | Causa Defuncion                | Escolaridad                                 | Total |
|--------|----------------------|---------------------------------------------|--------|
| hombre | COVID-19             | PRIMARIA COMPLETA                           | 10938  |
| hombre | COVID-19             | SECUNDARIA COMPLETA                         | 10382  |
| mujer  | COVID-19             | PRIMARIA COMPLETA                           | 7852   |
| hombre | COVID-19             | LICENCIATURA O PROFESIONAL COMPLETO         | 7554   |
| hombre | COVID-19             | BACHILLERATO O PREPARATORIA COMPLETA        | 7520   |
| hombre | DIABETES             | PRIMARIA COMPLETA                           | 5444   |
| mujer  | DIABETES             | PRIMARIA COMPLETA                           | 5250   |
| hombre | INFARTO              | PRIMARIA COMPLETA                           | 4890   |
| mujer  | INFARTO              | PRIMARIA COMPLETA                           | 4720   |
| hombre | COVID-19             | PRIMARIA INCOMPLETA                         | 4640   |
| mujer  | COVID-19             | SECUNDARIA COMPLETA                         | 4388   |
| mujer  | COVID-19             | PRIMARIA INCOMPLETA                         | 3602   |
| mujer  | COVID-19             | BACHILLERATO O PREPARATORIA COMPLETA        | 3494   |
| hombre | DIABETES             | SECUNDARIA COMPLETA                         | 3430   |
| mujer  | DIABETES             | PRIMARIA INCOMPLETA                         | 3014   |
| hombre | ENFERMEDAD PULMONAR  | PRIMARIA COMPLETA                           | 2858   |
| mujer  | INFARTO              | PRIMARIA INCOMPLETA                         | 2844   |
| mujer  | CANCER               | PRIMARIA COMPLETA                           | 2816   |
| mujer  | ENFERMEDAD PULMONAR  | PRIMARIA COMPLETA                           | 2578   |
| hombre | INFARTO              | PRIMARIA INCOMPLETA                         | 256    |
      
