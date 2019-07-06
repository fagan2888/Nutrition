import pandas as pd
import sqlite3 as db
import csv

conn = db.connect('Instacart.db')
c = conn.cursor()

df = pd.read_csv(r'..\\Instacart\\products.csv')
df.to_sql(name='product_id', con=conn, if_exists='append', index = False)
#print (df)

#code to read db:

pd.read_sql("select * from product_id", conn)