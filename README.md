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
		id BIGSERIAL PRIMARY KEY,
		-- Este atributo nos servira para pasar los datos 		posteriormente
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
|NO ESTUVO EMBARAZADA EN LOS ÚLTIMOS 11 MESES PREVIOS A LA MUERTE|	6381|
|EL PUERPERIO|	44|
|43 DÍAS A 11 MESES DESPUÉS DEL PARTO O ABORTO	|24|
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
|CALLE O CARRETERA (VÍA PÚBLICA)	|1393|
|SE IGNORA	|739|
|VIVIENDA PARTICULAR	|725|
|OTRO	|157|
|ÁREA COMERCIAL O DE SERVICIOS	|156|
|NO ESPECIFICADO	|81|
|VIVIENDA COLECTIVA (ASILO, ORFANATO, ETC)	|78|
|ÁREA INDUSTRIAL (TALLER, FABRICA U OBRA)	|38|
|ESCUELA U OFICINA PUBLICA	|14|
|ÁREA DEPORTIVA	|12|
|GRANJA (RANCHO O PARCELA)	|9|

### 6. **Conteo de valores nulos**
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

### 7. **Inconsistencias en las fechas**
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


### 8. **Inconsistencias en la hora de defunción**
Para checar si hay alguna hora que este fuera de los rangos de un día, ejecutamos:
```sql
SELECT hora_defuncion
FROM staging
WHERE hora_defuncion<'00:00:00' OR hora_defuncion>'23:59:59';
```

📌 **Resultados:**  
No obtuvimos ningun caso que estuviera fuera de los rangos de un día de 24 horas.


### 9. **Inconsistencias en el sexo**
Para checar si hay alguna incosistencia en el sexo, checamos si algun hombre esta embarazado:
```sql
SELECT sexo, durante_embarazo
FROM staging
WHERE sexo ILIKE 'hombre' AND (durante_embarazo NOT ILIKE 'NO APLICA' AND durante_embarazo NOT ILIKE 'NO ESPECIFICADO');
```

📌 **Resultados:**  
No obtuvimos ninguna inconsistencia.

### 10. **Inconsistencias en las dos columnas de fecha de defunción**
Para checar si la fecha de defunción coincide en ambas columnas, ejectuamos:
```sql
SELECT fecha_defuncion1, fecha_defuncion, fecha_defuncion1=fecha_defuncion AS coincide
FROM staging
WHERE fecha_defuncion1!=fecha_defuncion;
```

📌 **Resultados:**  
No obtuvimos ninguna inconsistencia, todas las fechas son iguales en ambas columnas.

### 11. **Inconsistencias entre los municipios residenciales y las entidades residenciales**
Para checar si hay algun municipio que tenga varias entidades residenciales, ejecutamos:
```sql
SELECT municipio_residencia, COUNT(DISTINCT entidad_residencia) AS entidades_distintas
FROM staging
GROUP BY municipio_residencia
HAVING COUNT(DISTINCT entidad_residencia) > 1
ORDER BY municipio_residencia;
```

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
|LA PAZ	|2|
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

En México, es común que distintos estados tengan municipios con nombres homónimos, como "Benito Juárez", "Álvaro Obregón" o "San Miguel", por lo que es perfectamente posible que un mismo nombre de municipio aparezca con distintas entidades en el conjunto de datos. Esta situación no indica una contradicción, sino una limitación del uso de nombres sin claves geográficas únicas, como los códigos del INEGI. Por otro lado, el valor NULL en la columna municipio_residencia no representa una inconsistencia con entidad_residencia, sino un dato faltante que debe tratarse como tal. Por lo tanto, no se eliminarán estos registros por considerarse inconsistentes, pero se recomienda revisar y, de ser posible, normalizar la información utilizando catálogos oficiales para mayor precisión en el análisis.

### 12. **Inconsistencias entre entidad de defuncion y alcaldia**
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

### 13. Inconsistencias en las causas de muerte 

Aunque ciertos registros no están etiquetados explícitamente como "muerte_accidental_violenta" en la columna correspondiente, al revisar la columna "causa_defuncion", se observa que las causas de defunción reportadas corresponden a situaciones que deberían ser clasificadas como muertes accidentales violentas.

**Para Ahogamiento como causa_defuncion :**

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

**Para Autoinfligida como causa_defuncion :**

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
|LESIÌÒN AUTOINFLIGIDA INTENCIONALMENTE POR OTROS MEDIOS ESPECIFICADOS, LUGAR NO ESPECIFICADO	|1|

**Para Asfixia como causa_defuncion :**

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

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%LEUCEMIA%'; 

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%TUMOR%'; 

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%CARCINOMA%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%MELANOMA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%MELANOMA%'; 
 
UPDATE staging
SET causa_defuncion='INFARTO' 
WHERE causa_defuncion ILIKE '%INFARTO%'; 

UPDATE staging
SET causa_defuncion='DIABETES' 
WHERE causa_defuncion ILIKE '%DIABETES%';

UPDATE staging
SET causa_defuncion='SINDROME' 
WHERE causa_defuncion ILIKE '%SINDROME%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%CEREBR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ALZHEIMER%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%DEMENCIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ANEUR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%PARKINSON%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%CARDIACA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%FIBRILACIION Y ALETEO VENTRICULAR%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%INFEC%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%HEPATITIS%';

UPDATE staging
SET causa_defuncion='MALA ALIMENTACIÓN' 
WHERE causa_defuncion ILIKE '%DESNUTRI%';

UPDATE staging
SET causa_defuncion='MALA ALIMENTACIÓN' 
WHERE causa_defuncion ILIKE '%OBESIDAD%';

UPDATE staging
SET causa_defuncion='SEPSIS' 
WHERE causa_defuncion ILIKE '%SEPSIS%';

UPDATE staging
SET causa_defuncion='HIDROPESIA' 
WHERE causa_defuncion ILIKE '%HIDROPESIA%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMORRAGIA%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMATEMESIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL PANCREAS' 
WHERE causa_defuncion ILIKE '%PANCRE%';

UPDATE staging
SET causa_defuncion='APENDICITIS' 
WHERE causa_defuncion ILIKE '%APENDIC%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%GENERALE%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN LA VESICULA BILIAR' 
WHERE causa_defuncion ILIKE '%COLECISTITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN LA VESICULA BILIAR' 
WHERE causa_defuncion ILIKE '%COLANGITIS%';

UPDATE staging
SET causa_defuncion='HERNIA' 
WHERE causa_defuncion ILIKE '%HERNIA%';

UPDATE staging
SET causa_defuncion='ALCOHOLISMO' 
WHERE causa_defuncion ILIKE '%ALCOH%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD HEPATICA'  
WHERE causa_defuncion ILIKE '%HEP%';

UPDATE staging
SET causa_defuncion='ACCIDENTE' 
WHERE causa_defuncion ILIKE '%ACCIDENTE%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RENAL' 
WHERE causa_defuncion ILIKE '%RENAL%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL INTESTINO' 
WHERE causa_defuncion ILIKE '%INTESTINO%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%MUCORMIC%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%TROMBOCITOPENIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL HIGADO' 
WHERE causa_defuncion ILIKE '%HIGADO%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%MENINGITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%EPILEPSIA%';

UPDATE staging
SET causa_defuncion='AGRESION' 
WHERE causa_defuncion ILIKE '%AGRE%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%HIPERPOTASEMIA%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%PERITONITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%HIPERTENSI%';

UPDATE staging
SET causa_defuncion='SIGNOS GENERALES' 
WHERE causa_defuncion ILIKE '%ABDOMEN AGUDO%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%ABORTO%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%EMBARAZO%';

UPDATE staging
SET causa_defuncion='ABSCESO' 
WHERE causa_defuncion ILIKE '%ABSCESO%';

UPDATE staging
SET causa_defuncion='SINDROME' 
WHERE causa_defuncion ILIKE '%ACONDROPLASIA%';

UPDATE staging
SET causa_defuncion='ADHERENCIAS' 
WHERE causa_defuncion ILIKE '%ADHERENCIAS%';

UPDATE staging
SET causa_defuncion='HEMORRAGIA' 
WHERE causa_defuncion ILIKE '%HEMORR%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%AGRANULOCITOSIS%';

UPDATE staging
SET causa_defuncion='SUSTANCIAS' 
WHERE causa_defuncion ILIKE '%SUSTANCIAS%';

UPDATE staging
SET causa_defuncion='COMPLICACIONES EN EL EMBARAZO' 
WHERE causa_defuncion ILIKE '%PERINATAL%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DERMATOLÓGICA' 
WHERE causa_defuncion ILIKE '%ERITEMATOSA%';

