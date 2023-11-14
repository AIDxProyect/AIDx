-- Crea la base de datos EncuestaDB si no existe
CREATE DATABASE IF NOT EXISTS EncuestaDB;

-- Selecciona la base de datos EncuestaDB
USE EncuestaDB;

-- Crear una tabla para las preguntas
CREATE TABLE IF NOT EXISTS Pregunta (
    PreguntaID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    PreguntaTexto VARCHAR(255) NOT NULL
);

-- Insertar preguntas
INSERT INTO Pregunta (PreguntaTexto)
VALUES
    ('¿Cuánto está dispuesta su organización a pagar por recuperar los archivos encriptados en la carpeta files?'),
    ('¿Ha perdido información de vital importancia por el ransomware?'),
    ('¿Cuál es el valor estimado que asigna a los archivos encriptados en la carpeta files?'),
    ('¿Qué tipo de archivos predominan en los datos cifrados?'),
    ('¿La información cifrada se respalda regularmente?'),
    ('¿Has sido previamente víctima de un ataque de ransomware?'),
    ('Si decides no pagar el rescate, ¿tienes un plan alternativo para recuperar la información?'),
    ('¿Cómo te enteraste de la infección por ransomware en tu sistema?'),
    ('¿Cuál es su dirección de correo electrónico?');

-- Crear una tabla para las respuestas de la encuesta
CREATE TABLE IF NOT EXISTS Respuesta (
    RespuestaID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    PreguntaID INT,
    RespuestaTexto VARCHAR(255) NOT NULL,
    FOREIGN KEY (PreguntaID) REFERENCES Pregunta(PreguntaID)
);

-- Insertar respuestas para las preguntas
INSERT INTO Respuesta (PreguntaID, RespuestaTexto)
VALUES
    (1, 'Menos de $50,000 CLP'),
    (1, '$50,000 CLP - $100,000 CLP'),
    (1, '$100,000 CLP - $200,000 CLP'),
    (1, 'Más de $200,000 CLP'),
    (2, 'Sí'),
    (2, 'No'),
    (3, '$10,000 CLP'),
    (3, '$20,000 CLP'),
    (3, '$50,000 CLP'),
    (3, '$100,000 CLP'),
    (3, '$500,000 CLP'),
    (3, '$1,000,000 CLP'),
    (4, 'Documentos personales (p. ej., fotos, diarios)'),
    (4, 'Documentos de trabajo o profesionales'),
    (4, 'Archivos de software o proyectos'),
    (4, 'Información financiera'),
    (4, 'Otros'),
    (5, 'Sí, diariamente'),
    (5, 'Sí, semanalmente'),
    (5, 'Sí, mensualmente'),
    (5, 'No'),
    (5, 'No estoy seguro'),
    (6, 'Sí'),
    (6, 'No'),
    (7, 'Sí'),
    (7, 'No'),
    (8, 'Mensaje en pantalla'),
    (8, 'Fallo al intentar abrir archivos'),
    (8, 'Alerta de software de seguridad'),
    (8, 'Otros');

-- Crear una tabla para almacenar las encuestas
CREATE TABLE IF NOT EXISTS Encuesta (
    EncuestaID INT PRIMARY KEY AUTO_INCREMENT,
    Fecha DATE
);

-- Crear una tabla para vincular encuestas y respuestas
CREATE TABLE IF NOT EXISTS RespuestaEncuesta (
    RespuestaEncuestaID INT AUTO_INCREMENT PRIMARY KEY,
    EncuestaID INT NOT NULL,
    PreguntaID INT NOT NULL,
    RespuestaID INT NOT NULL,
    FOREIGN KEY (EncuestaID) REFERENCES Encuesta(EncuestaID),
    FOREIGN KEY (PreguntaID) REFERENCES Pregunta(PreguntaID),
    FOREIGN KEY (RespuestaID) REFERENCES Respuesta(RespuestaID)
);

-- Crear una tabla para almacenar respuestas individuales de encuestas
CREATE TABLE IF NOT EXISTS EncuestaDetalle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255),
    conocimiento VARCHAR(255),
    experiencia VARCHAR(255),
    comentario TEXT,
    tipo_archivos VARCHAR(255),
    respaldo VARCHAR(255),
    victima_previa VARCHAR(255),
    plan_alternativo VARCHAR(255),
    notificacion_ransomware VARCHAR(255)
);
