def binary_search(arr: int, target: int) -> int:
  low = 0
  high = len(arr) - 1

  while low <= high:
    midpoint = low + (high - low) // 2

    if arr[midpoint] == target:
      return midpoint
    elif arr[midpoint] < target:
      low = midpoint + 1
    else:
      high =  midpoint - 1
  return None




def verify(index:int) -> str:
  if index != None:
    print(f"Target in array at index {index}")
  else:
    print("Target not in array")


my_array = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(my_array, 7)
verify(result)
