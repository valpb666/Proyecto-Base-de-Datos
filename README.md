# Proyecto Base de Datos

## Introducción al conjunto de datos y al problema a estudiar considerando aspectos éticos del conjunto de datos empleado
  Equipo: Julia Rojas Pereyra, Nuria Garcia Valdecasas, Valentina Pineda, Valentina Covarrubias Faure, Alejandro Salas Aguilar

  La base de datos escogida fue la siguiente: 
    https://datos.cdmx.gob.mx/dataset/certificados-de-defuncion-sedesa/resource/fc38b701-964d-4c36-8c63-cca9205ab53f

  *Descripción general de los datos*
  
    Este conjunto de datos recolecta información ace
    
  *¿Quién los recolecta?*
  
    Los datos son recolectados por la Secretaría de Salud de la Ciudad de México, a partir de los Certificados de Defunción.
    Estos son procesados y codificados por médicos codificadores según los criterios establecidos por la OMS, y capturados en
    el Subsistema Epidemiológico y Estadístico de las Defunciones (SEED) a nivel Federal.
    
  *¿Cuál es el propósito de su recolección?*
  
    Este conjunto de datos tiene como propósito el brindar información detallada sobre los fallecimientos que ocurren en
    la Ciudad desde una perspectiva epidemiológica. Es decir, describir las condiciones de salud de la población, identificar
    la causa de las enfermedades, controlar las enfermedades y prevenir la aparición de nuevas enfermedades.
    
  *¿Dónde se pueden obtener?*
    
    Se pueden obtener en el portal de datos abiertos de la Ciudad de México, al entrar en ese portal hay varias secciones en la que se pueden             consultar conjuntos de datos, los que nosotros usaremos están en la sección de administración y finanzas, donde posteriormente aparecen las           instituciones disponibles, nuestros datos se encuentran ingresando al apartado de secretaría de salud.

  *¿Con qué frecuencia se actualizan?*

    La última actualización fue el 7 de julio del 2023, y se creó el 13 de marzo del 2021. No se especifica cada cuanto tiempo se actualiza pero ya        pasó más de 1 año desde la última actualización.
  
  *¿Cuántas tuplas y cuántos atributos tiene el set de datos?*
  
    Nuestro set de datos cuenta con 28 atributos, pero dentro de estos se encuentran unos atributos con diferente nombre pero misma información. Este      set contiene 127286 tuplas.

| Atributo                   | Tipo de dato en SQL (Variable)  | Descripción                                                   |
|----------------------------|--------------------------------|---------------------------------------------------------------|
| sexo                       | text (Categórica)             | Género de la persona.                                         |
| fecha_nacimiento           | date (Fecha)               | Fecha de nacimiento de la persona.                           |
| nacionalidad               | text (Categórica)             | Nacionalidad declarada.                                       |
| lengua_indigena            | text (Categórica)             | Indica si habla una lengua indígena.                         |
| estado_civil               | text (Categórica)             | Estado civil de la persona.                                   |
| entidad_residencia         | text (Categórica)             | Entidad federativa de residencia.                            |
| municipio_residencia       | text (Categórica)             | Municipio o alcaldía de residencia.                          |
| escolaridad                | text (Categórica)             | Nivel educativo alcanzado por la persona.                   |
| ocupacion                  | text (Categórica)             | Ocupación o trabajo habitual.                                |
| afiliacion_medica          | text (Categórica)             | Tipo de afiliación médica que tiene la persona.             |
| fecha_defuncion1           | date (Fecha)               | Fecha exacta de la defunción.                                |
| hora_defuncion             | time (Fecha)               | Hora exacta de la defunción.                                 |
| lugar_defuncion            | text (Categórica)             | Lugar donde ocurrió la defunción.                           |
| entidad_defuncion          | text (Categórica)             | Entidad federativa donde ocurrió la defunción.              |
| alcaldia                   | text (Categórica)             | Alcaldía o municipio donde ocurrió la defunción.            |
| atencion_medica            | text (Categórica)             | Indica si recibió atención médica antes de la defunción.    |
| necropsia                  | text (Categórica)             | Indica si se realizó necropsia.                             |
| causa_defuncion            | text (Categórica)             | Causa oficial de la defunción.                              |
| durante_embarazo           | text (Categórica)             | Indica si la defunción ocurrió durante el embarazo.        |
| causado_embarazo           | text (Categórica)             | Indica si la defunción fue causada por el embarazo.        |
| complicacion_embarazo      | text (Categórica)             | Indica si hubo complicaciones relacionadas con el embarazo.|
| muerte_accidental_violenta | text (Categórica)             | Indica si la muerte fue accidental o violenta.              |
| tipo_evento                | text (Categórica)             | Tipo de evento relacionado con la muerte.                  |
| en_trabajo                 | text (Categórica)             | Indica si el evento ocurrió en el trabajo.                 |
| sitio_lesion               | text (Categórica)             | Lugar físico donde ocurrió la lesión.                      |
| municipio_ocurrencia       | text (Categórica)             | Municipio donde ocurrió el evento.                        |
| fecha_defuncion            | date (Fecha)               | Fecha de la defunción.                                      |
| edad                       | int (Numérica)                | Edad de la persona en años.                                |


 *¿Cuál es el objetivo buscado con el set de datos?*
  
    Llevar un control del tipo de gente que muere, si obtuvieron atención médica, y el lugar donde murieron. Pueden sacarse
    muchas conclusiones de este set de datos, desde ver épocas de mayor mortalidad (como durante la pandemia de covid-19),
    lugares con mayores índices de mortalidad, o la eficacia de
    atención médica.
    
  *¿Para qué se usará por el equipo?*
  
    Decidimos utilizar esta base de datos para realizar un análisis detallado de la mortalidad en la Ciudad de México,
    identificando patrones y tendencias en función de variables clave como la causa de muerte (la enfermedad), la edad,
    el género y la ubicación geográfica (alcaldía) de los fallecimientos. A través de la estructuración de las entidades
    principales, como defunciones, alcaldías y pacientes, se podrá evaluar qué enfermedades son más frecuentes en
    determinados grupos poblacionales y en qué zonas de la ciudad se registran las tasas de mortalidad más altas.
    Además, esta información permitirá comparar datos a lo largo del tiempo para detectar posibles cambios en las causas
    de defunción y su relación con factores demográficos o socioeconómicos.
    
  *¿Qué consideraciones éticas conlleva el análisis y explotación de dichos datos?*
  
    El análisis de esta base de datos conlleva diversas consideraciones éticas, ya que implica el acceso a información sensible sobre personas            fallecidas. Por ello, es fundamental respetar la privacidad y confidencialidad de los datos, asegurándonos de que la información utilizada no         permita identificar a individuos específicos, pues esto podría vulnerar la dignidad de los fallecidos y sus familias. Además, es importante           evitar sesgos en la interpretación de los resultados, ya que una mala contextualización de las cifras podría llevar a conclusiones erróneas o         incluso discriminatorias hacia ciertos grupos poblacionales o regiones.
    
