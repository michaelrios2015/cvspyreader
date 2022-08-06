import csv
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)

# change this weekly
data_path = 'data/input/fedHoldings2022-08-03.csv'

with open(data_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    output = []

    for row in reader:
        isaggregated = False

        if row["is Aggregated"] == 'Y':
            isaggregated = True
        output.append([row["As Of Date"], eval(row["CUSIP"]),
                      row["Current Face Value"], isaggregated])

fields = ["asofdate", "cusip", "currentfacevalue", "isaggregated"]

with open('data/output/fed.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(output)

conn.autocommit = True
cursor = conn.cursor()

csv_file_name = 'data/output/fed.cvs'
sql = "COPY fedholdings FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))


conn.commit()
conn.close()


# \COPY fedholdings FROM 'C:\Users\micha\cvsPyReaders\data\output\fed.cvs' DELIMITER ','  CSV HEADER;


#
# looks like we will need this hopefully it is orginal face
# Issuance Investor Security UPB': '26260359.00'

# november 2023 I think
# 'Maturity Date': '112023',
