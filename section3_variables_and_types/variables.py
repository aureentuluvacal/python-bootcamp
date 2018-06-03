# Use snake case for variable names.
num_of_cats = 99
print(num_of_cats * 2)

str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
print(str_three)
# or
str_one += " face"
print("or " + str_one)
# Cannot concatenate integers and strings. Type matters, unlike JS.

# But can use string interpolation.
num_cats = 10
print(f"You have {num_cats} cats")

# String indices.
name = "Caryssa"
print(name[0])