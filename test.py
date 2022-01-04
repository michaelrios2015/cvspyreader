import csv

with open('data/FNM_MF_202112.txt', newline='') as csvfile:
    # data = list(csv.reader(csvfile, delimiter='|'))
    reader = csv.DictReader(csvfile, delimiter='|')

    head = []
    body = []

    # for row in reader:
    #     head.append([row["Prefix"], row["Security Identifier"], row["CUSIP"]])
    #     body.append([row["CUSIP"], row["Security Factor"], row["WA Issuance Interest Rate"], row["WA Loan Age"], row["WA Issuance Remaining Months to Maturity"]])

    for row in reader:
        print(row)
        break    



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







# 
# looks like we will need this hopefully it is orginal face 
# Issuance Investor Security UPB': '26260359.00'

# november 2023 I think 
# 'Maturity Date': '112023',