import csv

with open('data/input/fedHoldings2022-01-12.csv', newline='') as csvfile:
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
        output.append([row["As Of Date"], eval(row["CUSIP"]),
                      row["Current Face Value"], isaggregated])
        # print(output)
        # break


fields = ["asofdate", "cusip", "currentfacevalue", "isaggregated"]

with open('data/output/fed.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(output)


#
# looks like we will need this hopefully it is orginal face
# Issuance Investor Security UPB': '26260359.00'

# november 2023 I think
# 'Maturity Date': '112023',
