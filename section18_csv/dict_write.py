from csv import DictWriter

with open("example.csv", "w") as file:
  headers = ["Name", "Age"]
  csv_writer = DictWriter(file, fieldnames=headers)
  csv_writer.writeheader()
  csv_writer.writerow({
    "Name": "Horace", 
    "Age": "49"
  })
