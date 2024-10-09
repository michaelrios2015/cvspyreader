import csv
import psycopg2
from zipfile import ZipFile
import io
import requests
from datetime import datetime

# connects to database
conn = psycopg2.connect(
    database="cmos_builder",
    user="postgres",
    password="JerryPine",
    host="localhost",
    port="5432",
)

###########################################################
# change THESE

data_path_2 = "data/input/Mikey_GNMAPoolCohortSMMTest_Oct.txt"

date = "2024-10-01"

# STOP CHANGE
#########################################################


# 1st file

with open(data_path_2, newline="") as csvfile:
    next(csvfile)
    data = list(csv.reader(csvfile, delimiter=","))

    head = []

    for row in data:

        name = row[0]
        fha_cpr = row[1].strip()
        va_cpr = row[2].strip()

        head.append([name, fha_cpr, va_cpr, date])


headfields = ["name", "fha_cpr", "va_cpr", "date"]

with open("data/output/fhava_cpr.cvs", "w", newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(headfields)

    # writing the data rows
    csvwriter.writerows(head)


#################################################################################
# database
##############################################################################

# connecting to database
# what is autocommit
conn.autocommit = True
cursor = conn.cursor()


# read in fhava_cpr's
csv_file_name = "data/output/fhava_cpr.cvs"
sql = "COPY fhava_cpr FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csv_file_name, "r"))

########################################################
# 2nd part
#################################################

print("fhava_cpr")
print("----------------------------------")
sql = """
SELECT * FROM fhava_cpr order by date desc limit 5;
"""
cursor.execute(sql)
records = cursor.fetchall()

for row in records:
    for column in row:
        print(column, end=", ")
    print()


sql = (
    """
SELECT COUNT(*) FROM fhava_cpr where date =  """
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


# # SECON FILE GET LATTER IN MONTH
# ##############################################################################################


# ###########################################################
# # change THESE

# # so not getting the two files at the same time

# data_path = "data/input/Mikey_GNMAStreamliner_Sep24.txt"


# date = "2024-09-01"

# # STOP CHANGE
# #########################################################


# # 1st file read in

# with open(data_path, newline="") as csvfile:
#     next(csvfile)
#     data = list(csv.reader(csvfile, delimiter=","))

#     head = []

#     for row in data:

#         name = row[0]
#         fha = row[1].strip()
#         va = row[2].strip()

#         head.append([name, fha, va, date])


# headfields = ["name", "fha_2", "va_2", "date"]

# # spit out

# with open("data/output/fhava_2.cvs", "w", newline="") as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(headfields)

#     # writing the data rows
#     csvwriter.writerows(head)


# #################################################################################
# # database
# ##############################################################################

# # connecting to database
# # what is autocommit
# conn.autocommit = True
# cursor = conn.cursor()


# # read in fhava_2's 1st one
# csv_file_name = "data/output/fhava_2.cvs"

# sql = "COPY fhava_2 FROM STDIN DELIMITER ',' CSV HEADER"
# cursor.copy_expert(sql, open(csv_file_name, "r"))

# # first part
# print("fhava_2")
# print("----------------------------------")
# sql = """
# SELECT * FROM fhava_2 order by date desc limit 5;
# """
# cursor.execute(sql)
# records = cursor.fetchall()

# for row in records:
#     for column in row:
#         print(column, end=", ")
#     print()


# sql = (
#     """
# SELECT COUNT(*) FROM fhava_2 where date =  """
#     + "'"
#     + date
#     + "'"
#     + """;
# """
# )
# cursor.execute(sql)
# records = cursor.fetchall()

# print("\ncount = ", records[0][0])
