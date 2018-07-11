nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

print(list(zip(nums1, nums2)))

nums3 = [1, 4]
print(list(zip(nums1, nums3)))

nums4 = [(0, 1), (1, 2), (13, 1)]
print(list(zip(*nums4)))

midterms = [100, 32, 89]
finals = [23, 56, 94]
students = ["dan", "john", "kate"]

final_grades = {t[0]:max(t[1], t[2]) for t in zip(students,midterms, finals)}

scores = zip(
  students, 
  map(
      lambda pair: max(pair), 
      zip(midterms, finals)
  )
)

print(final_grades)
print(dict(scores))