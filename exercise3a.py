from urllib.request import Request, urlopen
import csv, io
import xlsxwriter

url = "https://storage.data.gov.sg/public-transport-utilisation-average-public-transport-ridership/resources/public-transport-utilisation-average-public-transport-ridership-2018-03-15T07-17-43Z.csv"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
con = urlopen(req)
rows = csv.DictReader(io.TextIOWrapper(con))

year = ['Year']
mrt = ['MRT']
bus = ['Bus']
taxi = ['Taxi']
lrt = ['LRT']

for row in rows:
    if row['type_of_public_transport'] == 'MRT':
        mrt.append(row['average_ridership'])
        year.append(row['year'])
    elif row['type_of_public_transport'] == 'Bus':
        bus.append(row['average_ridership'])
    elif row['type_of_public_transport'] == 'Taxi':
        taxi.append(row['average_ridership'])
    elif row['type_of_public_transport'] == 'LRT':
        lrt.append(row['average_ridership'])

con.close()

xls_file = "ex3.xlsx"
workbook = xlsxwriter.Workbook(xls_file)
worksheet = workbook.add_worksheet()
worksheet.write_column('A1', year)
worksheet.write_column('B1', mrt)
worksheet.write_column('C1', bus)
worksheet.write_column('D1', taxi)
worksheet.write_column('E1', lrt)
chart = workbook.add_chart({'type':'line'})

chart.add_series({
    'name' : '=Sheet1!$B$1',
    'categories' : '=Sheet1!$A$2:$A$23',
    'values' : '=Sheet1!$B$2:$B$23'
})
worksheet.insert_chart("F1", chart)
workbook.close()