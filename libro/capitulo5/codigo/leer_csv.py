import csv
with open('file.csv') as file:
   reader = csv.reader(file, delimiter=',', quotechar='"')
   print("header: " + str(reader.__next__()))
   for line in reader:
        print(line)