UPDATE staging
SET causa_defuncion='AHOGAMIENTO' 
WHERE causa_defuncion ILIKE '%AHOGAMIENTO%';

UPDATE staging
SET causa_defuncion='SUICIDIO' 
WHERE causa_defuncion ILIKE '%AUTOINFLIGIDA%';

UPDATE staging
SET causa_defuncion='AHORCAMIENTO' 
WHERE causa_defuncion ILIKE '%AHORCAMIENTO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%ALETEO AURICULAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%CARDIA%';

UPDATE staging
SET causa_defuncion='INFECCION' 
WHERE causa_defuncion ILIKE '%AMEBIASIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DEGENERATIVA' 
WHERE causa_defuncion ILIKE '%AMILOIDOSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ANEMIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CEREBRAL' 
WHERE causa_defuncion ILIKE '%ANENCEFALIA%';

UPDATE staging
SET causa_defuncion='TRASTORNOS DEL EQUILIBRIO ÁCIDO-BASE' 
WHERE causa_defuncion ILIKE '%ALCALOSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ANGII%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD CARDIACA' 
WHERE causa_defuncion ILIKE '%ANGINA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%HEMANGIOMA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%MICROANGIOPATIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RENAL' 
WHERE causa_defuncion ILIKE '%NEFROPA%';

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%LINFANGIOMA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD EN EL COLON' 
WHERE causa_defuncion ILIKE '%COLON%';

UPDATE staging
SET causa_defuncion='ANOMALIA' 
WHERE causa_defuncion ILIKE '%ANOMALI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD AUDITIVA' 
WHERE causa_defuncion ILIKE '%ANQUILOSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD HEMATOLOGICA' 
WHERE causa_defuncion ILIKE '%APLASIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD AUDITIVA' 
WHERE causa_defuncion ILIKE '%ARTR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%ARTERITI%';

UPDATE staging
SET causa_defuncion='ASFIXIA' 
WHERE causa_defuncion ILIKE '%ASFIXIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%ASMA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%APNEA DEL SUEIOO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%APNEA PRIMARIA DEL SUEIOO DEL RECIIaN NACIDO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD NEUROLOGICA' 
WHERE causa_defuncion ILIKE '%ATROFIA%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PSIQUIATRICA' 
WHERE causa_defuncion ILIKE '%BIPOLAR%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DE LA SANGRE' 
WHERE causa_defuncion ILIKE '%CARDIO%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD DIGESTIVA' 
WHERE causa_defuncion ILIKE '%CIRROSIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD NEUROLOGICA' 
WHERE causa_defuncion ILIKE '%CONVULSIONES%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD PSIQUIATRICA' 
WHERE causa_defuncion ILIKE '%DEPRESI%';

UPDATE staging
SET causa_defuncion='CAIDA' 
WHERE causa_defuncion ILIKE '%CAIDA%';

UPDATE staging
SET causa_defuncion='COMA' 
WHERE causa_defuncion ILIKE '%COMA %';

UPDATE staging
SET causa_defuncion='CELULITIS' 
WHERE causa_defuncion ILIKE '%CELULITIS%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%RESPI%';
```

### • Revisar ubicación residencial (municipio residencia y entidad residencia)

Para verificar si había inconsistencias, se decidió comprobar si cada municipio de residencia correspondía con una única entidad de residencia, ya que así debería ser. Detectamos que había muchas inconsistencias, las cuales fuimos corrigiendo una por una, identificando a qué entidad pertenecía cada municipio con error.

```sql
--Código para detectar las inconsistencias
--10 de ABRIL:
UPDATE staging
SET entidad_residencia='QUERETARO'
WHERE municipio_residencia ILIKE '10 DE ABRIL' AND entidad_residencia NOT LIKE 'QUERETARO';

--Acajete:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'ACAJETE' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Acayucan:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'ACAYUCAN' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Acolman...:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ACOLMAN DE NEZA%' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--ACOSTA MAZA:
UPDATE staging
SET municipio_residencia='TIERRA BLANCA'
WHERE municipio_residencia ILIKE 'ACOSTA MAZA';

--Actopan V:
UPDATE staging
SET municipio_residencia='ACTOPAN V'
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia LIKE 'VERACRUZ%';

--Actopan H:
UPDATE staging
SET municipio_residencia='ACTOPAN H'
WHERE municipio_residencia ILIKE 'ACTOPAN' AND entidad_residencia LIKE 'HIDALGO';

--Agua bendita:
UPDATE staging
SET municipio_residencia=NULL
WHERE municipio_residencia ILIKE 'AGUA BENDITA';

--Agua dulce:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'AGUA DULCE' AND entidad_residencia NOT LIKE 'VERACRUZ%';

--CAMBIAR TODOS LOS VERACRUZ IGUALES
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE entidad_residencia ILIKE 'VERACRUZ%';

--Agua zarca:
UPDATE staging
SET entidad_residencia='QUERETARO'
WHERE municipio_residencia ILIKE 'AGUA ZARCA' AND entidad_residencia NOT LIKE 'QUERETARO';

--Alvaro Obregon:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'ALVARO OBREGON' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Amatepec:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'AMATEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Azcapotzalco:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'AZCAPOTZALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Barrio de Guadalupe:
UPDATE staging
SET entidad_residencia='NUEVO LEON'
WHERE municipio_residencia ILIKE 'BARRIO DE GUADALUPE' AND entidad_residencia NOT LIKE 'NUEVO LEON';
  
--Benito Juarez:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'BENITO JUAREZ' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Buenavista:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'BUENAVISTA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Coyoacan:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'COYOACAN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Cruz Blanca:
UPDATE staging
SET municipio_residencia='Zacualpan'
WHERE municipio_residencia ILIKE 'CRUZ BLANCA';

UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ZACUALPAN' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Cuauhtemoc CDMX:
UPDATE staging
SET municipio_residencia='CUAUHTEMOC CDMX'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND (entidad_residencia LIKE 'CIUDAD DE MEXICO' OR entidad_residencia LIKE 'MEXICO');

UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC CDMX' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Cuauhtemoc:
UPDATE staging
SET entidad_residencia='CHIHUAHUA'
WHERE municipio_residencia ILIKE 'CUAUHTEMOC' AND entidad_residencia NOT LIKE 'CHIHUAHUA';

--Cuautepec:
UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'CUAUTEPEC' AND entidad_residencia NOT LIKE 'HIDALGO';

--Dos rios:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'DOS RIOS' AND entidad_residencia NOT LIKE 'VERACRUZ';

--El arenal:
UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'EL ARENAL' AND entidad_residencia NOT LIKE 'HIDALGO';

--El carmen:
UPDATE staging
SET entidad_residencia='CAMPECHE'
WHERE municipio_residencia ILIKE 'EL CARMEN' AND entidad_residencia NOT LIKE 'CAMPECHE';

--Emiliano zapata:
UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'EMILIANO ZAPATA' AND entidad_residencia NOT LIKE 'HIDALGO';

--Guadalupe Victoria:
UPDATE staging
SET municipio_residencia='GUADALUPE VICTORIA PUEBLA'
WHERE municipio_residencia ILIKE 'GUADALUPE VICTORIA' AND entidad_residencia LIKE 'PUEBLA';

--Gustavo A. Madero:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'GUSTAVO A. MADERO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Iztacalco:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'IZTACALCO' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--La loma:
UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'LA LOMA' AND entidad_residencia NOT LIKE 'PUEBLA';

--La nopalera:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'LA NOPALERA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--La paz:
UPDATE staging
SET entidad_residencia='BAJA CALIFORNIA SUR'
WHERE municipio_residencia ILIKE 'LA PAZ' AND entidad_residencia NOT LIKE 'BAJA CALIFORNIA SUR';

--Metepec:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'METEPEC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Ojo de Agua:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'OJO DE AGUA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Papalotla:
UPDATE staging
SET entidad_residencia='TLAXCALA'
WHERE municipio_residencia ILIKE 'PAPALOTLA' AND entidad_residencia NOT LIKE 'TLAXCALA';

--Paracuaro:
UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'PARACUARO' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--Piedras negras:
UPDATE staging
SET entidad_residencia='COAHUILA'
WHERE municipio_residencia ILIKE 'PIEDRAS NEGRAS' AND entidad_residencia NOT LIKE 'COAHUILA';

--San Agustin:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'SAN AGUSTIN' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--San Felipe:
UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'SAN FELIPE' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--San Fernando:
UPDATE staging
SET entidad_residencia='CHIAPAS'
WHERE municipio_residencia ILIKE 'SAN FERNANDO' AND entidad_residencia NOT LIKE 'CHIAPAS';

