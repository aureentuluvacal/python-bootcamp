def current_beat():
  beats = (1, 2, 3, 4)
  index = 0

  while True:
    if index >= len(beats):
      index = 0

    yield beats[index]
    index += 1

counter = current_beat()
for i in range(0, 9):  
  print(next(counter))