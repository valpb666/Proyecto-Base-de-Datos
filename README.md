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
## 3️⃣ Conexión a la Base de Datos y Carga Inicial de Datos
Regresa a la consola psql y ejecuta los siguientes comandos:

```sql
\c mortalidad;
SET CLIENT_ENCODING TO 'UTF8';
\copy staging(sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica, fecha_defuncion1, hora_defuncion, lugar_defuncion, entidad_defuncion, alcaldia, atencion_medica, necropsia, causa_defuncion, durante_embarazo, causado_embarazo, complicacion_embarazo, muerte_accidental_violenta, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, fecha_defuncion, edad) FROM /Users/nuria/Downloads/sedesa_2020_limpia_limp.csv WITH (FORMAT CSV, HEADER true, DELIMITER ',', NULL 'NA');
```
## 📊 Análisis Preliminar
Para comenzar con el análisis de los datos, ejecutamos los siguientes comandos en SQL Query en TablePlus:
1. Existen columnas con valores únicos
```sql
SELECT column_name
FROM staging
GROUP BY column_name
HAVING COUNT(DISTINCT column_name)=COUNT(*);
```
Las columnas con valores únicos fueron las siguientes:
- municipio_residencia
- fecha_nacimiento
- alcaldia
- causa_defuncion
- municipio_ocurrencia

```sql
```

  
  
