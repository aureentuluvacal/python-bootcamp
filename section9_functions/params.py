def square(num):
  return num**2

print(square(4))
print(square(8))

def multiply(first, second):
  return first * second

print(multiply(11, 17))

def exponent(num, power = 2):
  return num ** power

print(exponent(4,3))
print(exponent(5))

# Param ordering
#  1. parameters
#  2. *args 
#  3. default parameters
#  4. **kwargs