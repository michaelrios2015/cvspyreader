import csv

# staring out with platinums because they seem pretty easy...
# 
# platinumbodies and poolbodies whould be reall easy it's just about making a csv file that follows the tables for each
# 
# platinums is pretty much teh same but I need to write some psql that will put the data into a temp table and do nothing
# on a conflict or just update, which is also fine since the information will not have changed.. i wonder what happen to the 
# old ones I feel like I probably could just delete and reload the data each month.. no real reason though

# so this seems to work

# file path needs to be changed
with open('data\input\platmonPPS_202110.txt', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter='|'))
    # reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []

    i = 0

    for row in data:
        if row[0] == 'PS':
            head.append([row[1], row[2], row[4], row[5], row[7], row[8]])

            # date need to be changed
            body.append( [row[1], row[6], row[9], row[10], row[16], row[17], row[18], '', '', '', '2021-12-01', '', '', '', '', '', '', ''])

# cusip: csvMonthPlatinums[i][1], name: csvMonthPlatinums[i][2], type: csvMonthPlatinums[i][4], issuedate: csvMonthPlatinums[i][5], maturitydate: csvMonthPlatinums[i][7], originalface: csvMonthPlatinums[i][8]})

# cusip: csvPlatinumMonthBodies[i][1], interestrate: csvPlatinumMonthBodies[i][6], remainingbalance: csvPlatinumMonthBodies[i][9], 
# factor: csvPlatinumMonthBodies[i][10], gwac: csvPlatinumMonthBodies[i][16], wam: csvPlatinumMonthBodies[i][17], wala: csvPlatinumMonthBodies[i][18], indicator: null, istbaelig: null,  cpr: null, date


# so seems to work would put in a temp table then switch to 



with open('data/input/fedHoldings2022-01-05.csv', newline='') as csvfile:
    # data = list(csv.reader(csvfile, delimiter='|'))
    reader = csv.DictReader(csvfile, delimiter=',')

    output = []

    # for row in reader:
    #     head.append([row["Prefix"], row["Security Identifier"], row["CUSIP"]])
    #     body.append([row["CUSIP"], row["Security Factor"], row["WA Issuance Interest Rate"], row["WA Loan Age"], row["WA Issuance Remaining Months to Maturity"]])

    for row in reader:
        isaggregated = False
        # print(row)
        
        if row["is Aggregated"] == 'Y':
            isaggregated = True        
        output.append([row["As Of Date"], eval(row["CUSIP"]), row["Current Face Value"], isaggregated])
        # print(output)
        # break   



print(output[0])


print(body[0])


# headfields = [ "cusip", "name", "type", "issuedate", "maturitydate", "originalface"]

# with open('data/platinums.cvs', 'w', newline='') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(headfields) 
        
#     # writing the data rows 
#     csvwriter.writerows(head)


# # print(body)

# bodyFields = ["cusip", "interestrate", "remainingbalance", "factor" ,"gwac", "wam", "wala", "indicator", "istbaelig", "cpr", "date", "cdr", "predictedcpr", "predictedcprnext", "predictedcdr", "predictedcdrnext", "cprnext", "cdrnext"]

# with open('data/platinumbodies.cvs', 'w', newline='') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(bodyFields) 
        
#     # writing the data rows 
#     csvwriter.writerows(body)