# 📌 Carga Inicial y Análisis Preliminar  

Para realizar la carga inicial del set de datos a una base de datos de tipo **PostgreSQL**, sigue los siguientes pasos:  

## ✅ Requisitos Previos  
Antes de comenzar, asegúrate de tener:  
- **PostgreSQL** instalado (`psql` o `pgAdmin`).  
- El archivo de datos **CSV** completamente descomprimido:  
  [Certificados de Defunción - SEDESA](https://datos.cdmx.gob.mx/dataset/certificados-de-defuncion-sedesa).  

---

## 1️⃣ Creación de la Base de Datos  
En la consola de **psql**, ejecuta el siguiente comando:  

```sql
CREATE DATABASE mortalidad;
```
## 2️⃣ Creación de Tablas en TablePlus
Abre TablePlus y crea una nueva conexión con la base de datos mortalidad (categoría PostgreSQL).

Abre la opción SQL Query e ingresa el siguiente comando para crear la tabla:

```sql
CREATE TABLE staging (
    sexo TEXT,
    fecha_nacimiento TEXT,
    nacionalidad TEXT,
    lengua_indigena TEXT,
    estado_civil TEXT,
    entidad_residencia TEXT,
    municipio_residencia TEXT,
    escolaridad TEXT,
    ocupacion TEXT,
    afiliacion_medica TEXT,
    fecha_defuncion TEXT,
    hora_defuncion TEXT,
    lugar_defuncion TEXT,
    entidad_defuncion TEXT,
    alcaldia TEXT,
    atencion_medica TEXT,
    necropsia TEXT,
    causa_defuncion TEXT,
    durante_embarazo TEXT,
    causado_embarazo TEXT,
    complicacion_embarazo TEXT,
    muerte_accidental_violenta TEXT,
    tipo_evento TEXT,
    en_trabajo TEXT,
    lugar_lesion TEXT,
    municipio_ocurrencia TEXT,
    fecha_defuncion_r TEXT,
    edad TEXT
);
```
## 3️⃣ Conexión a la Base de Datos y Carga Inicial de Datos
Regresa a la consola psql y ejecuta los siguientes comandos:

```sql
\c mortalidad;
SET CLIENT_ENCODING TO 'UTF8';
\copy staging (sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica, fecha_defuncion, hora_defuncion, lugar_defuncion, entidad_defuncion, alcaldia, atencion_medica, necropsia, causa_defuncion, durante_embarazo, causado_embarazo, complicacion_embarazo, muerte_accidental_violenta, tipo_evento, en_trabajo, lugar_lesion, municipio_ocurrencia, fecha_defuncion_r, edad) FROM 'path_to_downloaded_csv' WITH (FORMAT CSV, HEADER true, DELIMITER ',');
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

### 7. Conteo de valores nulos (Para contar los valores nulos contamos las casillas que dijeran 'se ingora' o 'no especificado' ya que es lo mismo a no tener el dato, en realidad es un valor nulo)
```sql
--Para checar valores nulos:
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
El resultado que obtuvimos fue el siguiente:
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




  
  
