def enforce(*types):
  def decorator(fn):
    def new_func(*args, **kwargs):
      # Convert args into something mutable.
      new_args = []
      for (a,t) in zip(args, types):
        new_args.append(t(a))
      return fn(*new_args, **kwargs)
    return new_func
  return decorator

@enforce(str, int)
def repeat_msg(msg, times):
  for time in range(times):
    print(msg)

repeat_msg("hello", "3")
