teacher = {
  "name": "Colt Steele",
  "age": "who knows",
  "gender": "M",
  "likesCats": True
}

clone = teacher.copy()
print(clone)

dictionary = {}.fromkeys(["name", "age", "gender"], None)
print(dictionary)

name = teacher.get("name")
print(name)

teacher.pop("gender")
print(teacher)

teacher.popitem()
print(teacher)

second_teacher = {}
second_teacher.update(teacher)
print(second_teacher)

teacher.clear()
print(teacher)