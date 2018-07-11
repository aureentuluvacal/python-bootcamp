def colorize(text, color):
  colors = ["red", "blue", "purple"]

  if color not in colors:
    raise ValueError("{color} not a valid color")
  return f"Printed {text} in {color}"

print(colorize("bacon", "red"))
print(colorize("bacon", "chicken"))