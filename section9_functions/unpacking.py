def sum_all_values(*args):
  total = 0
  for num in args:
    total += num
  return total 

nums = [1,2,49,82,10]
print(sum_all_values(*nums))

def display_names(first, second):
  print(f"{first} says hello to {second}")

names = { "first": "Caryssa", "second": "Irma" }
display_names(**names)