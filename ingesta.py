import os
import pandas as pd
import pymysql
import boto3

# Conexión a MySQL
conn = pymysql.connect(
    host='mysql-simulada',     # o la IP interna si es un contenedor
    port=3306,
    user='root',
    password='utec',
    database='empleados'
)

# Leer tabla
df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

# Guardar CSV
csv_file = "data.csv"
df.to_csv(csv_file, index=False)

# Subir a S3
s3 = boto3.client('s3')

bucket = 's6-ingesta02'
s3.upload_file(csv_file, bucket, csv_file)

print("Ingesta completada")
