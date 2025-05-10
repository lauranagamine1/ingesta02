import pandas as pd
import pymysql
import boto3

conn = pymysql.connect(
    host='host.docker.internal', 
    port=3307,
    user='root',
    password='1234',
    database='empresa'
)

df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

csv_file = "data.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client('s3')
s3.upload_file(csv_file, "s6-ingesta02", csv_file)

print("Ingesta completa")