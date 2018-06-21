from urllib.request import Request, urlopen
import csv, io

url = "https://storage.data.gov.sg/public-transport-utilisation-average-public-transport-ridership/resources/public-transport-utilisation-average-public-transport-ridership-2018-03-15T07-17-43Z.csv"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
con = urlopen(req)
rows = csv.DictReader(io.TextIOWrapper(con))
for row in rows:
    if row['type_of_public_transport']== "MRT":
        print(row['year'], row['average_ridership'] )
        #print (dict(row))

con.close()
