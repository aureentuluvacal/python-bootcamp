# Custom for loop
def my_for(iterable, func):
  iterator = iter(iterable)
  
  while True:
    try:
      func(next(iterator))
    except StopIteration:
      print("End of iterator")
      break

def square(x):
  print(x*x)

my_for("bacon", print)
my_for([1, 2, 3, 4, 5], square)