--San Isidro:
UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'SAN ISIDRO' AND entidad_residencia NOT LIKE 'PUEBLA';

--San Marcos:
UPDATE staging
SET entidad_residencia='GUERRERO'
WHERE municipio_residencia ILIKE 'SAN MARCOS' AND entidad_residencia NOT LIKE 'GUERRERO';

--San Miguel:
UPDATE staging
SET entidad_residencia='GUANAJUATO'
WHERE municipio_residencia ILIKE 'SAN MIGUEL' AND entidad_residencia NOT LIKE 'GUANAJUATO';

--Santa clara:
UPDATE staging
SET entidad_residencia='DURANGO'
WHERE municipio_residencia ILIKE 'SANTA CLARA' AND entidad_residencia NOT LIKE 'DURANGO';

--Tecamachalco:
UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'TECAMACHALCO' AND entidad_residencia NOT LIKE 'PUEBLA';

--Tenango:
UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'TENANGO' AND entidad_residencia NOT LIKE 'HIDALGO';

--Tepetitlan:
UPDATE staging
SET entidad_residencia='HIDALGO'
WHERE municipio_residencia ILIKE 'TEPETITLAN' AND entidad_residencia NOT LIKE 'HIDALGO';

--Tepetzintla:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'TEPETZINTLA' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Tlalnepantla:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'TLALNEPANTLA' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Tlaxco:
UPDATE staging
SET entidad_residencia='TLAXCALA'
WHERE municipio_residencia ILIKE 'TLAXCO' AND entidad_residencia NOT LIKE 'TLAXCALA';

--Tonala:
UPDATE staging
SET municipio_residencia='TONALA CHIAPAS'
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'CHIAPAS';

UPDATE staging
SET municipio_residencia='TONALA JALISCO'
WHERE municipio_residencia ILIKE 'TONALA' AND entidad_residencia LIKE 'JALISCO';

--Tuxpan:
UPDATE staging
SET entidad_residencia='MICHOACAN DE OCAMPO'
WHERE municipio_residencia ILIKE 'TUXPAN' AND entidad_residencia NOT LIKE 'MICHOACAN%';

--Venustiano Carranza:
UPDATE staging
SET entidad_residencia='CIUDAD DE MEXICO'
WHERE municipio_residencia ILIKE 'VENUSTIANO CARRANZA' AND entidad_residencia NOT LIKE 'CIUDAD DE MEXICO';

--Villa Cuauhtemoc:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'VILLA CUAUHTEMOC' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Xico:
UPDATE staging
SET entidad_residencia='VERACRUZ'
WHERE municipio_residencia ILIKE 'XICO' AND entidad_residencia NOT LIKE 'VERACRUZ';

--Zacualpan
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ZACUALPAN' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Zaragoza:
UPDATE staging
SET entidad_residencia='PUEBLA'
WHERE municipio_residencia ILIKE 'ZARAGOZA' AND entidad_residencia NOT LIKE 'PUEBLA';

--Ecatepec de Morelos:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ECATEPEC DE MORELOS' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';

--Ecatzingo de hidalgo:
UPDATE staging
SET entidad_residencia='ESTADO DE MEXICO'
WHERE municipio_residencia ILIKE 'ECATZINGO DE HIDALGO' AND entidad_residencia NOT LIKE 'ESTADO DE MEXICO';
```

### • Arreglar las inconsistencias en las complicaciones en el embarazo (complicacion embarazo)

Para corregir las inconsistencias en las complicaciones durante el embarazo, se verificó que hubiera coincidencia entre la causa de defunción y la complicación en el embarazo. Cuando se detectaron discrepancias entre estos campos, se actualizó el valor de la complicación en el embarazo para que coincidiera con la causa de defunción correspondiente.

```sql
UPDATE staging
SET complicacion_embarazo='SI'
WHERE causa_defuncion ILIKE '%EMBARAZO%';
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
| residencia_id      (fk) |
| escolaridad             |
| ocupación               |
| afiliación_medica       |
| defuncion_id       (fk) |

#### Entidad: municipio
| municipio         |
--------------------|
| id                |
| entidad_id   (fk) |
| nombre            |

#### Entidad: entidad
| entidad           |
|-------------------|
| id                |
| nombre            |

#### Entidad: Defunción
| defuncion                   |
|-----------------------------|
| id                          |
| fecha_defuncion             |
| hora_defuncion              |
| lugar_defuncion             |
| causa_defuncion             |
| alcaldia_defuncion_id  (fk) |
| atencion_medica             |
| necropsia                   |


#### Entidad: Embarazo
| embarazo                  |
|---------------------------|
| id                        |
| persona_id           (fk) |
| durante_embarazo          |
| causa_embarazo            |
| complicacion_embarazo     |

### • Dependencias funcionales y multivaluadas
Después de analizar los datos se encontraron las siguientes dependencias:
#### Dependencias Funcionales no triviales:

Como nuestras tablas estan normalizadas correctamente y en FNBC, no hay dependencias multivaluadas, y las unicas dependencias funcionales nacen de la superclave de cada tabla; el ID.

**-DF1: {persona.id} → {sexo, fecha_nacimiento, lengua_indigena, estado_civil, residencia_id, escolaridad, ocupacion, afiliacion_medica, defuncion_id}**
**-DF2: {defuncion.id} → {fecha_defuncion, hora_defuncion, lugar_defuncion, causa_defuncion, alcaldia_defuncion_id, atencion_medica, necropsia}**

Inicialmente se consideró que defuncion_id formaba parte de la dependencia funcional de la tabla persona, bajo la idea de que cada persona tiene asociada una defunción. Sin embargo, esto es incorrecto desde el punto de vista de la normalización, ya que una persona no determina su defunción. En realidad, es la defunción la que hace referencia a una persona mediante el atributo persona_id.

Esto implica que la relación es:
defuncion.persona_id → defuncion.id,
y no al revés. Por tanto, incluir defuncion_id como dependiente de persona.id viola la Tercera Forma Normal (3FN), ya que introduce una dependencia transitiva: persona.id → defuncion_id → otros atributos, lo cual no es aceptable.

Como resultado, se elimina defuncion_id de la dependencia funcional de la tabla persona, y se incorpora el atributo persona_id directamente en la tabla defuncion:
**-DF1 (nueva): {persona.id} → {sexo, fecha_nacimiento, lengua_indigena, estado_civil, residencia_id, escolaridad, ocupacion, afiliacion_medica}**
**-DF2 (nueva): {defuncion.id} → {fecha_defuncion, hora_defuncion, lugar_defuncion, causa_defuncion, alcaldia_defuncion_id, atencion_medica, necropsia, persona_id}**

**-DF3: {municipio.id} → {entidad_id, nombre}**  
**-DF4: {entidad.id} → {nombre}**  

Aunque las dependencias funcionales originales ({municipio.id} → {entidad_id, nombre} y {entidad.id} → {nombre}) cumplen con la Tercera Forma Normal, es válido fusionar ambas tablas en una sola llamada entidad_municipio, con la dependencia {entidad_municipio.id} → {entidad, municipio}, siempre que la combinación de entidad y municipio sea única. Esta fusión simplifica el modelo y reduce la necesidad de realizar joins, lo cual es útil si no se requiere trabajar con entidades o municipios de forma independiente. La denormalización es aceptable mientras no se introduzcan redundancias ni se violen las dependencias funcionales directas.

**-DF3 (nueva): {entidad_municipio.id} → {entidad, municipio}**

**-DF4: {embarazo.id} → {persona_id, durante_embarazo, causa_embarazo, complicacion_embarazo}**  
Esta dependencia funcional se justifica en el hecho de que cada atributo presente en la tabla embarazo está relacionado únicamente con el identificador (id) de la misma. Por lo tanto, al conocer el valor del identificador, es posible determinar de manera unívoca todos los demás atributos de la tabla.

#### Dependencias Multivaluadas no triviales:
No hay dependencias multivaluadas porque:
- Cada atributo de cada entidad depende únicamente de su clave primaria.
- No hay atributos multivalorados o con combinaciones múltiples independientes.
- Las relaciones están en FNBC, lo que garantiza la eliminación de este tipo de redundancia.

# Análisis de Normalización de Tablas

## **1. Tabla: `Persona`**

