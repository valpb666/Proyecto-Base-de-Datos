
/* ************************* */
/*          LIMPIEZA         */
/* ************************* */
-- ELIMINACIÓN DE TUPLAS

DELETE FROM staging
WHERE
  nacionalidad != 'MEXICANA'
  OR muerte_accidental_violenta = 'SI';

-- ELIMINACIÓN DE COLUMNAS

ALTER TABLE staging 
DROP COLUMN edad,
DROP COLUMN nacionalidad,
DROP COLUMN muerte_accidental_violenta,
DROP COLUMN tipo_evento,
DROP COLUMN en_trabajo,
DROP COLUMN sitio_lesion,
DROP COLUMN municipio_ocurrencia,
DROP COLUMN fecha_defuncion1,
DROP COLUMN entidad_defuncion;

-- Actualización de Valores No Especificados

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

-- Cambio a booleanos 

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

-- Agrupar Causa de Defunción

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

UPDATE staging
SET causa_defuncion='CELULITIS' 
WHERE causa_defuncion ILIKE '%CELULITIS%';

SELECT causa_defuncion
FROM staging
WHERE causa_defuncion ILIKE '%RESPI%';

UPDATE staging
SET causa_defuncion='ENFERMEDAD RESPIRATORIA' 
WHERE causa_defuncion ILIKE '%RESPI%';


--- Arreglar las inconsistencias en las complicaciones en el embarazo (complicacion embarazo)
UPDATE staging
SET complicacion_embarazo = 'SI'
WHERE causa_defuncion ILIKE '%EMBARAZO%';
