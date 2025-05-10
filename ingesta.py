import os
import pandas as pd
import pymysql
import boto3

# 1) Conexión a MySQL (lee de variables de entorno)
conn = pymysql.connect(
    host     = os.environ.get('MYSQL_HOST', 'localhost'),
    port     = int(os.environ.get('MYSQL_PORT', 3306)),
    user     = os.environ.get('MYSQL_USER', 'root'),
    password = os.environ.get('MYSQL_PASSWORD', ''),
    database = os.environ.get('MYSQL_DATABASE', '')
)

# 2) Leer todos los registros de la tabla
table = os.environ.get('MYSQL_TABLE', '')
df = pd.read_sql(f"SELECT * FROM {table};", conn)
conn.close()

# 3) Volcar a CSV
output_file = os.environ.get('OUTPUT_FILE', 'data.csv')
df.to_csv(output_file, index=False, encoding='utf-8')

# 4) Subir a S3
s3 = boto3.client('s3')
bucket = os.environ.get('S3_BUCKET')
s3.upload_file(output_file, bucket, output_file)

print(f"Ingesta completada: `{output_file}` subido a s3://{bucket}/")
