class GrumpyDict(dict):
  def __repr__(self):
    print("NONE OF YOUR BUSINESS")
    return super().__repr__()

  def __missing__(self, key):
    print("YOU WANT THE IMPOSSIBLE")
  
  def __setitem(self, key, value):
    print("YOU'RE ASKING FOR A LOT")
    super().__setitem__(key, value)

data = GrumpyDict({ "first": "Tom", "animal": "dog" })
print(data)
data["city"]
data["food"] = "bacon"
print(data)