/* ************************************************************ */
/*          ANÁLISIS DE DATOS A TRAVÉS DE CONSULTAS SQL         */
/* ************************************************************ */

/*
1. Análisis de mortalidad y contexto socioeconómico**

Pregunta: ¿Existe una relación entre escolaridad y causa de defunción por sexo? 
*/

SELECT sexo, defuncion.causa_defuncion, escolaridad, COUNT(*) as total
FROM persona
JOIN defuncion ON defuncion.persona_id=persona.id
GROUP BY sexo, escolaridad, causa_defuncion
HAVING COUNT(*) > 1000
ORDER BY total DESC;

/*
2. **Análisis de enfermedades por alcaldías**

Pregunta: ¿Qué alcaldías concentran más muertes por enfermedades respiratorias?
*/

SELECT entidad_municipio.municipio as alcaldia,causa_defuncion, COUNT(*) as total
FROM defuncion
JOIN entidad_municipio ON entidad_municipio.id=alcaldia_defuncion_id
WHERE causa_defuncion ILIKE '%RESP%' OR causa_defuncion ILIKE '%COVID%'
GROUP BY entidad_municipio.municipio, causa_defuncion
ORDER BY total DESC;

/*
3. **Análisis de muertes por fechas**

Pregunta: ¿Se repiten ciertos patrones de mortalidad en los mismos meses a lo largo de los años?
*/

SELECT EXTRACT (MONTH FROM fecha_defuncion) as mes_de_defuncion, COUNT(*) cantidad_de_muertes
FROM defuncion
GROUP BY EXTRACT (MONTH FROM fecha_defuncion)
ORDER BY cantidad_de_muertes DESC;

/*
4. **Análisis mortalidad materna**

Pregunta: ¿Cuántas muertes relacionadas con embarazo se reportan, y en qué etapas?
*/

SELECT AGE(defuncion.fecha_defuncion,persona.fecha_nacimiento) as edad, persona.escolaridad, durante_embarazo
FROM embarazo
JOIN persona ON persona.id=embarazo.persona_id
JOIN defuncion ON defuncion.persona_id=persona.id
WHERE causado_embarazo ILIKE 'SI' AND durante_embarazo IS NOT NULL AND durante_embarazo NOT LIKE 'NO %'
GROUP BY edad, persona.escolaridad, durante_embarazo
ORDER BY edad DESC;

/*
5. **Análisis entre atención médica y tipo de muerte**

Pregunta: ¿Las personas que no recibieron atención médica presentan más muertes?
*/

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



/*
6. **Análisis entre municipio residencia y municipio ocurrencia**

Pregunta: ¿Cuántas personas fallecieron en el mismo municipio de la Ciudad de México en el que residían?
*/

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
