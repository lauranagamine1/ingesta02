import os
import pandas as pd
import pymysql
import boto3

# Usar variables de entorno con valores por defecto
conn = pymysql.connect(
    host=os.environ.get('MYSQL_HOST', 'localhost'),
    port=int(os.environ.get('MYSQL_PORT', 3306)),
    user=os.environ.get('MYSQL_USER', 'root'),
    password=os.environ.get('MYSQL_PASSWORD', 'utec'),
    database=os.environ.get('MYSQL_DATABASE', 'empresa')
)

df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

csv_file = "data.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client('s3')
bucket = os.environ.get('S3_BUCKET', 's6-ingesta02')
s3.upload_file(csv_file, bucket, csv_file)

print("Ingesta completada")
