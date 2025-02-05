# Proyecto Base de Datos

# Introducción al conjunto de datos y al problema a estudiar considerando aspectos éticos del conjunto de datos empleado
  Equipo: Julia Rojas Pereyra, Nuria Garcia Valdecasas, Valentina Pineda, Valentina Covarrubias Faure, Alejandro Salas Aguilar

  La base de datos escogida fue la siguiente: 
    https://datos.cdmx.gob.mx/dataset/certificados-de-defuncion-sedesa/resource/fc38b701-964d-4c36-8c63-cca9205ab53f

  *Descripción general de los datos*
  
    Este conjunto de datos recolecta información ace
    
  *¿Quién los recolecta?*
  
    Los datos son recolectados por la Secretaría de Salud de la Ciudad de México, a partir de los Certificados de Defunción. Estos son procesados y codificados por médicos codificadores según los criterios     establecidos por la OMS, y capturados en el Subsistema Epidemiológico y Estadístico de las Defunciones (SEED) a nivel Federal.
    
  *¿Cuál es el propósito de su recolección?*
  
    Este conjunto de datos tiene como propósito el brindar información detallada sobre los fallecimientos que ocurren en la Ciudad desde una perspectiva epidemiológica. Es decir, describir las condiciones      de salud de la población, identificar la causa de las enfermedades, controlar las enfermedades y prevenir la aparición de nuevas enfermedades.
    
  *¿Dónde se pueden obtener?*
  
  *¿Con qué frecuencia se actualizan?*
  
  *¿Cuántas tuplas y cuántos atributos tiene el set de datos?*
  
  *¿Qué significa cada atributo del set?*
  
  *¿Qué atributos son numéricos?*
  
  *¿Qué atributos son categóricos?*
  
  *¿Qué atributos son de tipo texto?*
  
  *¿Qué atributos son de tipo temporal y/o fecha?*
    Los atributos del tipo fecha son los siguientes:
    Fecha de nacimiento, con el formato AAAA/MM/DD, llamada fecha_nacimiento
    Fecha de defunción, con el formato AAAA/MM/DD, llamada fecha_defuncion
    La hora de defunción, que registra la hora, minuto, y segundo de muerte, llamada hora_defuncion
    Hay otro atributo que registra la fecha de defunción en el mismo formato, llamado fecha_def
    
  *¿Cuál es el objetivo buscado con el set de datos?*
    Llevar un control del tipo de gente que muere, si obtuvieron atención médica, y el lugar donde murieron. Pueden sacarse muchas conclusiones de este set de datos, desde ver épocas de mayor mortalidad        (como durante la pandemia de covid-19), lugares con mayores índices de mortalidad, o la eficacia de atención médica.
    
  *¿Para qué se usará por el equipo?*
    Decidimos utilizar esta base de datos para realizar un análisis detallado de la mortalidad en la Ciudad de México, identificando patrones y tendencias en función de variables clave como la causa de         muerte (la enfermedad), la edad, el género y la ubicación geográfica (alcaldía) de los fallecimientos. A través de la estructuración de las entidades principales, como defunciones, alcaldías y              pacientes, se podrá evaluar qué enfermedades son más frecuentes en determinados grupos poblacionales y en qué zonas de la ciudad se registran las tasas de mortalidad más altas. Además, esta información     permitirá comparar datos a lo largo del tiempo para detectar posibles cambios en las causas de defunción y su relación con factores demográficos o socioeconómicos.
    
  *¿Qué consideraciones éticas conlleva el análisis y explotación de dichos datos?*
    El análisis de esta base de datos conlleva diversas consideraciones éticas, ya que implica el acceso a información sensible sobre personas fallecidas. Por ello, es fundamental respetar la privacidad y      confidencialidad de los datos, asegurándonos de que la información utilizada no permita identificar a individuos específicos, pues esto podría vulnerar la dignidad de los fallecidos y sus familias.         Además, es importante evitar sesgos en la interpretación de los resultados, ya que una mala contextualización de las cifras podría llevar a conclusiones erróneas o incluso discriminatorias hacia            ciertos grupos poblacionales o regiones.
