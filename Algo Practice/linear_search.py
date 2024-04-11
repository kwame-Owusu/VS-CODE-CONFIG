
def linear_search(arr, targ):
  for i in range(0, len(arr)):
    if arr[i] == targ:
      return i
  return -1




array = [1,2,3,5,67,32,8,53]
target  = 67

result = linear_search(array, target)

if result == -1:
  print('Element not in array')
else:
  print(f"Element in array, at index {result}")