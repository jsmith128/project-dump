import csv
def fitem(item):
    item=item.strip()
    try:
        item=float(item)
    except ValueError:
        pass
    return item        

with open('/home/jon/Desktop/python/urlLister/domains.csv', 'r') as csvIn:
    reader=csv.DictReader(csvIn)
    data={k.strip():[fitem(v)] for k,v in reader.__next__().items()}
    for line in reader:
        for k,v in line.items():
            k=k.strip()
            data[k].append(fitem(v))

print(data)