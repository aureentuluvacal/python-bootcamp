from functools import wraps

def ensure_first_arg_is(required):
  def inner(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      if args and args[0] == required:
        return fn(*args, **kwargs)
      return f"Invalid! First argument must be {required}"
    return wrapper
  return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
  print(foods)

print(fav_foods("burrito", "pizza", "bacon"))
print(fav_foods("burgers", "pizza", "bacon"))