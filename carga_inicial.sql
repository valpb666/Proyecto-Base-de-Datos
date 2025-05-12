/* ****************************** */
/*          CARGA INICIAL         */
/* ****************************** */

--- PASOS EN CONSOLA ---

	CREATE DATABASE proyecto;

	\c proyecto;

	SET CLIENT_ENCODING TO 'UTF8';

--- Carga de base de datos en Table Plus ---

--Primero conectar a la base de proyecto

CREATE TABLE staging(
		id BIGSERIAL PRIMARY KEY,
		-- Este atributo nos servira para pasar los datos posteriormente
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

/*

--- PASOS EN CONSOLA ---
	
	\copy staging(sexo, fecha_nacimiento, nacionalidad, lengua_indigena, estado_civil, entidad_residencia, municipio_residencia, escolaridad, ocupacion, afiliacion_medica, fecha_defuncion1, hora_defuncion, lugar_defuncion, entidad_defuncion, alcaldia, atencion_medica, necropsia, causa_defuncion, durante_embarazo, causado_embarazo, complicacion_embarazo, muerte_accidental_violenta, tipo_evento, en_trabajo, sitio_lesion, municipio_ocurrencia, fecha_defuncion, edad) FROM 'ubicación del archivo.csv' WITH (FORMAT CSV, HEADER true, DELIMITER ',', NULL 'NA');
*/