| **Pregunta** | **Respuesta** |
| --- | --- |
| **¿Está en 1FN?** (¿La tabla tiene solo valores atómicos?) | Sí, todos los atributos de la tabla `persona` son atómicos (no hay listas o conjuntos de valores). |
| **¿Está en 2FN?** (¿Está en 1FN y no hay dependencias parciales?) | Sí, todos los atributos dependen completamente de la clave primaria `id`. No hay dependencias parciales. |
| **¿Está en 3FN?** (¿Está en 2FN y no hay dependencias transitivas?) | Sí, todos los atributos dependen directamente de `id`, sin depender de otros atributos. |
| **¿Está en FNBC?** (¿Cada dependencia funcional tiene como determinante una superclave?) | Sí, todos los atributos dependen exclusivamente de la clave primaria `id`, que es una superclave. No hay dependencias funcionales donde el determinante no sea una superclave. |
| **¿Está en 4FN?** (¿Está en 3FN y no hay dependencias multivaluadas?) | Sí, no hay dependencias multivaluadas. Cada atributo depende exclusivamente de `id`. |

---

## **2. Tabla: `Municipio`**

| **Pregunta** | **Respuesta** |
| --- | --- |
| **¿Está en 1FN?** (¿La tabla tiene solo valores atómicos?) | Sí, todos los atributos en la tabla `municipio` son atómicos. |
| **¿Está en 2FN?** (¿Está en 1FN y no hay dependencias parciales?) | Sí, todos los atributos dependen completamente de la clave primaria `id` de municipio. No hay dependencias parciales. |
| **¿Está en 3FN?** (¿Está en 2FN y no hay dependencias transitivas?) | Sí, todos los atributos dependen directamente de `id`, sin depender de otros atributos. |
| **¿Está en FNBC?** (¿Cada dependencia funcional tiene como determinante una superclave?) | Sí, en la tabla `municipio` todos los atributos dependen únicamente de `id`, que es una superclave. No existen dependencias funcionales que violen esta condición. |
| **¿Está en 4FN?** (¿Está en 3FN y no hay dependencias multivaluadas?) | Sí, no hay dependencias multivaluadas. Cada atributo depende exclusivamente de `id`. |

---

## **3. Tabla: `Entidad`**

| **Pregunta** | **Respuesta** |
| --- | --- |
| **¿Está en 1FN?** (¿La tabla tiene solo valores atómicos?) | Sí, los atributos `id` y `nombre` son atómicos. |
| **¿Está en 2FN?** (¿Está en 1FN y no hay dependencias parciales?) | Sí, todos los atributos dependen completamente de la clave primaria `id`. No hay dependencias parciales. |
| **¿Está en 3FN?** (¿Está en 2FN y no hay dependencias transitivas?) | Sí, no hay dependencias transitivas, ya que `nombre` depende exclusivamente de `id`. |
| **¿Está en FNBC?** (¿Cada dependencia funcional tiene como determinante una superclave?) | Sí, la única dependencia funcional es `id` → `nombre`, donde `id` es clave primaria. Esto cumple con la definición de la FNBC. |
| **¿Está en 4FN?** (¿Está en 3FN y no hay dependencias multivaluadas?) | Sí, no hay dependencias multivaluadas, ya que no hay atributos que dependan de otros atributos en forma multivaluada. |

---
## **4. Tabla: `Defuncion`**

| **Pregunta** | **Respuesta** |
| --- | --- |
| **¿Está en 1FN?** (¿La tabla tiene solo valores atómicos?) | Sí, todos los atributos de la tabla `defuncion` son atómicos. |
| **¿Está en 2FN?** (¿Está en 1FN y no hay dependencias parciales?) | Sí, todos los atributos dependen completamente de la clave primaria `id` de `defuncion`. No hay dependencias parciales. |
| **¿Está en 3FN?** (¿Está en 2FN y no hay dependencias transitivas?) | Sí, no hay dependencias transitivas en la tabla `defuncion`. |
| **¿Está en FNBC?** (¿Cada dependencia funcional tiene como determinante una superclave?) | Sí, todas las dependencias funcionales tienen como determinante la clave primaria `id`. No hay violaciones a FNBC. |
| **¿Está en 4FN?** (¿Está en 3FN y no hay dependencias multivaluadas?) | Sí, no hay dependencias multivaluadas en la tabla `defuncion`. |

---

## **5. Tabla: `Embarazo`**

| **Pregunta** | **Respuesta** |
| --- | --- |
| **¿Está en 1FN?** (¿La tabla tiene solo valores atómicos?) | Sí, todos los atributos de la tabla `embarazo` son atómicos. |
| **¿Está en 2FN?** (¿Está en 1FN y no hay dependencias parciales?) | Sí, todos los atributos dependen completamente de la clave primaria `id` de `embarazo`. No hay dependencias parciales. |
| **¿Está en 3FN?** (¿Está en 2FN y no hay dependencias transitivas?) | Sí, todos los atributos dependen directamente de `id`, sin depender de otros atributos. |
| **¿Está en FNBC?** (¿Cada dependencia funcional tiene como determinante una superclave?) | Sí, la clave primaria `id` determina todos los atributos y no hay otras dependencias funcionales. La tabla cumple con la FNBC. |
| **¿Está en 4FN?** (¿Está en 3FN y no hay dependencias multivaluadas?) | Sí, no hay dependencias multivaluadas en la tabla `embarazo`. |

No modificamos nada de las tablas que propusimos originalmente, pues ya estaban en Cuarta Forma Normal desde el principio. Las tablas no presentaban dependencias multivaluadas no triviales, lo cual es el criterio principal para cumplir con 4FN. Cada atributo de las tablas depende exclusivamente de la clave primaria, y no existían atributos que dependieran de otros de manera multivaluada, lo que podría generar redundancias o problemas de integridad de datos. Además, no había necesidad de dividir las tablas ni eliminar dependencias, ya que todas las dependencias funcionales eran triviales y las relaciones entre los datos estaban bien definidas sin violar las reglas de normalización. Por lo tanto, las tablas ya cumplían con las condiciones necesarias para estar en 4FN.

Estas tablas fueron diseñadas teniendo en cuenta la **naturaleza de los datos** que representan, lo que garantizó que se cumplieran las reglas de normalización y se mantuviera la integridad de los mismos. Cada tabla refleja una entidad específica del dominio, como `Persona`, `Municipio`, `Entidad`, `Defuncion`, y `Embarazo`, las cuales están estructuradas de forma que reflejan la relación única y directa entre los atributos de cada entidad. Por ejemplo, la tabla `Persona` contiene atributos como `sexo`, `fecha_nacimiento`, `estado_civil`, etc., que dependen exclusivamente del identificador único de la persona, lo cual refleja su naturaleza única y no repetitiva. Asimismo, las relaciones entre las tablas están definidas de manera que se eviten redundancias y se optimice el acceso y la manipulación de los datos, lo que hace que el modelo sea eficiente y adecuado para representar la realidad del dominio de forma clara y coherente. Las dependencias funcionales fueron cuidadosamente consideradas para asegurar que las tablas se mantuvieran en 4FN, evitando dependencias multivaluadas y asegurando que cada conjunto de atributos dependiera únicamente de la clave primaria. Así, el diseño de las tablas no solo sigue las reglas de normalización, sino que también refleja la estructura y la lógica inherente a los datos que se almacenan.

### • Entidades Finales

#### Entidad: Persona
| persona                 |
|-------------------------|
| id                      |
| sexo                    |
| fecha_nacimiento        |
| lengua_indígena         | 
| estado_civil            |
| residencia_id      (fk) |
| escolaridad             |
| ocupación               |
| afiliación_medica       |

#### Entidad: entidad_municipio
| municipio         |
--------------------|
| id                |
| entidad           |
| municipio         |


#### Entidad: Defunción
| defuncion                   |
|-----------------------------|
| id                          |
| persona_id             (fk) |
| fecha_defuncion             |
| hora_defuncion              |
| lugar_defuncion             |
| causa_defuncion             |
| alcaldia_defuncion_id  (fk) |
| atencion_medica             |
| necropsia                   |


#### Entidad: Embarazo
| embarazo                  |
|---------------------------|
| id                        |
| persona_id           (fk) |
| durante_embarazo          |
| causa_embarazo            |
| complicacion_embarazo     |

### • Creación de tablas en SQL

