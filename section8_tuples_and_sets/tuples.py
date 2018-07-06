# tuples are immutable
# they can be used as keys to dicts
locations = {
  (35.6895, 39.6917): "Tokyo Office",
  (40.7128, 74.0060): "New York Office"
}

nums = (1, 2, 3, 3, 4, 7, 1, 10, 9, 3)
for num in nums:
  print(num)

print(nums.count(3))

print(nums.index(10))
