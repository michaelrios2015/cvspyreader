import csv
from zipfile import ZipFile
import io
import requests
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder",
    user="postgres",
    password="JerryPine",
    host="localhost",
    port="5432",
)

# should be what I need


# change this weekly

date = "2024-10-02"

data_url = (
    "https://markets.newyorkfed.org/api/soma/agency/get/mbs/asof/" + date + ".csv"
)

data_path = "data/input/fedHoldings" + date + ".csv"


r = requests.get(data_url)  # create HTTP response object

with open("data/input/fedHoldings" + date + ".csv", "w") as f:
    f.write(r.text)

###########################################################################


with open(data_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")

    output = []

    for row in reader:
        isaggregated = False

        if row["is Aggregated"] == "Y":
            isaggregated = True
        output.append(
            [
                row["As Of Date"],
                eval(row["CUSIP"]),
                row["Current Face Value"],
                isaggregated,
            ]
        )

fields = ["asofdate", "cusip", "currentfacevalue", "isaggregated"]

with open("data/output/fed.cvs", "w", newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(output)

conn.autocommit = True
cursor = conn.cursor()

csv_file_name = "data/output/fed.cvs"
sql = "COPY fedholdings FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))


sql = """
SELECT * FROM fedholdings order by asofdate desc limit 5;
"""
cursor.execute(sql)
records = cursor.fetchall()

for row in records:
    for column in row:
        print(column, end=", ")
    print()


sql = (
    """
SELECT COUNT(*) FROM fedholdings where asofdate =  """
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


# \COPY fedholdings FROM 'C:\Users\micha\cvsPyReaders\data\output\fed.cvs' DELIMITER ','  CSV HEADER;


#
# looks like we will need this hopefully it is orginal face
# Issuance Investor Security UPB': '26260359.00'

# november 2023 I think
# 'Maturity Date': '112023',
