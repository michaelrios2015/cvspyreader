import csv

with open('data\platmonPPS_202110.txt', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter='|'))
    # reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []

    # for row in reader:
    #     head.append([row["Prefix"], row["Security Identifier"], row["CUSIP"]])
    #     body.append([row["CUSIP"], row["Security Factor"], row["WA Issuance Interest Rate"], row["WA Loan Age"], row["WA Issuance Remaining Months to Maturity"]])

    i = 0

    for x in range(3):
        if data[x][0] == 'PS':
            # print(data[x])
            head.append([data[x][1], data[x][2], data[x][4], data[x][5], data[x][7], data[x][8]])
        # if i == 2:
        #     break    
            body.append( [data[x][1], data[x][6], data[x][9], data[x][10], data[x][16], data[x][17], data[x][18], '', '', '', '2021-12-01'], '', '', '', '', '', '', '')

# cusip: csvMonthPlatinums[i][1], name: csvMonthPlatinums[i][2], type: csvMonthPlatinums[i][4], issuedate: csvMonthPlatinums[i][5], maturitydate: csvMonthPlatinums[i][7], originalface: csvMonthPlatinums[i][8]})

# cusip: csvPlatinumMonthBodies[i][1], interestrate: csvPlatinumMonthBodies[i][6], remainingbalance: csvPlatinumMonthBodies[i][9], 
#           factor: csvPlatinumMonthBodies[i][10], gwac: csvPlatinumMonthBodies[i][16], wam: csvPlatinumMonthBodies[i][17], wala: csvPlatinumMonthBodies[i][18], indicator: null, istbaelig: null,  cpr: null, date


# so seems to work would put in a temp table then switch to 
print(body)

# headfields = ["Prefix", "Security Identifier", "CUSIP"]

# with open('data/head.cvs', 'w', newline='') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(headfields) 
        
#     # writing the data rows 
#     csvwriter.writerows(head)



# bodyFields = ["CUSIP", "Security Factor", "WA Issuance Interest Rate", "WA Loan Age", "WA Issuance Remaining Months to Maturity"]

# with open('data/body.cvs', 'w', newline='') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(bodyFields) 
        
#     # writing the data rows 
#     csvwriter.writerows(body)







