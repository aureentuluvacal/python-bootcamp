# def add(x, y):
#   '''Add together x and y

#   >>> add(1,2)
#   3
#   '''
#   return x + y

def double(values):
  ''' Double the values in a list.
  >>> double([1,2,3,4])
  [2, 4, 6, 8]

  >>> double([])
  []

  >>> double(['a','b','c'])
  ['aa', 'bb', 'cc']

  >>> double([True, None])
  Traceback (most recent call last):
      ...
  TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
  '''
  return [value * 2 for value in values]