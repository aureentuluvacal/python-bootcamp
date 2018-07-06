teacher = {
  "name": "Colt Steele",
  "age": "who knows",
  "gender": "M"
}

clone = teacher.copy()
print(clone)

dictionary = {}.fromkeys(["name", "age", "gender"], None)
print(dictionary)

name = teacher.get("name")
print(name)

teacher.clear()
print(teacher)