import csv

with open("name.csv", mode='a') as csv_file:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'name': 'John Smith', 'age': 25})
    writer.writerow({'name': 'Jane Smith', 'age': 30})
    