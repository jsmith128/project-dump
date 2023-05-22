import csv
with open('/home/jon/Desktop/python/urlLister/domains2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Domain'])
        with open('/home/jon/Desktop/python/urlLister/domains.txt', 'a+') as f:
            f.write( row['Domain']+'\n') 