```sql
-- Entidad: entidad_municipio
CREATE TABLE entidad_municipio (
	id BIGSERIAL PRIMARY KEY,
	entidad VARCHAR(200),
	municipio VARCHAR(100),
	
	CONSTRAINT pares_unicos UNIQUE(entidad,municipio)
);

INSERT INTO entidad_municipio(id,municipio,entidad) VALUES
(0, 'NO ESPECIFICADO', 'NO ESPECIFICADO');

INSERT INTO entidad_municipio(municipio, entidad)
SELECT DISTINCT municipio_residencia, entidad_residencia
FROM staging
WHERE NOT EXISTS (
    SELECT 1
    FROM entidad_municipio 
    WHERE municipio = municipio_residencia
      AND entidad = entidad_residencia
);

INSERT INTO entidad_municipio(municipio,entidad)
SELECT DISTINCT alcaldia, 'CIUDAD DE MEXICO'
FROM staging
WHERE NOT EXISTS (
    SELECT 1
    FROM entidad_municipio 
    WHERE municipio = staging.alcaldia
      AND entidad = 'CIUDAD DE MEXICO'
);

-- Entidad: Persona
CREATE TABLE persona (
	id BIGSERIAL PRIMARY KEY,
	sexo VARCHAR(20),
	fecha_nacimiento DATE,
	lengua_indigena BOOLEAN,
	estado_civil VARCHAR(50),
	entidad_residencia VARCHAR(100),
	municipio_residencia VARCHAR(100),
	--Estos atributos residencia son temporales en lo que se ingresan los nuevos ids
	residencia_id BIGINT,
	escolaridad VARCHAR(200),
	ocupacion VARCHAR(200),
	afiliacion_medica VARCHAR(200)
);

INSERT INTO persona (id,sexo, fecha_nacimiento, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica)
SELECT id,sexo, fecha_nacimiento,lengua_indigena,estado_civil,entidad_residencia,municipio_residencia,escolaridad,ocupacion,afiliacion_medica
FROM staging;

SELECT setval('public.persona_id_seq', (SELECT MAX(id) FROM persona));

UPDATE persona
SET residencia_id = (
    SELECT em.id
    FROM entidad_municipio em
    JOIN staging s ON s.entidad_residencia = em.entidad
    AND s.municipio_residencia = em.municipio
    WHERE s.id = persona.id
);

ALTER TABLE persona DROP COLUMN entidad_residencia;
ALTER TABLE persona DROP COLUMN municipio_residencia;

ALTER TABLE persona
ALTER COLUMN residencia_id SET DEFAULT 0;--> Tupla donde la entidad y el municipio no estan especificados

ALTER TABLE persona
ADD CONSTRAINT fk_entidad_municipio
FOREIGN KEY (residencia_id) REFERENCES entidad_municipio(id) ON DELETE SET DEFAULT;

-- Entidad: Defuncion
CREATE TABLE defuncion (
	id BIGSERIAL PRIMARY KEY,
	persona_id BIGINT UNIQUE NOT NULL CONSTRAINT fk_persona REFERENCES persona(id) ON DELETE CASCADE,
	fecha_defuncion DATE NOT NULL,
	hora_defuncion TIME,
	lugar_defuncion VARCHAR(500),
	causa_defuncion VARCHAR(500),
	alcaldia_defuncion_id VARCHAR (500), --valor provisional en lo que transferimos los datos
	atencion_medica BOOLEAN,
	necropsia BOOLEAN
);

INSERT INTO defuncion (persona_id,fecha_defuncion, hora_defuncion, lugar_defuncion, causa_defuncion, alcaldia_defuncion_id, atencion_medica, necropsia)
SELECT id, fecha_defuncion, hora_defuncion, lugar_defuncion, causa_defuncion, alcaldia, atencion_medica, necropsia
FROM staging;

UPDATE defuncion
SET alcaldia_defuncion_id = (
	SELECT id 
	FROM entidad_municipio
	WHERE (entidad_municipio.entidad,entidad_municipio.municipio)=('CIUDAD DE MEXICO', alcaldia_defuncion_id)
);


ALTER TABLE defuncion
ALTER COLUMN alcaldia_defuncion_id TYPE BIGINT USING alcaldia_defuncion_id::bigint,
ALTER COLUMN alcaldia_defuncion_id SET NOT NULL,
ALTER COLUMN alcaldia_defuncion_id SET DEFAULT 0, --> Tupla donde la entidad y el municipio no estan especificados
ADD CONSTRAINT fk_entidad_municipio
FOREIGN KEY (alcaldia_defuncion_id) REFERENCES entidad_municipio(id) ON DELETE SET DEFAULT;

-- Entidad Embarazo

CREATE TABLE embarazo (
	id BIGSERIAL PRIMARY KEY,
	persona_id BIGINT NOT NULL CONSTRAINT fk_persona REFERENCES persona(id) ON DELETE CASCADE,
	durante_embarazo VARCHAR(500),
	causado_embarazo VARCHAR(200),
	complicacion_embarazo VARCHAR(200)
);

INSERT INTO embarazo (persona_id,durante_embarazo, causado_embarazo, complicacion_embarazo)
SELECT id, durante_embarazo, causado_embarazo, complicacion_embarazo
FROM staging
WHERE durante_embarazo NOT ILIKE '%NO APLICA%'
	AND durante_embarazo NOT ILIKE '%NO ESPECIFICADO%'
	AND NOT (
    complicacion_embarazo ILIKE '%NO APLICA%'
    AND causado_embarazo ILIKE '%NO APLICA%'
  );

DROP TABLE IF EXISTS staging;
```
### ERD
El ERD con todas las entidades después de la normalización, es el siguiente:

![erd 001](https://github.com/user-attachments/assets/5d6c7e42-b39d-416d-b556-7228844b5173)

## Análisis de datos a través de consultas SQL

Teniendo en cuenta que el enfoque de nuestro proyecto es analizar las deficiencias de atención medica por municipios y entidades, realizamos las siguientes consultas para obtener una conclusión que responda a nuestro objetivo. 

Algunas de las consultas que hicimos son las siguientes:

### 1. **Análisis de mortalidad y contexto socioeconómico**

Pregunta: ¿Existe una relación entre escolaridad y causa de defunción por sexo? 


Ejecutamos:
```sql
SELECT defuncion.causa_defuncion, escolaridad, COUNT(*) as total
FROM persona
JOIN defuncion ON defuncion.persona_id=persona.id
GROUP BY escolaridad, causa_defuncion
HAVING COUNT(*) > 1000
ORDER BY total DESC;
```
📌 **Resultados:**  

# Análisis de Causa de Defunción por Nivel de Escolaridad

| **Causa de Defunción**            | **Escolaridad**                                | **Total de Muertes** |
|----------------------------------|------------------------------------------------|-----------------------|
| COVID-19                         | PRIMARIA COMPLETA                              | 9379                  |
| COVID-19                         | SECUNDARIA COMPLETA                            | 7362                  |
| COVID-19                         | BACHILLERATO O PREPARATORIA COMPLETA           | 5486                  |
| DIABETES                         | PRIMARIA COMPLETA                              | 5334                  |
| COVID-19                         | LICENCIATURA O PROFESIONAL COMPLETO            | 4810                  |
| INFARTO                          | PRIMARIA COMPLETA                              | 4768                  |
| COVID-19                         | PRIMARIA INCOMPLETA                            | 4105                  |
| DIABETES                         | SECUNDARIA COMPLETA                            | 2741                  |
| INFARTO                          | PRIMARIA INCOMPLETA                            | 2695                  |
| DIABETES                         | PRIMARIA INCOMPLETA                            | 2652                  |
| CÁNCER                           | PRIMARIA COMPLETA                              | 2438                  |
| INFARTO                          | SECUNDARIA COMPLETA                            | 2008                  |
| CÁNCER                           | LICENCIATURA O PROFESIONAL COMPLETO            | 1907                  |
| CÁNCER                           | SECUNDARIA COMPLETA                            | 1811                  |
| CÁNCER                           | BACHILLERATO O PREPARATORIA COMPLETA           | 1724                  |
| NEUMONÍA, NO ESPECIFICADA        | PRIMARIA COMPLETA                              | 1613                  |
| COVID-19                         | NINGUNA                                        | 1610                  |
| DIABETES                         | BACHILLERATO O PREPARATORIA COMPLETA           | 1600                  |
| INFARTO                          | BACHILLERATO O PREPARATORIA COMPLETA           | 1599                  |
| INFARTO                          | NINGUNA                                        | 1593                  |
| INFARTO                          | LICENCIATURA O PROFESIONAL COMPLETO            | 1577                  |
| DIABETES                         | NINGUNA                                        | 1436                  |
| COVID-19                         | BACHILLERATO O PREPARATORIA INCOMPLETA         | 1412                  |
| DIABETES                         | LICENCIATURA O PROFESIONAL COMPLETO            | 1398                  |
| ENFERMEDAD CARDIACA              | PRIMARIA COMPLETA                              | 1265                  |
| CÁNCER                           | PRIMARIA INCOMPLETA                            | 1178                  |
| NEUMONÍA, NO ESPECIFICADA        | SECUNDARIA COMPLETA                            | 1104                  |
| COVID-19                         | SECUNDARIA INCOMPLETA                          | 1084                  |

El nivel de educación influye de manera importante en la salud de las personas. 
Los datos muestran que quienes tienen menor escolaridad son los más afectados por enfermedades graves como COVID-19, diabetes e infartos. Esto puede explicarse porque las personas con menos estudios suelen tener más dificultades para acceder a servicios médicos de calidad, comprender información sobre prevención o mantener hábitos saludables. Además, muchas veces viven en contextos sociales y económicos más desfavorables, lo que también impacta negativamente en su bienestar.
No solo se trata de mejorar el sistema de salud, sino también de reforzar la educación y generar conciencia desde etapas tempranas sobre la importancia del cuidado personal y la prevención. 
Al mismo tiempo, es necesario diseñar políticas públicas que atiendan de manera prioritaria a las poblaciones más vulnerables.
El hecho de que haya más muertes en el grupo con primaria completa que en el de primaria incompleta no significa necesariamente que tengan peor salud, sino que puede deberse a que hay muchas más personas que lograron terminar la primaria, especialmente entre las generaciones mayores, que son también las más vulnerables a enfermedades graves. 
Además, en los registros oficiales, es común que se anote el último nivel de estudios completado, lo que agrupa a más personas bajo "primaria completa", aunque hayan tenido estudios posteriores incompletos.

### 2. **Análisis de enfermedades por alcaldías**

Pregunta: ¿Qué alcaldías concentran más muertes por enfermedades respiratorias)?

