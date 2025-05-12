
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

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%LEUCEMIA%'; 

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%TUMOR%'; 

UPDATE staging
SET causa_defuncion='CANCER' 
WHERE causa_defuncion ILIKE '%CARCINOMA%';

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
WHERE causa_defuncion ILIKE '%ABSCESO%'

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


--Checar que cada municipio residencia sea igual en entidad residencia
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

--- Arreglar las inconsistencias en las complicaciones en el embarazo (complicacion embarazo)
UPDATE staging
SET complicacion_embarazo = 'SI'
WHERE causa_defuncion ILIKE '%EMBARAZO%';
