# try:
#   foobar
# except NameError as err:
#   print(err)

def get(d, key):
  try:
    return d[key]
  except KeyError:
    return None

d = { "name": "Caryssa" }
print(get(d, "city"))