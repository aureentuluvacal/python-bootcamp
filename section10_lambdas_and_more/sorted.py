nums = [17, 55, 2991, 23, 10]
print(sorted(nums))

print(sorted(nums, reverse=True))

users = [
  { "name": "Irma" },
  { "name": "Caryssa" },
  { "name": "Lolita" }
]

print(sorted(users, key=lambda user: user["name"]))