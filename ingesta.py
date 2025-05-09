import boto3
import pandas as pd
import pymysql

nombreBucket = "s6-ingesta02"

conn = pymysql.connect(
    host='host.docker.internal', 
    port=3307,
    user='root',
    password='1234',
    database='empleados'
)

df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

# Guardar como CSV
csv_file = "data.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client('s3')
response = s3.upload_file(csv_file, nombreBucket, csv_file)

print("Ingesta completada desde MYSQL")