Ejecutamos:
```sql
SELECT entidad_municipio.municipio as alcaldia,causa_defuncion, COUNT(*) as total
FROM defuncion
JOIN entidad_municipio ON entidad_municipio.id=alcaldia_defuncion_id
WHERE causa_defuncion ILIKE '%RESP%' OR causa_defuncion ILIKE '%COVID%'
GROUP BY entidad_municipio.municipio, causa_defuncion
ORDER BY total DESC;
```
📌 **Resultados:**  

| Alcaldía                         | Causa de defunción         | Total |
|----------------------------------|-----------------------------|-------|
| IZTAPALAPA                       | COVID-19                    | 4797  |
| GUSTAVO A. MADERO               | COVID-19                    | 4687  |
| BENITO JUAREZ                   | COVID-19                    | 4246  |
| AZCAPOTZALCO                    | COVID-19                    | 4114  |
| MIGUEL HIDALGO                  | COVID-19                    | 3520  |
| CUAUHTEMOC                      | COVID-19                    | 3384  |
| ALVARO OBREGON                  | COVID-19                    | 2889  |
| IZTACALCO                       | COVID-19                    | 2809  |
| COYOACAN                        | COVID-19                    | 2752  |
| TLALPAN                         | COVID-19                    | 2593  |
| TLAHUAC                         | COVID-19                    | 633   |
| VENUSTIANO CARRANZA             | COVID-19                    | 410   |
| XOCHIMILCO                      | COVID-19                    | 228   |
| NO ESPECIFICADO                 | COVID-19                    | 212   |
| VILLA MILPA ALTA                | COVID-19                    | 174   |
| LA MAGDALENA CONTRERAS          | COVID-19                    | 104   |
| CUAJIMALPA DE MORELOS           | COVID-19                    | 81    |
| GUSTAVO A. MADERO               | ENFERMEDAD RESPIRATORIA     | 73    |
| IZTAPALAPA                      | ENFERMEDAD RESPIRATORIA     | 37    |
| AA MILPA ALTA                   | COVID-19                    | 34    |
| ALVARO OBREGON                  | ENFERMEDAD RESPIRATORIA     | 28    |
| AZCAPOTZALCO                    | ENFERMEDAD RESPIRATORIA     | 27    |
| BENITO JUAREZ                   | ENFERMEDAD RESPIRATORIA     | 24    |
| IZTACALCO                       | ENFERMEDAD RESPIRATORIA     | 22    |
| CUAUHTEMOC                      | ENFERMEDAD RESPIRATORIA     | 20    |
| TLALPAN                         | ENFERMEDAD RESPIRATORIA     | 13    |
| NO ESPECIFICADO                 | ENFERMEDAD RESPIRATORIA     | 13    |
| VENUSTIANO CARRANZA             | ENFERMEDAD RESPIRATORIA     | 12    |
| COYOACAN                        | ENFERMEDAD RESPIRATORIA     | 12    |
| MIGUEL HIDALGO                  | ENFERMEDAD RESPIRATORIA     | 10    |
| XOCHIMILCO                      | ENFERMEDAD RESPIRATORIA     | 6     |
| ALBERGUE ALPINO AJUSCO         | COVID-19                    | 3     |
| TLAHUAC                         | ENFERMEDAD RESPIRATORIA     | 2     |
| ACALIPA                         | COVID-19                    | 2     |
| OJO DE AGUA                     | COVID-19                    | 2     |
| SAN PEDRO ATOCPAN               | COVID-19                    | 2     |
| SAN MIGUEL                      | COVID-19                    | 1     |
| SANTA ANA TLACOTENCO            | COVID-19                    | 1     |
| LA MAGDALENA CONTRERAS          | ENFERMEDAD RESPIRATORIA     | 1     |
| SAN ANDRES MIXQUIC              | COVID-19                    | 1     |
| SAN MIGUEL TOPILEJO             | COVID-19                    | 1     |
| COLA DE PATO                    | COVID-19                    | 1     |
| SANTA CATARINA YECAHUITZOTL     | COVID-19                    | 1     |
| AMPLIACION SAN MIGUEL           | COVID-19                    | 1     |
| SAN SALVADOR CUAUHTENCO         | COVID-19                    | 1     |
| SAN PABLO OZTOTEPEC             | COVID-19                    | 1     |
| NINGUNO                         | COVID-19                    | 1     |
| SAN JUAN IXTAYOPAN              | COVID-19                    | 1     |
| CANSACABALLOS                   | COVID-19                    | 1     |
| SAN NICOLAS TETELCO             | COVID-19                    | 1     |
| TEMAXCATITLA (KILOMETRO 32.2)   | COVID-19                    | 1     |

Las defunciones por enfermedades respiratorias, particularmente por COVID-19, se concentraron principalmente en alcaldías densamente pobladas como Iztapalapa, Gustavo A. Madero, Benito Juárez y Azcapotzalco, lo cual refleja una relación entre la alta densidad demográfica, condiciones socioeconómicas desfavorables y mayor vulnerabilidad sanitaria. Aunque el COVID-19 tuvo un impacto transversal en toda la ciudad, las muertes por otras enfermedades respiratorias fueron considerablemente menores, lo que sugiere un posible subregistro o que muchas de ellas fueron clasificadas como COVID-19 durante la emergencia sanitaria. En contraste, las alcaldías con menor número de muertes, como Milpa Alta, Magdalena Contreras y Cuajimalpa, son zonas con menor densidad poblacional, lo que podría haber reducido la propagación del virus, aunque también podría reflejar limitaciones en el registro de datos. Además, se observan registros dispersos en localidades rurales o no especificadas, lo que indica desigualdad en el acceso a servicios de salud y en la calidad de los sistemas de información. En conjunto, los datos revelan que el impacto de las enfermedades respiratorias estuvo profundamente influenciado por factores territoriales y sociales.

### 3. **Análisis de muertes por fechas**

Pregunta: ¿Qué patrones mensuales de mortalidad se observan en 2020 y cómo se relacionan con el contexto de la pandemia de COVID-19 y otras causas estacionales de muerte?

Ejecutamos:
```sql
SELECT 
    EXTRACT(MONTH FROM fecha_defuncion) AS mes_de_defuncion, 
    COUNT(*) AS cantidad_de_muertes 
FROM defuncion 
GROUP BY mes_de_defuncion 
ORDER BY mes_de_defuncion;
```
📌 **Resultados:**  

| Mes | Cantidad de Muertes |
|-----|----------------------|
| 1   | 7496                |
| 2   | 5995                |
| 3   | 5977                |
| 4   | 8389                |
| 5   | 16596               |
| 6   | 12990               |
| 7   | 9795                |
| 8   | 9787                |
| 9   | 9203                |
| 10  | 9498                |
| 11  | 9869                |
| 12  | 17424               |

