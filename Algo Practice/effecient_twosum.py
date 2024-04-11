# two sum but with time complexity of O(n) linear time
# this is because we are looping over the array only once.

def TwoSum(array, target):
  Hashmap = {}
  for i, nums in enumerate(array):
    difference_index = Hashmap.get(nums)
    if difference_index != None:
        return [difference_index, i]
    Hashmap[target - nums] = i


lst = [2,4,5,7,8,9,10]

print(TwoSum(lst, 19))