numbers = [1, 2, 3, 5, 7]
new_numbers = [num*num for num in numbers]
print(new_numbers)

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]

newer_numbers = [num * 2 if num % 2 == 0 else num/2 for num in numbers]
print(newer_numbers)

with_vowels = "Oh hey, girl, hey"
no_vowels = "".join([char for char in with_vowels if char not in "aeiou"])
print(no_vowels)

nested_numbers = [[n for n in numbers] for num in numbers]
print(nested_numbers)