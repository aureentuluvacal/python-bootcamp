nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

people = ["Caryssa", "Irma", "Lolita"]
fav_people = list(map(lambda name: f"Your favorite person is {name}", filter(lambda name: len(name) < 5, people)))

print(fav_people)