# import urllib.request
# with ('https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/monthlySFPS_202201.zip') as f:
#     html = f.read().decode('utf-8')

# print(f)

import pandas as pd

# data = pd.read_csv(
#     'https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/monthlySFPS_202201.zip', delimiter='|')


# data = pd.read_csv(
#     'https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/monthlySFPS_202201.zip', auth=('dar27@columbia.edu', 'bank street'), verify=False)

data = pd.read_csv(
    'https://dar27@columbia.edu:bankstreet@bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/monthlySFPS_202201.zip', delimiter='|')


print(data)

# import csv
# from datetime import datetime
# import psycopg2

# # connects to database
# conn = psycopg2.connect(
#     database="cmos_builder", user='postgres',
#     password='JerryPine', host='localhost', port='5432'
# )

# # change this monthly
# data_path = 'data/input/monthlySFPS_202201.txt'

# date = data_path[-10:-6] + "-" + data_path[-6:-4] + "-01"

# with open(data_path, newline='') as csvfile:
#     data = list(csv.reader(csvfile, delimiter='|'))
#     # reader = csv.DictReader(csvfile, delimiter='|')

#     head = []
#     body = []

#     for row in data:
#         if row[0] == 'PS':

#             maturitydate = row[7]
#             issuedate = row[5]

#             # print(issuedate)
#             # print(int(issuedate[0:4]))
#             # print(int(issuedate[4:6]))
#             # print(int(issuedate[6:8]))

#             end_date = datetime(int(maturitydate[0:4]), int(
#                 maturitydate[4:6]), int(maturitydate[6:8]))
#             start_date = datetime(int(issuedate[0:4]), int(
#                 issuedate[4:6]), int(issuedate[6:8]))

#             num_months = (end_date.year - start_date.year) * \
#                 12 + (end_date.month - start_date.month)

#             istbaelig = False

#             indicator = row[3]
#             type = row[4]
#             originalface = int(row[8])

#             if originalface >= 250000 and type == 'SF' and (indicator == 'X' or indicator == 'M') and num_months >= 336:

#                 istbaelig = True

#             head.append([row[1], row[2], indicator, type,
#                         row[5], row[7], originalface, istbaelig])

#             body.append([row[1], row[6], row[9], row[10],
#                         row[17], row[18], row[19], date])


# headfields = ["cusip", "name", "indicator", "type",
#               "issuedate", "maturitydate", "originalface", "istbaelig"]

# with open('data/output/pools.cvs', 'w', newline='') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(headfields)

#     # writing the data rows
#     csvwriter.writerows(head)


# bodyFields = ["cusip", "interestrate", "remainingbalance",
#               "factor", "gwac", "wam", "wala", "date"]

# with open('data/output/poolbodies.cvs', 'w', newline='') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(bodyFields)

#     # writing the data rows
#     csvwriter.writerows(body)


# # connecting to database
# # what is autocommit
# conn.autocommit = True
# cursor = conn.cursor()

# csv_file_name = 'data\output\poolbodies.cvs'
# sql = "COPY poolbodies FROM STDIN DELIMITER ',' CSV HEADER"
# cursor.copy_expert(sql, open(csv_file_name, "r"))

# sql = '''
# create temporary table poolstemp (cusip varchar, name varchar , indicator varchar, type varchar, issuedate integer, maturitydate integer, originalface double precision, istbaelig boolean);
# '''
# cursor.execute(sql)

# # maybe there is an easier way to do this but I don't know it
# csv_file_name = 'data\output\pools.cvs'
# sql = "COPY poolstemp FROM STDIN DELIMITER ',' CSV HEADER"
# cursor.copy_expert(sql, open(csv_file_name, "r"))


# sql = '''
# INSERT INTO pools (cusip, name, indicator, type, issuedate, maturitydate, originalface, istbaelig)
# SELECT cusip, name, indicator, type, issuedate, maturitydate, originalface, istbaelig
# FROM poolstemp
# ON CONFLICT (cusip)
# DO NOTHING;

# DROP TABLE poolstemp;
# '''

# cursor.execute(sql)


# conn.commit()
# conn.close()
