import csv
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)

# UPDATE CURRENT MONTH AND FED DATE the rest should be good

currentmonth = "'" + '2022-02-01' + "'"
feddate = "'" + '2022-03-30' + "'"

# connecting to database
# probably don't need to
conn.autocommit = True
cursor = conn.cursor()

sql = '''

Call processdataforweb(''' + currentmonth + ''', ''' + feddate + ''');

'''

# print(sql)

cursor.execute(sql)

conn.commit()
conn.close()


conn = psycopg2.connect(
    database="cmos", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = ''' TRUNCATE ginnies; '''
cursor.execute(sql)


csv_file_name = 'C:/Users/Public/ginnieplatswithcurrfloatM'
sql = "COPY ginnies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

csv_file_name = 'C:/Users/Public/ginnieplatswithcurrfloatX'
sql = "COPY ginnies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

csv_file_name = 'C:/Users/Public/poolswithcurrfloatM'
sql = "COPY ginnies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

csv_file_name = 'C:/Users/Public/poolswithcurrfloatX'
sql = "COPY ginnies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))


conn.commit()
conn.close()


# this seems to work not sure if i really need to make the cvs file... but well i know how to do it this way so
