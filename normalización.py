
-- Entidad: entidad_municipio

CREATE TABLE entidad_municipio (
	id BIGSERIAL PRIMARY KEY,
	entidad VARCHAR(200) NOT NULL,
	municipio VARCHAR(100) NOT NULL,
	
	CONSTRAINT pares_unicos UNIQUE(entidad,municipio)
);

INSERT INTO entidad_municipio(municipio, entidad)
SELECT DISTINCT municipio_residencia, entidad_residencia
FROM staging;

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
	sexo VARCHAR(20) NOT NULL,
	fecha_nacimiento DATE,
	lengua_indigena BOOLEAN,
	estado_civil VARCHAR(50) NOT NULL,
	entidad_residencia VARCHAR(100),
	municipio_residencia VARCHAR(100),
	--Estos atributos residencia son temporales en lo que se ingresan los nuevos ids
	residencia_id BIGINT,
	escolaridad VARCHAR(200) NOT NULL,
	ocupacion VARCHAR(200) NOT NULL,
	afiliacion_medica VARCHAR(200) NOT NULL
);

INSERT INTO persona (id,sexo, fecha_nacimiento, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica)
SELECT id,sexo, fecha_nacimiento,lengua_indigena,estado_civil,entidad_residencia,municipio_residencia,escolaridad,ocupacion,afiliacion_medica
FROM staging;

SELECT setval('public.persona_id_seq', (SELECT MAX(id) FROM persona));

UPDATE persona
SET residencia_id = (
	SELECT id 
	FROM entidad_municipio
	WHERE (entidad_municipio.entidad,entidad_municipio.municipio)=(entidad_residencia, municipio_residencia)
);

ALTER TABLE persona DROP COLUMN entidad_residencia;
ALTER TABLE persona DROP COLUMN municipio_residencia;

ALTER TABLE persona
ALTER COLUMN residencia_id SET NOT NULL,
ALTER COLUMN residencia_id SET DEFAULT 1539, --> Tupla donde la entidad y el municipio no estan especificados
ADD CONSTRAINT fk_entidad_municipio
FOREIGN KEY (residencia_id) REFERENCES entidad_municipio(id) ON DELETE SET DEFAULT;


-- Entidad: Defuncion
CREATE TABLE defuncion (
	id BIGSERIAL PRIMARY KEY,
	persona_id BIGINT UNIQUE NOT NULL CONSTRAINT fk_persona REFERENCES persona(id) ON DELETE CASCADE,
	fecha_defuncion DATE NOT NULL,
	hora_defuncion TIME,
	lugar_defuncion VARCHAR(500) NOT NULL,
	causa_defuncion VARCHAR(500) NOT NULL,
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
ALTER COLUMN alcaldia_defuncion_id SET DEFAULT 1539, --> Tupla donde la entidad y el municipio no estan especificados
ADD CONSTRAINT fk_entidad_municipio
FOREIGN KEY (alcaldia_defuncion_id) REFERENCES entidad_municipio(id) ON DELETE SET DEFAULT;

-- Entidad Embarazo

CREATE TABLE embarazo (
	id BIGSERIAL PRIMARY KEY,
	persona_id BIGINT NOT NULL CONSTRAINT fk_persona REFERENCES persona(id) ON DELETE CASCADE,
	durante_embarazo VARCHAR(500) NOT NULL,
	causado_embarazo VARCHAR(200) NOT NULL,
	complicacion_embarazo VARCHAR(200) NOT NULL
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

DROP TABLE staging;
```
