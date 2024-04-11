# implementation of binary search
# given a sorted array of distinct integers and a target value
# return the index if target found, if not return the index where it would be
# if it were inserted in order

# example:  nums = [1,3,4,5,6], target= 5
# output: 2



def  search(lst, target):
  low = 0
  high = len(lst) -1

  while low <= high:
    mid = low + (high - low) // 2

    if lst[mid] == target:
      return mid
    if lst[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  
  return low


nums = [1,3,4,5,6]

print(search(nums, 2)) 



