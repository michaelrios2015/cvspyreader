import psycopg2

conn = psycopg2.connect(
    database="cmos_builder", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''SELECT * FROM platinums limit 1;'''

cursor.execute(sql)

records = cursor.fetchall()

print(records)

conn.commit()
conn.close()
