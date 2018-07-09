nums = [39, 291, 23, 15, 11, 9]

doubles = list(map(lambda x: x*2, nums))

print(doubles)

people = ["Caryssa", "Irma", "Lolita"]
peeps = map(lambda name: name.upper(), people)
print(list(peeps))