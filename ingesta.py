import pandas as pd
import pymysql
import boto3
import os

conn = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    port=int(os.environ.get('MYSQL_PORT', 3306)),
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

csv_file = "data.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client('s3')
s3.upload_file(csv_file, "s6-ingesta02", csv_file)

print("Ingesta completa")