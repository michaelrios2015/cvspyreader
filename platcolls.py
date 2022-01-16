import csv
import sys

#  So I seem to be able to read in the platcolls just fine
# but inserting it might be a bit trickier.. that will be seen in laoding scripts section


file = 'data\input\platcoll_202112.txt'


# Using readlines()
file1 = open(file, 'r')
Lines = file1.readlines()

data = []

# date = (sys.argv[1])[-10:-6] + '-' + (sys.argv[1])[-6:-4] + '-01'
date = file[-10:-6] + '-' + file[-6:-4] + '-01'

# print(date)

i = 0

for row in Lines:
    # print(row)
    # print(row[0:9], row[19:25], row[25:26], row[53:68], row[79:80], date)
    data.append([row[0:9], row[19:25], row[25:26],
                row[53:68], row[79:80], date])

    # console.log(csvMonthCollateral[i])
    # const cusip = csvMonthCollateral[i][0].slice(0, 9);
    # const poolname = csvMonthCollateral[i][0].slice(19, 25);
    # const indicator = csvMonthCollateral[i][0].slice(25, 26);
    # const faceinplatinum = csvMonthCollateral[i][0].slice(53, 68);
    # const active = csvMonthCollateral[i][0].slice(79, 80);

# so seems to work would put in a temp table then switch to

fields = ["cusip", "poolname", "indicator", "faceinplatinum", "active", "date"]

with open('data/output/platcolls.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(data)
