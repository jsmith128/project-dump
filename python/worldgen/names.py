import csv

def CSVRead(filename, column):
		output = []
		with open (filename, newline='', encoding='utf-8') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			i=0
			for row in reader:
				i+=1
				if i == 1:
					continue
				output.append( row[column] )
		return output

class Names:
	def __init__(self):
		self.Male = CSVRead('census-male-names.csv', 0)
		self.Female = CSVRead('census-female-names.csv', 0)
		self.Country = CSVRead('countries.csv', 1)
		self.State = CSVRead('states.csv', 1)
		self.City = CSVRead('cities.csv', 1)