Durante 2020 se observa un claro efecto de la pandemia de COVID-19 sobre la mortalidad mensual. Los primeros tres meses del año (enero–marzo) muestran cifras relativamente bajas (entre 5 977 y 7 496 defunciones), antes de que el virus cobrara fuerza en México. A partir de abril (8 389 muertes) y sobre todo en mayo (16 596), coincide con la primera gran ola de contagios y la saturación hospitalaria; el alza abrupta en mayo–junio (12 990) refleja tanto muertes directamente por COVID-19 como otras asociadas a la falta de acceso oportuno a servicios médicos. Durante los meses de verano y principios de otoño (julio–octubre), las cifras se estabilizan alrededor de 9 200–9 800 muertes, probablemente por una combinación de disminución parcial de la transmisión, medidas de confinamiento y también el impacto de otras causas (accidentes de tránsito, violencia, enfermedades crónicas desatendidas). Finalmente, en noviembre (9 869) y especialmente en diciembre (17 424), se aprecia un segundo pico de mortalidad que coincide con la segunda ola de COVID-19 y, por otro lado, con factores estacionales como la circulación de influenza, el clima frío y el incremento de accidentes o violencias típicas de las festividades. En conjunto, estos patrones mensuales reflejan cómo las olas pandémicas y las variaciones estacionales de otras causas confluyeron para moldear la curva de mortalidad en 2020.

### 4. **Análisis mortalidad materna**

Pregunta: ¿Cuántas muertes relacionadas con embarazo se reportan, y en qué etapas?

Ejecutamos:
```sql
SELECT 
    durante_embarazo,
    persona.escolaridad,
    COUNT(*) AS cantidad_muertes
FROM embarazo
JOIN persona ON persona.id = embarazo.persona_id
JOIN defuncion ON defuncion.persona_id = persona.id
WHERE causado_embarazo ILIKE 'SI' 
  AND durante_embarazo IS NOT NULL 
  AND durante_embarazo NOT LIKE 'NO %'
GROUP BY durante_embarazo, persona.escolaridad
ORDER BY cantidad_muertes DESC;
```
📌 **Resultados:**  

| Etapa                                        | Nivel Educativo                                | Cantidad de  muertes |
|----------------------------------------------|------------------------------------------------|----------|
| EL PUERPERIO                                 | BACHILLERATO O PREPARATORIA COMPLETA           | 6        |
| EL PUERPERIO                                 | SECUNDARIA COMPLETA                            | 4        |
| EL EMBARAZO                                  | SECUNDARIA COMPLETA                            | 3        |
| EL EMBARAZO                                  | LICENCIATURA O PROFESIONAL COMPLETO            | 2        |
| EL PUERPERIO                                 | BACHILLERATO O PREPARATORIA INCOMPLETA         | 2        |
| EL PUERPERIO                                 | LICENCIATURA O PROFESIONAL COMPLETO            | 2        |
| 43 DÍAS A 11 MESES DESPUÉS DEL PARTO O ABORTO | PRIMARIA COMPLETA                              | 1        |
| EL PUERPERIO                                 | SECUNDARIA INCOMPLETA                          | 1        |
| EL EMBARAZO                                  | PRIMARIA COMPLETA                              | 1        |
| EL PUERPERIO                                 | LICENCIATURA O PROFESIONAL INCOMPLETO          | 1        |
| EL PUERPERIO                                 | NINGUNA                                        | 1        |
| EL PUERPERIO                                 | POSGRADO COMPLETO                              | 1        |
| EL PUERPERIO                                 | PRIMARIA COMPLETA                              | 1        |

El análisis de los casos de mortalidad materna revela que la mayoría de las muertes ocurrieron durante el puerperio, es decir, después del parto, lo que indica una etapa crítica en la atención médica de las mujeres. De las 26 muertes registradas, al menos 19 ocurrieron en el puerperio, mientras que solo 6 sucedieron durante el embarazo y 1 entre los 43 días y 11 meses posteriores al parto o aborto. Las edades de las mujeres oscilaban entre los 20 y los 45 años, siendo más frecuente en mujeres de entre 25 y 40 años. En cuanto a escolaridad, predominan los niveles de secundaria y bachillerato, aunque también hay casos con licenciatura e incluso posgrado, lo que sugiere que la mortalidad materna no está limitada únicamente a bajos niveles educativos. Estos datos subrayan la necesidad de mejorar el seguimiento médico durante el posparto, una etapa frecuentemente desatendida pero de alto riesgo para la salud materna.

### 5. **Análisis entre atención médica y muerte**

Pregunta: ¿¿Cuál es la distribución porcentual de la atención médica (recibida, no recibida o desconocida) entre los casos correspondientes a las 10 enfermedades con mayor tasa de mortalidad?

Ejecutamos:
```sql
-- Paso 1: Obtener las 10 causas con más muertes
WITH top_causas AS (
    SELECT causa_defuncion
    FROM defuncion
    GROUP BY causa_defuncion
    ORDER BY COUNT(*) DESC
    LIMIT 10
),

-- Paso 2: Contar atención médica por tipo en esas 10 causas
atencion_por_causa AS (
    SELECT 
        d.causa_defuncion,
        d.atencion_medica,
        COUNT(*) AS total
    FROM defuncion d
    INNER JOIN top_causas t ON d.causa_defuncion = t.causa_defuncion
    GROUP BY d.causa_defuncion, d.atencion_medica
),

-- Paso 3: Total por causa para calcular porcentajes
total_por_causa AS (
    SELECT 
        causa_defuncion,
        SUM(total) AS total_causa
    FROM atencion_por_causa
    GROUP BY causa_defuncion
)

-- Paso 4: Calcular porcentajes finales
SELECT 
    a.causa_defuncion,
    CASE 
        WHEN a.atencion_medica IS TRUE THEN 'Sí'
        WHEN a.atencion_medica IS FALSE THEN 'No'
        ELSE 'No se sabe'
    END AS atencion_medica,
    a.total,
    ROUND((a.total * 100.0 / t.total_causa), 2) AS porcentaje
FROM atencion_por_causa a
JOIN total_por_causa t ON a.causa_defuncion = t.causa_defuncion
ORDER BY a.causa_defuncion, porcentaje DESC;
```
📌 **Resultados:**  
| Enfermedad                   | Atención médica | Total de muertes | Porcentaje (%) |
|-----------------------------|-----------------|------------------|----------------|
| CÁNCER                      | Sí              | 10,808           | 98.46%         |
| CÁNCER                      | No se sabe      | 87               | 0.79%          |
| CÁNCER                      | No              | 82               | 0.75%          |
| COVID-19                    | Sí              | 36,908           | 97.93%         |
| COVID-19                    | No se sabe      | 435              | 1.15%          |
| COVID-19                    | No              | 347              | 0.92%          |
| DIABETES                    | Sí              | 16,267           | 98.47%         |
| DIABETES                    | No              | 127              | 0.77%          |
| DIABETES                    | No se sabe      | 125              | 0.76%          |
| ENFERMEDAD CARDIACA         | Sí              | 3,891            | 98.73%         |
| ENFERMEDAD CARDIACA         | No se sabe      | 26               | 0.66%          |
| ENFERMEDAD CARDIACA         | No              | 24               | 0.61%          |
| ENFERMEDAD PULMONAR         | Sí              | 2,919            | 97.04%         |
| ENFERMEDAD PULMONAR         | No              | 52               | 1.73%          |
| ENFERMEDAD PULMONAR         | No se sabe      | 37               | 1.23%          |
| ENFERMEDAD RENAL            | Sí              | 2,888            | 98.70%         |
| ENFERMEDAD RENAL            | No se sabe      | 23               | 0.79%          |
| ENFERMEDAD RENAL            | No              | 15               | 0.51%          |
| HEMORRAGIA                  | Sí              | 2,133            | 98.11%         |
| HEMORRAGIA                  | No              | 24               | 1.10%          |
| HEMORRAGIA                  | No se sabe      | 17               | 0.78%          |
| INFARTO                     | Sí              | 15,028           | 97.50%         |
| INFARTO                     | No              | 262              | 1.70%          |
| INFARTO                     | No se sabe      | 123              | 0.80%          |
| INFECCIÓN                   | Sí              | 2,495            | 98.62%         |
| INFECCIÓN                   | No se sabe      | 18               | 0.71%          |
| INFECCIÓN                   | No              | 17               | 0.67%          |
| NEUMONÍA, NO ESPECIFICADA   | Sí              | 5,922            | 98.49%         |
| NEUMONÍA, NO ESPECIFICADA   | No se sabe      | 62               | 1.03%          |
| NEUMONÍA, NO ESPECIFICADA   | No              | 29               | 0.48%          |

