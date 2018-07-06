# no order, no duplicates, like mathematical sets, cannot access items via index
s = {1, 4, 5}

print(1 in s)

for num in s: 
  print(num)

cities = { "Chicago", "Chicago", "Indianapolis", "Columbus", "St. Louis", "Columbus"}

print(set(cities))