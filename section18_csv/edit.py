from csv import reader, writer

with open('books.csv') as file:
  csv_reader = reader(file)
  books = [[s.upper() for s in row] for row in csv_reader]
  for row in books:
    print(row)

with open('screaming_books.csv', 'w') as file:
  csv_writer = writer(file)

  for book in books:
    csv_writer.writerow(book)
