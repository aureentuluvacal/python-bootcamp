def eat(food, is_healthy):
  if is_healthy:
    ending = "because my body is a temple."
  else:
    ending = "because YOLO!"

  return f"I'm eating {food} {ending}"

def nap(num_hours):
  if num_hours >= 2:
    return f"No! I overslept! I didn't mean to nap for {num_hours} hours!"
  return f"I feel refreshed after my {num_hours} hour nap!"