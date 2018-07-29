import time

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time() - list_start_time

print(f"Gen exp took {gen_time}")
print(f"List comp took {list_time}")

def nums():
  for num in range(1, 10):
    yield num

#g = (num for num in range(1, 10))