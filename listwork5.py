import itertools
import random
nums = [5,15,35,8,98]
nums2 = [3,4,7,9,10]

#print index and values of a list
for num_index, num_val in enumerate(nums):
        print(num_index, num_val)
for i in nums:
    print(nums.index(i), i)

#print all combinations of permuations.
print(list(itertools.permutations([1,2,3])))

#convert all items to strings
new_list = []
for item in nums:
    new_list.append(str(item))
print(new_list)

#map functions which is kinda indteresting
def square(numbers):
    return numbers ** 2

squared = map(str, nums)
print(list(squared))

print(list(map(str, nums)))

#randomn select an objecxt from a list
print(random.choice(nums))

#append nums to nums2
for item in nums:
    nums2.append(item)
print(nums2)

nums2.extend(nums)
print(nums2)
