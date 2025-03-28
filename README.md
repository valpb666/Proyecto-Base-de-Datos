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
  
  *¿Qué significa cada atributo del set?*

    -sexo: Categoriza el sexo del individuo como hombre o mujer.
    -fecha_nacimiento: Da la fecha de nacimiento del individuo en el formato el formato AAAA/MM/DD. En caso de desconocerse se categoriza como NA
    -nacionalidad: Categoriza la nacionalidad del individuo entre MEXICANA, OTRA o SE IGNORA.
    -lengua_indigena: Categoriza si el individuo habla una lengua indígena como SI, NO, NO ESPECIFICADO o SE IGNORA.
    -estado_civil: Categoriza el estado civil del individuo como SOLTERO, CASADO, DIVORCIADO, VIUDO, UNION LIBRE, SEPARADO o SE IGNORA. 
    -entidad_residencia: Da el estado de la república donde residía el individuo.
    -municipio_residencia: Da el municipio de la república donde residía el individuo.
    -escolaridad: Categoriza la escolaridad del individuo como: NINGUNA, NO ESPECIFICADO, SE IGNORA o los diversos niveles de escolaridad                 distinguiendo entre completo o terminado.
    -ocupacion: Categoriza la ocupación del individuo como SE IGNORA, NO ESPECIFICADO, NO OCUPADO o diversas otras categorías descriptivas de la          ocupación del individuo, algunas que distinguen entre remunerado o no remunerado.
    -afiliacion_medica: Categoriza la afiliación médica del individuo como: NINGUNA, NO ESPECIFICADA, SE IGNORA, ISSTE, IMSS, SEDENA, SEGURO POPULAR      u OTRA.
    -fecha_defuncion: Da la fecha de defunción del individuo en el formato AAAA/MM/DD. En caso de desconocerse se categoriza como NA
    -hora_defuncion: Da la hora de defunción del individuo en el formato hora, minuto, y segundo. En caso de desconocerse se categoriza como NA
    -lugar_defuncion: Categoriza el lugar de defunción del individuo como HOGAR, ISSSTE, SECRETARIA DE SALUD, UNIDAD MEDICA PRIVAD, VÍA PÚBLICA,          HOGAR u OTRO LUGAR.
    -entidad_defuncion: Da la entidad de la república donde falleció el individuo.
    -alcaldia: Da la alcaldía de la Ciudad de México donde falleció el individuo, o la categoriza como NO ESPECIFICADA.
    -atencion_medica: Categoriza si el individuo obtuvo atención médica como SI, NO, SE IGNORA o NO ESPECIFICADO
    -necropsia: Categoriza si se realizó una necropsia para el individuo como SI, NO, NO ESPECIFICADO o SE IGNORA.
    -causa_defuncion: Clasifica la muerte del individuo en una de las numerosas categorías disponibles.
    -durante_embarazo: Categoriza si el fallecimiento sucedió en el embarazo mediante las categorías: SI, NO APLICA, NO ESTUVO EMBARAZADA EN LOS          ÚLTIMOS 11 MESES PREVIOS A LA MUERTE, o NO ESPECIFICADO.
    -causado_embarazo: Categoriza si el fallecimiento fue causado por el embarazo mediante las categorías: SI, NO, NO APLICA o NO ESPECIFICADO.
    -muerte_accidental_violenta: Categoriza si el individuo sufrió una muerte accidental violenta como SI o NO
    -tipo_evento: En caso de que el individuo haya sufrido una muerte accidental violenta, la clasifica como SUICIDIO, HOMICIDIO, ACCIDENTE o NO          ESPECIFICADO. En caso de que no, entonces se clasifica como NO APLICA, o si no, como SE IGNORA.
    -en_trabajo: Cuando el individuo falleció por muerte accidental o violenta, se categoriza si falleció en el trabajo como : SI, NO o SE IGNORA. Si     no como NO APLICA.
    -sitio_lesion: Cuando el individuo falleció por muerte accidental o violenta, se categoriza el sitio donde se lesionó como CALLE O CARRETERA (VÍA     PÚBLICA), VIVIENDA PARTICULAR, VIVIENDA PARTICULAR, VIVIENDA COLECTIVA (ASILO, ORFANATO, ETC), o SE IGNORA. Si no, entonces se categoriza como NO     APLICA.
    -municipio_ocurrencia: Cuando el individuo falleció por muerte accidental o violenta se categoriza el municipio donde falleció. Si no, se             categoriza como NO APLICA o SE IGNORA.
    -fecha_def: Da la fecha de defunción del individuo en formato AAAA/MM/DD. En caso de desconocerse se categoriza como NA
    -edad: Da la edad del individuo al momento de fallecer en años. En caso de desconocerse se categoriza como NA

  *¿Qué atributos son numéricos?*

    El set de datos solo cuenta con el atributo numérico edad, que se expresa en años.
    
  *¿Qué atributos son categóricos?*

    Los atributos categóricos del set son:
    -Sexo
    -Nacionalidad
    -Lengua indígena
    -Estado civil
    -Entidad de residencia
    -Municipio de residencia
    -Escolaridad
    -Ocupación
    -Afiliación médica
    -Lugar de defunción
    -Entidad de defunción
    -Alcaldía
    -Atención médica
    -Necropsia
    -Causa de defunción 
    -Durante embarazo
    -Causado por embarazo
    -Complicación embarazo
    -Muerte accidental violenta
    -Tipo de evento
    -En trabajo
    -Sitio lesión 
    -Municipio de ocurrencia
  
  *¿Qué atributos son de tipo texto?*

    El set no cuenta con atributos tipo texto, debido a que aquellos atributos que utilizan texto pertenecen todos a categorías predeterminadas, es       decir, no existe algún atributo donde haya texto libre.

  *¿Qué atributos son de tipo temporal y/o fecha?*
  
    Los atributos del tipo fecha son los siguientes:
    -Fecha de nacimiento, con el formato AAAA/MM/DD, llamada fecha_nacimiento
    -Fecha de defunción, con el formato AAAA/MM/DD, llamada fecha_defuncion
    -La hora de defunción, que registra la hora, minuto, y segundo de muerte, llamada hora_defuncion
    -Hay otro atributo que registra la fecha de defunción en el mismo formato, llamado fecha_def
    
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

  
  
