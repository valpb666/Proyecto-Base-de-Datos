/* ************************************ */
/*          ANÁLISIS PRELIMINAR         */
/* ************************************ */

/*
1. Columnas con valores únicos
*/

SELECT column_name
FROM staging
GROUP BY column_name
HAVING COUNT(DISTINCT column_name) = COUNT(*);

/*
2. Mínimos y máximos de fechas
*/

SELECT 
    MIN(fecha_nacimiento) AS fecha_nacimiento_min,
    MAX(fecha_nacimiento) AS fecha_nacimiento_max,
    MIN(fecha_defuncion) AS fecha_defuncion_min,
    MAX(fecha_defuncion) AS fecha_defuncion_max
FROM staging
WHERE fecha_nacimiento NOT IN ('NA');

/*
3. Mínimos, máximos y promedios de valores numéricos
*/

SELECT 
    MIN(edad::INTEGER) AS edad_min,
    MAX(edad::INTEGER) AS edad_max,
    AVG(edad::NUMERIC) AS edad_promedio
FROM staging
WHERE edad NOT IN ('NA');

/*
4. Duplicados en atributos categóricos
*/

SELECT columna_categorica, COUNT(*) AS frecuencia
FROM staging
GROUP BY columna_categorica
ORDER BY frecuencia DESC;

/*
5. Columnas redundantes
*/

SELECT column_name, COUNT(*) 
FROM staging
GROUP BY column_name
ORDER BY COUNT(*) DESC;

/*
6. Conteo de valores nulos
*/

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

/*
7. Inconsistencias en las fechas
*/

SELECT fecha_nacimiento, fecha_defuncion
FROM staging
WHERE fecha_nacimiento>fecha_defuncion;

/*
8. Inconsistencias en la hora de defunción
*/

SELECT hora_defuncion
FROM staging
WHERE hora_defuncion<'00:00:00' OR hora_defuncion>'23:59:59';

/*
9. Inconsistencias en el sexo
*/

SELECT sexo, durante_embarazo
FROM staging
WHERE sexo ILIKE 'hombre' AND (durante_embarazo NOT ILIKE 'NO APLICA' AND durante_embarazo NOT ILIKE 'NO ESPECIFICADO');

/*
10. Inconsistencias en las dos columnas de fecha de defunción
*/

SELECT fecha_defuncion1, fecha_defuncion, fecha_defuncion1=fecha_defuncion AS coincide
FROM staging
WHERE fecha_defuncion1!=fecha_defuncion;

/*
11. Inconsistencias entre los municipios residenciales y las entidades residenciales
*/

SELECT municipio_residencia, COUNT(DISTINCT entidad_residencia) AS entidades_distintas
FROM staging
GROUP BY municipio_residencia
HAVING COUNT(DISTINCT entidad_residencia) > 1
ORDER BY municipio_residencia;

/*
12. Inconsistencias en las causas de muerte 
*/

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
