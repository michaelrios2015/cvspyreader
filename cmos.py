import csv
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)


# so this seems to work
data_path = 'data\input\CMOS_2023-01-01.csv'

date = data_path[-14:-4]

# print(date)

# file path needs to be changed
with open(data_path, newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    # reader = csv.DictReader(csvfile, delimiter='|')

    input = []

    for row in data:

        cmo = row[4][5:] + '-' + row[3][1:]
        # print(row[4][5:] + '-' + row[3][1:])
        # print(row[3][1:])
        # print(row)
        input.append([cmo, row[0], row[2], date])
        # break


# print(input)
fields = ["cmo", "cusip", "faceincmo", "date"]

with open('data/output/cmos.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(input)


# connecting to database
# probably don't need to
conn.autocommit = True
cursor = conn.cursor()

# create temp table
sql = '''
create temporary table cmostemp (cmo varchar, cusip varchar, faceincmo double precision, date date);
'''
cursor.execute(sql)

# read in cvs into temp table
csv_file_name = 'data\output\cmos.cvs'
sql = "COPY cmostemp FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

# transfer to actaul table and drop temp table
sql = '''
INSERT INTO ofincmos(cmo, cusip, faceincmo, date)
SELECT cmo, cusip, faceincmo, date
FROM cmostemp;
 
DROP TABLE cmostemp;
'''

cursor.execute(sql)


conn.commit()
conn.close()
