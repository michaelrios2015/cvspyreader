import csv
import psycopg2

# connects to database
conn = psycopg2.connect(
    database="cmos_builder", user='postgres',
    password='JerryPine', host='localhost', port='5432'
)


# reads in ginnie files take what i need and orders it
# file path needs to be changed
with open('data\input\platmonPPS_202112.txt', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter='|'))
    # reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []

    i = 0

    for row in data:
        if row[0] == 'PS':
            head.append([row[1], row[2], row[4], row[5], row[7], row[8]])

            # date need to be changed
            body.append([row[1], row[6], row[9], row[10], row[16], row[17],
                        row[18], '', '', '', '2021-12-01', '', '', '', '', '', '', ''])


# spits out cvs files
headfields = ["cusip", "name", "type",
              "issuedate", "maturitydate", "originalface"]

with open('data/output/platinums.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(headfields)

    # writing the data rows
    csvwriter.writerows(head)


# print(body)

bodyFields = ["cusip", "interestrate", "remainingbalance", "factor", "gwac", "wam", "wala", "indicator", "istbaelig",
              "cpr", "date", "cdr", "predictedcpr", "predictedcprnext", "predictedcdr", "predictedcdrnext", "cprnext", "cdrnext"]

with open('data/output/platinumbodies.cvs', 'w', newline='') as csvfile:
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

csv_file_name = 'data\output\platinumbodies.cvs'
sql = "COPY platinumbodies FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

sql = '''

create temporary table platinumstemp (cusip varchar, name varchar , type varchar, issuedate integer, maturitydate integer, originalface double precision);

'''
cursor.execute(sql)

# maybe there is an easier way to do this but I don't know it
csv_file_name = 'data\output\platinums.cvs'
sql = "COPY platinumstemp FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))


sql = '''

INSERT INTO platinums (cusip, name, type, issuedate, maturitydate, originalface)
SELECT cusip, name, type, issuedate, maturitydate, originalface
FROM platinumstemp
ON CONFLICT (cusip)
DO NOTHING;

DROP TABLE platinumstemp;


'''

cursor.execute(sql)

# records = cursor.fetchall()

# print(records)

conn.commit()
conn.close()


# this seems to work not sure if i really need to make the cvs file... but well i know how to do it this way so
