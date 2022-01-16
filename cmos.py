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
with open('data\input\CMOS_2021_12.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    # reader = csv.DictReader(csvfile, delimiter='|')

    input = []

    for row in data:

        cmo = row[4][5:] + '-' + row[3][1:]
        # print(row[4][5:] + '-' + row[3][1:])
        # print(row[3][1:])
        # print(row)
        input.append([cmo, row[0], row[2], '2021-12-01'])
        # break


# print(input)
fields = ["cmo", "cusip", "faceincmo", "date"]

with open('data/output/cmos.cvs', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(input)
