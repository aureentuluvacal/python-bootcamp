import sys

people = ["Caryssa", "Carla", "Cassie", "Coco"]

print(all([name[0] == "C" for name in people]))

nums = [0, 1 , 2]
print(any(nums))
print(any([num % 2 == 2 for num in nums]))

# use a generator if you don't need to use the result again
print(all(name[0] == "C" for name in people))

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")