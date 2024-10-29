import csv
with open('output.csv', mode='w') as file_output:
	with open('file.csv') as file:
		dictReader = csv.DictReader(file, delimiter=',', quotechar='"')
		dictWriter = csv.DictWriter(file_output, delimiter=',',quotechar='"', fieldnames=dictReader.fieldnames)
		
		for line in dictReader:
			dictWriter.writerow(line)

