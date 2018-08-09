from csv import reader

#reader is an iterator, not a list
with open("books.csv") as file:
  csv_reader = reader(file)

  for row in csv_reader:
    print(row)