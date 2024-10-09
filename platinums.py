import csv
import psycopg2
from zipfile import ZipFile
import io
import requests
import os


# connects to database
conn = psycopg2.connect(
    database="cmos_builder",
    user="postgres",
    password="JerryPine",
    host="localhost",
    port="5432",
)

# change these two monthly
data_url = "https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/platmonPPS_202408.zip"


data_path = "data\input\platmonPPS_202408.txt"

#########################################################

# r = requests.get(url=data_url)  # create HTTP response object

# print(r.headers)


# print(r)
# # extract file
# z = ZipFile(io.BytesIO(r.content))
# # send it to data
# z.extractall("data\input")


# file_name, file_extension = os.path.splitext(r.content)

# print(file_name)
# print(file_extension)


# with ZipFile(io.BytesIO(r.content)) as z:
#     z.extractall("data\input")

# # the rest is the same
date = data_path[-10:-6] + "-" + data_path[-6:-4] + "-01"

# reads in ginnie files take what i need and orders it
with open(data_path, newline="") as csvfile:
    data = list(csv.reader(csvfile, delimiter="|"))
    # reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []

    # i = 0

    for row in data:
        if row[0] == "PS":
            head.append([row[1], row[2], row[4], row[5], row[7], row[8]])

            body.append(
                [
                    row[1],
                    row[6],
                    row[9],
                    row[10],
                    row[16],
                    row[17],
                    row[18],
                    "",
                    "",
                    "",
                    date,
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ]
            )


# spits out cvs files
headfields = ["cusip", "name", "type", "issuedate", "maturitydate", "originalface"]

with open("data/output/platinums.cvs", "w", newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(headfields)

    # writing the data rows
    csvwriter.writerows(head)


# print(body)

bodyFields = [
    "cusip",
    "interestrate",
    "remainingbalance",
    "factor",
    "gwac",
    "wam",
    "wala",
    "indicator",
    "istbaelig",
    "cpr",
    "date",
    "cdr",
    "predictedcpr",
    "predictedcprnext",
    "predictedcdr",
    "predictedcdrnext",
    "cprnext",
    "cdrnext",
]


with open("data/output/platinumbodies.cvs", "w", newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(bodyFields)

    # writing the data rows
    csvwriter.writerows(body)


# connecting to database
# probably don't need to
conn.autocommit = True
cursor = conn.cursor()

# should be fine
# "'" + '2022-03-30' + "'"
sql = (
    """
DELETE FROM platinumbodies
WHERE date = """
    + "'"
    + date
    + "'"
    + """;
"""
)
cursor.execute(sql)

csv_file_name = "data\output\platinumbodies.cvs"
sql = "COPY platinumbodies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

sql = """

create temporary table platinumstemp (cusip varchar, name varchar , type varchar, issuedate integer, maturitydate integer, originalface double precision);

"""
cursor.execute(sql)

# maybe there is an easier way to do this but I don't know it
csv_file_name = "data\output\platinums.cvs"
sql = "COPY platinumstemp FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))


sql = """
INSERT INTO platinums (cusip, name, type, issuedate, maturitydate, originalface)
SELECT cusip, name, type, issuedate, maturitydate, originalface
FROM platinumstemp
ON CONFLICT (cusip)
DO NOTHING;

DROP TABLE platinumstemp;
"""

cursor.execute(sql)

sql = """
SELECT * FROM platinumbodies order by date desc limit 5;
"""
cursor.execute(sql)
records = cursor.fetchall()

for row in records:
    for column in row:
        print(column, end=", ")
    print()


sql = (
    """
SELECT COUNT(*) FROM platinumbodies where date =  """
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


# this seems to work not sure if i really need to make the cvs file... but well i know how to do it this way so
