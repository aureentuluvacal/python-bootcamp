dog = {
  "name": "Lolita",
  "age": 10,
  "color": "blonde"
}

for key, value in dog.items():
  print(f"{key}: {value}")

for value in dog.values():
  print(value)

for key in dog.keys():
  print(key)