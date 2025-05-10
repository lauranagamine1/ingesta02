USE empresa;

CREATE TABLE IF NOT EXISTS empleados (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL
);

INSERT INTO empleados (nombre, correo) VALUES
  ('Valeria Núñez', 'valeria.nunez@correo.com'),
  ('Jorge Ramírez', 'jorge.ramirez@correo.com'),
  ('Camila Paredes', 'camila.paredes@correo.com');
