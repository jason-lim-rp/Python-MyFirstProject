from urllib.request import Request, urlopen
import csv, io

url = "https://storage.data.gov.sg/public-transport-utilisation-average-public-transport-ridership/resources/public-transport-utilisation-average-public-transport-ridership-2018-03-15T07-17-43Z.csv"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
con = urlopen(req)
rows = csv.reader(io.TextIOWrapper(con))
for row in rows:
    print(row)
con.close()


'''
    
rows = csv.DictReader(io.TextIOWrapper(con))
for row in rows:
    print(dict(row))
    

rows = csv.DictReader(io.TextIOWrapper(con))
for row in rows:
    if int(row['year']) > 2010:
        print(row['year'])
    else:
        print ("skipping", row['year'])
        
'''