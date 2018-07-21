class Counter:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.start < self.end:
      num = self.start
      self.start += 1
      return num
    raise StopIteration

for n in Counter(50, 55):
  print(n)