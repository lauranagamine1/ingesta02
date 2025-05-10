import os
import pandas as pd
import pymysql
import boto3

# 1) Conexión a MySQL leyendo de variables de entorno
conn = pymysql.connect(
    host     = os.environ.get('MYSQL_HOST', 'mysql-simulada'),
    port     = int(os.environ.get('MYSQL_PORT', 3306)),
    user     = os.environ.get('MYSQL_USER', 'root'),
    password = os.environ.get('MYSQL_PASSWORD', 'utec'),
    database = os.environ.get('MYSQL_DATABASE', 'empresa')
)

# 2) Leer tabla
table = os.environ.get('MYSQL_TABLE', 'empleados')
df = pd.read_sql(f"SELECT * FROM {table};", conn)
conn.close()

# 3) Guardar CSV
output_file = os.environ.get('OUTPUT_FILE', 'data.csv')
df.to_csv(output_file, index=False)

# 4) Subir a S3
s3       = boto3.client('s3')
bucket   = os.environ['S3_BUCKET']   # obligatorio
s3.upload_file(output_file, bucket, output_file)

print(f"Ingesta completada: `{output_file}` → s3://{bucket}/")
