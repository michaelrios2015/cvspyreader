import csv
from datetime import datetime
import sys

# staring out with platinums because they seem pretty easy...
# 
# platinumbodies and poolbodies whould be reall easy it's just about making a csv file that follows the tables for each
# 
# platinums is pretty much teh same but I need to write some psql that will put the data into a temp table and do nothing
# on a conflict or just update, which is also fine since the information will not have changed.. i wonder what happen to the 
# old ones I feel like I probably could just delete and reload the data each month.. no real reason though


# print system arguments
print(sys.argv)


# so this seems to work

# file path needs to be changed
with open('data/input/monthlySFPS_202112.txt', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter='|'))
    # reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []


    for row in data:
        if row[0] == 'PS':

            maturitydate = row[7]
            issuedate = row[5]

            # print(issuedate)
            # print(int(issuedate[0:4]))
            # print(int(issuedate[4:6]))
            # print(int(issuedate[6:8]))


            end_date = datetime(int(maturitydate[0:4]),int(maturitydate[4:6]),int(maturitydate[6:8]))
            start_date = datetime(int(issuedate[0:4]),int(issuedate[4:6]),int(issuedate[6:8]))

            num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

            # print(num_months)

            istbaelig = False

            indicator = row[3]
            type = row[4]
            originalface = int(row[8])
            
            if originalface >= 250000 and type == 'SF' and (indicator == 'X' or indicator == 'M') and num_months  >= 336:

                istbaelig = True

            head.append([row[1], row[2], indicator, type, row[5], row[7], originalface, istbaelig ])

# cusip: csvMonthPools[i][1], name: csvMonthPools[i][2], indicator: csvMonthPools[i][3], type: csvMonthPools[i][4]
# issuedate: csvMonthPools[i][5], maturitydate: csvMonthPools[i][7], originalface: csvMonthPools[i][8]


            # DATE NEEDS TO BE CHANGED
            body.append( [row[1], row[6], row[9], row[10], row[17], row[18], row[19], '2021-12-01'] )

# cusip: csvPoolMonthBodies[i][1], interestRate: csvPoolMonthBodies[i][6], remainingBalance: csvPoolMonthBodies[i][9], 
# factor: csvPoolMonthBodies[i][10], GWAC: csvPoolMonthBodies[i][17], WAM: csvPoolMonthBodies[i][18], WALA: csvPoolMonthBodies[i][19], date})


headfields = [ "cusip", "name", "indicator", "type", "issuedate", "maturitydate", "originalface", "istbaelig" ]

with open('data/output/pools.cvs', 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(headfields) 
        
    # writing the data rows 
    csvwriter.writerows(head)


# print(body)

bodyFields = ["cusip", "interestrate", "remainingbalance", "factor" ,"gwac", "wam", "wala", "date"]

with open('data/output/poolbodies.cvs', 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(bodyFields) 
        
    # writing the data rows 
    csvwriter.writerows(body)







