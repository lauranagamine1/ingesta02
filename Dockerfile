FROM python:3-slim

# Crear y moverse al directorio de trabajo
WORKDIR /programas/ingesta

# Instalar dependencias necesarias
RUN pip3 install --no-cache-dir pandas pymysql boto3

# Copiar todos los archivos del proyecto al contenedor
COPY . .

# Ejecutar el script
CMD ["python3", "ingesta.py"]
