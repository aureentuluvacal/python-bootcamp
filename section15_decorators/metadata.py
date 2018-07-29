from functools import wraps

def log_function_data(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    print(f"Calling function {fn.__name__}")
    print(f"Here's the docs: {fn.__doc__}")
    return fn(*args, **kwargs)
  return wrapper

@log_function_data
def add(x, y):
  """Adds two numbers together."""
  return x+y

print(add.__doc__)
print(add.__name__)