El análisis de la atención médica en los casos de las diez enfermedades con mayor mortalidad revela que la gran mayoría de las personas que fallecieron sí recibieron atención médica previa. En todos los casos, el porcentaje de atención médica recibida supera el 97%, destacando enfermedades como la enfermedad cardíaca (98.73%), enfermedad renal (98.70%), infecciones (98.62%) y cáncer (98.46%). Las proporciones de muertes sin atención médica o con datos desconocidos son mínimas, rondando entre el 0.5% y 1.7% en la mayoría de los padecimientos. Este patrón sugiere que, aunque los pacientes acceden al sistema de salud, la gravedad de estas enfermedades o la posible tardanza en su atención podrían limitar la efectividad de los tratamientos médicos, abriendo la discusión sobre la calidad, oportunidad y continuidad del cuidado médico recibido.

### 6. **Análisis entre nacimientos y muertes en la misma residencia**

Pregunta: ¿Cuántas personas fallecieron en el mismo municipio de la Ciudad de México en el que residían?

Ejecutamos:
```sql
WITH mismo_lugar AS(
	SELECT residencia_id, COUNT(*) as total
	FROM persona
	JOIN defuncion ON defuncion.persona_id=persona.id
	WHERE residencia_id=defuncion.alcaldia_defuncion_id
	GROUP BY residencia_id
	ORDER BY total DESC
),
diferente_lugar AS(
	SELECT residencia_id, COUNT(*) as total
	FROM persona
	JOIN defuncion ON defuncion.persona_id=persona.id
	WHERE residencia_id!=defuncion.alcaldia_defuncion_id
	GROUP BY residencia_id
	ORDER BY total DESC
)

SELECT entidad_municipio.municipio, mismo_lugar.total AS total_mismo_lugar, diferente_lugar.total AS total_diferente_lugar
FROM mismo_lugar
JOIN entidad_municipio ON entidad_municipio.id=residencia_id
LEFT JOIN diferente_lugar ON mismo_lugar.residencia_id= diferente_lugar.residencia_id
ORDER BY mismo_lugar.residencia_id;
```
📌 **Resultados:**  
| Municipio                         | Muertes (misma residencia) | Muertes (diferente residencia) |
|----------------------------------|-----------------------------|---------------------------------|
| AA MILPA ALTA                    | 312                         | 170                             |
| VENUSTIANO CARRANZA              | 2636                        | 2669                            |
| XOCHIMILCO                       | 2199                        | 1818                            |
| SANTA CATARINA YECAHUITZOTL      | 11                          | 11                              |
| MIGUEL HIDALGO                   | 2312                        | 1406                            |
| GUSTAVO A. MADERO                | 10,529                       | 3009                            |
| MANANTIALES DE MONTE ALEGRE     | 1                           | 3                               |
| SAN LORENZO TLACOYUCAN           | 6                           | 8                               |
| SAN FRANCISCO TECOXPA            | 3                           | 5                               |
| IZTACALCO                        | 2967                        | 1898                            |
| SAN LORENZO ACOPILCO             | 2                           | 3                               |
| SAN NICOLAS TETELCO              | 8                           | 6                               |
| ALBERGUE ALPINO AJUSCO          | 26                          | 22                              |
| EJIDOS DE SAN ANDRES TOTOLTEPEC  | 1                           | 1                               |
| ACALIPA                          | 9                           | 9                               |
| OJO DE AGUA                      | 25                          | 3                               |
| SAN PABLO OZTOTEPEC              | 14                          | 29                              |
| LA CONCEPCION                    | 1                           | NULL                            |
| NO ESPECIFICADO                  | 2825                        | 2275                            |
| SAN BARTOLOME XICOMULCO          | 2                           | 10                              |
| SAN ANDRES MIXQUIC               | 26                          | 11                              |
| TLAHUAC                          | 1654                        | 1145                            |
| SAN SALVADOR CUAUHTENCO          | 13                          | 18                              |
| IZTAPALAPA                       | 11,251                       | 5669                            |
| AMPLIACION SAN MIGUEL            | 7                           | 8                               |
| BENITO JUAREZ                    | 2617                        | 987                             |
| VILLA MILPA ALTA                 | 272                         | 191                             |
| COYOACAN                         | 3691                        | 2540                            |
| SAN ANTONIO TECOMITL             | 21                          | 36                              |
| AZCAPOTZALCO                     | 3482                        | 1581                            |
| SANTA ANA TLACOTENCO             | 12                          | 15                              |
| CUAJIMALPA DE MORELOS            | 785                         | 682                             |
| SAN MIGUEL TOPILEJO              | 7                           | 14                              |
| ACOPIAXCO [CAMPAMENTO FORESTAL]  | 28                          | 52                              |
| SAN JUAN IXTAYOPAN               | 34                          | 29                              |
| CRUZ BLANCA                      | 1                           | 1                               |
| CUAUHTEMOC                       | 3641                        | 2209                            |
| SAN MIGUEL                       | 29                          | 9                               |
| LA NOPALERA                      | 1                           | 3                               |
| TEMAXCATITLA (KILOMETRO 32.2)    | 1                           | 1                               |
| ALVARO OBREGON                   | 4683                        | 2348                            |
| SAN PEDRO ATOCPAN                | 15                          | 26                              |
| LA MAGDALENA CONTRERAS           | 1050                        | 1016                            |
| TLALPAN                          | 3326                        | 1950                            |
| COLA DE PATO                     | 14                          | 18                              |
| SAN MIGUEL AJUSCO                | 1                           | 5                               |

El análisis muestra que en la Ciudad de México, una gran mayoría de las personas fallecieron en el mismo municipio en el que residían. Delegaciones como Iztapalapa (11,251 muertes en su lugar de residencia), Gustavo A. Madero (10,529), y Tlalpan (3,326) lideran en esta tendencia, reflejando probablemente su alta densidad poblacional y una mayor disponibilidad de servicios de salud locales o el hecho de que muchas personas envejecen y fallecen en sus domicilios. En contraste, algunas localidades como Acopiaxco y San Miguel Topilejo presentan más muertes fuera que dentro de su área de residencia, lo que podría indicar traslados a hospitales en otros municipios. El dato "No especificado" también tiene un peso importante, con 2,825 muertes en el lugar de residencia y 2,275 en otro, lo que sugiere un margen de incertidumbre en la geolocalización del evento. En conjunto, estos datos reflejan una fuerte correspondencia entre lugar de residencia y defunción, útil para planear políticas de salud pública localizadas.

### 7. **Análisis de la mortalidad en distintos grupos de edad**

Pregunta: ¿Cuántas muertes hubo por cada rango de edad?

Ejecutamos:
```sql
SELECT 
  CONCAT(
    FLOOR(EXTRACT(YEAR FROM AGE(defuncion.fecha_defuncion, persona.fecha_nacimiento)) / 10) * 10,
    ' - ',
    FLOOR(EXTRACT(YEAR FROM AGE(defuncion.fecha_defuncion, persona.fecha_nacimiento)) / 10) * 10 + 9
  ) AS rango_edad,
  COUNT(*) AS num_muertes
FROM persona
JOIN defuncion ON persona.id = defuncion.persona_id
GROUP BY rango_edad
ORDER BY MIN(EXTRACT(YEAR FROM AGE(defuncion.fecha_defuncion, persona.fecha_nacimiento)));
```
📌 **Resultados:**
| Rango de Edad | Número de Muertes |
|---------------|-------------------|
| 0 - 9         | 2152              |
| 10 - 19       | 681               |
| 20 - 29       | 1876              |
| 30 - 39       | 4278              |
| 40 - 49       | 10388             |
| 50 - 59       | 19562             |
| 60 - 69       | 27340             |
| 70 - 79       | 26539             |
| 80 - 89       | 21147             |
| 90 - 99       | 8479              |
| 100 - 109     | 500               |
| 110 - 119     | 23                |
| -             | 54                |

El análisis por rangos de edad revela que en la Ciudad de México, la mayoría de las defunciones se concentran en personas mayores de 50 años. Los grupos de 60 a 69 años (27,340 muertes), 70 a 79 años (26,539) y 80 a 89 años (21,147) representan los picos más altos, lo que refleja el impacto del envejecimiento poblacional en la mortalidad general. El grupo de 50 a 59 años también registra un número considerable (19,562), lo cual podría vincularse a enfermedades crónicas que se manifiestan a partir de esa edad.

En contraste, los rangos de edad más jóvenes, como 0 a 9 años (2,152 muertes) y 10 a 19 años (681), muestran una mortalidad significativamente menor, aunque no despreciable, lo que podría apuntar a factores como enfermedades congénitas.


