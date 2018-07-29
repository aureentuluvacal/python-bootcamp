def shout(fn):
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs).upper()
  return wrapper

@shout
def greet(name):
  return f"Hi, I'm {name}"

@shout
def order(main, side):
  return f"I'd like order {main} with {side}"

print(greet("Caryssa"))
print(order("pizza", "more pizza"))