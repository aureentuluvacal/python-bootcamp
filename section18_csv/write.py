from csv import writer

with open('pets.csv', 'w') as file:
  csv_writer = writer(file)
  csv_writer.writerow(['Name', 'Species'])
  csv_writer.writerow(['Schnookums', 'cat'])
  csv_writer.writerow(['Lolita', 'dog'])