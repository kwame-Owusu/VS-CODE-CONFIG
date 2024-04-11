
# HashMap == dictionary

def TwoSum(array, target):
  prev_map = {} # value : index

  for i, num in enumerate(array):
    diff = target - num
    if diff in prev_map:
      return [prev_map[diff], i]
    prev_map[num] = i
  return


lst = [2,7,11,15] 
print(TwoSum(lst, 13))



