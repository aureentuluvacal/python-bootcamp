from csv import DictReader

with open("books.csv") as file:
  csv_reader = DictReader(file)

  for row in csv_reader:
    print(row['Title'])