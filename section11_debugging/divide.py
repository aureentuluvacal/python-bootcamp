def divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    print("Can't divide by zero")
  except TypeError:
    print("Need to use ints or floats")
  else:
    print(result)

divide(1, 2)
divide(1, 0)
divide("ham", 10)