import csv
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder",
    user="postgres",
    password="JerryPine",
    host="localhost",
    port="5432",
)


# so this seems to work
data_path = "data\input\CMOS_2023-08-01.csv"

date = data_path[-14:-4]

# print(date)

# file path needs to be changed
with open(data_path, newline="") as csvfile:
    data = list(csv.reader(csvfile, delimiter=","))
    # reader = csv.DictReader(csvfile, delimiter='|')

    input = []

    for row in data:
        cmo = row[4][5:] + "-" + row[3][1:]
        # print(row[4][5:] + '-' + row[3][1:])
        # print(row[3][1:])
        # print(row)
        input.append([cmo, row[0], row[2], date])
        # break


# print(input)
fields = ["cmo", "cusip", "faceincmo", "date"]

with open("data/output/cmos.cvs", "w", newline="") as csvfile:
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
sql = """
create temporary table cmostemp (cmo varchar, cusip varchar, faceincmo double precision, date date);
"""
cursor.execute(sql)

# read in cvs into temp table
csv_file_name = "data\output\cmos.cvs"
sql = "COPY cmostemp FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

# transfer to actaul table and drop temp table
sql = """
INSERT INTO ofincmos(cmo, cusip, faceincmo, date)
SELECT cmo, cusip, faceincmo, date
FROM cmostemp;

DROP TABLE cmostemp;
"""

cursor.execute(sql)

# we have some duplicate cmos that need to be combined
sql = (
    """
SELECT cmo, cusip, date, sum(faceincmo) AS ofincmo
INTO TEMP TABLE tempuniqueofincmos
FROM ofincmos
GROUP BY cmo, cusip, date;


--puts my temp table into a real table
INSERT INTO uniqueofincmos (cmo, cusip, date, faceincmo)
SELECT cmo, cusip, date, ofincmo
FROM tempuniqueofincmos
WHERE tempuniqueofincmos.date = """
    + "'"
    + date
    + "'"
    + """;

DROP TABLE tempuniqueofincmos;

"""
)

cursor.execute(sql)

# just puting the cmos into the cmo table we will show
sql = (
    """
INSERT INTO cmos (cmo, date)
SELECT DISTINCT cmo, TO_DATE("""
    + "'"
    + date
    + "'"
    + """,'YYYY-MM-DD')
FROM uniqueofincmos
WHERE uniqueofincmos.collapsed is null
AND uniqueofincmos.date <= """
    + "'"
    + date
    + "'"
    + """;

"""
)

cursor.execute(sql)


sql = """
SELECT * FROM uniqueofincmos order by date desc limit 5;
"""
cursor.execute(sql)
records = cursor.fetchall()

for row in records:
    for column in row:
        print(column, end=", ")
    print()


sql = (
    """
SELECT COUNT(*) FROM uniqueofincmos where date =  """
    + "'"
    + date
    + "'"
    + """;
"""
)
cursor.execute(sql)
records = cursor.fetchall()

print("\ncount = ", records[0][0])

conn.commit()
conn.close()
