def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total

print(sum_all_nums(4, 6, 9))

def ensure_correct_info(*args):
  if "Caryssa" in args and "Perez" in args:
    return "Welcome back Caryssa!"
  return "Not sure who you are..."

print(ensure_correct_info("Caryssa", "bacon", True, "Perez"))