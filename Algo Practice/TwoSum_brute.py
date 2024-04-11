# this is a brute force method that will run at O(n^2)
# because of the nested for loops that we are using

def TwoSum(array, target):
  # i counter
  for index_1, item_1 in enumerate(array):
    # j counter
    for index_2, item_2 in enumerate(array):
      if item_1 + item_2 ==target:
        return [index_1, index_2]
   


lst = [1,4,5,6]

print(TwoSum(lst, 10))
