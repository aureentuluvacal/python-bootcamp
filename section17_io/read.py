file = open('story.txt')

print(file.read())
print(file.read())
file.seek(0)
print(file.read())
file.seek(0)
print(file.readline())
print(file.readlines())

file.close()
print(file.closed)

# Or do
with open('story.txt') as file:
  data = file.read()

print(data)