# no order, no duplicates, like mathematical sets, cannot access items via index
s = {1, 4, 5}

print(1 in s)

for num in s: 
  print(num)

cities = { "Chicago", "Chicago", "Indianapolis", "Columbus", "St. Louis", "Columbus"}

print(set(cities))

cities.add("New York")
cities.remove("St. Louis")
cities.discard("Oslo")

more_cities = cities.copy()
more_cities.clear()

more_cities = { "Chicago", "Terre Haute", "Miami" }

print(cities | more_cities)
print(cities & more_cities)

# Find a union
